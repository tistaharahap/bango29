+++
author = "Batista Harahap"
categories = ["Android", "Augmented Reality", "location based service", "mixare", "Nexus One", "Tutorial"]
date = 2010-05-12T14:53:35Z
description = ""
draft = false
slug = "another-mixare-snippet"
tags = ["Android", "Augmented Reality", "location based service", "mixare", "Nexus One", "Tutorial"]
title = "Another #Mixare Snippet"

+++


Lately, there's been quite an amount of traffic to my blog related to Mixare. So I figure why not share more insights. You are most welcomed to share too by commenting this or other Mixare posts.

To be honest, I've been focusing my efforts with another yet closed source Augmented Reality viewer in Android. I will post a tutorial soon.

From all the frameworks I got my hands on, I must say Mixare is the simplest and most definitely easier to implement than any other frameworks. I accentuated simple because the app itself is still very simple and in its early stages of development. I would be happy to have the ability to replace the circles in every POIs with an icon of my own. It's a viewer, that's it (for now).

Anyways, my last tutorial about Mixare was to actually hard code the the URL for Mixare to load the JSON. Actually, I didn't have to do that as you can see from Daniele's comment. All I needed to do are described below:
<ol>
	<li>Add proper MIME types to your web server or directly in your web application. My PHP looks something like the source code below.
<pre lang="php">header('Content-type: application/mixare-json');
echo '{
 "status": "OK",
 "num_results": 3,
 "results": [
 {
 "id": "212",
 "lat": "-6.225062",
 "lng": "106.790636",
 "elevation": "0",
 "title": "Guess PIM2",
 "distance": "1.24",
 "has_detail_page": "1",
 "webpage": "http%3A%2F%2Fwww.mediafusion.web.id"
 },
 {
 "id": "213",
 "lat": "-6.179467592090026",
 "lng": "106.79054260253906",
 "elevation": "0",
 "title": "iBox Plaza EX",
 "distance": "10.24",
 "has_detail_page": "1",
 "webpage": "http%3A%2F%2Fwww.mediafusion.web.id"
 },
 {
 "id": "215",
 "lat": "-6.175030310631483",
 "lng": "106.79054260253906",
 "elevation": "0",
 "title": "Red Mango GI",
 "distance": "9.24",
 "has_detail_page": "1",
 "webpage": "http%3A%2F%2Fwww.mediafusion.web.id"
 }
 ]
 }';</pre>
</li>
	<li>Just pass the URL where you put that PHP file into a web server and make a hyperlink to it. Mixare will automatically launch when you click on the link.</li>
	<li>If you don't want to manually add the proper MIME type everytime you code, add the MIME type to your web server, a proper extension for files containing Mixare JSON Arrays and you're set.</li>
</ol>
It couldn't be any simpler than this. My appreciation to all of Mixare's team!