+++
author = "Batista Harahap"
categories = ["apache", "api", "biznet", "business", "cloud", "einstein", "energy", "httpd", "light", "mongodb", "mysql", "nginx", "oauth", "requests", "scaling", "startup", "urbanesia"]
date = 2011-01-24T22:13:01Z
description = ""
draft = false
slug = "small-is-not-so-small"
tags = ["apache", "api", "biznet", "business", "cloud", "einstein", "energy", "httpd", "light", "mongodb", "mysql", "nginx", "oauth", "requests", "scaling", "startup", "urbanesia"]
title = "Small is NOT so small"

+++


It's been like a few months not posting into my own blog. The 24th day of 2011 and it seems that months have passed by just like that. In the span of 24 days that have passed, every single day is cramped with all the aspects of being a startup. Just today, I went from a programmer, a cable crimper, a business partner, a troubleshooter, a mobile app consultant, a colleague to a friend for a friend, all in just one day. Multiply that by 24 and that's exactly what's been going on. The dynamics revolving is mind blowing.

I can't help to wonder exactly what I'm doing right now is to look back and kinda being nostalgic to myself to figure out how so much energy can be exuded with far less sleep than ever before. Physics defines e (energy) equals m (mass) times c (speed of light) square. There is no indefinite variable there although I have to admit my mass is fluctuating but it is drastically paled to insignificance when multiplied with the square of the speed of light which is 3.6 millions meters/second. NO, the speed of light is a constant and therefore always have the same value while mass is the dynamics.

Well mass is the variable and this is where energy can be increased or decreased exponentially literally. With Einstein's theory of energy, it's safe to say that without mass, it's just light. The same light currently transporting zillions of gigabit traffic around the world to every connected computers globally. What's best of all, at least for now, light is unlimited and available anywhere in the world. What the world lack is mass.

These past months, we've been having a 40% problem in Urbanesia. Our sudden drop of traffic is just weird. Efforts to tackle the drop were taken, from AB testing new designs to optimizing codes to be able to serve faster were done like it's do or die. We found a really troubling fact. Our Google Analytics Javascript code is not loading as expected in most parts of Urbanesia.

With the new look, we introduced a new framework for Urbanesia. We hate inline JS and CSS, so we created a framework to parse JS and CSS, minified them and put them in separated files. The Google Analytics loader JS was one of them. We put it at the bottom like any other sane website. Well that was the problem. Most of our visitors' Internet connection was not fast enough to grab the loader file in a way to keep up with their engagement with the website.

So with every good programming practice, we refactored the codes. Affectionally, we put the codes up top before closing the HEAD tag and pointed ga.js to load from our CDN. The result is a 40% difference! This is a big lesson for everyone in Urbanesia. With Google Analytics measuring the right numbers of traffic, our approach to enable Urbanesia to scale is now sane again.

During the process, we treated ourselves a new Cloud Server at Biznet and boy that has made another big impact towards our traffic. From the beginning of the new look for Urbanesia, we concentrated our efforts so that our application servers can be migrated to multiple servers instantly. The big roadblock was that we didn't had a good enough API to support this. So we went on to create one of the best API to date for Urbanesia.

By having a great API, we managed to localize each parts of Urbanesia to scale with proportion. Optimizing Apache is trivial to be able to handle this many API calls/seconds. Because of Apache's great flexibility, it became its own worst nightmare. Our Apache configuration is hand tuned slowly to cope with the changes. Thank God for nginx!

Our cloud server is a single core, 1 GB RAM server and it's serving half of Urbanesia's traffic with that little man namely nginx. Nginx as a proxy load balancer is amazing. Just by having 1 nginx, we boosted 300% of our concurrent traffic. With proper caching of static contents, this has been a relieve. Since we now have 2 nginx instances, we have increased our daily traffic to cope with multi Mbps traffic constantly.

In parallel, we transitioned Urbanesia from a 100% MySQL oriented website to switch to a 70% portion for MySQL and 30% portion of MongoDB. The problem with MySQL is that it can't keep up with our increasing needs and we don't wanna scale hardware yet. So it's back to the applications we used. By using MongoDB, we put all of our high volumes &amp; low value data in it. The best thing about MongoDB is that it's really fast! The catch is MongoDB uses a lot and i mean a lot of physical memory to be able to do this. Think of of it as MySQL + Memcache on steroids. To keep MongoDB performing like this, we revamped our Database server to cope with MongoDB's need for memory.

So as you can see, logically we have separated Urbanesia into partitions. Now we can scale Urbanesia according to the needs of each partitions. A Googler told me that "<em>Faster loading of pages equals more revenues</em>". We measure revenue notÂ necessarilyÂ in $$$. Users engagements is one of our metrics. Well the words were proven. We hit a new record this January with users engagements. The total number of reviews as of 24 January 2011 have beaten the best month of 2010 and we still have 7 days to get more reviews.

Our marketing and development team is moving with right pace both independently and as a big team. This is key to our sudden increase of performance in January 2011. We learned to work it out as a team and makeÂ decisionsÂ based on data collected. We AB Test all of our changes and introduced a heat map. The data we gained was invaluable to our efforts. Because of the nature of Urbanesia being so vast, we couldn't just highlight everything all at once, we needed to move single minded. Reinforcing everything one step at a time.

The last 3 months of 2010 were allocated to create a rock solid foundation for 2011 and it worked out like a charm. I'm very proud to say that our team of superheroes are incredible. The dedication and affection towards Urbanesia are not like what you can expect in any other ordinary workplace. Salute to every one of us!

In closing, I learned an important lesson with scaling. Scaling is an artwork, nothing is for certain until you get to the point where every destination is mapped and prepped for dynamics. Meaning that anytime, our infrastructure must be ready for changes while maintaining a high level of stability. From a business side, well when you got the software, hardware and human resource right then you just gotten your most invaluable asset: A living and breathing product manifested in all of our work. This will pay the bills, just gotta have faith :D