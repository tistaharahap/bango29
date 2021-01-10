+++
author = "Batista Harahap"
categories = ["Android", "Augmented Reality", "mixare", "Nexus One", "Tutorial"]
date = 2010-04-26T17:16:49Z
description = ""
draft = false
slug = "mixare-augmented-reality-tutorial"
tags = ["Android", "Augmented Reality", "mixare", "Nexus One", "Tutorial"]
title = "Mixare Augmented Reality Tutorial"

+++


Good evening to you guys before I start.

[flashvideo file=http://www.bango29.com/mixare.flv /]

I've been in guerilla mode for Augmented Reality solutions these past few weeks and I found Mixare to be one of the best to date. It's Open Source and have put enough knowledge in my head to make my own app. I wanna share the knowledge I got from Mixare. This is my contribution.

Before starting, please make sure you have all the requirements of a regular Android development environment. I'm using Eclipse Galileo with Android SDK Tools Revision 5. My target build is for Android 2.1 API Level 7.

This tutorial is still basic, it's basically an introduction to Mixare without changing much of its base code. Sufficiently changing what's needed just enough to show our own POI's.

First of, you will need to download the source code from Mixare's website at <a href="http://www.mixare.org" target="_blank">www.mixare.org</a>. The download is available at Google Code.

Once you've download the source code, import them into your Eclipse by clicking <strong>File -&gt; Import</strong> from the menu. In my Macbook, there were no problems importing the project but in my Hackintosh, I can't get it to compile. I haven't figure out why yet.

[caption id="attachment_278" align="alignnone" width="356" caption="Import Mixare - Step 1"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.50.51-PM.png"><img class="size-full wp-image-278 " title="Import Mixare - Step 1" src="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.50.51-PM.png" alt="Import Mixare - Step 1" width="356" height="305" /></a>[/caption]

[caption id="attachment_279" align="alignnone" width="359" caption="Import Mixare - Step 2"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.52.03-PM.png"><img class="size-full wp-image-279 " title="Import Mixare - Step 2" src="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.52.03-PM.png" alt="Import Mixare - Step 2" width="359" height="391" /></a>[/caption]

After importing the project, to be on the safe side, Clean your Mixare project first by <strong>Project -&gt; Clean</strong> from the menu. Select Mixare from the following window.

[caption id="attachment_280" align="alignnone" width="331" caption="Clean The Project"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.57.27-PM.png"><img class="size-full wp-image-280 " title="Clean The Project" src="http://www.bango29.com/go/wp-content/uploads/2010/04/Screen-shot-2010-04-26-at-11.57.27-PM.png" alt="Clean The Project" width="331" height="219" /></a>[/caption]

Now let's get down to business. The only you need to change is the DataView.java file from the <strong>src/org/org.mixare</strong> tree. Guess what, you'll only need to change one line :)

<pre lang="java">/** default URL */
String HOME_URL = "http://bango29.com/mix.php";</pre>

I've changed it to a web server which is my blog with the request file <strong>mix.php</strong>. The default was using a Wikipedia server. Again, this is a very basic tutorial. My mix.php file source is as follows.

<pre lang="php" line="1">
<?php
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
	  }';
?>
</pre>

As you can see, my mix.php is only generating static content. It's a JSON encoded array. The PHP file does not care any GET variables it gets, it's only statically serving the 3 POI's above. You can see more documentation about the format of the JSON array <a href="http://code.google.com/p/mixare/wiki/DisplayYourOwnData">here</a>.

Now plug in your Android phone to your USB port, build and run the project. The final outcome is shown above with the video.

My next step will be changing that red circle for the POI's into custom icons. You can do this by editing the file <strong>Marker.java</strong> at <strong>src/org/org.mixare</strong> tree. Until next time!