+++
author = "Batista Harahap"
categories = ["unraid", "server", "home", "plex", "media"]
date = 2020-02-03T14:16:34Z
description = ""
draft = false
image = "/images/2020/02/IMG_2373.jpeg"
slug = "supernas-with-unraid-at-home"
tags = ["unraid", "server", "home", "plex", "media"]
title = "SuperNAS with unRAID at Home"

+++


This started with a spare CPU and a dead motherboard. Had an Intel Core i3 6100 lying around with 16 gigs of memory sticks. Was leaning towards an AMD Hackintosh but Youtube convinced me [unRAID](https://unraid.net) is my next curiousity target. So I build a PC (again).

<a href="https://pcpartpicker.com/list/rfcJmg">PCPartPicker Part List</a>
<table class="pcpp-part-list">
  <thead>
    <tr>
      <th>Type</th>
      <th>Item</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="pcpp-part-list-type">CPU</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/hV7CmG/intel-cpu-bx80662i36100">Intel Core i3-6100 3.7 GHz Dual-Core Processor</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">CPU Cooler</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/xm22FT/intel-e97379-001-cpu-cooler-e97379-001">Intel E97379-001 CPU Cooler</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Motherboard</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/wqWrxr/biostar-racing-z170gtn-mini-itx-lga1151-motherboard-racing-z170gtn">Biostar RACING Z170GTN Mini ITX LGA1151 Motherboard</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Memory</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/mykwrH/gskill-memory-f42400c15s8gnt">G.Skill NT Series 8 GB (1 x 8 GB) DDR4-2400 Memory</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Memory</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/mykwrH/gskill-memory-f42400c15s8gnt">G.Skill NT Series 8 GB (1 x 8 GB) DDR4-2400 Memory</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Storage</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/vBkj4D/western-digital-green-480-gb-25-solid-state-drive-wds480g2g0a">Western Digital Green 480 GB 2.5" Solid State Drive</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Case</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/6wR48d/cooler-master-case-rc130kkn1">Cooler Master Elite 130 Mini ITX Tower Case</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Power Supply</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/6rc48d/corsair-vs-450w-80-certified-atx-power-supply-cp-9020170-na">Corsair VS 450 W 80+ Certified ATX Power Supply</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Wired Network Adapter</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/4sdqqs/intel-wired-network-card-e1g44htblk">Intel E1G44HTBLK PCIe x4 1000 Mbit/s Network Adapter</a></td>
    </tr>
  </tbody>
</table>

The parts list listed a standard Intel CPU fan but I hated the noise. I had a generic brand CPU water cooler I installed onto the CPU.

![Initial Tinker](/content/images/2020/02/IMG_2361.jpg)

This was my first time building a Mini ITC board. First impression: it's tiny, really. It only has 4 SATA ports and 1 NVMe slot on the backside of the motherboard. I'm limited to 5 storage devices which eventually will be:

* Parity Drive: 1x SATA SSD
* Cache Drive: 1x NVMe
* Storage Array: 3x SATA SSD

## Storage Drives

The issue that Youtubers talk about unRAID is exactly its name. The drives are not configured as RAID, it's essentially a JBOD. But I'm still new at this, I might be wrong. Another note is I'm using SSD's because I don't like the noise of spinning hard drives. Most people will use spinning hard drives for their larger capacities.

### Parity Drive

With unRAID you can have as much as 2 parity drives. This means you can loose up to 2 drives simultaneously and you won't loose data. You build the data on the replacements with 0's and 1's from the parity drives. 

The parity drive acts like an index of all the 0's and 1's on your array. Just like database indexes, writes will be slower than reads. Each time new data is written, the parity drive indexes them. Hence the need for the next drive type.

### Cache Drive

To mitigate slow writes, unRAID defer writes using this Cache Drive. All new data are written to this cache drive before eventually being written to its destination. A perfect illusion of speed mechanism.

### Storage Array

There is only 1 rule. The maximum size of any storage drive must not exceed the size of the parity drive. This means if you have a 1 TB parity drive, you can only use 1 TB storage drives or lower. unRAID supports mixing different sized storage drives as long as it's not larger than the parity drive.

Another gotcha is unRAID by default only spreads the data to 1 storage drive. When you create a share, you need to manually configure it to spread to more than 1 drive.

---

![Multi Port Ethernet](/content/images/2020/02/IMG_2365.jpg)

One of the things that I wanna do for this unRAID box is set it up as router for my home network. So I bought an Intel 4 Port Gigabit card to do this. This Intel card offloads all network related processing off of the CPU.

When I booted up the box, I was pleasantly surprised unRAID by default bonded both the Intel card and the onboard Ethernet into 1 interface. This bonded interface comes with fault tolerance and 5x 1000 Mbps.

I went a little bit overboard with the network setup so I can be sure Plex would be streaming comfortably. Although I haven't really tested it, was mainly toying with all the features unRAID offers.

![Generic Watercooler](/content/images/2020/02/IMG_2369.jpg)

![Generic Watercooler](/content/images/2020/02/IMG_2368.jpg)

To my surprise, this generic watercooler kept my CPU at 50 Degrees Celsius at 100% load. I won't know yet about its longevity but I'm glad it turns out great.

![unRAID Dashboard](/content/images/2020/02/unraid-dashboard.png)

Yeah if you look at the ethernet interfaces, `eth3` is showing up 10 Mbps. I don't haven't got around to troubleshooting it. I crimped the cables myself but I have to admit, the cables I used are recycled cables.

Also at the moment, I'm only using 1 SSD, this is in test drive mode. Apparently 1 SSD is enough to get started unlike what the forums is telling noobs.

## Plex Media Server

The single most defining reason why I'm motivated is Plex. Plex is worth the money spent for it. I always liked the idea of your media following you around wherever you go. With Plex I can watch my medias while on the train or waiting for a meeting. So many possibilities.

I'm a Plex Pass subscriber, with this I can enjoy hardware (GPU) accelerated transcoding. But, to set it up is not as straightforward. Did I tell you that unRAID supports Docker out of the box? The screenshot of my dashboard shows Plex and the other 2 apps running as docker apps.

Now there are some few things that need to happen when you want to use hardware acceleration: _Intel Quick Sync must be supported by the CPU_. Read more [here](https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video). My CPU is an Intel Core i3 6100 and it supports Quick Sync. I'm gonna be offloading the transcoding to its iGPU.

My research told me the best GPU to do transcoding is Nvidia P2000.

![Enable Hardware Transcoding in Plex](/content/images/2020/02/plexpass-settings-docker.png)

I added a setting called `HW Accel DRI Card` for Docker to `forward` the host's `/dev/dri` to the container. Another thing you should do is to add some entries to unRAID's `go` file.

```shell
$ modprobe i915 && chmod -R 777 /dev/dri
$ vim /boot/config/go
# Add these lines
modprobe i915
chmod -R 777 /dev/dri
```

![Hardware Acceleration in Plex](/content/images/2020/02/Screen-Shot-2020-02-04-at-04.07.37.png)

If everything is ok, when you go to Plex's `Activity > Dashboard`, you will see that `hw` status confirming that video transcoding is offloaded to the GPU. You'd see that CPU usage is significantly lower.

---

Next steps would be to run out unRAID's trial period and buying a proper license. It's definitely worth my money. Some projects I have in mind to do with the box:

1. Set up VPN Gateway
2. Set up DNS-over-HTTPS
3. Delegate routing from my FO modem to the unRAID box
4. Add more drives and configure unRAID properly

Using an Intel Core i3 processor (the lowest spec of its generation) is pretty easy on the power usage. Max power usage is projected at 111 Watts. It won't compete with a Raspberry Pi for power but it's quite low profile to my liking.