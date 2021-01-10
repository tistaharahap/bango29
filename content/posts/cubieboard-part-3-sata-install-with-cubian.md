+++
author = "Batista Harahap"
categories = ["hack", "cubieboard", "cubian", "sata", "micro-sd"]
date = 2013-12-22T13:15:33Z
description = ""
draft = false
slug = "cubieboard-part-3-sata-install-with-cubian"
tags = ["hack", "cubieboard", "cubian", "sata", "micro-sd"]
title = "Cubieboard A10 - Part 3 - SATA Install with Cubian"

+++


Managed to get a temporary micro-SD Card lending from my wife and so a new episode with my Cubieboard starts. First off is to get the image writing to the micro-SD Card correctly.

The problem is, I don't have the SD Card adapter for the micro-SD Card. My Macbook has an SD Card reader but it's useless without the adapter. So I rebooted my wife's Galaxy S2 into the recovery ROM and mounted the micro-SD Card to my Macbook.

I downloaded [Cubian r7](http://cubian.org/downloads/) and went ahead with the process. The micro-SD Card was mounted from `/dev/disk4`, I had to unmount it first, reformat with a single `FAT` partition and it's all done within the almighty `Disk Utility`.

**WARNING:** The instructions below is only for Cubieboard A10 owners. For A20 owners, please observe with caution. Adjust to your own configs.

## Write to micro-SD Card

Long story short, I tried to write the image using `dd` to the micro-SD Card only to fail when I plugged it in into the Cubieboard. It kept booting to `NAND`. So I guess having the Galaxy S2 as a memory card ready was not a lifesaver.

I figured why not use the micro-SD Card reader of the Cubieboard, which I finally did. Here are the steps I took.

<pre>$ dd if=Cubian-base-r7-arm-a10.img of=/dev/mmcblk0 bs=4096
$ sync
$ reboot</pre>

It worked. My Cubieboard loaded the Cubian on the micro-SD Card. After getting its IP from my router, I tried to SSH into the board. To my surprise I couldn't SSH to port 22. I thought maybe something is wrong and it was me. I didn't read enough of Cubian's docs. The default SSH port is 36000.

<pre>$ ssh -p 36000 -v cubie@192.168.1.x</pre>

Cubian is shipped with a locked `root` account. However, the `cubie` account have `sudo` privileges. The default password is also `cubie`.

After getting in, you should also do these:

<pre>$ apt-get update && apt-get upgrade -y</pre>

## Install to NAND

Before getting the image into my SATA drive, I need to verify a few things and also do a NAND install of a clean Cubian so I can revert to it anytime I need to.

<pre>
$ apt-get install cubian-nandinstall
$ cubian-nandinstall
</pre>

After 2 reboots and I'm already booting from NAND. Here's a few things I said I need to verify:

* `uEnv.txt` is on `/boot/` meaning I can meddle with boot arguments to changes `rootfs` for instance.
* Unlike my previous distro, SATA support is compiled into the kernel and NOT as a module. I can boot `rootfs` from SATA :D

## Install to SATA

Can't believe it's this simple after all.

### Format The SATA Drive

**Note**: Only if this is necessary.

<pre>$ mkfs -t ext4 /dev/sda1</pre>

### Write to SATA

<pre>
$ dd if=/dev/nandb of=/dev/sda1 bs=1M
$ sync
</pre>

**WARNING**: For A20 owners please follow the instructions below instead. All credits to Martin from the comments below. More info, please read the comment.

<pre>
$ dd if=/dev/nandc of=/dev/sda1 bs=1M
$ sync
</pre>

### NAND Boot Arguments

We're gonna need to modify `/boot/uEnv.txt` to boot the `rootfs` from `/dev/sda1`.

Before
<pre>console=tty0
extraargs=console=ttyS0,115200 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x800p60 root=/dev/nandb rootwait panic=10 consoleblank=0</pre>

After
<pre>console=tty0
extraargs=console=ttyS0,115200 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1920x1080p60 root=/dev/sda1 rootwait panic=10 consoleblank=0</pre>

I changed 2 things:

* Enlarge the HDMI output to 1080p
* Changed the `rootfs` to `/dev/sda1`

Now Reboot
<pre>$ reboot</pre>

## Resize SATA Partition Size

When you login to the board, the partition size only 4.1 gigs same as the NAND partition it mirrored. We need to resize the partition so the whole storage is usable.

<pre>$ resize2fs /dev/sda1</pre>

## Done

Now I have a SATA Install of Cubian. Yeay!

<script type="text/javascript">
var amzn_assoc_placement = "adunit0";
var amzn_assoc_search_bar = "true";
var amzn_assoc_tracking_id = "bango29-20";
var amzn_assoc_ad_mode = "manual";
var amzn_assoc_ad_type = "smart";
var amzn_assoc_marketplace = "amazon";
var amzn_assoc_region = "US";
var amzn_assoc_title = "Buy Now";
var amzn_assoc_linkid = "37ddc99aabea4f2a5b575620b01a230c";
var amzn_assoc_asins = "B00JUG7R60,178328157X,B00ISKS416,B00KCS8ZUC";
</script>
<script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>