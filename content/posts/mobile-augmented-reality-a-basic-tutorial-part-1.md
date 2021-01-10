+++
author = "Batista Harahap"
categories = ["application", "Augmented Reality", "javascript", "Mobile", "Open Source", "titanium developer", "Tutorial", "Web"]
date = 2010-04-06T07:48:29Z
description = ""
draft = false
slug = "mobile-augmented-reality-a-basic-tutorial-part-1"
tags = ["application", "Augmented Reality", "javascript", "Mobile", "Open Source", "titanium developer", "Tutorial", "Web"]
title = "Mobile Augmented Reality, A Basic Tutorial - Part 1"

+++


On my last post, I mentioned the definition of Augmented Reality (AR). Now I'm adding the word Mobile to it.

At the current time, platforms that I've tried to developed upon supporting AR are iPhone and Android. Well actually I coded once and used <a href="http://www.appcelerator.com/" target="_blank">Titanium Developer</a> to make the actual executable files for each platform.

Titanium offers current web standards as a mean to create those mobile applications. I'm now using Titanium Developer 1.0 with the 1.1 Mobile SDK. The requirements to be able to run Titanium and produce for iPhone &amp; Android are:
<ul>
	<li>A decent Mac running Snow Leopard (Leopard will do). I used my Macbook and a Hackintosh hehe.</li>
	<li><a href="http://developer.apple.com/technologies/xcode.html" target="_blank">Xcode</a>. Get it from your installation cd that comes with your Mac.</li>
	<li><a href="http://developer.apple.com/iphone/" target="_blank">iPhone SDK</a> 3.0 minimal. I used 3.1.2 on my Hackintosh and 3.1.3 on my Macbook.</li>
	<li><a href="http://developer.android.com/sdk/index.html" target="_blank">Android SDK R5</a></li>
	<li><a href="http://www.appcelerator.com/products/download/" target="_blank">Titanium Developer 1.0</a></li>
</ul>
So fire up your Titanium and let's begin the tutorial. It will start on the Dashboard module. Go ahead and click on the NEW PROJECT top left icon.

[caption id="attachment_205" align="alignnone" width="297" caption="Step 1 - New Project"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step1.jpg"><img class="size-full wp-image-205" title="Step 1 - New Project" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step1.jpg" alt="Step 1 - New Project" width="297" height="74" /></a>[/caption]

Next up, it will show a screen showing metadata and configurations for the application. Choose <em><strong>Mobile</strong></em> as the project type. Type in the application name on the name column; I'm naming it <em><strong>Mobile AR Demo</strong></em>. Identify our application and in this case, it's <em><strong>com.mf.ardemo</strong></em>. Choose the directory where our application will reside and enter a URL for it. I'm using Titanium 1.1 so I choose <em><strong>1.1.0</strong></em> as the Titanium SDK Version. Now if Titanium successfully found your iPhone and Android SDK path, it will show a check mark on both, if not, you will have to specify the path. Click on <strong>Create Project</strong> afterwards and it will show another screen displaying editable fields.

[caption id="attachment_208" align="alignnone" width="412" caption="Step 2 - Project Metadata &amp; Configuration 1"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step2.jpg"><img class="size-full wp-image-208 " title="Project Metadata &amp; Configuration" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step2.jpg" alt="Project Metadata &amp; Configuration" width="412" height="269" /></a>[/caption]

[caption id="attachment_211" align="alignnone" width="407" caption="Step 3 - Project Metadata &amp; Configuration 2"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step3.jpg"><img class="size-full wp-image-211 " title="Project Metadata &amp; Configuration 2" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step3.jpg" alt="Project Metadata &amp; Configuration 2" width="407" height="308" /></a>[/caption]

The most important part on Step 3 will be specifying your <strong>Application Icon</strong>. Use any 57x57 pixels icon of your choosing. It will default to Titanium's icon if not specified.

Next up, you may wanna change the default splash screen when the application is launched. To do this, go to the directory where your application resides. In my case it will be <strong>/Users/Tista/Development/iPhone/Mobile AR Demo</strong>. When you're in there, go to the <strong>Resources </strong>sub folder. That is where we're gonna put all our JavaScript files along with all other resources. Inside the directory, you will find an <strong>android</strong> and an <strong>iphone </strong>directory. Make a 320x480 pixels splash screen and you're set. Put your splash screen there replacing the <strong>Default.png</strong> file. What's interesting is that you can specify different Application Icons and Splash Screens for both platforms, just put them in the respective directories and Titanium will automatically configure.

[caption id="attachment_213" align="alignnone" width="386" caption="Step 4 - Application Icon &amp; Splash Screen"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step4.jpg"><img class="size-full wp-image-213 " title="Step 4 - Application Icon &amp; Splash Screen" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step4.jpg" alt="Step 4 - Application Icon &amp; Splash Screen" width="386" height="90" /></a>[/caption]

The 4 steps we did earlier is already enough to show a Hello World application on your device. If you wanna test it, you can go ahead and use the emulators. Back in Titanium, click on the <strong>Test &amp; Package</strong> tab. I will try running on an iPhone emulator, it's chosen by default so I go ahead and choose the SDK I'm aiming for which is <strong>3.1.2</strong> and just click <em><strong>Launch</strong>. </em>Afterward Titanium will show verbose output of what it's currently doing on the blank window. Upon success, it will immediately launch the application on the emulator.

[caption id="attachment_214" align="alignnone" width="350" caption="Step 5 - Run on Emulator 1"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step5.jpg"><img class="size-full wp-image-214  " title="Step 5 - Run on Emulator" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step5.jpg" alt="Step 5 - Run on Emulator" width="350" height="270" /></a>[/caption]

[caption id="attachment_215" align="alignnone" width="375" caption="Step 5 - Run on Emulator 2"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/04/step5.2.jpg"><img class="size-full wp-image-215   " title="Step 5 - Run on Emulator 2" src="http://www.bango29.com/go/wp-content/uploads/2010/04/step5.2.jpg" alt="Step 5 - Run on Emulator 2" width="375" height="182" /></a>[/caption]

OK so the 5 steps above wraps up Part 1 of the tutorial. Should you have any questions, drop a comment or <a href="http://twitter.com/tista" target="_blank">tweet me</a>. Thanks for tuning in ;)