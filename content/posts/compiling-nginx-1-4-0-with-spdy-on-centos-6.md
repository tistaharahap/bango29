+++
author = "Batista Harahap"
categories = ["centos", "compile", "linux", "nginx", "spdy", "Web"]
date = 2013-05-06T17:43:39Z
description = ""
draft = false
slug = "compiling-nginx-1-4-0-with-spdy-on-centos-6"
tags = ["centos", "compile", "linux", "nginx", "spdy", "Web"]
title = "Compiling nginx 1.4.0 With SPDY on CentOS 6"

+++


Just a few days ago, the latest version of <a title="nginx" href="http://nginx.org" target="_blank">nginx</a> at 1.4.0 was released to the public. The version bump adds a lot of new capabilities for your web stack. The most interesting for me was support for <a title="SPDY" href="http://www.chromium.org/spdy" target="_blank">SPDY</a> 2 protocol.

Excerpts from Chromium SPDY's page reads below:
<blockquote><em>As part of the "Let's make the web faster" initiative, we are experimenting with alternative protocols to help reduce the latency of web pages. One of these experiments is SPDY (pronounced "SPeeDY"), an application-layer protocol for transporting content over the web, designed specifically for minimal latency. Â In addition to a specification of the protocol, we have developed a SPDY-enabled Google Chrome browser and open-source web server. In lab tests, we have compared the performance of these applications over HTTP and SPDY, and have observed up to 64% reductions in page load times in SPDY. We hope to engage the open source community to contribute ideas, feedback, code, and test results, to make SPDY the next-generation application protocol for a faster web.</em></blockquote>
In order for SPDY to work, one will need an SSL certificate and OpenSSL 1.0.1c at least to compile and run a website successfully with nginx. SPDY needs NPN enabled with OpenSSL and CentOS only provides 1.0.0. According to a blog post <a title="Update to OpenSSL 1.0.1c" href="http://clsung.tumblr.com/post/35686837957/centos-update-to-openssl-1-0-1c" target="_blank">here</a>, we can just add a repo to get OpenSSL to work nicely.
<p style="text-align: left;">Here are the steps needed to compile nginx with SPDY support:
<code>$Â rpm -ivh --nosignature http://rpm.axivo.com/redhat/axivo-release-6-1.noarch.rpm</code>
<code>$Â yum --enablerepo=axivo update openssl</code>
<code>$ cd /opt/src</code>
<code>$ wgetÂ http://nginx.org/download/nginx-1.4.0.tar.gz</code>
<code>$ tar xfz nginx-1.4.0.tar.gz</code>
<code>$ cd nginx-1.4.0</code>
<code>$Â ./configure --with-pcre --with-http_ssl_module --with-http_spdy_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_stub_status_module --prefix=/usr/local/nginx</code>
<code>$ make -j4</code>
<code>$ make install</code></p>
Now that the steps above are through, it's time enable SPDY with your websites assuming that you already have a working nginx configuration with SSL enabled. It's actually really simple, the full explanation is located at <a title="nginx SPDY Documentation" href="http://nginx.org/en/docs/http/ngx_http_spdy_module.html" target="_blank">nginx's SPDY documentation</a>.
<p style="text-align: left;"><code>server {
listen 443 ssl spdy;
ssl_certificate server.crt;
ssl_certificate_key server.key;
...
}</code></p>
Now test your website at <a title="SPDY Check" href="http://spdycheck.org/" target="_blank">spdycheck.org</a> to see if your SPDY implementation is successful. Cheers!