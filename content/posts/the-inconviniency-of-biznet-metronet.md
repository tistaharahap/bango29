+++
author = "Batista Harahap"
categories = ["biznet", "biznet metronet", "corporate internet", "internet connection", "metronet"]
date = 2010-04-08T11:15:28Z
description = ""
draft = false
slug = "the-inconviniency-of-biznet-metronet"
tags = ["biznet", "biznet metronet", "corporate internet", "internet connection", "metronet"]
title = "The Inconviniency of Biznet MetroNET"

+++


<strong>Update: 14 April 2010 - A certain engineer from Biznet called me this afternoon. He was one of the engineers who were responsible for a great Yahoo OHD 2009 Internet connection. He sensibly told me that it was indeed a flaw in their recent policy change and that all MetroNET 1 Mbps accounts are experiencing the same thing. He said there will be a policy change yet again this Saturday so I'm gonna keep my fingers crossed. Thanks Biznet.</strong>

Okay, it's been a while since I first subscribed to Biznet at my office. In Kemang Point, there's practically only 2 ISPs providing Internet access which are Biznet and Telkom Speedy.

I had a very bad experience with Telkom Speedy. In the day time, I can't even connect and if when I did managed to connect, it's still not as I've come to expect. Very slow and very problematic.

So I opted for Biznet as the office's ISP. I started subscribing around November 2009. The first time I subscribed to MetroNET 1 Mbps was wonderful. Everything was as I expected. I even upgraded the connection speed to 4Mbps for 3 days following urgent needs. Because of my satisfactory level was high, I recommended Biznet as one of 2 ISPs contracted to provide Internet access to Yahoo South East Asia Open Hack Day 2009 event. There were some oops moments with Biznet before the event started but their incredible support team prevailed and make all the woes go away.

I remembered it was a Saturday and I was at the office configuring a bunch of wireless routers for DD-WRT and 4 PCs to be set up as servers. The Internet connection suddenly dropped. I had no connection whatsoever. I really needed the Internet connection to download Linux &amp; FreeBSD distros. I wanted to try them out to the servers. I called it in to their customer care and waited for hours and still no Internet. At around 10PM, the support team came to my office. They tried to figure out what's been happening with the connection. From their conversation, I can assume the sudden drop was because of a glitch made by one of their engineer. The glitch knocked down the whole Kemang area. I was still satisfied with all the efforts the support team had to extend on a Saturday night :)

Just a few months ago, another connection drop happened. So again I contacted Biznet's customer care and doing the usual troubleshooting. The problem was on their end. I didn't care actually what the problem is and I paid full every month so I want to be online. They gave a temporary account and it was a 4Mbps. I also got a public static IP with the account. How great was that? I even assigned a subdomain and made my office Hackintosh as a web server. It's for work related reasons mind you ;) lol

Sadly, all things must come to an end. Another connection drop happened. This was because Biznet has fixed the problems and normalizing my connection to the primary account. I received an email saying that all MetroNET 1Mbps subscribers will be assigned a dynamic local IP address. That's nothing new from a NAT point of view and I didn't even consider any problems from it. Well unfortunately for me, it became a problem.

I noticed that I was failing all the time to login to my WHMCS admin module. I thought it was because the version I'm running is not current. I upgraded WHMCS and the same thing is still happening. I'm also having difficulties logging in into my Cpanel/WHM server. It keeps asking me for passwords. My Cpanel/WHM is the latest STABLE version. I guerrilla my way into Google to find a solution only to find I'm lonely with this phenomena. So I dived into raw logs on the server. I noticed that the connections from my end was from 2 IPs. That's a BIG road block for Cpanel/WHM servers. I'm sure it's security related and I'm not happy disabling security features only to let me login without a hitch.

Squid is the answer. I tried logging in by using a Squid server. It worked on Cpanel/WHM but failed with WHMCS. I called it in to Biznet Customer Care. They asked me if they can use my account at their end to reproduce the problem. I gave the a demo account login on my Cpanel/WHM server to try for themselves. They said they're experiencing the same old thing. A couple days after, they told me that they've resolved the issue. When I got to the office, THEY DIDN'T! I was still having the same difficulties because the IPs kept alternating and both Cpanel/WHM and WHMCS couldn't be logged in. They called me and I said it was still happening. They wanted to use my account again (leaving me with no Internet on a working day). I refused and they said they'll try their best.

It's been a month or so and still I'm having the same problem. Still no appropriate action. I'm very disappointed with them. Their change of policy with the alternating IPs is something that I'm sure well considered by them because I believe Biznet has a great corporate culture to which every ISP in Indonesia must follow. However, as you can see above, my tolerance for dropped connections and the login issue is just at its max.

If you're having the same problem I'm having, tell me! Why not start a petition so Biznet will see that it's affecting more subscribers than just me?

Anyways, I'm still within a moderate satisfactory level with their service and I hope they will deliver better services in the future. So to wrap things up, my sincere gratitude for Biznet services, they are an example to follow.