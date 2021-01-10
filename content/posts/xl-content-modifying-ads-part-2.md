+++
author = "Batista Harahap"
categories = ["ads", "banner", "content", "hijack", "Mobile", "tweet", "urbanesia", "Web", "XL"]
date = 2013-10-24T10:01:45Z
description = ""
draft = false
slug = "xl-content-modifying-ads-part-2"
tags = ["ads", "banner", "content", "hijack", "Mobile", "tweet", "urbanesia", "Web", "XL"]
title = "XL Content Modifying Ads - Part 2"

+++


My tweets and <a href="http://www.bango29.com/go/blog/2013/xl-intrusive-content-modifying-banner-in-mobile-websites" target="_blank">the previous post</a> have gone viral. Lots of reactions both positive and negative. Some retweeted immediately and some calling me a fool for writing about injecting content within an SSL connection. Amazing to see all the responses. There is a pattern to be seen with people who reacted negatively: they tend to don't care about the ads.

Here's my said tweet:
<blockquote class="twitter-tweet"><p>Jangan pake KlikBCA di jaringan <a href="https://twitter.com/XL123">@xl123</a> kecuali login credential lo mau lo share sama xl, kalo begitu monggo. <a href="http://t.co/AvNfUuhORN">pic.twitter.com/AvNfUuhORN</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/statuses/392927921582534658">October 23, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Here are some replies:

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/tista">@tista</a> baru baca blog nya. iya, dengan <a href="https://twitter.com/XL123">@XL123</a> naro web asli di iframe, dia bisa ngebaca apa yang di key in. gila aja. &#10;/<a href="https://twitter.com/zmaintance">@zmaintance</a></p>&mdash; snydez (@snydez) <a href="https://twitter.com/snydez/statuses/393201381525295104">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/tista">@tista</a> <a href="https://twitter.com/XL123">@XL123</a> anda makai hp SMARTPHONE tapi otk anda tidak membuktikan anda sebagai pengguna yg smart :) itu hanya ads dari xl :)</p>&mdash; Adzuan (@zmaintance) <a href="https://twitter.com/zmaintance/statuses/393062569117626369">October 23, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/tista">@tista</a> <a href="https://twitter.com/kakilangit">@kakilangit</a> <a href="https://twitter.com/XL123">@XL123</a> eh memang ngga https?</p>&mdash; Heriyadi Janwar (@heriyadi) <a href="https://twitter.com/heriyadi/statuses/393168847533916160">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p>alasan kekhawatiran kemanan tersebut diulas <a href="https://twitter.com/tista">@tista</a> di <a href="http://t.co/WKzp1Q98FI">http://t.co/WKzp1Q98FI</a> cc <a href="https://twitter.com/XL123">@XL123</a></p>&mdash; Ivan (@stevanushk) <a href="https://twitter.com/stevanushk/statuses/393196872631738368">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/tista">@tista</a> <a href="https://twitter.com/XL123">@xl123</a> hoax... karena klikbca itu menggunakan HTTPS artinya layer di enkripsi... jd jgn buat statement yang ga2 klo ga ngerti mas</p>&mdash; Kendi (@kendivhy) <a href="https://twitter.com/kendivhy/statuses/393225064130174976">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/za_ka">@za_ka</a> <a href="https://twitter.com/XL123">@xl123</a> <a href="https://twitter.com/tista">@tista</a> situ bisa baca traffic ssl encrypted 128bit? wah otak lu secanggih mainframe CIA klo gituh xiixi <a href="http://t.co/o4gHOFjWwq">pic.twitter.com/o4gHOFjWwq</a></p>&mdash; Kendi (@kendivhy) <a href="https://twitter.com/kendivhy/statuses/393225906124111872">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/tista">@tista</a> <a href="https://twitter.com/za_ka">@za_ka</a> <a href="https://twitter.com/XL123">@XL123</a> sy sdh baca, tp statement situ barusan ttg share credential itu tidak sahih, silahkan lampirkan bukti traffic kl benar</p>&mdash; Kendi (@kendivhy) <a href="https://twitter.com/kendivhy/statuses/393240952426356736">October 24, 2013</a></blockquote>

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/BigGuzz">@BigGuzz</a> <a href="https://twitter.com/za_ka">@za_ka</a> <a href="https://twitter.com/XL123">@xl123</a> <a href="https://twitter.com/tista">@tista</a> ini yg dilihat dengan mata telanjang untuk traffic k arah https klikbca.. mana pass sy? <a href="http://t.co/lVUPb5pI7F">pic.twitter.com/lVUPb5pI7F</a></p>&mdash; Kendi (@kendivhy) <a href="https://twitter.com/kendivhy/statuses/393253089039220736">October 24, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

What some of the repliers didn't notice was the juicy stuffs happening behind the scene not even touching the network layer or its HTTPS protocol, doesn't have to. Just now I tried accessing KlikBCA and the ads are gone. People who tried now may not get the same page I got from my first screenshot.

If you've heard of <a href="http://en.wikipedia.org/wiki/Phishing" title="Phishing" target="_blank">Phishing</a> then you'll know that it doesn't take sophisticated means to get credentials. You fake a login page as if it's coming from the rightful owner. This is what actually was happening with me. XL served me a login page of KlikBCA which XL had injected their own codes. The codes displayed ads on a connection I <strong>already paid</strong> for.

Other than the ads display, the measure of power XL can utilize with this kind of unethical practice is only depending on your imaginations. XL are serving web pages as if the web pages are coming from KlikBCA.com or any other domain for that matter. They have within their grasp the ability to alter, intercept, modify and also collect information from us. Not by using complicated SSL penetration technique, you don't have too. A few lines of JavaScript is enough.

Here's a jQuery style demo of how you can do this with KlikBCA as the target:

<script src="https://gist.github.com/tistaharahap/7134283.js"></script>

So we as users are on XL's mercy, if they decide to do nasty stuffs or worst, XL doesn't even know they're doing nasty things to us. It's just too easy. I don't know what XL is doing so I won't trust them with any of my web based authentications and you should too.

<a href="https://twitter.com/kendivhy" target="_blank">@kendivhy</a> is also saying that the added bytes that users have to download are free of charge from XL. This is one of the more absurd statement I've read so far. For every website XL is injecting ads, our user experience quickly degrades. Why? The download times multiplies. As a web developer, I do work to shave off download times and XL just made years of work into the garbage. And why do you give in to the ads XL is serving? We've paid for our 3G connection remember?

Bottomline, your opinions are your own and this is mine. I can't agree with these kind of practices. Period.