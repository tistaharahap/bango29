+++
author = "Batista Harahap"
categories = ["hack", "memcache", "optimize", "speed", "wordpress"]
date = 2013-07-01T23:32:28Z
description = ""
draft = false
slug = "accident-happens"
tags = ["hack", "memcache", "optimize", "speed", "wordpress"]
title = "Accident Happens"

+++


Just a few days ago, an accident happened. It was 4 AM and I am moving this blog over to <a href="http://www.cloudkilat.com" target="_blank">CloudKilat</a>. Already got the MySQL dump transferred, would need to have the whole site rsync-ed to the new server. So I did it. Without me realizing, I misplaced the source and destination ending up the new server's home directory rsync-ed to the original server. A fundamental mistake.

Luckily, as I said above, the MySQL dump is already safe at hand so to rebuild another Wordpress blog would be a matter of configurations.

From what I read across the web, Wordpress is relatively easier to scale and having only a single core at work, I will need to scale this blog properly. I haven't though. As of this writing, I have only set up <code>nginx + php-fpm + APC</code>.

<strong>Disclaimer:</strong> This is a for fun project, nothing too serious, most will be proof of concepts. Some tricks were absorbed when scaling <a href="http://www.urbanesia.com" target="_blank">Urbanesia's</a> frontend, <a href="http://dailysocial.net" target="_blank">DailySocial</a> and <a href="http://www.trenologi.com" target="_blank">Trenologi's</a> WordPress installation.

What I'm planning to do is to prepare the blog by scaling minimally only on what's needed. This CloudKilat VM is packed with 2 GB of memory so it's spacious enough to run a minimal dynamic web server with MySQL in it. However, I am not getting that illusion of speed even though CloudKilat is here in Indonesia. The web server is curl-ing post pages at 11 seconds. Way too much overhead there.

The specs are as follow:
<ul>
	<li>1 CPU Core</li>
	<li>2 GB RAM</li>
	<li>20 GB Hard Drive</li>
	<li><a href="http://www.nginx.org" target="_blank">nginx</a></li>
	<li><a href="http://www.php.net" target="_blank">PHP-FPM</a></li>
	<li><a href="https://downloads.mariadb.org/mariadb/" target="_blank">MariaDB 5.5</a></li>
	<li><a href="http://www.redis.io" target="_blank">Redis 2.6.14</a></li>
	<li><a href="http://www.memcached.org" target="_blank">Memcached 1.4.15</a></li>
	<li><a href="http://www.cloudflare.com" target="_blank">CloudFlare</a></li>
</ul>

<h3>First Look</h3>

Initial assessment shows that the server is not capable of handling high loads without some special tunings. I am also testing CloudFlare with this server and when it's cached, the response time is great. On the dynamic side, the server is lagging to spit out HTML as fas as it can. Execution time to render an HTML can be as long as 6 seconds. Unacceptable at all.

Since this is a VM and <code>root</code> access is a given, I'm starting off by removing all unnecessary services below:
<ul>
	<li>Apache httpd</li>
	<li>Sendmail</li>
	<li>Samba</li>
	<li>Bind</li>
</ul>

I never want to have <code>sendmail</code> to be installed by default on any of my servers. Spammers know what their doing and will surely take advantage of unsecure <code>sendmail</code> installations.

<h3>Dumb Cache</h3>

So the first easiest thing to do is hack WordPress' <code>index.php</code> file and add my own code to do caching with Memcached. What I want to do is cache every dynamically generated pages into memory, purge cache if I make any changes and hook with WordPress' output to do this.

As it turns out, I don't need to hook with WordPress' output, I just need to hook into PHP's <a href="http://php.net/manual/en/book.outcontrol.php" target="_blank">output buffering</a> mechanism. The codes below is a rather crude way of doing it.

<script src="https://gist.github.com/tistaharahap/5905509.js"></script>

The problem with the code above is that I can't refresh by will let's say if I had to make an Edit on one of my blog posts. So a line with code needs to be adjusted, specifically line 9 to be:

<code>$cache = !empty($_GET['refresh']) && $_GET['refresh'] == 'waku' ? FALSE : $mem->get($key);</code>

The final code becomes below.

<script src="https://gist.github.com/tistaharahap/5905530.js"></script>

Execution time goes as fast as <code>0.00081706047058105 second</code> and it's exactly what I'm after. Haven't really diagnosed any problems with the codes yet.

<h3>Moral of The Story</h3>

I accidentally deleted my blog and ended up hacking Wordpress to my taste. Everything does happen for a reason ;)