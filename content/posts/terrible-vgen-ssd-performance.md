+++
author = "Batista Harahap"
categories = ["vgen", "ssd", "gigabit"]
date = 2020-04-01T15:50:48Z
description = ""
draft = false
image = "/images/2020/04/vgenssd-1.jpeg"
slug = "terrible-vgen-ssd-performance"
tags = ["vgen", "ssd", "gigabit"]
title = "Terrible Vgen SSD Performance"

+++


The title is not clickbait, it is what it is. For my [Unraid box](https://bango29.com/unraid-semi-pro-home/), I used 3 SSD's I bought from Vgen. The first SSD was bought a year ago, it was a data drive for my work computer. The other 2 SSD's was bought a few months ago.

As it turns out, not all SSD are made equal, even if they were from the same brand. The packaging says it's 550 MB/s reads and 477 MB/s writes. Here's a bit more detail about the drives I bought from `fdisk`.

```
$ fdisk -l # Redacted some entries for brevity
Disk /dev/sdb: 447.13 GiB, 480103981056 bytes, 937703088 sectors
Disk model: VGEN08SM18EU480G
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start       End   Sectors   Size Id Type
/dev/sdb1          64 937703087 937703024 447.1G 83 Linux


Disk /dev/sdc: 447.13 GiB, 480103981056 bytes, 937703088 sectors
Disk model: V-GEN12SM19AR480
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start       End   Sectors   Size Id Type
/dev/sdc1          64 937703087 937703024 447.1G 83 Linux


Disk /dev/sdd: 447.13 GiB, 480103981056 bytes, 937703088 sectors
Disk model: V-GEN12SM19AR480
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start       End   Sectors   Size Id Type
/dev/sdd1          64 937703087 937703024 447.1G 83 Linux
```

As you can see `/dev/sdb` was unique while `/dev/sdc` and `/dev/sdd` were the same model. You can't tell how different those 2 models were just by looking at this information. The models are:

* VGEN08SM18EU480G
* V-GEN12SM19AR480

For [my Hackintosh](https://bango29.com/hackintosh-2019-2020-msi-z370-gaming-m5/) I just bought a new PCIe network card. It's an HP NC360T Pro 1000 with an Intel chip and dual ports. The reason for the purchase was because I got a pleasant surprise from my ISP. They emailed me last night that there were disruptions in my area, the next morning here's what I got.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Got a love letter from the ISP last night about a disruption in service, might take 48 hours to resolve. Woke up this morning and internet is already up. Did a speedtest and now my internet connection is as fast as my LAN 😍😍😍 <a href="https://t.co/aWtr8BM0lJ">pic.twitter.com/aWtr8BM0lJ</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1245225457257025541?ref_src=twsrc%5Etfw">April 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

A welcomed surprise! What's not welcomed was whenever the Internet bandwidth is maxed out, the fans on my Hackintosh screamed. I was using the onboard Ethernet, a Killer E2500 Gigabit LAN controller. The onboard LAN chip was hogging the CPU. So I decided to say good bye the onboard LAN. When I installed the new PCIe network card I bought from [this seller](https://www.tokopedia.com/interfacemaster/lan-card-intel-dual-port-gigabit-hp-nc360t-pro-1000-pt-network-adapter) in Tokopedia, the CPU hogging was gone.

But, another issue came up. I restarted to Windows to install a new game I purchased from Steam. The Windows installation was using the same second Vgen SSD model that was on my Unraid box. I proceeded to download the game. I was downloading at gigabit speed for sure but the download keeps stalling after a few seconds and then resuming again. At the moment I never thought my SSD was a bottleneck. I thought my ISP is throttling long running high bandwidth downloads.

My first thought was right. Here's a disk speed test from my Unraid boxes.

```
$ hdparm -tT /dev/sdb

/dev/sdb:
 Timing cached reads:   20280 MB in  1.99 seconds = 10191.91 MB/sec
 Timing buffered disk reads: 1136 MB in  3.00 seconds = 378.29 MB/sec
$ hdparm -tT /dev/sdc

/dev/sdc:
 Timing cached reads:   18640 MB in  1.99 seconds = 9360.94 MB/sec
 Timing buffered disk reads: 142 MB in  3.02 seconds =  47.04 MB/sec
$ hdparm -tT /dev/sdd

/dev/sdd:
 Timing cached reads:   18120 MB in  1.99 seconds = 9098.61 MB/sec
 Timing buffered disk reads: 124 MB in  3.02 seconds =  41.13 MB/sec
$ hdparm -tT /dev/sdb

/dev/sdb:
 Timing cached reads:   19370 MB in  1.99 seconds = 9729.26 MB/sec
 Timing buffered disk reads: 1106 MB in  3.00 seconds = 368.33 MB/sec
```

The drives `/dev/sdc` and `/dev/sdd` were in the 40s MB/sec throughput. I was very very disappointed to have bought SSD's with the speed of mechanical drives. The download stalls I experienced were caused by the SSD. My next test was to copy files from my Hackintosh to the Unraid box. It was stalled as well. I had the same stalling before but never thought it was the SSD that was the culprit.

The positive side of things is I am assured that mechanical drives are ok for NAS because streaming content for Plex wasn't really affected. The good thing about Unraid is that it provides a cache drive feature to combat throughput, I haven't used it but now I can see the importance.

---

![Bad Vgen SSD](/content/images/2020/04/vgenssd.jpeg)

Don't trust the packaging, it's a lie. I guess this is what you get buying generic brands. There's so many generic brands in distribution in Indonesia for SSD's, memories, etc. You can only be sure after you test.

After knowing how slow it is, the next question would be: would it last?