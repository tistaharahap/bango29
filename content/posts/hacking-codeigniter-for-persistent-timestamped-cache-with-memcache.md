+++
author = "Batista Harahap"
categories = ["cache", "codeigniter", "memcache", "memcached", "output", "persistent", "web development"]
date = 2012-02-02T19:36:31Z
description = ""
draft = false
slug = "hacking-codeigniter-for-persistent-timestamped-cache-with-memcache"
tags = ["cache", "codeigniter", "memcache", "memcached", "output", "persistent", "web development"]
title = "Hacking CodeIgniter for Persistent Timestamped Cache with Memcache"

+++


I've got myself a long title for a blog post this time. This post is exactly what the title says. Been twisting my head figuring out how to bypass CodeIgniter's internal to hack CodeIgniter's ability to do a persistent timestamped cache of generated HTML contents using Memcached. I couldn't find any other way to speed up cached HTML content serving within the framework, so after a long talk with <a href="http://twitter.com/chazzuka">@chazzuka</a>, I made the choice to skip framework.

The main purpose is actually what all websites want, to spit out content as fast as possible and maintaining a high satisfactory levels of perceived speed for users. CodeIgniter wasn't built for that. To make matter more complicated, CodeIgniter has its own session handling mechanism, this made fundamental changes to caching for logged in users a risky business. Comparing the benefits and losses of the change, <code>0.00001242 second</code> execution time outbid even the fastest execution time on our servers.

Please share the codes :)

[gist]<script src="https://gist.github.com/1725281.js"> </script>[/gist]