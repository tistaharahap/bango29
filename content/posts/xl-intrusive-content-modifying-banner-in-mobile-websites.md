+++
author = "Batista Harahap"
categories = ["ads", "banner", "content", "hijack", "Mobile", "urbanesia", "Web", "XL"]
date = 2013-10-07T17:31:55Z
description = ""
draft = false
slug = "xl-intrusive-content-modifying-banner-in-mobile-websites"
tags = ["ads", "banner", "content", "hijack", "Mobile", "urbanesia", "Web", "XL"]
title = "XL Intrusive Content Modifying Banner in Mobile Websites"

+++


Last Friday, October 4th 2013 I was hanging out with some friends and while searching for a place to do so, I opened up Urbanesia on it mobile web <a href="http://m.urbanesia.com/" title="Urbanesia" target="_blank">http://m.urbanesia.com/</a>. While I was searching, I noticed there's a banner displayed on top of the page, it was definitely not Urbanesia's and so I got curious.

When digging into the mobile web source code, we didn't activated any codes that'll lead to any banner placements on top so this banner must surely be injected by a third party. My mind were full of technical ideas translating into security breaches/flaws making the injection a reality.

First of all, we didn't use any JavaScript library on our mobile web, it was all pure JavaScript. All the JavaScript and CSS the website needed were embedded into the HTML. The website is very light and yet it took a relatively extended period of time to load on my Nexus 4. So I switched to opening it with my Z10 and it loaded as fast as I expected it to be. There wasn't any banner, I was using a Telkomsel 3G connection on my Z10.

So the culprit is XL definitely since they also took the time to display their logo on the banner. Here's a screenshot.

<a href="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-ads-urb.jpg"><img src="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-ads-urb-180x300.jpg" alt="XL Ads" width="180" height="300" class="size-medium wp-image-1104" /></a>

This is most definitely a low blow by XL. They're practically monetizing using our content and also displaying ads on a 3G connection I already paid for. For both the content provider and user, this is a very unethical and disgraceful act to say the least.

My blog post here will talk more about the technicalities on how XL is able to do this. I won't be 100% correct but I'll settle for 99%.

XL's technique has a flaw. Try refreshing Urbanesia's mobile web and soon you'll notice that in some cases, it will show code fragments instead of the website. Why? Urbanesia's mobile uses Google Analytics server side implementation to track our statistics. By doing so, we have a small <code>ga.php</code> on our server to track users. Here are the codes below.

<script src="https://gist.github.com/tistaharahap/6871276.js"></script>

The script displays a small 1x1 GIF file and I made some modifications to only track users and not bots. Now instead of showing the GIF file, it showed code fragments. They mistakenly thought the <code>ga.php</code> file for a document when in fact it's an image. The <code>Content-Type</code> was correct as <code>image/gif</code> but I think they filter by looking at its file extension. Here's the screenshot.

<a href="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-ads-codes.jpg"><img src="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-ads-codes-180x300.jpg" alt="XL Codes" width="180" height="300" class="aligncenter size-medium wp-image-1106" /></a>

There were some JavaScript URLs there so I went on to download the JavaScript file. The file is only downloadable if you're on their 3G network. They have a minified and obfuscated version named <code>ibn_complete_20130930.min.js</code> and a more readable version named <code>ibn_complete_20130930.js</code>. Here's a Github Gist of the readable version: <a href="https://gist.github.com/tistaharahap/6837508" title="ibn_complete_20130930.js" target="_blank">https://gist.github.com/tistaharahap/6837508</a>.

You'll notice that they included their development and production URLs intact within the source code. They also included jQuery with the codes. When looking at the codes, they were only doing minimal DOM manipulation using jQuery and yet the bloated user's download size with the whole source code.

So my attention went into the JavaScript file they served. To disable the ad serving mechanism, I thought I can just nullify any requests to their ad servers URLs. So I tried to do so <a href="https://gist.github.com/tistaharahap/6871441" title="Anti XL Ads" target="_blank">here</a>. It didn't work which gets me even more curious. This leaves me only 1 option, to debug straight into my Nexus 4 by following the instructions from Google <a href="https://developers.google.com/chrome-developer-tools/docs/remote-debugging" title="Remote Chrome Android Debugging" target="_blank">here</a>.

What got me more pissed off than before, I found out that Urbanesia's content was served as an <code>IFRAME</code> inside their HTML document. There were placeholders for top, left, right and bottom banners. But if you see the screenshots above, the domain of the website is still Urbanesia's. So basically XL did not only modified contents, they also manipulate users into believing that the ads are coming from Urbanesia's server. This disgusts me.

<a href="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-htmls.jpg"><img src="http://www.bango29.com/go/wp-content/uploads/2013/10/xl-htmls-300x121.jpg" alt="xl-htmls" width="300" height="121" class="aligncenter size-medium wp-image-1107" /></a>

You see above, it's ridiculously inappropriate at all. Urbanesia did not consent to anything like this at all nor there were any notifications to our part about their practices. This is just wrong.

My tweets were responded by friends in the startup community and also from outside the community. The responds were in Facebook, I'm auto posting tweets to Facebook by the way. I can't represent them as this blog post is my personal thoughts but suffice to say, my thoughts are not much different than theirs.

So whether you're a content provider or a user, we are both offended by this kind of practice by XL. The big boys said that they are writing a protest letter to XL, let's see how this can stop XL from violating our rights. Yes we live in Indonesia which gets me even more pissed off. If you wanna help, retweet this blog post and let more people know.

<strong>DISCLAIMER</strong>: While I work at Urbanesia, this blog post is my personal thoughts and therefore does not imply the views of Urbanesia as an entity.