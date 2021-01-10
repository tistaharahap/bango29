+++
author = "Batista Harahap"
categories = ["/etc/hosts", "dns", "dnsmasq", "hosts", "resolve", "virtual host", "web development"]
date = 2012-04-28T21:31:07Z
description = ""
draft = false
slug = "easy-dns-names-for-virtual-hosts-in-mac-os-x"
tags = ["/etc/hosts", "dns", "dnsmasq", "hosts", "resolve", "virtual host", "web development"]
title = "Easy DNS Names for Virtual Hosts in Mac OS X"

+++


I got tired of manually inserting lines into my <code>/etc/hosts</code> file and decided to look for other solutions. The DD-WRT router has a DNSMAsq feature in which I list domains that are supposed to be internal domains to be resolved to its local IP. I still have to insert lines but now it's more organized and better than seeing mumbo jumbo in your hosts file.

Here are my steps:
[gist]<script src="https://gist.github.com/2522184.js"> </script>[/gist]