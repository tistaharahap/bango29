+++
author = "Batista Harahap"
categories = ["Android", "code", "compile", "cyanogenmod", "disk", "source", "space", "swap"]
date = 2013-07-28T10:55:07Z
description = ""
draft = false
slug = "fetching-android-cyanogenmod-sources-on-a-512-mb-vm"
tags = ["Android", "code", "compile", "cyanogenmod", "disk", "source", "space", "swap"]
title = "Fetching Android CyanogenMod sources on a 512 MB VM"

+++


Last night, I synced CyanogenMod's Android source code into my laptop. It took ~12 hours to complete. The Internet connection I have is 6 Mbps and to download ~9 GB of source code shouldn't take that long. So I created a 512 MB VM on my <a href="http://www.digitalocean.com" target="_blank">Digital Ocean</a> account.

I opted for the US$ 5/month VM which is a 1 Core, 512 MB RAM and 20 GB SSD. The VM <strong>DOES NOT</strong> have any swap space.

You know what happened? A few actually:
<ul>
	<li>Out of Memory while fetching <code>git://github.com/CyanogenMod/android_vendor_qcom_opensource_v8</code></li>
	<li>Out of Disk Space after fetching the above</li>
</ul>

Android's source code has gotten large and it's very much not recommended even to do the fetching (<code>git pull</code>) on such a low spec VM. You can easily solve the out-of-memory issue by adding a swap partition. Being an SSD VM, the performance degradation is acceptable.

However, you can't cheat out-of-disk-space at all. The solution is simple: Get a bigger spec VM.

Just as a side note, here's how to have a file swap partition added on runtime:
<pre lang="bash">
$ dd if=/dev/zero of=/mnt/swap512mb bs=1024 count=524288
$ chmod 600 /mnt/swap512mb
$ mkswap /mnt/swap512mb
$ swapon /mnt/swap512mb
</pre>

Now you have a temporary swap partition, do a <code>cat /proc/meminfo</code> to confirm.