+++
author = "Batista Harahap"
categories = ["ads", "annoy", "facebook", "google", "machine learning"]
date = 2013-07-06T22:10:27Z
description = ""
draft = false
slug = "google-adsense-and-facebook-ads-annoyances"
tags = ["ads", "annoy", "facebook", "google", "machine learning"]
title = "Google Adsense and Facebook Ads Annoyances"

+++


I have been having questions every time I am served ads by Google Adsense for the last few months. With Adsense, essentially everywhere you go on the Internet, you are followed by it. Almost any website with ads I visited were serving them from Adsense. It is annoying! Not because of the nature of being served ads but because of being served the same ads over and over.

My first reaction when I began realizing how annoying this has been was to figure how Adsense can pull something like this. The amount of data that would need to be analyzed at run time is just huge and I'm sure that's still an understatement. Technically, this is one of the better feats of how technology on the internet is growing and implemented like never before. I mean, just a few years ago, Big Data isn't as cool as it is today, back then terms like Data Warehouse is more common. Sounded more like SDLC while in college: Obsolete and enterprisey.

But then again no matter how great an engineering feat it is, it's still annoying.

Facebook is as equally annoying as Adsense. It's basically serving me ads while I am at Facebook.com with ads that are repetitively boring. I can appreciate the level of engineering needs to be done to achieve this but still I am not a product, I am a human being. So this post is me being human versus an army of ads machines.

I have a pretty good example. I first heard about <a href="http://www.digitalocean.com" target="_blank">Digital Ocean</a> from an article at Hacker News comparing Cloud providers. When I visited their website, I was sold instantly. A cheap SSD cloud VM with enough spec for me for only  a fixed US$ 5/month. At that time I still have 2 <a href="http://www.rackspace.com" target="_blank">Rackspace</a> cloud VMs costing me about US$ 40/month. So for 2 cloud VMs, I would only spend US$ 10/month at Digital Ocean.

Instantly I signed up and was blown away by how fast they can provision a VM. Their promise was 55 seconds to provision a new VM and the promise is good. My VM was ready in less than 55 seconds by the way. When I was able to login to the newly created VM, I instantly check their I/O performance.

<pre lang="bash">
$ dd if=/dev/zero of=/tmp/out.img bs=8k count=512k
</pre>

The result was <code>120 MB/s</code> which is ~20 MB/s faster than the SSD I'm using in my Macbook right now.

Just tonight when I was Facebook-ing, I noticed an ad on the right sidebar. The ad was about Digital Ocean. Now almost every time I log on to Facebook, the Digital Ocean ad mostly reveal itself. I was thinking to myself, I was already blown away by the I/O benchmark, why keep trying to win me over? I am already your customer. 

To see Digital Ocean's ad makes me annoyed more than Adsense. Other than I'm already their customer, it's because the algorithm for Facebook ads doesn't even care about me already as Digital Ocean's customer. The algorithm figures out that I'm into those things, offer me ads about those things and sell my eyeballs to the highest bidder.

Now comes Adsense. I just watched some videos on YouTube about airplanes and I love airplanes. You know what ad is shown? It's <a href="http://www.mailgun.com/" target="_blank">Mailgun</a>. I have visited Rackspace and Mailgun's website before and was sold to Rackspace but definitely not sold with Mailgun. I have my reasons about Mailgun.

So why do I kept being served ads from Mailgun when in honest truth, I don't wanna be their customer. I am already very happy with <a href="https://aws.amazon.com/ses/" target="_blank">Amazon SES</a>.

I wasn't signed in into YouTube so I figured the recent privacy policy changes Google made us agree to a few months ago must be enabling this to happen. Google knows who I am as long as I have signed in to any of their services. I don't like this at all. Not just because my profile is essentially public within Google's web properties but why offer me ads from Mailgun which their services I have no interest at all.

On a contextual level, yes the algorithm works to know what I am in to but it failed miserably to detect that my past visit to Mailgun didn't end up with me as their customer. So stop serving me those ads.

Another case with both Facebook and Adsense is <a href="http://www.newrelic.com" target="_blank">New Relic</a>. I have just signed up for a free account there to trial how easy can my life be if New Relic can help me analyze codes and performance hickups by just the most simple steps.

As I said, I am a New Relic customer. Very happy with the T-shirt they sent out to free. Their product is also really awesome. I have a dashboard that is enabling me to measure performance easily. They also have an API that I can query for more specific needs. It's great.

Since I became New Relic's customer both Facebook and Google served me all their inventories about New relic almost all the time. I got bored by the tagline "Nerd's Life" because it popped in all New Relic ads be it in Facebook or Google. Why do I have to be served more ads like this, why not serve me ads about something else like where I wanna spend my honeymoon later with my wife to be?

This made me rethink the whole strategy of serving ads to users. Ads is the most successful internet business model to generate revenue. But instead of second guessing what my interest are, why not just ask me?

I am more than willing to increase their Click Through Rate so long as the ads are relevant and current to me. The context of me liking anything geeky is just not enough to serve me geeky ads. I am still a human being, I like to go out, travel and do more stuffs than just how my profile look to Facebook and Google.

Facebook and Google hasn't even introduce who they are to me personally, so why act like they know me? I know from first hand experience that context is the most important element to serve content, I appreciate it. However, the data is not rich enough to stop me being annoyed by the same ads over and over.

They say consistency is a recipe for success but for the cases I mentioned above, consistency consistently makes me block my brain for ad spots. Whenever I see ads, I look for any <code>[X]</code> button to hide them and hopefully permanent.

Never really liked ads but I'm totally not against ads, I just hope the ads served are more relevant than like just saying: "<em>oh yes I know that guy, he's a geek.</em>". Why not do a: "<em>Of course, Tista is already a customer for New Relic and Digital Ocean, he doesn't really like Mailgun so let's take a chance to serve him ads about travelling. Let's see if the CTR increases.</em>"

Just my piece of thought and a plea for ads based revenue first tiers to show some interest towards me before feeding me crap. Facebook and Google, great engineering implementation even though you guys suck at predicting what I want to see.

Do me a favor, give a chance for the algorithm to be creative, I'm sure machines will someday be more creative than us. Hell, <a href="https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov" target="_blank">machine once beaten Gary Kasparov at chess</a> although eventually the tally concludes human over machine dominance.