+++
author = "Batista Harahap"
categories = ["hack", "dns", "openvpn", "expressvpn", "gateway", "network"]
date = 2020-01-06T11:41:48Z
description = ""
draft = false
image = "/images/2020/01/positif-1.png"
slug = "overkilling-privacy-protection-with-expressvpn-and-virtualbox-on-a-hackintosh"
tags = ["hack", "dns", "openvpn", "expressvpn", "gateway", "network"]
title = "Overkilling Privacy Protection with ExpressVPN and VirtualBox on a Hackintosh"

+++


I live in Indonesia. Here, ISP and telcos likes to do the absurd: hijacking DNS queries. Public DNS services like Google (8.8.8.8), Cloudflare (1.1.1.1), OpenDNS (208.67.222.222), etc are hijacked at the ISP level. Even more so, if you're on Telkom Indihome, they will also hijack websites you visit with their content. All the other telcos are doing the same thing for our paid data plans. So I thought why not overkill this, I got plenty of RAM, CPU Cores and storage on my Hackintosh.

Here's my previous post of [my 2020 Hackintosh](https://bango29.com/hackintosh-2019-2020-msi-z370-gaming-m5/). It's beefy and it will serve me well for this exercise.

## The Idea

I enjoy [ExpressVPN](https://www.expressrefer.com/refer-friend?referrer_id=37517983&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard) VERY much. 

DISCLAIMER: the link is an affiliate link, you will get 30 days free and so do I when you sign up.

Other than it's available for all my gadgets, it's fast. I got a 150 Mbps connection and ExpressVPN will saturate the pipe. The latency does have an effect when I'm trading but nothing too worrying.

Back to business, what I wanna have are these 2 components:

1. ExpressVPN as a network gateway
2. Cloudflare 1.1.1.1 for DNS over HTTPS/TLS

I wanted to execute using Raspberry PI 4 but I don't have any. The next best thing is to use [VirtualBox](https://www.virtualbox.org/wiki/VirtualBox) to set up 3 VM's running Ubuntu 18.04 LTS. Part 2 of this exercise would be to actually use Raspberry PI 4s.

So why is this overkill? ExpressVPN already has an app for Macs right? I'm already using it but then only devices with the app would be able to do VPN. I want the VPN to be available transparently, nothing should ever be needed to be installed.

As a bonus, if I decided to changes my iTunes Store region to the US, I can watch US Netflix on my Apple TV. Food for thought for now.

**ATTENTION:** For fellow Indonesians on Indihome reading this, you want this at your home, why would you want to be advertised for a connection you've paid? Why would you trust the ISP's good will not to do funny business?

## What You Need

I'm gonna save you time, I went ahead and created OVA images you can use directly with your VirtualBox. Whether you're running a Mac, Windows or any other Host OS that VirtualBox and other virtualization software supports, you're good.

* Router VPN - This will act as your network gateway - [Download here](https://drive.google.com/file/d/1vs3YsCdbT-fpCFxVkolQCX67jne0W1w8/view?usp=sharing)
* DNS over HTTPS/TLS - This will act as your DNS server - [Download here](https://drive.google.com/file/d/1rOtQDIZlsVlHh62a_D3MMn72EVPeF-nX/view?usp=sharing)

Both images username/password are:

```
Username: routervpn
Password: bango29.com
```

## Router VPN

The VM is configured to use the IP `192.168.100.10`. Do below to change.

```shell
$ sudo vim /etc/netplan/50-cloud-init.yaml # Adjust to your network
$ sudo netplan apply
```

Login to your and go the address below.

[https://www.expressvpn.com/setup#manual](https://www.expressvpn.com/setup#manual)

You will see your username and password to connect to ExpressVPN through OpenVPN. Take note to configure your VPN connection. The image includes OpenVPN configs for USA and Singapore locations. You can add your own connections to `/etc/openvpn`. Rename the `.ovpn` extension to `.conf`.

On your `routervpn` machine, do the following.

```shell
$ sudo vim /etc/openvpn/login # First line for username, second for password
$ sudo systemctl enable openvpn@sg # For Singapore location, openvpn@usa for USA
$ sudo systemctl start openvpn@sg
```

### Your Client Machines

Depending on your OS, change your network gateway to the `routervpn` IP address. Google an IP checker and you'll see that your IP is now matching the corresponding ExpressVPN location you chosen earlier.

## DNS Over HTTPS/TLS

This machine is simpler. You only need to change the static IP assigned to it.

```shell
$ sudo vim /etc/netplan/50-cloud-init.yaml # Adjust to your network
$ sudo netplan apply
$ sudo vim /etc/cloudflared/config.yml # Change proxy-dns-address to your IP
$ sudo systemctl enable cloudflared
$ sudo systemctl start cloudflared
```

Next step depending on your OS, change your DNS resolver to the IP address you set up for the machine.

## Run VMs at Boot

I won't go into details, this gist is very clear.

<script src="https://gist.github.com/str8edgedave/b0b96e12396aaa7d383456778079ee7b.js"></script>

---

This is definitely overkill. While I was writing the blog post, I wondered that all this is possible with Docker. If port forwarding is something Docker doesn't object, this can work. While for the DNS over HTTPS/TLS would surely work. Another exercise for another time.

Here's logo for you.

![Fuck this shit!](/content/images/2020/01/positif.png)