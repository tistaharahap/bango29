+++
author = "Batista Harahap"
date = 2013-10-30T20:19:57Z
description = ""
draft = false
slug = "disable-xls-content-modifying-ads"
title = "Disable XL's Content Modifying Ads"

+++


Was doing more research and discovered that you can disable XL's ads if your website is infected with it. The solution is far simpler than the problem. Browser makers deserve all the credits for making something like this so simple.

So basically all you have to do is to add a header to your HTTP/S responses, the header in question is <code>X-Frame-Options</code>. It's pretty simple to do this, you can either use your server side platform or directly into the web server, it's your choice.

<strong>Nginx</strong>

I love nginx and it's dead simple to configure. Just add the line below inside your <code>server</code> configuration.

<pre>
add_header X-Frame-Options DENY;
</pre>

Browser support is also satisfying if you don't plan to utilize advance <code>ALLOW-FROM</code> permission:
<ul>
	<li>Chrome 4.1.*+</li>
	<li>Firefox 3.6.9+</li>
	<li>Internet Explorer 8.0+</li>
	<li>Opera 10.5+</li>
	<li>Safari 4.0+</li>
</ul>

Heads up though, if you have any content you purposely want to be able to be embedded in an <code>IFRAME</code>, the code above will disable it. There are multiple ways you can do basic ACL with this header and you should head up to Mozilla Developer Network from the link below.

<a href="https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options" target="_blank">X-Frame-Options at MDN</a>