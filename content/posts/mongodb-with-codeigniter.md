+++
author = "Batista Harahap"
categories = ["apache", "apc", "Code Igniter", "memcache", "mongodb", "optimize", "performance", "scale", "speed", "web development"]
date = 2010-12-30T12:48:34Z
description = ""
draft = false
slug = "mongodb-with-codeigniter"
tags = ["apache", "apc", "Code Igniter", "memcache", "mongodb", "optimize", "performance", "scale", "speed", "web development"]
title = "MongoDB With CodeIgniter"

+++


Today was started with a bigÂ curiosityÂ towards Urbanesia's recent performance drop. This week we discovered that although we have completely revamped our codes to hack CI to use MongoDB as its session storage instead of MySQL, we found that Memcache is the bottleneck. When I woke up today, I was devastated to know that it took at minimum 5.7 seconds to load any of our business profiles.

So I went hunting for the source of this irritating loading time. The Memcache problem was because our Sofvia server is at its limit, we've pushed the CPU utilization to her max and Memcache is simply not getting enough CPU Power. The main cause is putting 2 Memcache instances in Sofvia which in turn made CPU utilizations soar. When Memcache was out of CPU resource, the server was on an endless loop with load averages sky rocketing to &gt; 100. Reference is <a href="http://r.bango29.com/dNj60F" target="_blank">here</a>.

So we moved Memcache to another server and increased PHP's Memcache module chunk size to 32 MB by adding this line to php.ini:
<pre lang="php">memcache.chunk_size = 32768</pre>
I was reluctant at first to install APC because I wanted to test our v1 codes against real world conditions. Sufficient to say, we did all the optimization we could in terms of codes. It is time to optimize it in another way. So today I installed APC, for its performance gain, I have to say the installation routine was too easy to be true lol.

The Memcache server is moved to another server so Sofvia had a lot of unused memories. Before installing APC, the free memory was ~10Gigs. APC is easy to install but cryptic with its configuration, I read a lot of references before actually enabling APC and do a little trial and error with it. The configuration for APC is:
<pre lang="php">extension=apc.so
apc.enabled=1
apc.shm_segments=1
apc.optimization=1
apc.shm_size=1G
apc.ttl=7200
apc.user_ttl=7200
apc.num_files_hint=1024
apc.mmap_file_mask=/tmp/apc.XXXXXX</pre>
You might have guessed why apc.stat is not zeroed out. Just for today, I don't want to refactor any codes while configuring APC, as is will have to do fine. When I set apc.stat = 0, Urbanesia went crazy because CI by default used relative paths which is acceptable because of its general purpose design. With apc.stat = 1, APC will check for changes with the file every time a request is made.

Now all happy and grinning in front of my Macbook when I restarted Apache only to find that the total execution time was lowered only to ~4.8 seconds. Not acceptable at all! So I went ahead to Xdebug the problems. Looking from the result, it was supposed to be smooth sails with functions ran under 100ms. If I total the whole execution time of each functions, it was not even close to 4.8 seconds.

So I surrendered a few restrictions for today, this must have something to do with bad codes and or slow response time either from Memcache, MongoDB, MySQL or Sphinx. All and all, I remembered turning on pageviews log and being confidence that by using MongoDB as its backend, it wouldn't slow things down, well at least not significantly. I was wrong :(

It turns out that the culprit is MongoDB. The daemon was not in Sofvia, it was in Davinci. So requests to MongoDB was at our network's mercy. Now I can conclude that it was not our network's performance, okay maybe it was something to do with the network cables but from a software point of view, it was top notch. Yes we're gonna upgrade the cables :)

I turned off logging from our codes breaking today's restriction :( The execution time went from ~4.8 seconds to a mere ~0.7 seconds. So for now performance is gained once again by disabling the logs. Checking the MongoDB collection, we had over than 5 millions rows worth of logs. Xdebug complained about our CI driver's Get method for MongoDB. I hope this will be a CI driver problem because for its worth, MongoDB is a performance gainer almost every time against MySQL.

The funny thing is, our CI sessions collections had more rows and performance was not affected at all, we used the same CI driver too.

So for anyone out there reading this blog post, would love to have your comments about MongoDB and CI. Truly in need of inspiration :)