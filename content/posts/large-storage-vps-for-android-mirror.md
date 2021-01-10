+++
author = "Batista Harahap"
categories = ["Android", "build", "compile", "cyanogenmod", "hosting", "large storage", "vps"]
date = 2013-07-29T12:05:26Z
description = ""
draft = false
slug = "large-storage-vps-for-android-mirror"
tags = ["Android", "build", "compile", "cyanogenmod", "hosting", "large storage", "vps"]
title = "Large Storage VPS for Android Mirror"

+++


Been trying to build my own Android build server only to find insufficient resource to do so like <a href="http://www.bango29.com/go/blog/2013/fetching-android-cyanogenmod-sources-on-a-512-mb-vm" target="_blank">here</a>. After some digging around, I found the perfect deal for this to happen.

I found <a href="http://reliablehostingservices.net/vps.php" target="_blank">Reliable Hosting Services</a> while reading through some blog posts <a href="http://www.lowendbox.com/blog/reliable-hosting-services-3month-512mb-ram-100gb-hdd-in-baltimore-md/" target="_blank">here</a>. The specs I went for is below:
<ul>
<li>2 CPU Cores</li>
<li>1 GB RAM</li>
<li>200 GB Disk</li>
<li>1000 GB Bandwidth</li>
<li>Price: US$ 5/month</li>
</ul>

Got it for cheap using a coupon code available at the blog post link I posted above.

Now for the last round of cheap and cheats, instead of checking out the CyanogenMod source codes, I did a full mirror. It's faster to download and more memory friendly.
<pre lang="bash">
$ repo init -u git://github.com/CyanogenMod/android.git -b cm10.1 --mirror
</pre>

It's still downloading all the source codes now and it's doing so a lot faster than before.