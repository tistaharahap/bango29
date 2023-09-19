+++
author = "Batista Harahap"
categories = ["unraid", "build", "pc", "nas", "server"]
date = 2023-09-19T19:36:27Z
description = ""
draft = false
image = "/content/images/2023/09/rm.jpg"
slug = "Yet Another Unraid Build"
tags = ["unraid", "build", "pc", "nas", "server"]
title = "Yet Another Unraid Build"

+++

Why right? Short answer, I had 2 server builds and 1 of them smoked in the literal sense. Smoke was coming from the CPU socket and I had to put the air purifier in max to get rid of the awful smell. It was supposed to be a ProxMox build to host all of my VMs in my home lab. What an epic fail!

## Smoked Build

It was my first time ever building PCs that went horribly wrong. But the good news is I can salvage most everything from the build except for the PSU, CPU, Motherboard and GPU. I remember I had a slip of the fingers when I was installing the GPU into the motherboard but I was sure I didn't knocked any components in the GPU. To be safe, I wrote off that old Quadro GPU.

Although the smoke looked like it came from the CPU socket, I can't be 100% certain the CPU caused it. What I know for sure is that the CPU has been showing problem ever since I bought it. It's an AMD Ryzen 5700G that was constantly giving blue screens when being used for light gaming. The motherboard is a really low end Gigabyte B550m motherboard which I'm not too concerned about.

Better be safe than sorry, the smoked build is decommissioned.

## The Other Build

This is the build that is the Unraid build, or supposedly. I have been having problems with the build for a while. Every time I needed to restart the PC, it would just hang randomly. I had to connect a monitor to figure out. It's not Unraid's fault, I suspect the motherboard eventually gives up after being always on for years.

So at this point I had 2 builds and both of them failed. To add insult to injury, on this build, there were 2 hard drives that have failed. I bought 4x 2TB HDDs and to date I have had 3 of them failed, luckily the 1st failure was returned and replaced with a new one since it failed just a few days after the purchase. Unlucky for the other 2 unfortunately. Oh and 1 of the failing drive is the parity drive.

I said to myself, for the next build, I'm moving away from HDDs and will strictly use SATA SSDs. It's low power, noiseless but not supported by Unraid because Unraid says Unraid will wear out SSDs writes quickly. Fortunately for me, I started my first Unraid build with a couple of SSDs and to date, I never had any problems with SSDs, in fact not 1 failed.

## Unraid, Yet Again

A few days ago, I had a plan to just use Unraid for NAS and use ProxMox for applications (Containerized or VM). My ProxMox experience when trying to build a hackintosh as a VM in it was great! It's a bit more complex to do hardware passthroughs but having that kind of control is neat and it pushes me to learn something new. That's when the smoke build happened. It was suppose to be the ProxMox build.

On that day, I had zero build, both builds failed at exactly the same time. What are the odds? And I consigned myself having to say good bye to the data stored in the failed HDDs. There were no critical data stored and since the parity drive was one of the failing drive, I just bit the bullet.

### Picking SSD Drives

This is an important step after having burned and knowing that SSDs are more expensive than HDDs. The most storage I could find available for SATA SSDs was 2TB. This was enough for the home lab needs, I eventually bought 6x 2TB SATA SSDs, the max that any modern motherboard would allow. I know I don't need a fast write throughput so I didn't have to choose SSDs with fast cache. I just needed to find it cheap.

It doesn't make any sense to optimize for speed on a 1GBe network at home. The network bandwidth wouldn't be able to saturate the drives high throughput even with cheap SSDs.

What's important though is their lifespan. The drives I bought were TLC NAND drives, 1 of 6 is a 3D cell, while the other 5 are regular. The 3D cell drive is supposedly more write resistant up to 3x more than regular NAND drives, I should use that drive as a parity drive but I had that knowledge all too late, 1 of the regular drive was already a parity and I already filled it up with data. The 3D cell drive was shipped later.

This gives opportunity for me to think about expanding the number of drives so I can have a second parity drive. That involves getting myself a SAS controller PCIe card that is not readily available in Dubai. At least not used, I don't need to buy new. It's good that I now have urgency so I can do more than just read about what's compatible with Unraid.

### Motherboard & CPU

I thought hard about this. As a consumer, you don't really care about PCIe lanes provided by the Motherboard and CPU, you don't need to care because there will always be just enough for your peripherals which usually would only be a GPU plugged into the primary 16x slot. As a server though, the number of PCIe lanes is what limit your expansion capability.

This build is powered by an AMD Ryzen 3700X, an 8 core/16 thread CPU capable of giving 24 PCIe lanes. This particular CPU can be paired with a B550 or X570 chipset equipped motherboard, both of which will have different number of PCIe lanes given by the chipset and it's PCIe version.

However, I'm not concerned with the chipset's PCIe lanes, they're not directly connected to the CPU which means there will be latency/bottleneck caused by this. I hardly use the chipset's PCIe lanes when building a PC except for specific use cases like using a TV919 Wifi/Bluetooth PCIe card so that it works out of the box for a hackintosh.

Having a TRX40 motherboard with a Threadripper CPU seems sexy at this point. They come with up to 64 cores and 88 PCIe lanes with Quad Channel DDR4. But, it's damn right overkill and expensive. I haven't had a use case that would require me to need them yet. You see, I'm all about hosting my own apps with my own hardware because the cloud is cheap to begin with but expensive in the long run. Before this gets serious, I need to get serious with my internet connection at home first.

So I settled with a B550 Asus motherboard, VRMs are high quality and I suspect will last at least 2-3 years.

### Case & Cooling

I knew what I want, since I don't use HDDs anymore, I can go for a small ATX case with plenty of airflow and enough room to double tape the SSDs. I got myself an off brand case that gets the job done. Best thing I love about the case is that it fits my Noctua NH-D15 CPU cooler. Why though right?

My use of the apps (Docker or VM) are mostly bursty in nature. I got MongoDB running as a Docker container in Unraid which I use as the primary database for me when doing my development. Thanks to Tailscale, that MongoDB container is available from anywhere in the world for me to access, although usually it's still in the same subnet. Since I don't do testing (which needs MongoDB) all the time, I don't need performance all the time, I only need it when I need it. This fits perfectly with AMD's Precision Boost Overdrive (PBO) which I enabled from the BIOS.

It might seem trivial but when you have hundreds of test cases needed to be run whenever you have changes, you'll be glad that the bottleneck wouldn't be the database.

Idle temperature of a Ryzen 3700X using a Wraith air cooler that comes with the CPU is around 60 degrees C in this case. I started with the wraith to get a baseline. When I replaced it with a Noctua NH-D15, it dropped to to 50 degrees C, that's a 10 degrees C delta that will help in extending the life of the CPU.

At load the temperature fluctuates from 70-80 degrees C with the Wraith cooler while with the Noctua NH-D15 it's steady between 50-60 degrees C. I measured this when installing VMs.

The case and the CPU cooler meant I won't have to worry about temperatures ever.

### GPU

It's a dilemma that's been eating me ever since I built my first Unraid build. Do I need a GPU? Tried to make do with an Nvidia Quadro P400, the one that I suspect smoked my Proxmox build. It was great, H264 videos are transcoded easily but not so great with X265 videos. Been looking for an Nvidia GTX 1050 Ti but it's so expensive these days, doesn't make any sense, at all. That is until I found an Nvidia GTX 1650 for AED750 which is a steal! Didn't think twice, bought it!

The only catch with a 1650 is I can only have 3 parallel transcoding streams which is enough for my use case. Plugged it into the machine and it worked instantly after I changed the GPU ID in the Plex containers. It worked brilliantly for transcoding, instant gratification huh? Haha.

## Full Specs

This is the final full specs for the build:

* AMD Ryzen 3700X
* Asus TUF Gaming B550-Plus
* 32GB DDR4 Kingston Fury X RAM
* 5x Patriot P210 2TB SATA SSD
* 1x Silicon Power Ace A55 2TB SATA SSD
* EVGA 450BR 80+ Bronze 450W PSU
* Zotac Gaming GeForce GTX 1650 OC GDDR6
* Noctua NH-D15 CPU Air Cooler 

Memory usage with all the VMs and containers is steady at around 45-50%, this is making me slightly uncomfortable. When it gets more than 75%, it's time to add another 32GB to round up to 64GB. I should've just commissioned my apps as Docker containers but I have 4 dedicated VMs for apps that receives a lot of usage. For instance, I used to run Tailscale as a container but then I realized that having a VM just for it gives me a chance to learn more about optimizing my network. Started reading about [jumbo frames](https://www.techtarget.com/searchnetworking/definition/jumbo-frames).

---

The knowledge here have little to do with my day-to-day programming work but learning how stuff works never ceases to amaze. A few weeks ago, something came in the mail. I forgot I bought this but when it came, I remember perfectly what I can do with it, it's a [Beepy](https://beepy.sqfmi.com/). The convenience of a Blackberry keyboard and a small monochrome display powered by a [Raspberry Pi Zero board](https://www.raspberrypi.com/products/raspberry-pi-zero/).

Beepy coupled with an Unraid server is limitless. As long as the Beepy device gets a Wifi signal, I have a terminal that's always available. I'm thinking about coding a push to talk terminal app for my son, like an intercom. My son can always send me a voice message using it. Send the recorded audio to a container app on the Unraid build which will subsequently send a Telegram message to me. This is possible because the Pi has Bluetooth, or i just get a USB combo mic/earbuds.

I love having a home lab, it pushes me to learn more.
