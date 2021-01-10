+++
author = "Batista Harahap"
categories = ["analytics", "events", "flurry", "mobile app", "mobile app analytics"]
date = 2010-08-24T16:46:39Z
description = ""
draft = false
slug = "mobile-app-analytics"
tags = ["analytics", "events", "flurry", "mobile app", "mobile app analytics"]
title = "Mobile App Analytics"

+++


We've all heard, used, tweaked and cherish Google Analytics either for its web or mobile web capabilities of serving us information about our visitors. So I've been wondering about a mobile app equivalent I can use with the exception of mobile ad networks. I came across <a href="http://www.flurry.com" target="_blank">Flurry</a> a couple months ago and still using it until now.

One of Flurry's edge compared to other platforms is plainly and simply because it's the most flexible and complete with a price tag 0 in any currency. For time being it doesn't have any options for paid versions but they do say that in the future they will add paid features.

Another point to be considered is Flurry's libraries for mobile platforms is extensive. Flurry supports J2ME, Blackberry, Android, iPhone and iPad. I used the Android version and its SDK is dead simple. For the basics, all you have to do is just insert Flurry codes in the onStart() and onStop() method of your app's activities. I can't say for sure with other platforms but in the coming weeks I'm sure to offer more updates.

The next gem is Flurry Events. These are events that happens in your app. It basically tracks all interactions anonymously. For instance, when a user is registering for an account, it sends a Register Account event and when the registration is complete, Flurry then sends a Register Complete event. Yes you can do this on your own with your web services statistics but what if you don't have access to it? Or if you just want to focus on the app itself and not have more efforts with the statistics.

My second favorite is User Paths. From the first time your app is launched until a user stops the session (Flurry has 2 minutes idle time before considering a new session), Flurry tracked them and therefore spits up useful information about what users are doing with your app. This can help a lot with business related decissions.

Last but not least is a more technical side which is the ability to track Exceptions in your app and log it according to handsets. This has been one of the feature of Flurry that helped me a lot with bug fixing. Android Market does have error reporting but NOT as informative as Flurry's subjectively.

There you go, one of the best mobile app analytics platform: FLURRY!