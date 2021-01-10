+++
author = "Batista Harahap"
date = 2012-07-21T00:33:16Z
description = ""
draft = false
slug = "techtorial-responsive-with-zurb-foundation-html5"
title = "[Techtorial] Responsive With Zurb Foundation & HTML5"

+++


Responsive techniques with websites have been around for a while now. Not many websites here in Indonesia are responsive. Being responsive for me is out of necessity, mobile web traffic is increasing very rapidly and being responsive is the next logical step despite already having a mobile web. It will look good with search engines too :)

Zurb Foundation is one of a handful collection of <span style="text-decoration: underline;">frontend</span> Responsive frameworks out there. However, to get your website to be really resilient, you should start from the server side. There's a slide show <a href="http://www.slideshare.net/yiibu/adaptation-why-responsive-design-actually-begins-on-the-server" target="_blank">here</a> by <a href="http://www.slideshare.net/yiibu" target="_blank">Yiibu</a> covering all the aspects why being responsive starts from the server side part. Keep in mind that frontend Responsive frameworks does not actually help with optimizing the images your clients will download nor do it will strip HTML fragments that shouldn't be included, it simply hides them with CSS, but with some clever JavaScript, you could take them off from DOM but then again that's more work for handsets with minimum CPU power.

To get into perspective, by making your website Responsive, you start Mobile First. Why? Because mobile version is considered as the lowest fidelity in terms of the Information Architecture and also from a visual point of view. By doing this, you can actually devise a scale of priority and get to know your products/features deeper. If you're still not sure, you can always A/B test it.

For the purpose of this Techtorial, we're going to build a simple news reader application for <a title="Rama Mamuaya" href="http://twitter.com/rampok" target="_blank">my friend</a>'s Tech Blog <a title="Daily Social" href="http://dailysocial.net" target="_blank">DailySocial.net</a>. We're going to extract contents using only frontend technologies, JavaScript to be exact. There will be no caching (persistency) at all, you are welcomed to fork and do your own implementation, you could try to persist by using <a title="HTML5 Local Storage" href="http://www.w3schools.com/html5/html5_webstorage.asp" target="_blank">Local Storage</a> or even cookies (beware of the 4 KB limit for this).

Before going through, these are the things you will need for later:
<ol>
	<li><a title="Zurb Foundation" href="http://foundation.zurb.com" target="_blank">Zurb Foundation 3.0</a></li>
	<li>Code editor, <a title="Smultron" href="http://sourceforge.net/projects/smultron/" target="_blank">Smultron</a> will suffice for Mac users</li>
	<li>Some <a title="HTML5 Rocks!" href="http://www.html5rocks.com/en/" target="_blank">HTML5 Knowledge</a></li>
	<li>Github repository for the source code in this tutorial is available <a title="Github Repository for This Article" href="https://github.com/tistaharahap/techtorial-responsive-html5" target="_blank">here</a></li>
</ol>
We're gonna start by building the layout. Every layout elements in Foundation is made up of grids. Every row, there are 12 columns with a default gutter size of 30 pixels. The interesting part of Foundation 3.0 is that now it provides mobile columns. Mobile columns spans 4 columns and it will be really useful in cases like when on the Desktop the first column is 4 columns wide, the second is 8 columns while on the mobile version you'd want it to be equally divided columns.Â You can create your own custom Foundation by the way.

Starting up we want a layout with a website name at the top, articles at the belly, sidebar on the right and some fancy notes for the footer.

<script src="https://gist.github.com/3153967.js"> </script>

You can see how easy it is to do the columns. Of course, it's just a single row occupying the whole width. Let's make it more interesting by dividing into 2 belly columns consisting of the articles and a sidebar.

<script src="https://gist.github.com/3153987.js"> </script>

When you resize your browser, the layout will automagically be adjusted with the screen resolution. Looking the code above, I encourage you to hack the left column by adding a <code>mobile-three</code> class and a <code>mobile-one</code> class on the right. The behaviour of the layout changes by persisting the sidebar to always be on the right. Doesn't look good right? Revert it.

<script src="https://gist.github.com/3154000.js"> </script>

Now the footer is done and you've got a working layout that is responsive and ready for some JavaScript manipulations.

The data source comes from DailySocial's JSONP endpoint. If you don't know what JSONP is, there's a good reading about it <a href="http://json-p.org/" target="_blank">here</a>. Because of the nature of JSONP, all we gotta do is just create a callback function in JavaScript and include a script from DailySocial's JSONP endpoint after your callback function is declared.

<script src="https://gist.github.com/3154015.js"> </script>

<script src="https://gist.github.com/3154022.js"> </script>

We're done! So quick and painless to finish this Techtorial right? There are a lot of improvements in store for this DailySocial reader. On the next tutorial, we're gonna cache our JSON into the browser's Local Storage. So for now, have fun with the codes!