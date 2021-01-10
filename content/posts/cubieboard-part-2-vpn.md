+++
author = "Batista Harahap"
categories = ["hack", "cubieboard", "pptp", "vpn", "remote", "python", "ubuntu", "tunnel"]
date = 2013-12-20T11:37:02Z
description = ""
draft = false
slug = "cubieboard-part-2-vpn"
tags = ["hack", "cubieboard", "pptp", "vpn", "remote", "python", "ubuntu", "tunnel"]
title = "Cubieboard - Part 2 - VPN"

+++


So after setting my Cubieboard for my liking, another thing I want is to be able to access it anywhere and anytime. The trouble is, the ISP I am with right now is blocking all incoming ports, needs a work around.

After some browsing and also from past experiences, I feel `PPTP` is my best bet. Incredibly easy to implement from a client/server perspective. The challenge is to keep the tunnel open at all times.

I'm using [Digital Ocean](https://www.digitalocean.com/?refcode=2bac813f3a2d) to host the `PPTP` server and it so happens they already have a tutorial in their blog right [here](https://www.digitalocean.com/community/articles/how-to-setup-your-own-vpn-with-pptp). I'm just customizing based on that blog post.

The VM is using Ubuntu 13.04 Server image.

## PPTP Server Side

This is what I did on the server end.

<pre>$ apt-get update && apt-get upgrade -y # Optional
$ apt-get install -y pptpd</pre>

### Server & Client IP Allocations

Now let's setup the IP Range we're gonna allocate to connecting clients. Add the lines below to `/etc/pptpd.conf`.

<pre>localip 10.0.0.1
remoteip 10.0.0.100-200</pre>

The `localip` part is for the server and the `remoteip` part is for connecting clients.

### Defining Valid Users

Next up we're gonna setup valid clients and allocate IP Addresses based on the user they are connecting as. Edit `/etc/ppp/chap-secrets` to reflect the followings.

<pre>cubie pptpd cubie_secret 10.0.0.23</pre>

We can add as many users we want. If you don't want to assign static IPs, you can use the template below.

<pre>john pptpd john_secret *</pre>

### DNS for Clients

The lines below is using Google's DNS servers, if you have local DNS Servers, it will shorten round trips.

Go ahead and edit `/etc/ppp/pptpd-options`.

<pre>ms-dns 8.8.8.8
ms-dns 8.8.4.4</pre>

### PPTPD Configuration Done

Restart the daemon.

<pre>service pptpd restart</pre>

### Setting Up Forwarding & NAT

First of all, we need to enable IP Forwarding. Go ahead and edit `/etc/sysctl.conf`.

<pre>net.ipv4.ip_forward = 1</pre>

Let's setup forwarding with `iptables` and let clients communicate with each other.

<pre>$ iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && iptables-save
$ iptables --table nat --append POSTROUTING --out-interface ppp0 -j MASQUERADE
iptables -I INPUT -s 10.0.0.0/8 -i ppp0 -j ACCEPT
iptables --append FORWARD --in-interface eth0 -j ACCEPT</pre>

## Setting Up Cubieboard As a Client

My Cubieboard has a GUI set using `LXDE` but I want to do this from the CLI. I've also setup a small Python script to keep monitoring the VPN Tunnel.

### Installing The PPTP Client

<pre>$ apt-get install network-manager-pptp
$ modprobe ppp_mppe</pre>

### Configuring The PPTP Client

This is the easy part. Fire up an editor and create a new file: `/etc/ppp/peers/pptpserver`.

<pre>pty "pptp x.x.x.x --nolaunchpppd"
name cubie
password cubie_password
remotename pptpserver
require-mppe-128</pre>

Replace the `x.x.x.x` line with the IP Address of your PPTPD Server. You can rename that particular `pptpserver` name to something more descriptive.

### Connecting To The Server

Let's connect now!

<pre>$ pppd call pptpserver</pre>

Now it won't show any logging, you can `tail` the log at `/var/log/syslog`.

<pre>$ tail -f /var/log/syslog</pre>

Or you can just check if `ppp0` is already available by doing a `ifconfig -s ppp0`. A successful connection will output something like below.

<pre>Iface   MTU Met   RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
ppp0       1496 0         7      0      0 0             7      0      0      0 MOPRU</pre>

### IP Routes

Let's add some more routes like so.

<pre>$ ip route add 10.0.0.0/8 dev ppp0</pre>

## Making The VPN Tunnel Persistent

We need the tunnel to always be available at all times so we're gonna need a monitoring solution to reconnect when the tunnel is broken. I made a small Python script available below.

<script src="https://gist.github.com/tistaharahap/8059219.js"></script>

Save the file as `/root/bin/checkapp.py`, adjust permission and let's add this to our crontab.

<pre>$ curl https://gist.github.com/tistaharahap/8059219/raw/e3e8ac07308cc06e24694c182b09428901f36f9b/checkppp.py > /root/bin/checkapp.py
$ chmod +x /root/bin/checkapp.py
$ crontab -e</pre>

Add the following line below for a 5 minute check interval.

<pre>*/5 * * * * /root/bin/checkapp.py</pre>

## Done

Now I have a persistent tunnel and available anytime I need it.

<script type="text/javascript">
var amzn_assoc_placement = "adunit0";
var amzn_assoc_search_bar = "true";
var amzn_assoc_tracking_id = "bango29-20";
var amzn_assoc_ad_mode = "manual";
var amzn_assoc_ad_type = "smart";
var amzn_assoc_marketplace = "amazon";
var amzn_assoc_region = "US";
var amzn_assoc_title = "My Amazon Picks";
var amzn_assoc_linkid = "37ddc99aabea4f2a5b575620b01a230c";
var amzn_assoc_asins = "B00JUG7R60,B00ISKS416,B00KCS8ZUC,B010Q57T02";
</script>
<script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>