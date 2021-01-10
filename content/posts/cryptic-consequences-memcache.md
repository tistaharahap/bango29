+++
author = "Batista Harahap"
categories = ["apache", "httpd", "memcache", "memory", "namespace", "php", "solution", "urbanesia", "XDEBUG"]
date = 2011-01-03T11:18:06Z
description = ""
draft = false
slug = "cryptic-consequences-memcache"
tags = ["apache", "httpd", "memcache", "memory", "namespace", "php", "solution", "urbanesia", "XDEBUG"]
title = "Cryptic Consequences - Memcache"

+++


This is yet another blog post about the almighty Memcache hehehe. As do all of us I assume, more than often Memcache has always been a lifesaver won't you say? Well at least when it is tamed, I'm positive it's a lifesaver anytime, when it's still wild, extremely saying: you shit bricks lol. Well here's another Memcache experience.

First of all you gotta visit <a href="http://r.bango29.com/gOdJGS" target="_blank">http://memcached.org</a> man. The header from the top right is littered with illustrations of either rabbits or cats. I can't seem to distinguish which animal but for sure Memcache is an animal need taming lol. Your codes needs to be able to cope with Memcache's wild behavior hehehe.

I wrote about Memcache earlier <a href="http://www.bango29.com/go/blog/2010/mongodb-with-codeigniter" target="_blank">here</a>. Relieved to say that my early diagnosis about the problem is either bad codes or slow response times from daemons like Memcache were true. It turns out that bad codes were the number one culprit contributing directly to slow responses. Now I know what exactly went wrong. My hands got so full that I missed the finer details, yeah it happens a lot man, macro is good but evidently micro is a lifesaver.

We have a dedicated model to do things with Memcache and thanks to XDEBUG, I managed to localize the problem to a method called _setNamespace(). There were 3 conditions of which does not have the right namespace handling logics to cope with our v1's namespace conventions. Our bad yes it was to not be thorough and micro. Particularly the code below:
<pre lang="php">$ns_array = $this-&gt;_defalsify($this-&gt;memcache_obj-&gt;get($this-&gt;host_key . '#ns_' . $needle[0]))</pre>
All of our namespaces started with v1 and delimited by #. So essentially for every namespace being set, the model tried to get all namespaces with v1 as its first segment. Apache processes bloated to eat away ~400 MB of memory each. While experiencing this, I had to lower down MaxClients to a very low number which basically increases CPU usage because Apache processes got forked and killed too frequent.

Anyways, after adjusting the codes, it was smooth sails once more. Visit <a href="http://r.bango29.com/esOEup" target="_blank">Urbanesia</a> now and you will see how fast it is right now. This particular case ended a 2 months wild chase to figure out what's wrong with our codes and very thankful we did got it fixed early 2011, with all the challenges this year, we need to focus more on strategies instead of code refactorings. New codes for new products is what we're after.

The cool thing is, I solved this mystery while having aÂ diarrheaÂ last night while bringing my laptop while "<em>ejecting</em>" hahaha. I guess the bathroom is full of inspiration. Back in 2010, I had inspirations coming when I was in the shower. So for 2011, the bathroom is my most sacred space of them all :D