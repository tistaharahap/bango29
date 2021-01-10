+++
author = "Batista Harahap"
date = 2009-01-18T11:08:44Z
description = ""
draft = false
slug = "tutorial-a-simple-url-redirector-part-1"
title = "Tutorial: A Simple URL Redirector - Part 1"

+++


A few months ago I made a simple URL redirector to mimic <a href="http://tinyurl.com" target="_blank">tinyurl.com</a>'s service. You may use it if you like it by the way. The redirector is located at <a href="http://r.bango29.com/" target="_blank">http://r.bango29.com/</a>.

The basic ingredients are the usuals:
<ul>
	<li>Apache with mod_rewrite</li>
	<li>PHP</li>
	<li>MySQL</li>
</ul>
Before getting into the actual coding, I did the htaccess part first. In any Apache installation, we can use htaccess files to extend Apache's capabilities. The is actually only an extension and if you're working on a Windows platform, you can only rename it by using the command line. The file must be exactly named:
<pre lang="apache">.htaccess</pre>
Just put the htaccess on your root public html directory and type in the codes below:
<pre lang="apache">
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^/\.]+)/?$ /index.php?q=$1 [L]</pre>
Now let's go into the details of the above code. The first line query Apache if the rewrite module is available or not. We then activate the rewrite engine and set our base URL as our rewrite base.

The fourth line is where the trickyness start. It's basically telling Apache if the visitor's request is not a file (indicated by the !-f flag) then proceed to our next condition. The next condition query Apache if it is a directory or not (indicated by the !-d flag).

Now if both the conditions are satisfied, we then go to the last rule (indicated by [L]). This particular rule is basically telling Apache to throw everything after the last <strong>/</strong> as an HTTP GET variable named <strong>q</strong> and let our PHP script process the request.

Okay the first part of this tutorial is a wrap. Next we're gonna set up a MySQL database for our URL Redirector. On the third part, let's talk about the actual PHP script. Part 4 is basically a few tips on how to further develop and maximize our finished product. Until then, if you have any questions you can always reach me through my <a href="batista@bango29.com">email</a> or message me in <a href="http://r.bango29.com/tistafb">Facebook</a>.