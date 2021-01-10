+++
author = "Batista Harahap"
categories = ["compile", "fulltext", "fulltext search engine", "install", "Mac", "realtime indexes", "search engine", "snow leopard", "sphinx", "Tutorial"]
date = 2010-11-24T08:16:21Z
description = ""
draft = false
slug = "sphinx-fulltext-search-engine-part-1"
tags = ["compile", "fulltext", "fulltext search engine", "install", "Mac", "realtime indexes", "search engine", "snow leopard", "sphinx", "Tutorial"]
title = "Sphinx - Fulltext Search Engine - Part 1"

+++


It has been a few weeks after my first encounter with this Egyptian named gem called Sphinx. At first glance, it's complicated when looking at an already made sphinx.conf. However, after careful redesigning andÂ re-tinkering, it turns out to be one of the most flexible and yet light fulltext search engine available today.Â There are others but nothing as light, fast and sleek as Sphinx. The cold truth is that Sphinx is supporting SQL based databases as far as I know. Since Urbanesia is already using MySQL as our backend, we're lucky.

The first and most difficult part of learning Sphinx is it's installation routine. Numerous times I have failed compiling Sphinx on my Macbook and also on CentOS servers. That made me stayed away too far from it. So after a few Googling sessions, I thought it was time to tame the beast. First step was to compile Sphinx on my Macbook.

What you're gonna need are:
<ol>
	<li>Sphinx source code provided <a href="http://sphinxsearch.com/downloads/" target="_blank">here</a>. I downloaded the latest 1.10 Beta version, spoilers: Realtime Indexes :)</li>
	<li>expat library provided <a href="http://expat.sourceforge.net/" target="_blank">here</a>.</li>
	<li>libiconv library provided <a href="http://www.gnu.org/software/libiconv/" target="_blank">here</a>.</li>
</ol>
Where you're all set, we're gonna go ahead and start the fiesta. Just a note, this tutorial is downloading everything to /opt/sources and installing everything on /usr/local directory. You're free to tinker.
<ol>
<pre>sudo -s</pre>
<pre>cd /opt/sources</pre>
<pre>tar xfz expat-2.0.1.tar.gz</pre>
<pre>cd expat-2.0.1</pre>
<pre>./configure --prefix=/usr/local</pre>
<pre>make &amp;&amp; make install</pre>
<pre>cd ..</pre>
<pre>tar xfz libiconv-1.12.tar.gz</pre>
<pre>cd libiconv-1.12</pre>
<pre>./configure --prefix=/usr/local</pre>
<pre>make &amp;&amp; make install</pre>
<pre>cd ..</pre>
<pre>tar xfz sphinx-1.10-beta.tar.gz</pre>
<pre>cd sphinx-1.10-beta</pre>
<pre>./configure '--prefix=/usr/local/sphinx' CPPFLAGS="-I/usr/local/include
-I/opt/local/include -I/Applications/xampp/xamppfiles/include
-I/Applications/xampp/xamppfiles/include -arch i386" LDFLAGS="-L/usr/local/lib
-L/opt/local/lib" 'CFLAGS=-O -arch i386' 'LDFLAGS=-arch i386' 'CXXFLAGS=-O -arch i386'</pre>
<pre>make -j4 install</pre>
</ol>
So you now have successfully compiled Sphinx and installed it to your Macbook. In any case, as long as it's a Unix flavored OS, the routine is basically the same. Only in Mac OS X Snow Leopard I'd have to put the compiler in 32 bit mode because it mistakenly overridden all flags to 64 bit if not.

The next part of the tutorial will be about generating your own sphinx.conf. Until then!