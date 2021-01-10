+++
author = "Batista Harahap"
categories = ["2011", "api", "biznet", "cdn", "googlebot", "http", "nginx", "oma", "opung", "proxy", "sofvia", "spontaneous", "spontaneous writing", "urbanesia", "writing"]
date = 2011-02-04T19:02:28Z
description = ""
draft = false
slug = "spontaneous-writing-episode-ii"
tags = ["2011", "api", "biznet", "cdn", "googlebot", "http", "nginx", "oma", "opung", "proxy", "sofvia", "spontaneous", "spontaneous writing", "urbanesia", "writing"]
title = "Spontaneous Writing Episode II"

+++


The second episode of Spontaneous Writing is now in session continuing from <a href="http://r.bango29.com/gjCDHa" target="_blank">this</a> previous session. For tonight, my iTunes is happily playing songs by Tohpati in his rather old solo album. By the way, from what I've been trying to do the past few weeks, it seems that only when I got home will then writing moments will be abundant for my fingers. Can't seem to do this while at the office.

Since it's still warm and huggable, the first topic will definitely be about Urbanesia and itsÂ unprecedentedÂ outcome this past few months. Just got home from a long 2 weeks marathon at the office. I must say the last 2 weeks were one of those times when redefining moments just happen without no specific reasonings. My last piece of spontaneous writing noted December 2010 as one of those times and yet it happened again early this year.

In a more technical way, all of our preparation to ready Urbanesia for 2011 were making results faster and better than what we expected them to be. Since we are migrating every models we had to retrieve data from our newly crafted API, Sofvia our application server were flooded with a high number of locally inbound HTTP requests. Load averages soar high looking from our Munin graphs.

The most obvious reason for this to happen is because we just migrated on of our application server to <a href="http://r.bango29.com/g8J6a4" target="_blank">Biznet's Cloud Computing</a> platform. We took a spin with the lowest spec available which is a 1 core, 1 GB RAM, 100 GB SAN Storage and 100 Mbps shared International Bandwidth. Freshly installed CentOS and wiped everything not needed due to the resource constraints. We knew it wouldn't be ideal to make it a full fledged application server so instead we made it to be a full fledged proxy server for our international traffic. Geo targeted DNS with Bind was executed so the local and international is routed accordingly.

With the changes above, Googlebots scour our website like never before. Just 18 days after its premier, our stats show that in January 2011, Googlebots downloaded a whooping 217 GB worth of data from our website. The amazing thing is with nginx in our Biznet cloud server, the load average never even touched 1.0. Memory usage was also amazingly lean with no swap space at all. It's great to know all those gigabytes of data is served by a tiny server.

With all that traffic, the strain was with Sofvia. We had to optimize a step further. This time we physically separated our CDN with our application server. It's a bit risky for us because we didn't have any network shared filesystem implemented yet but again because of needs, we implemented what's necessary and to our expectations memory usages dropped significantly from Sofvia. Sofvia now has more breathing space for us to optimize. Sofvia is now purely an application server and doing only that. The migration is almost complete for Sofvia.

Enough about technicalities, now the next topic will be family. I come from a Batak family and as with any Batak family, the number one thing we Bataks have in mind is family. As I come home today, I bought my Oma 3 CDs of which she wanted me to get for her to accompany her during the long hours she was on the road everyday. For the record, she is a feisty Oma, 75 years old but never looked like she's getting any older.

I remembered as a little boy, my Oma and Opung took me and my brothers to Singapore for the new years. Me and my Opung was exhausted after a long walk around Orchard accompanying my Oma. Yes you guessed right, my Oma was not even bothered. She couldn't care less that we are waiting in front of one of the mall she's entering. She is still exactly in her late age today. Everytime I got to accompany her into a mall, she will most definitely have the stronger legs! It's a blessing for all of us that age is not an obstacle for her.

She's the kind of person who always want to be with family no matter how bad or how destructive you are at any point of your lives. She never gave up on me when I didn't have any job, only a freelancer and even when I have nothing to give her. An inspiring icon for me and for all of us in this big family. All she wants is for all of us to be happy and I don't know how but she managed to get the best out of me in any situation, I guess it's her faith in Him is glowing and automatically shines. She's an example to follow and boy my Opung was a lucky guy!

Next up is also something close to my heart. I am blessed with great friends with every phase of my life. Wherever I am, there is always a friend I can confide and tell stories vice versa. No different today, I'm surrounded with the best persons in the startup scene. They're not just colleagues, they are more than that and I put special care and attention to each one. Okay this is about Urbanesia (again), it's just automatic that everything I am right now is Urbanesia, it's part of my identity. We worked smart and hard to leverage Urbanesia.

Suffice to say, everyone is supercharged for anything that's gonna happen next. It's like we're starved and the hunger is pushing everyone to the limit. <a href="http://r.bango29.com/dHgwtM" target="_blank">Selina Limman</a> I quote saying this: "<em>Urbanesia is not only a professional matter, it's personal for all of us</em>". In my point of view, we have successfully introduced an <span style="text-decoration: underline;">unlimited amount of fuel</span> which is <span style="text-decoration: underline;">passion</span>. No matter what your position is, you matter to all of us, without you, we are not complete.

The prove is when night falls. When the sun is still shining, my creativity is hindered by the amount of routinity obliging me to perform everyday. I call it nurturing so when they grow up, I can happily let go each one and empower the growth they are contributing. Coming back to the main point, at night, the usual suspects still at the office will almost certainly be me and <a href="http://r.bango29.com/gegDfy" target="_blank">Ridhi Mahendra</a>. Some nights, there are others but most of it will be us and beer bottles lol.

Cutting it short, Ridhi is a marketing guy and I'm the technical guy. We discuss and measure everything. With every conclusions, we reacted instantly to respond to what the data is telling us. This I tell you is not an easy thing to do, it's an art because how dynamic the web is. One day it can conclude to A and another day it will conclude to -A. So the challenge was to be as dynamic as possible while maintaining a high level of consistency with everything we developed.

Thanks to one of the partners at East Ventures, <a href="http://r.bango29.com/eD83bp" target="_blank">Willson Cuaca</a>, we have managed to scale and metric everything. It all comes down to what you know and what you don't know. To know what you don't already know, we're lucky to have shortcuts like East Ventures. However, the challenge was to experience what you don't know and excel from it to give lessons of what to do and what not to do. It's been a roller coaster ride honestly!

The last topic is very personal because it's about a date I'm having tomorrow :) Since my last relationship, this will be the second date I will have with the same person I might add. Hoping for a great night tomorrow to wrap off a long and fruitful 2 weeks. We're gonna see The Green Hornet and boy this year will be full of superheroes movies, YEAYYY!!!

Okay am not gonna talk more about this date tomorrow. It's 1.57 AM and I'm wasted. A good night sleep on a genuine bed is what I've been longing. So I'm off now, thanks for reading. I'm gonna wrap things up by quoting one of my own blog post.
<blockquote><strong>You are you're own StartUP</strong></blockquote>