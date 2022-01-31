+++
author = "Batista Harahap"
categories = ["hackintosh", "windows", "virtualization", "proxmox", "vm"]
date = 2022-01-31T15:53:44Z
description = ""
draft = false
image = "/images/2022/01/yeah-right.jpg"
slug = "hackintosh-virtualized-vs-bare-metal"
tags = ["hackintosh", "windows", "virtualization", "proxmox", "vm"]
title = "Hackintosh: Virtualized VS Bare Metal"

+++


It's been a few days since [my last blog post about a virtualized hackintosh](https://bango29.com/virtualized-hackintosh-and-gaming-pc/), I've got some time to tinker and form opinions and gather facts about it. It's not bad at all but it comes with a compromise, let me try to follow up on what I've written before.

## Why Virtualize At All?

Why not? But a more convincing argument is because I have a gaming PC with a 16 core/32 thread CPU lying around. It's rather fiddly to dual boot between macOS and Windows because both my GPUs (Radeon RX 570 and RTX 3080 Ti) are connected to my monitors and on Windows [this is not ideal](https://dortania.github.io/OpenCore-Install-Guide/extras/spoof.html). The best possible experience is to use an HDMI or DP switch to connect the GPUs to my monitors, I don't have such a device and I'm pretty sure I don't want to explore the quirks that comes with using it.

Virtualization was the only way to go to share resources of a single PC for different operating system installs. It slices and dices components so that the virtual machine we create are assigned with the right hardware for the right OS. In theory this is a godsend, solves my use case and I get to learn something new.

## Virtualized Hackintosh

Reporting back my experience with a virtualized hackintosh is pretty much a hit and miss in short. But this was predominantly caused by not using an Intel CPU for the host. It will be a different picture with an Intel CPU, very different.

### Pitfalls

The install was not that complex to understand, but having an AMD CPU crippled my use case. There's now workaround for not having an Intel CPU to do nested virtualization, so Docker, Virtualbox, Kubernetes, etc will not work. Not wanting to give up easily I set up another Linux VM just for Docker and Kubernetes.

To do Docker is straightforward, I just set `DOCKER_HOST` env var to point to the Linux VM.

```shell
$ echo "export DOCKER_HOST=ssh://user@ip:port" >> ~/.zshrc
```

I setup my workflow, pods are running but then some parts of my workflow didn't work, namely anything that has gotta do between inter-container communication and exposing the containers to the outside world (the macOS install). At least it's not straightforward to debug and going down this rabbit hole would take time.

Afterwards I tried doing other things like setting up Kubernetes with `minikube` rather than `microk8s` but these small quirks that would seem harmless for devops folks looked like Mt. Everest to me. Again I didn't want to spend more time with it than I wanted to.

Given time I'm sure I can iron out these quirks but I wasn't motivated enough, mainly because I needed to do more optimizations on the virtualization part. My Geekbench scores were lower, [bare metal](https://browser.geekbench.com/v5/cpu/10517013) and [virtualized](https://browser.geekbench.com/v5/cpu/12313580). Yes this wasn't an equal comparison between macOS VS Windows but then I never built a hackintosh on that gaming PC before. Disregard the multi core scores though, the macOS was only given half the threads. The single core score for the macOS though was slower by **~17%** which in IPC terms, this is like skipping a generation of CPU performance.

[AMD's Precise Boost Overdrive](https://www.amd.com/en/support/kb/faq/cpu-pb2) I suspect was not utilized, I mean how? The CPU was spoofed as an old Intel Core2Duo by KVM to macOS, there were now Kexts for power management or the sorts for the AMD CPU. On a bare metal hackintosh, I can easily use [SMCAMDProcessor](https://github.com/trulyspinach/SMCAMDProcessor) to manage my CPU but not the case with a virtualized AMD hackintosh. Is this something Proxmox should've handled gracefully with its kernel? I don't know enough to answer this but conveniently I would say yes.

For this install, I didn't passthrough an NVMe drive, instead I use the boot drive as the storage for the VM's disk. This was counterproductive towards disk performance. My Samsung 970 Evo only got around 1000MB/s read/write throughput which is only about twice of a plain SATA SSD. So if disk performance is crucial to your workflow, you should passthrough a dedicated NVMe disk to minimize any virtualization overhead.

Costs also will balloon if you virtualize effectively for performance. I'll try to describe it:

1. My RAM was 32GB, I couldn't use all of it for my hackintosh, I gave macOS 16GB and Linux 8GB (for Docker, K8s, etc). Even if you only use macOS and nothing else, you still can't utilize the full 32GB. From experience, it's always more stable if you only use identical memory sticks across the DIMM slots, this means if I want to give 32GB to macOS, I needed to have 64GB of memory to take advantage of DDR.
2. Dedicated disk for each first class OS. In my case I didn't do this which results to micro stutters if you run more than 1 VM concurrently with 1 of them doing heavy tasks related with disk IO. I tried running macOS and Windows together from the boot drive and micro stutters were happening frequently. There was not enough IO headroom so be prepared to shell out more cash for dedicated disks.
3. You better have reliable and effective cooling for various components, not just the CPU. I thought I had myself covered here with a Noctua NH-D15 for the CPU but I was wrong. I couldn't install the second GPU on the third PCIe slot because that slot was controlled by the chipset, not the CPU. Therefore the GPU won't have its own IOMMU group and its bandwidth is shared with the chipset's overall bandwidth. Having both GPUs sandwiched on slot 1 and 2 made performance in gaming having a hit. I usually play open world games and these games are GPU intensive, my frame rates were not great.
4. DRM will not be straightforward for hardware based DRM. I did not give [this](https://github.com/acidanthera/WhateverGreen/blob/master/Manual/FAQ.Chart.md) much time but out of the box with `shikigva=128` which is appropriate for the model I chose, hardware DRM doesn't work. I'm sure I can invest more time in figuring this out.

### The Good Stuffs

I upgraded macOS Monterey easily, I had no problems whatsoever, I just let the installer do its thing. It takes away that fear if an OS upgrade would botch your hackintosh. This being virtualized, for the more paranoid part of me, I can just backup the disk in Proxmox right before I do the upgrade. If anything goes wrong, it's just a few clicks to revert to the backup. This is truly mindblowing for me.

The only hardware I had to worry about is the GPU, everything else just works. As long as the GPU is in [this GPU buyers guide](https://dortania.github.io/GPU-Buyers-Guide/), there will be minimal fuss, in my case with a Radeon RX 570, it works out of the box. As for Wifi/Bluetooth, I have a [Fenvi T919](https://www.fenvi.com/product_detail_16.html) Wifi/Bluetooth PCIe card I bought years ago, this worked out of the box on all my hackintoshes, including this one, I just pass this through to macOS.

Although for my virtualization use case it didn't worked very well but for others I'm convinced this is effective. Like if you need clusters of macOS installs to do tasks that can only be done on macOS. It's not going to be difficult to write a script to automate this in Proxmox, it's just another Linux distro, Debian to be more precise. Use cases that involves a cluster of macOS virtual machines could be for Xcode build bots or Adobe Photoshop automation with AppleScript. I can see real world use cases here.

## Bare Metal Hackintosh

Creating the EFI folder used to be straightforward, just follow [Dortania's OpenCore install guide](https://dortania.github.io/OpenCore-Install-Guide/). However, it's proving to be not as straightforward for 11-12th gen Intel platforms, it's easier to do this for AMD platforms surprisingly.

Before continuing, I should say I eventually decided I wanted to build another Hackintosh on Intel's 11th gen platform. Why? My laptop's life expentancy will be cut shorter faster if I never shut it down, I never did before. I was in this phase where I thought due to the new Macbook Pro M1 Pro/Max's insane performance and focus for pros, I only need a single machine for everything. It's fast, really fast, using the 16" Macbook Pro M1 Pro is perceptively more snappy than my Macbook Air M1 but having it on for 24 hours is starting to feel more ridiculous.

I sold the 16" Macbook Pro M1 Pro. Although the horsepower on that machine is great, I don't need it. I don't do heavy computing tasks, if I have to choose between CPU power and memory, I'll choose memory every time when I have enough cores to multi task. The idea of building a bare metal hackintosh VS optimizing the virtualized hackintosh VS Mac Mini M1 waged war in my head to which I finally asked myself, which of these gave me the option of having more memory? This eliminated the Mac Mini M1 as a solution.

That question left me with Bare Metal VS Virtualized, which one to choose? I chose Intel 11th gen platform, doesn't matter if it's bare metal or virtualized, either or is fine with me. For my workflow, knowing all the pitfalls above, an Intel CPU solves most of my concerns.

I then pulled the trigger to build a rig with this spec:

* Intel Core i5 11400 - 6 Core/12 Thread
* Asus B560M TUF Gaming Plus Wifi
* 2x16GB DDR4 3200MHz Memory
* Samsung 970 EVO 500GB NVMe
* NZXT C650 80+ Gold PSU
* Cooler Master Silencio S400 Case
* AMD Radeon RX 570 GPU

This is a MicroATX form factor build, and a really silent one. Having a 65W TDP CPU means the insides of the case wouldn't become an oven and that CPU is the right one for my workflow. Here's a Geekbench result, [here](https://browser.geekbench.com/v5/cpu/12507550). It scored higher than the virtualized hackintosh and obviously lower than an M1. Only a 12th gen Intel CPU can beat the M1 for now.

That Geekbench result is on a bare metal install of macOS. All my workflow works out of the box like how an Intel mac would. But, I didn't do this on my own. I googled [this](https://www.google.com/search?client=firefox-b-d&q=asus+b560m+plus+wifi+hackintosh) and got [this](https://hackintosh.expert/service/asus-tuf-gaming-b560m-plus-wifi-i9-11900k-rx-570-download-kext-monterey-efi-opencore/). Apart from the CPU, the other parts are identical to my specs and I know I didn't have to worry about CPU types. I paid US$ 3 through Paypal for them to give me a download link for the EFI folder.

Yes, I know I can do this on my own, can I? Yes I can, in fact I was in the middle of setting it up when it crossed my mind to google the motherboard. Also, US$ 3 is a very small price to pay for the time saved. I could've been doing trials and errors for hours, but instead I just copy paste, boot from the installer and installed macOS Monterey just like that. The only necessary modification to the EFI folder was to do [the post installs](https://dortania.github.io/OpenCore-Post-Install/), especially generating a proper serial. 

DRM might need some love with `shikigva=80` in the `boot-args`, after that everything works.

Out of the box, this hackintosh is every bit identical to how an Intel mac works but this machine is almost twice as fast as a [16" Intel Macbook Pro](https://browser.geekbench.com/v5/cpu/12508780) with only a third of the price and twice as much memory. This argument of having a hackintosh outperforming Intel macs never go stale, Intel's CPUs are just not great for later macs, period.

---

Much of what I just said is against virtualizing macOS but I'm happy to be proven wrong, 100%. Out of interest, I'm going to try the virtualization route too when I find the motivation to install a SATA SSD or a second NVMe into the hackintosh. But for now, I'm good with this.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Said goodbye to my hackintosh and Air M1 last week, the new 16&quot; Macbook Pro vindicated that decision. It&#39;s on a league of its own, truly. For a software engineer M1 Pro is plenty. Just 1 machine for work and home, at last after a long wait.</p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1456993405800783877?ref_src=twsrc%5Etfw">November 6, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

![Yeah right!](/images/2022/01/yeah-right.jpg)