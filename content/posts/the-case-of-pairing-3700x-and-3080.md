+++
author = "Batista Harahap"
categories = ["ryzen", "3080", "undervolt"]
date = 2020-10-23T20:11:38Z
description = ""
draft = false
image = "/images/2020/10/maxresdefault-1.jpg"
slug = "the-case-of-pairing-3700x-and-3080"
tags = ["ryzen", "3080", "undervolt"]
title = "The Case Of Pairing 3700X and 3080"

+++


It has been known that the 3080 is a power hungry GPU while 3700X is supposedly a power efficient CPU with a TDP of 65W. Pairing the two should not be a problem powered by a Corsair RM 750W PSU, or is it? Here's what happened to my rig.

## Hardware Spec

Before anything else, here is the spec I built:

* AMD Ryzen 7 3700X
* Corsair H115i Pro AIO Watercooler
* AsRock X570 Taichi Motherboard
* 32GB HyperX Fury 3200MHz
* Palit Geforce RTX 3080 GamingPro OC
* Corsair RM750 80+ Gold

## The Problem

The same 3080 was [paired before with an Intel i7 8700K rig](https://bango29.com/microsoft-flight-simulator-2020-beta-testing-using-your-customers/). I had no problem whatsoever from the hardware. Ran everything just as it should. But there were the occasional stutter when playing Microsoft Flight Simulator 2020, my theory was that there wasn't enough bandwidth somewhere to do something. So I tried to pair the 3080 with my AMD rig.

Long story short, the stuttering disappeared. Keep in mind I also used PCIe Gen 4 activated through the UEFI BIOS for the AMD rig. Then something else happened 3 times, the PC just restarted itself while I was playing. Could it be that the 3080 was overdrawing power from the PSU that triggered the PSU's protection?

I don't know.

## The Solution

Flying in a simulator from A to B involves a lot of waiting and when on final approach, that's when I feel the most excited. When the PC restarted itself multiple times while on final approach, I had to do something.

First thing was undervolting my Ryzen 3700X. I followed this video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DHdc9NeRiNc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The difference was I put 4.1GHz at one of its core instead of a uniformed 3.9GHz.

![Ryzen Master](/content/images/2020/10/ryzen-undervolt.png)

Playing the game after undervolting made no difference in performance, if there was any it was marginal, I didn't experience anything degraded.

Next up is to undervolt the 3080, I followed this video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FqpfYTi43TE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ended up with this curve for my 3080.

![3080 Undervolt](/content/images/2020/10/3080undervolt.png)

The final voltage is 987mV at 2000MHz.

Again when I played after the 3080 undervolt + 3700X undervolt, there was no noticeable degradation in performance. It was just fine. Let me put some screenshots of before and after the undervolts.

## Before and After Undervolting

### Before - Tokyo Dusk Flight

This is taken from a Tokyo flight at dusk.

![](/content/images/2020/10/20201023035805_1.jpg)

![](/content/images/2020/10/20201023035805_1--2-.jpg)

The CPU power draw is *46.5W at 4.35GHz*, GPU power draw at *322.425W* totaling to **368.925W**.

### After - Somewhere in Australia

This is taken off of a flight from Sydney to somewhere in Australia.

![](/content/images/2020/10/20201024080752_1.jpg)

![](/content/images/2020/10/20201024080752_1--2-.jpg)

The CPU power draw is *29.9W at 4.1GHz*, GPU power draw at *303.455W* totaling to **333.355W**.

### Before & After Conclusion

The power draw delta is **35.57W** which is **~10%** reduction in power usage. Temperatures improved though for the CPU, an 8C delta which translates to **~17%** while not much on the GPU of a delta of 2C translating to **~3%**. Lower temps mean a quieter PC since I don't play with headphones.

This can be further improved by undervolting the GPU even more.

---

Now there were no sudden restarts anymore, I could use a higher rated PSU but now I learned how to undervolt without sacrificing performance. It's a win-win in my books.

![Turn Down The Watts](/content/images/2020/10/maxresdefault.jpg)