+++
author = "Batista Harahap"
categories = ["Hackintosh", "Mac", "mavericks"]
date = 2014-02-16T23:11:30Z
description = ""
draft = false
slug = "hackintosh-rig-2014"
tags = ["Hackintosh", "Mac", "mavericks"]
title = "Hackintosh Rig 2014"

+++


A few weeks ago my brother in law asked me to help him build a Hackintosh rig. I obliged with the utmost curiosity. It's been a while since I last built one so this will be interesting.

The first thing I did was heading to InsanelyMac's forums. There were a lot of guides but one that interests me is the Mavericks guides. I downloaded a copy of it before for my Macbook.

## Constraints

Constraints for the yet to built rig as follows.

- Rp. 7.500.000 Max
- Plenty of horse power for Video Editing
- Large HD for rendered videos
- Full HD support
- Easy hardware upgrades

## Specs

After reading various topics about the right specs, I settled with the below specs.

- Gigabyte GA-H77-DS3H
- 1 x 8 GB DDR PC10600 DIMM
- Intel Core i5 3330 - 3.0 GHz Quad Core
- 500 GB SATA HD
- 160 GB SATA HD
- Digital Alliance Nvidia GT640 2 GB
- Asus DVD-RW
- Logitech USB Mouse/Keyboard
- Dazumba 911 Tower ATX Case
- Dazumba 450 Watts Pure PSU

The above spec costs **Rp. 7.450.000**.

One of the more difficult part was settling for the right CPU and Motherboard. Since it's meant as a Video Editing rig, the spec needs to be fast enough for memory, CPU and GPU intensive tasks.

Price being the utmost constraints I choose a Quad Core i5 3330 because it's the best bang for the buck. The Motherboard was cheap enough having a lot of room for upgrades. There are 4 DIMM slots, 6 SATA connectors and 2 full length PCIe slots.

I only used 1 DIMM slot leaving 3 more for more memory to come. Dual Channel should increase memory bandwidth but that's something to trade off for a better price.

There is an unused PCIe full length slot which in the future will have a GPU attached to it. My brother in law wanted multi monitors so the extra PCIe slot is a plus.

Opting for the GT640 GPU made life easier. Nvidia drivers for these GPUs are native. Minimal configuration needed.

## Installation

To do an installation, you need an already working Mac setup. Here are links for the software you're gonna need:

- [myHack 3.3.1](http://myhack.sojugarden.com/guide/)
- [Mac OS X Mavericks from App Store](https://itunes.apple.com/id/app/os-x-mavericks/id675248567?mt=12)
- [VoodooHDA 2.8.4](http://www.osx86.net/files/file/1194-voodoohda-2-8-4-pkg-installer/)
- [Shailua ALXEthernet 1.0.2](http://www.insanelymac.com/forum/topic/284119-experimental-atheros-ar813132515261627172-driver-for-107108/)

You will also need a spare USB thumb drive or HDD for the install media.

### Pre Installation

Run the provided myHack application and follow instructions to create a bootable Mavericks install. Point myHack to the USB drive you prepped.

### BIOS Settings

- Legacy BIOS Boot
- Save & Exit / Load Optimized Defaults
- Peripherals / SATA Mode Selection - AHCI
- BIOS Features / Intel Virtualization Technology - Disabled
- BIOS Features / VT-d - Disabled

### Install Mavericks

Plug the USB drive to the rig and make it boot from it by pressing F12 at startup.

You have to boot with the following kernel arguments.

```
-v -f npci=0x3000 PCIRootUID=0 GraphicsEnabler=No
```

With my USB Drive it booted straight into the installation process. When the mouse is available with a grey background, it will take a while until the language selection shows. Just wait for it.

#### Format HD

When the language selection shows up, click Utilities on the menu above and click Disk Utility. Make sure you select the right drive and format it as Mac OS X Journaled.

### Post Installation

myHack will make the hard drive you installed it to bootable. So you can restart without worry. But you will still need to enter the boot flags above. Here are the boot flags for convenience.

```
-v -f npci=0x3000 PCIRootUID=0 GraphicsEnabler=No
```

#### Audio & Ethernet Kexts

Now copy the kexts to your desktop. Run the following on a terminal window.

```
$ cd ~/Desktop
$ sudo cp -R VoodooHDA.kext /System/Library/Extensions
$ sudo cp -R ALXEthernet.kext /System/Library/Extensions
$ sudo diskutil repairPermissions /
$ sudo bless /System/Library/Extensions/
```

#### Chameleon Default Boot Options

Next up we're going to configure Chameleon so we don't have to enter boot flags at boot time. On a terminal window, do the below.

```
$ sudo vim /Extra/org.chameleon.boot.plist
```

Add/change to suit the line below.

```
<key>Kernel Flags</key>
<string>npci=0x3000 PCIRootUID=0 GraphicsEnabler=No</string>
```

Reboot.

## Done

Nowadays building and installing a Hackintosh is a **lot** easier than in the early days. Anyone with the right curiosity will succeed.