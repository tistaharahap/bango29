+++
author = "Batista Harahap"
categories = ["api", "ar", "Augmented Reality", "layar", "lbs", "location based service", "mixare", "wikitude"]
date = 2010-04-25T17:51:30Z
description = ""
draft = false
slug = "augment-your-reality"
tags = ["api", "ar", "Augmented Reality", "layar", "lbs", "location based service", "mixare", "wikitude"]
title = "Augment YOUR Reality"

+++


Good evening!

I'm liking my Nexus One, I'm sure you've read it over and over on my last posts. What's really inspiring is the freedom to do just about anything you want with the phone.

I love how I can just push my self-developed applications onto the phone just by using Eclipse. It makes it easier to do testings. No complicated code signing and or certificate applications needed.

Anyways, these past few weeks, I've been developing an Augmented Reality application for a client. So far it's been very challenging. Gotta learn new things fast and implement them as fast as I learn them. There are a lot of already available Augmented Reality apps out there with top names opening up their platform and giving developers their API. Here's a video using <a href="http://" target="_blank">Wikitude</a>'s API.

[flashvideo file=http://www.bango29.com/ar.flv /]

The data source for Wikitude's API can come from anywhere you would want it to be. For a demo, I hard coded the POI's and copied the icons to my Nexus One's SD Card. So this app does not need any Internet access, just GPS will do. It worked flawlessly as you can see on the video. I would say the API is quite matured and worth investigating. O yea, on the video you'd see BETA tags across the screen, it's because I didn't put an API key. You can request an API key from Wikitude to make the BETA tags go away.

The catch is, you must install their app along with your app to experience their AR platform. Only 1 platform gives you the flexibility of making your own which is <a href="http://www.mixare.org">Mixare</a>. It's Open Source (GPL v3) so we're free to use it as long as any app we make is GPL-ed v3 too. The app is pretty basic and needs more codes in it to make it mainstream. The best advantage from Mixare will be the ability to fully customize any aspects of the AR Viewer. Still trying JAR the app and using it as a library. Any pointers out there? Here's a video.

[flashvideo file=http://www.bango29.com/mixare.flv /]

There's another AR app opening up its platform but not as flexible as the two mentioned above. <a href="http://www.layar.com" target="_blank">Layar</a> is already growing into a big portal for AR. Developers are free to create layers of POI's and featured inside the application itself. Reasonable enough for an app that is well designed and one of the first for its kind. This doesn't meet my needs.

Wouldn't it be great if either Wikitude or Mixare be used as a module with <a href="http://appcelerator.com" target="_blank">Titanium Developer</a>? It will save a lot of development time. Again, if anyone is up for this, ring me!