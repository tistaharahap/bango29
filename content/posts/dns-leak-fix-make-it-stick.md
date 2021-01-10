+++
author = "Batista Harahap"
date = 2016-11-27T00:45:32Z
description = ""
draft = false
image = "/images/2016/11/Esensi-Ilmu-Leak-Yang--Mulai-Terkubur.jpeg"
slug = "dns-leak-fix-make-it-stick"
title = "DNS Leak Fix - Make it Stick"

+++


Just recently I read about the term [Transparent DNS Proxies](https://www.dnsleaktest.com/what-is-transparent-dns-proxy.html). Never knew that it was a term. Here in Indonesia the practice is regular amongst ISP's. My own home internet connection is plagued by this.

ISP's in Indonesia are somewhat obliged by the government to censor porn. Not all ISP's oblige though. For instance, business type internet connection mostly are free from this. My office has a Fiber Optic connection and their DNS are not doing it.

It's easy to imagine what kind of power proxying port 53 can do. When someone types in `facebook.com`, just hope that you're really resolving Facebook's IP's. For the sake of argument, the ISP can be hacked and silently showing up a phishing page instead of the real website.

Now imagine the above's scenario being applied to your Internet banking website. Of course high end websites are smarter to put precautions such as a long lived [HSTS header](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security). This will force the browser to always use HTTPS for that domain. However this is not a default and only applied after your first visit.

I can imagine someone opening up [www.klikbca.com](http://www.klikbca.com), received a phishing page and profit from it. Why KlikBCA? Because their root domain is still served over HTTP, no HTTPS is available. In reality, an attacker must have the account holder's KlikBCA Token physically but without it is enough to know more about a person. An attacker can download 3 months worth of transaction history for example.

[This is a fine read about ISP's](https://utcc.utoronto.ca/~cks/space/blog/web/ISPsAreThreats) potentially doing more harm than good.

---

In light of the above, I turn myself to [DNSCrypt](https://dnscrypt.org/).

> DNSCrypt is a protocol that authenticates communications between a DNS client and a DNS resolver. It prevents DNS spoofing. It uses cryptographic signatures to verify that responses originate from the chosen DNS resolver and haven't been tampered with.

However in Indonesia there is no known DNSCrypt resolver if you look into [the list](https://github.com/jedisct1/dnscrypt-proxy/blob/master/dnscrypt-resolvers.csv). The closest is [Singapore](https://github.com/jedisct1/dnscrypt-proxy/blob/master/dnscrypt-resolvers.csv#L47).

The above would mean that the local proxy would always try to resolve without caching. I needed something to cache and so I learned about [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html).

> Dnsmasq provides network infrastructure for small networks: DNS, DHCP, router advertisement and network boot. It is designed to be lightweight and have a small footprint, suitable for resource constrained routers and firewalls ...

When the 2 is combined, my DNS queries will be secured and cached. Let's get right to it.

---

I'm on macOS Sierra with [Homebrew](http://brew.sh/) installed, the download and installation are for it. For other OS, refer to your own package manager.

**Install**

`$ brew install dnscrypt-proxy dnsmasq`

Follow the post-install instructions to load both at startup.

**Configuration**

```
$ vim /usr/local/Cellar/dnscrypt-proxy/1.7.0/homebrew.mxcl.dnscrypt-proxy.plist
```

You might be on a different DNSCrypt proxy version, just change the version from the path above. You'd be interested with the `--resolver-name` argument. I choose Singapore as it's closest to me. For more options, you can refer to `/usr/local/opt/dnscrypt-proxy/share/dnscrypt-proxy/dnscrypt-resolvers.csv` locally or [here on Github](https://github.com/jedisct1/dnscrypt-proxy/blob/master/dnscrypt-resolvers.csv).

The `Name` column on the CSV represents the entry you should put it. An example of my config is below:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-/Apple/DTD PLIST 1.0/EN" "http:/www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>homebrew.mxcl.dnscrypt-proxy</string>
    <key>KeepAlive</key>
    <true/>
    <key>RunAtLoad</key>
    <true/>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/local/opt/dnscrypt-proxy/sbin/dnscrypt-proxy</string>
      <string>--ephemeral-keys</string>
      <string>--resolvers-list=/usr/local/opt/dnscrypt-proxy/share/dnscrypt-proxy/dnscrypt-resolvers.csv</string>
      <string>--resolver-name=d0wn-sg-ns1</string>
      <string>--user=nobody</string>
      <string>--local-address=127.0.0.1:5355</string>
    </array>
    <key>UserName</key>
    <string>root</string>
    <key>StandardErrorPath</key>
    <string>/dev/null</string>
    <key>StandardOutPath</key>
    <string>/dev/null</string>
  </dict>
</plist>
```

You'd see that I changed the `--local-address` option to bind to port `5355`. This is to let `dnsmasq` use port `53`.

Next let's configure `dnsmasq`. These are the options I used with explanation.

```
# Never forward plain names (without a dot or domain part)
domain-needed

# Never forward addresses in the non-routed address spaces.
bogus-priv

# Reject (and log) addresses from upstream nameservers which are in the private IP ranges. This blocks an attack where a browser behind a firewall is used to probe machines on the local network.
stop-dns-rebind

# Only use upstreams from this config file
no-resolv

# Point to DNSCrypt
server=127.0.0.1#5355

# Cache 150 hosts
cache-size=8192

# Loggings
log-async
log-dhcp
log-facility=/var/log/dnsmasq.log
```

Let's restart both services.

```
$ sudo brew services restart dnscrypt-proxy
$ sudo brew services restart dnsmasq
```

---

Next up, from `System Preferences > Network` change your DNS resolvers to `127.0.0.1`. Done.

Use [this](https://www.dnsleaktest.com/) to test your DNS.