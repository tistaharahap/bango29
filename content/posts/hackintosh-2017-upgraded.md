+++
author = "Batista Harahap"
categories = ["Hackintosh"]
date = 2017-06-27T04:02:11Z
description = ""
draft = false
image = "/images/2017/06/IMG_1048.jpg"
slug = "hackintosh-2017-upgraded"
tags = ["Hackintosh"]
title = "Hackintosh 2017 - Upgraded"

+++


I [built a Hackintosh a few weeks ago](https://bango29.com/hackintosh-2017-from-used-parts/) because I want an upgradeable Mac. And so I upgraded. Also since now I'm back in Jakarta, I took an SSD from my now defunct HTPC + Storage rig. The storage part which is a 3TB USB Harddrive decided to break.

So now my Hackintosh is upgraded with these parts:

```
* Biostar B250-GT3 - MicroATX - 4 DIMM slots FTW! And it's a newer chipset with 2 PCIe slots for more GPU power. Also has 4 SATA ports :)
* Kingston 8GB DDR4 2400 MHz memory stick which brings my memory to 12GB
* Kingston 120GB SSD taken from my HTPC rig
* Zotac GTX 1050 2GB GDDR5 - Slim and it doesn't require any added powering
* Fenvi Wireless AC PCIe with Bluetooth - Plug n Play!
* New Infinity casing
* Logitech Extreme 3D Pro joystick
* Generic Mac keys Bluetooth Keyboard
* Logitech M337 Bluetooth mouse
* Behringer Xenyx Q502USB Soundcard
```

It's worth noting that the new motherboard has a M.2 slot that'll enable me to use NVMe SSD's. Not going to do it sometime soon because support for Hackintoshes is [still patching kexts manually](https://github.com/RehabMan/patch-nvme). Although the 1000 MB/s read is totally a sexy appeal.

The new GTX 1050 GPU is Pascal based so [Nvidia web driver](http://www.insanelymac.com/forum/topic/312525-nvidia-web-driver-updates-for-macos-sierra-update-05152017/) works. I was on 10.12.1 before on my GTX 730 and upgraded to 10.12.5 to take advantage of the Nvidia web driver.

Of all the new upgrades, the 1 component that's been the best surprise is the [Fenvi Wireless card](https://www.tokopedia.com/sleepymind/fenvi-fv-t919-bcm94360cd-wireless-bluetooth-hackintosh). It just works out of the box. However, since I've already used a USB wifi dongle before, I had to delete all network interfaces and a plist somewhere to make App Store works. Another surprise is with the Fenvi card, it connected to the router at 1300 Mbps! Unlike other devices I have supporting AC but bottlenecked at 100 Mbps.

[Speedtests were able to consume almost all the available 300 Mbps](http://www.speedtest.net/my-result/d/10668708) of my home connection! Before the Fenvi, only Gigabit ethernet reached that speed in my house.

![Myrepublic 300 Mbps Connection on AC Router](/content/images/2017/06/Screen-Shot-2017-06-27-at-5.50.55-PM.png)

---

I'm still planning to install Windows 10 but my only justification is only to play Microsoft Flight Simulator X Steam Edition. Not sure if that's the right motivation.

Loving the Hackintosh build extremely! Another upgrade I will do is the CPU. The i3 6100 is bottlenecking when playing Football Manager 2017, looking into i7 6700K but the necessity of having to cool the CPU myself without any HSF bundled is puzzling. And I'll wait for Apple to support Kaby Lake CPU's natively without me having to mask them as Skylake.

The new casing's airflow is pretty good but when playing X Plane 11, the whole case warmed up. There is no fan for the casing yet, I have a fan I can use though. Also looking into water cooling the CPU. Thinking about a closed loops all in one solution for it.

---

On another note, I opened up a store in Tokopedia, aptly named [Bango 29 by tistaharahap](https://www.tokopedia.com/tistaharahap). The store contains used PC Parts or any other gadgets I don't use anymore. Those are stuffs I mostly use a little while and decided not to use them anymore or upgrade. Check it out!

Having built and upgraded the Hackintosh, i don't think anyone with the know-how should ever buy a desktop Mac. As long as the upgrade path for desktop Macs are what they are right now, it's crazy to spend more money just for the aesthetics. I can find justifications for Mac laptops but none for desktops.

![The Frontend of my upgraded Hackintosh](/content/images/2017/06/IMG_1039.jpg)

![My upgraded Hackintosh Rig](/content/images/2017/06/hack.jpg)