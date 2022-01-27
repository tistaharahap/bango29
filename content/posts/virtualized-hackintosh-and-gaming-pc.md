+++
author = "Batista Harahap"
categories = ["hackintosh", "windows", "virtualization", "proxmox", "vm"]
date = 2022-01-27T23:08:44Z
description = ""
draft = false
image = "/images/2022/01/virt-explained.jpg"
slug = "virtualized-hackintosh-and-gaming-pc"
tags = ["hackintosh", "windows", "virtualization", "proxmox", "vm"]
title = "Virtualized Hackintosh and Gaming PC"

+++

# Virtualized Hackintosh and Gaming PC

I have installed hackintoshes since the very beginning on a Core2Duo laptop. Back then the term was OSX86 and the only way to get the OS is through torrent downloads. Since then I've built hackintoshes especially when Intel Macbook Pros are so pro. I can't believe all these years I never tried to do the virtualization route. The past few years, my hackintoshes were always a dedicated PC separate from my gaming PC because Nvidia GPUs have no hope in hackintoshes, now it changes.

Building hackintoshes virtualized means I can do snapshots/backups easily, the whole system is just a file in a directory somewhere. I don't have to be discouraged with OS upgrades. In the future when I upgrade my machine, I don't need to reinstall everything, I just change a few configs to passthrough hardware from host to guest. I didn't know virtualization tech is this convenient to use day to day, I always thought it's more in the enterprise realm but I'm glad I did my due diligence for this.

## Hardware Spec

I'm starting from the hardware spec first to give you an idea how liberal anyone can be with caveats.

* Motherboard: Gigabyte Aorus Master X570
* CPU: AMD Ryzen 5950X - 16 Core 32 Threads
* CPU Cooler: Noctua NH-D15
* Memory: 32GB DDR4 3600MHz CL16
* Storage:
    * 1x Samsung 980 Pro NVMe - 500GB - Windows 10
    * 1x Samsung 970 Evo NVMe - 500GB - Boot drive
    * 1x Samsung 870 Qvo - 500GB - VM Disks
    * 1x Samsung 870 Qvo - 1TB - Game Disk
* PSU: Corsair HX1000 - 1000W
* GPU1: Palit Nvidia Geforce 3080 Ti
* GPU2: PowerColor Radeon RX 570
* Audio: Topping E30 DAC connected through USB

### Nested Virtualization Caveat

Because I'm using an AMD CPU, nested virtualization in the hackintosh won't work. We have to spoof macOS to register the CPU as an Intel CPU which uses `vmx` instructions for virtualization while AMD uses `svm` instructions. Things like Docker, Virtualbox, Hyperkit and other virtualization software just won't work.

The good news is, we're virtualizing, for my workflow I can mange having Docker and a k8s cluster on another Ubuntu VM. If you really want nested virtualization to work, get an Intel CPU. I considered Intel CPUs but the number of cores/threads on Intel CPUs are limited, and it's a hot CPU. But who knows, when Intel get their shit together and releases a CPU that's worth the switch, I'm easy to impress. I'll delegate this 5950X for Unraid.

### PCIe Lanes and IOMMU Group Caveat

Every chipset and every CPU has a hard limit for the number of PCIe lanes we can take advantage of. The number will dictate how and where we set up our components. On my motherboard, I had to install the GPUs side-by-side on PCIe slot 1 &amp; 2 because slot 3 was controlled by the chipset. Slot 3 will share PCIe lanes (bandwidth) with NVMe disks and SATA disks, to make matters worse in my motherboard the IOMMU group for slot 3 was in the same group with the other hardware controlled by the chipset, I can't do proper GPU passthrough.

Consult the motherboard's manual first before installing the components. I suppose Threadripper/Epyc and Xeon platforms are the ideal platforms if you need more PCIe lanes.

## Virtualization

I started my experiment on my [Unraid](https://unraid.net/) server but it was too nice for me. There's an Unraid app from the community called [Macinabox](https://github.com/SpaceinvaderOne/Macinabox) that will automate most of the grunt work but this feels like more of a hack on top of Unraid rather than something native. If your machine is on the happy path, it's great while if your machine needs more work, the actual work is hiding behind fancy UIs. That said, I looked for alternatives. For the record, my machine wasn't on the happy path.

Youtube offered plenty of content about virtualized hackintoshes, after looking at the alternatives, I set my eyes on Proxmox 7. Especially because of [this blog post](https://www.nicksherlock.com/2021/10/installing-macos-12-monterey-on-proxmox-7/) where Nicholas Sherlock the author described in detail how he set up his hackintosh in Proxmox. Reading the blog post, I immediately felt at ease because I have full control of the whole process, I can experiment freely.

### Hackintosh

Let me start by sharing my eventual hackintosh VM definition.

```
# /etc/pve/qemu-server/100.conf
agent: 1
args: -device isa-applesmc,osk="<redacted>" -smbios type=2 -cpu Penryn,kvm=on,vendor=GenuineIntel,+kvm_pv_unhalt,+kvm_pv_eoi,+hypervisor,+invtsc,+pcid,+ssse3,+sse4.2,+popcnt,+avx,+avx2,+aes,+fma,+fma4,+bmi1,+bmi2,+xsave,+xsaveopt,+rdrand,+svm,check,rdtscp -smp 16,sockets=1,cores=8,threads=2 -global nec-usb-xhci.msi=off -global ICH9-LPC.acpi-pci-hotplug-with-bridge-support=off
balloon: 0
bios: ovmf
cores: 16
cpu: Penryn
efidisk0: local-lvm:vm-100-disk-1,efitype=4m,size=4M
hostpci0: 0000:0c:00,pcie=1,x-vga=1
hostpci1: 0000:0e:00.3,pcie=1
machine: q35
memory: 16384
meta: creation-qemu=6.1.0,ctime=1642796011
name: monty
net0: virtio=<redacted>
numa: 1
onboot: 1
ostype: other
scsihw: virtio-scsi-pci
smbios1: uuid=<redacted>
sockets: 1
vga: none
virtio0: local-lvm:vm-100-disk-0,cache=unsafe,discard=on,size=300G
vmgenid: <redacted>
```

I suggest following the blog post I shared to set up your own virtualized hackintosh, it's all there. I'm posting here the modifications I had to do to make my Proxmox install work with my hardware.

```
# /etc/modprobe.d/vfio-pci.conf
options vfio-pci ids=<redacted> disable_vga=1  # Disabling VGA means I don't have to load a VBIOS
```

```
# /etc/default/grub
...
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on iommu=pt video=efifb:off pcie_acs_override=downstream,multifunction"  # pcie_acs_override is important to make things work
...
```

#### Geekbench Results

Baremetal: **1713** Single Core - [link](https://browser.geekbench.com/v5/cpu/10517013)<br />
Virtualized Hackintosh: **1440** Single core - [link](https://browser.geekbench.com/v5/cpu/12313580)

I haven't do any optimizations yet to crank up the single core results yet, I'm just happy it works for now. To be honest, when you're in the OS, the difference between the single core performances is negligible for my use case. I don't need massive computing power doing programming in Python, at least not yet. Then again, if I do need performance over everything else, I can always spin up a Linux VM which is more optimized to work in a virtualized environment to do the job.

### Gaming

Windows 10 virtualized just works. Here's my config for it.

```
# /etc/pve/qemu-server/101.conf
args: -smp 16,sockets=1,cores=8,threads=2
agent: 1
balloon: 0
bios: ovmf
boot: order=virtio0;
cores: 16
cpu: host
efidisk0: pcie4-imgs:101/vm-101-disk-0.qcow2,efitype=4m,size=528K
hostpci0: 0000:0b:00,pcie=1,x-vga=1
hostpci1: 0000:0e:00.3,pcie=1
machine: pc-q35-6.1
memory: 28672
meta: creation-qemu=6.1.0,ctime=1642844895
name: gaming
net0: virtio=<redacted>
numa: 1
ostype: win10
scsi5: /dev/disk/by-id/ata-Samsung_SSD_870_QVO_1TB_<redacted>,size=976762584K  # Passthrough SATA disk for games
scsihw: virtio-scsi-pci
smbios1: uuid=<redacted>
sockets: 1
vga: none
virtio0: local-lvm:vm-101-disk-0,cache=unsafe,discard=on,size=400G
vmgenid: <redacted>
```

I'm playing games on a 144Hz 1440p display, the games I play are mostly flight simulators, open world games and the occassional CS:GO playing time once in a while. I haven't tried Microsoft Flight Simulator 2020 on it but I have no reason to believe that it won't match bare metal performance, this warrants its own blog post later in the future.

I tested playing these games:

* FarCry 6
* Watch Dogs: Legion
* Red Dead Redemption 2
* CS:GO

I didn't notice anything that would pursuade me to go back to bare metal, it just works. Although in theory I can still do bare metal, I still have a bare metal Windows 11 install on one of the NVMe I haven't nuked. It's great to have that option if I ever wanted to switch back.

## What I Don't Like

Here are some things I notice running these VMs which I'm not a fan of:

1. You rely heavily on the host kernel's scheduler to choose which CPU to work with for your VMs. I have seen people pinning down CPU cores/thread for VMs but I'm not that moved by it. I don't like trusting the scheduler but it's something I can accept. Also, by relying on the scheduler, you won't be sure you will always be using your best core that can reach higher clocks.
2. Your usable RAM will be your total RAM minus 2GB for Proxmox. While this is of course something to expect, this will jack up the total cost of your machine. I always use the same RAM models on my RAM slots which is good practice to ensure stability. This means if I want 32GB of RAM for macOS or Windows, I would need 64GB of total RAM.
3. You can't overclock your CPU using Windows based tools, you rely 100% on the BIOS features. I've set my Windows VM to use passthrough CPU (host) but I can't get the right reading for boost clock, Windows always report the base clock. I can't tell if Ryzen's PBO is in effect.
4. Running macOS and Windows in parallel is doable but I never did because hardware passthrough is funky. Hardware sometimes just don't want to be reset and eventually you will need to reboot the host to reset. I once gamed on Windows, shut it down afterwards and booted the hackintosh, it wouldn't boot because of this.

---

In closing, I wished I'd have done this sooner. It would've saved me countless hours to begin with. There are quirks but I can accept them, the convenience of not having to worry about hardware is new and offers me a new way of thinking about building PCs, I'm keen to explore more of this.

It took me 3 or 4 reinstalls of Proxmox because I couldn't get the hackintosh to do proper GPU passthrough at first. I'm still scratching the surface, especially in optimizing for performance. I have a lot to learn.
