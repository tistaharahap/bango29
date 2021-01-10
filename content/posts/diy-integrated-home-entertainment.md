+++
author = "Batista Harahap"
categories = ["cubieboard", "raspberry pi", "home", "entertainment", "automation", "diy", "arm"]
date = 2014-08-16T12:17:02Z
description = ""
draft = false
slug = "diy-integrated-home-entertainment"
tags = ["cubieboard", "raspberry pi", "home", "entertainment", "automation", "diy", "arm"]
title = "DIY Integrated Home Entertainment"

+++


I've always wanted my own Home Entertainment solution before I bought my Cubieboard. Now, after buying a Raspberry Pi, what I want came true. With some research and a weekend, I got it up and running perfect.

What I have in my disposal for this to happen are:

1. Cubieboard A10 with [Cubian](http://cubian.org) - [NAS](http://en.wikipedia.org/wiki/Network-attached_storage), [nginx](http://nginx.org), [CouchPotato](https://couchpota.to/), [Transmission](http://transmissionbt.com), [Headphones](https://github.com/rembo10/headphones) and [SickBeard](http://sickbeard.com/)
2. Raspberry Pi B with [Raspbmc](www.raspbmc.com)
3. USB Hard Drive - Attached to the Cubieboard
4. [OpenWRT](https://openwrt.org) Wifi Router - or any router you can manipulate DNS with
5. Another Wifi Router - because the main router's coverage is spotty upstairs, Raspberry Pi is attached to this router
6. TV with HDMI (obviously) - spare HDMI input for the Raspberry Pi

Cubieboard and Raspberry Pi are connected using LAN cables. I'm not too sure about the Wifi's signal strength.

---

## Installation & Configuration

Using the links I provided above, we can deep dive into installing each service into each components. I'm sharing the recipe to make all of them work well together.

## Cubieboard

1. Consider using an externally powered USB hard drive. Cubieboard (and Raspberry Pi) are sensitive to power consumption should it go beyond 2 Amps.
2. I would recommend a 2 A power supply but 1 A will do.
3. I installed Cubian to the NAND partition. I don't have a spare microSD card available.
4. When all of the services are started, the 1 GB memory will run out quickly leaving only a few megabytes free. Make a swap file, like [here](http://www.bango29.com/cubieboard-part-1/#swapfile). Instead of creating at the external drive, I created the swap at the root of the NAND partition.

## Raspberry Pi

1. Consider using heatsinks to prevent overheating the chips if the device is to be ran 24/7.
2. **MUST USE** at least a 1 Amp power supply.

## Raspbmc

1. After booting the first time, make sure it's set a static IP Address by using Raspbmc Config Program available conveniently at XBMC's *Programs*.
2. I don't have a physical remote (and keyboard) to control XBMC. I did plug a mouse to it but that's just about it. I'm using the [Official XBMC app](http://wiki.xbmc.org/index.php?title=Official_XBMC_Remote/iOS) on my iPhone and [XBMC Constellation](https://itunes.apple.com/id/app/xbmc-constellation/id437807301?mt=8) on my iPad to control XBMC.

## Cubian

1. Mount the external USB Hard Drive and Swapfile at boot time. Add entries to `/etc/fstab`.
2. Give it a static IP, modify `/etc/network/interfaces`.
3. I encourage **NOT** to use `FAT32` partitions. It keeps unmounting. I would suggest to use `EXT4` for all partitions.

### Samba

Since we are using Samba to share the Hard Drive, it won't matter which filesystem is used for the USB External Hard Drive partitions. Might as well be native to Linux and release yourself of funky implementations.

In my case, I have 2 partitions mounted at `/media/EVO` and `/media/Linx`. Your mileage may vary. Here is my `smb.conf` as a template.

```
[global]
   workgroup = Bango29
   server string = %h server
   dns proxy = no
   log file = /var/log/samba/log.%m
   max log size = 1000
   syslog = 0
   panic action = /usr/share/samba/panic-action %d
   encrypt passwords = true
   passdb backend = tdbsam
   obey pam restrictions = yes
   unix password sync = yes
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
   pam password change = yes
   map to guest = bad user
   usershare allow guests = yes
   security = user

[EVO]
   comment = Movies, TV Shows and more
   path = /media/EVO
   create mask = 0777
   directory mask = 0777
   read only = no
   writable = yes
   browsable = yes
   guest ok = yes
   guest account = cubie
   guest only = yes
   public = yes

[Linx]
   comment = More Movies, TV Shows and more
   path = /media/Linx
   create mask = 0777
   directory mask = 0777
   read only = no
   writable = yes
   browsable = yes
   guest ok = yes
   guest account = cubie
   guest only = yes
   public = yes
```

I set all of my shares to be available publicly, browsable and a `guest` user is enough.

### Transmission

Who doesn't love [Transmission](http://www.transmission-bt.com)? I would say subjectively, this is the best Torrent client I've used so far.

Some will argue that [Deluge](http://deluge-torrent.org/) is a more suiting and Pythonic choice. I didn't care. My simple reason will be because my wife is already familiar with Transmission.

### CouchPotato

I am relieved that such application exists. I would just put in any movie I'd want to download and CouchPotato will rigirously scour the internet. It can even determine if the found item is suited to my liking or not. It's very convenient to say the least.

Whenever a match is found, it will make an API call to the Transmission daemon to download it if it's a torrent.

**More Win**: It has integration with [Pushbullet](http://pushbullet.com). For any event, it will push something to my iPhone or my Chrome for notifications. Sweet!

### SickBeard

Same as CouchPotato, only this one is for TV Shows. Need I say more?

### Headphones

Same as SickBeard, only this one is for music. Need I say more?

## DNS and nginx

So I wanted all the above services with a choosen subdomain that does not exists on the Internet. I only want it to exist locally. Praise The Lord for [OpenWRT](https://openwrt.org) and [nginx](http://nginx.org).

The subdomains were:

* movie.bango29.lan - CouchPotato
* music.bango29.lan - Headphones
* serial.bango29.lan - SickBeard
* torrent.bango29.lan - Transmission Web GUI
* tv.bango29.lan - Raspbmc

Here is where the DNS magic happened on OpenWRT.

![OpenWRT DNS Aliases](/content/images/2014/Aug/Screen-Shot-2014-08-17-at-2-03-55-AM.png)

nginx is used to reverse proxy the subdomains above to specific local ports where the services are serving. A simple nginx config file can be like below.

```
server {
	server_name movie.bango29.lan;
	listen 80;
	listen 8080;

	location / {
		proxy_pass http://127.0.0.1:5050/;
	}

	location ~ /\.ht {
		deny all;
	}
}
```

---

So the above is the current setup for my Integrated Home Entertainment system. My next venture will be buying an HDMI audio multiplexer. Right now my 5.1 speaker system is only outputting in stereo. It'd be complete when it outputs in truly 5.1.

Signing off with a picture of my Raspberry Pi after unboxing. USB TTL cable is a must have really. Makes everything a whole lot easier.

Cheers!

![Raspberry Pi](/content/images/2014/Aug/rpi.jpg)