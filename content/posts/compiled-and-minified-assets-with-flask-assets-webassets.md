+++
author = "Batista Harahap"
categories = ["flask", "flask-assets", "python", "Web", "webassets"]
date = 2013-08-17T19:19:44Z
description = ""
draft = false
slug = "compiled-and-minified-assets-with-flask-assets-webassets"
tags = ["flask", "flask-assets", "python", "Web", "webassets"]
title = "Compiled and Minified Assets with Flask-Assets & Webassets"

+++


All these times coding in PHP, I have yet to experience an elegant way to compile and minify assets including but not limited to CoffeeScript, JavaScript and or CSS. Watchers for specific transcompiler were needed and it blocks me from coding straight up. Well Python and Flask specifically is giving me sweet dreams.

Have a look first at <a href="http://elsdoerfer.name/docs/flask-assets/" target="_blank">Flask-Assets</a> and then dive in to <a href="http://elsdoerfer.name/docs/webassets/" target="_blank">Webassets</a>. FYI, Flask-Assets if you set it up as your dependency will include Webassets also. I love Flask because it's simple, to the point and very flexible to extend to your liking.

First of all, Webassets provides a number of transcompiled language support and also minification using <a href="http://elsdoerfer.name/docs/webassets/builtin_filters.html" target="_blank">filters</a>. Here are some the filters that I'm using routinely:
<ul>
	<li><a href="http://opensource.perlig.de/rjsmin/" target="_blank">rjsmin</a> - The default JavaScript minifier, this brings the best performance from my experience.</li>
	<li>cssmin - self explanatory</li>
	<li>less - Less markups to CSS</li>
	<li>coffeescript - A JavaScript transcompiler</li>
</ul>

Webassets is painless to set up and even easier to implement. The first thing you do is to set up a <code>Bundle</code> like so:

<script src="https://gist.github.com/tistaharahap/6258325.js"></script>

To put the compiled and minified assets into HTMLs, here's a rough example of the HTML template:

<script src="https://gist.github.com/tistaharahap/6258335.js"></script>

So it's trivially easier best of all, you don't have to set up any watchers. Just run the app like any Flask app and it will watch for changes automagically. My best advice is to put the static directory on a memory drive like <code>/dev/shm</code> if you're using Linux.

Take a look at Flask-Assets FAQ <a href="http://elsdoerfer.name/docs/webassets/faq.html#faq" target="_blank">here</a> and smile more everyday :D