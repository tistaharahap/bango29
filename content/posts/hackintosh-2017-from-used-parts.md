+++
author = "Batista Harahap"
categories = ["Hackintosh"]
date = 2017-06-20T07:48:51Z
description = ""
draft = false
image = "/images/2017/06/IMG_0994.jpg"
slug = "hackintosh-2017-from-used-parts"
tags = ["Hackintosh"]
title = "Hackintosh 2017 From Used Parts"

+++


After some motivation from a colleague about this game I'm after, I decided to build myself a PC. That idea got me thinking, why not build with parts that are Hackintosh compatible. Further more, since this is a PC, I can build lean in the beginning and upgrade along the way. Used parts are the best way to go I thought.

It's unfortunate that I couldn't find used parts for the GPU and SSD. I had to buy them new. So before anything else, here are the specs:

```
CPU: [Used] Intel Core i3 6100 - 3.7 GHz
Motherboard: [Used] Biostar H110MH-PRO-D4 - MicroATX
RAM: [Used] 1 x 4GB 2400 MHz running in 2133 MHz
Hard Drive: [Used] 1 TB Toshiba 7200 RPM
Casing: [Used] Infinity
Keyboard & Mouse: [Used] Logitech
PSU: [Used] Enlight 430W
SSD: [New] Western Digital Green 120 GB
GPU: [New] Gigabyte GV-N730D5-2GI Geforce 730 2GB GDDR5
```

The used parts set me back Rp. 3.030.000 while the new parts was Rp. 1.775.000. The grand total being **Rp. 4.805.000** or **US$ 370** in today's rate.

---

## Pre Installation

It's easier if you already have any mac available to this. I did all this using my Macbook.

Download list:

1. Unibeast 7.1.1, [here](https://www.tonymacx86.com/resources/unibeast-7-1-1.333/)
2. Multibeast Sierra 9.1.0, [here](https://www.tonymacx86.com/resources/multibeast-sierra-9-1-0.334/)
3. Nvidia Web Drivers - I'm installing Sierra 10.12.1, more about it [here](https://www.tonymacx86.com/threads/solving-nvidia-driver-install-loading-problems.161256/), download the appropriate driver for your Sierra version
4. macOS Sierra from App Store

### Unibeast

First thing you'd do is to use Unibeast to copy all the macOS Sierra installation files to a fresh 8GB USB stick and install Clover bootloader. Follow the instructions [here](http://www.tonymacx86.com/threads/unibeast-install-os-x-el-capitan-on-any-supported-intel-based-pc.172672/).

### Copy Files

After the USB stick is ready, don't unplug it yet. Copy Multibeast and Nvidia web driver to the USB stick. Then unplug it.

## BIOS

The H110 chipset supports Kaby Lake Intel CPUs but when I got the motherboard, it was still using its factory BIOS. I updated my BIOS not because of Kaby Lake but because the newer BIOS has a lot more settings I can play with.

### Updating

Go [here](http://www.biostar.com.tw/app/en/mb/introduction.php?S_ID=840#download) to download the latest version which is `H11RRA26.BSS` as of this writing.

1. Prepare an empty FAT formatted USB stick
2. Copy the BIOS file to the USB stick
3. Plug the USB stick in
4. Turn on Computer
5. Press F12

The BIOS will show a screen to update itself. Follow the instructions.

### BIOS Settings

Start by loading `Optimized Defaults`.

```
\Advanced
\\IT8625 Super IO Configuration\Serial Port 2 Configuration\Disabled
\\USB Configuration\XHCI Hand-off\Enabled
\\SATA and RST Configuration\SATA Mode Selection\AHCI

\Chipset
\\PCH-IO Configuration\ErP Control\Enabled in S4-S5
\\System Agent (SA) Configuration\VT-d\Disabled

\Security
\\Secure Boot\Attempt Secure Boot\Disabled

\Boot
\\Fast Boot\Disabled
\\CSM Support\Disabled
```

## Installing macOS Sierra

This is pretty much straight forward. After finishing up installing Sierra, keep the USB stick plugged in, will need it to boot since we don't have a bootloader yet.

### First Boot

Booting up, select the freshly installed partition to boot.

Welcome to your new Hackintosh.

### Multibeast

Note: I don't use the onboard audio, I have a really good USB sound card I usually use for music recording. Opting to use that since I'm pretty sure the onboard audio is crap.

#### Quickstart

Choose `UEFI Boot Mode`.

#### Drivers

Check `Network/Realtek/RealtekRTL8111 v2.2.1`.

#### Customize

Check `Graphics Configuration/Nvidia Web Driver`

#### Build

Will prompt for `sudo` and the config will be injected into Clover. Don't restart yet.

### Nvidia Driver

Run the package and afterwards the installation will ask to restart the system.

### Second Boot

Welcome to your second boot. Now the GPU should accelerate all drawings and the wallpaper for Sierra should show.

### SSDT

You need this so the CPU can go to proper power management steps. Ex: it won't run at full frequency all the time.

Follow [here](http://www.tonymacx86.com/threads/quick-guide-to-generate-a-ssdt-for-cpu-power-management.177456/).

### SSD TRIM

Open up a terminal and type this:

```
$ sudo trimforce enable
```

If you wanna know why this is important, read [here](http://www.buildcomputers.net/trim-support.html).

---

It's done.

Pretty straight forward considering that my last experience building a hackintosh involves patching kexts. Now Clover has done it for you and best of all, the patches will survive OS upgrades.

As I said, now I have hackintosh I can upgrade whenever I'd like to. Cheers!