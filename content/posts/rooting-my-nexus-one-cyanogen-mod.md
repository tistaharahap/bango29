+++
author = "Batista Harahap"
categories = ["amon ra recovery", "Android", "cyanogenmod", "Nexus One", "root", "rooted", "xda-developers"]
date = 2010-05-05T18:32:03Z
description = ""
draft = false
slug = "rooting-my-nexus-one-cyanogen-mod"
tags = ["amon ra recovery", "Android", "cyanogenmod", "Nexus One", "root", "rooted", "xda-developers"]
title = "Rooting My Nexus One - Cyanogen Mod"

+++


Okay let me be straight up to you first, I rooted my Nexus One a few hours after I got it :) Here's my experience rooting it.

[caption id="attachment_292" align="alignnone" width="274" caption="Google Nexus One"]<a href="http://www.bango29.com/go/wp-content/uploads/2010/05/nexus-one-specs-shot.png"><img class="size-full wp-image-292" title="Google Nexus One" src="http://www.bango29.com/go/wp-content/uploads/2010/05/nexus-one-specs-shot.png" alt="Google Nexus One" width="274" height="365" /></a>[/caption]

Before I start, while searching for a good picture of a Nexus One, I opened up <a href="http://www.google.com/phone/" target="_blank">Google's official Nexus One web page</a>. The Nexus One picture was actually a Flash applet lol. I hope this means that Google and Adobe are now soulmates lol. Would love to fire up Flash with my Nexus One.

What you're gonna need is some free time and a few readings. Some of the steps I copy pasted from sources listed, the credit should go to the wonderful community forum of <a href="http://forum.xda-developers.com/forumdisplay.php?f=556">XDA-Developers.com</a>. Been a member since my first XDA I with the antenna lol. Seems like a million years ago.

Here's a warning from cyanogen when you're gonna go ahead and root your Nexus One.
<pre lang="c">#include 
/*
 * Your warranty is now void.
 *
 * I am not responsible for bricked devices, dead SD cards,
 * thermonuclear war, or you getting fired because the alarm app failed. Please
 * do some research if you have any concerns about features included in this ROM
 * before flashing it! YOU are choosing to make these modifications, and if
 * you point the finger at me for messing up your device, I will laugh at you.
 */</pre>
That coming from the ROM chef so be sure that you know what you're doing! So for this to happen you should already have <a href="http://developer.android.com/sdk/">Android SDK Tools</a>, <a href="http://forum.xda-developers.com/showthread.php?t=611829">Amon Ra's Recovery Image</a> and of course <a href="http://forum.xda-developers.com/showthread.php?t=623496">CyanogenMod-5 Kang Central Station</a>. You can root using your own Mac, Linux or Windows computer. A few needed pointers, put all your downloaded files at your Desktop so you can navigate easily. When the guide asks you too navigate to the Android SDK Tools folder, follow these steps on your Terminal:
<pre lang="bash">MAC &amp; Linux
cd ~/Desktop/android-sdk-mac_86/tools</pre>
I rooted mine by following a guide from AndroidAndMe.com located <a href="http://androidandme.com/2010/01/hacks/video-how-to-unlock-and-root-a-nexus-one/">here</a>. To NOT do any content repetitions, I'm just gonna display the video on that page and you guys should go on from there to root your Nexus One. It's a very friendly guide already so I'm pretty sure you will get along just fine without any meaningful problems.

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="390" height="219" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="src" value="http://vimeo.com/moogaloop.swf?clip_id=8685475&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=c9ff23&amp;fullscreen=1" /><embed type="application/x-shockwave-flash" width="390" height="219" src="http://vimeo.com/moogaloop.swf?clip_id=8685475&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=c9ff23&amp;fullscreen=1" allowscriptaccess="always" allowfullscreen="true"></embed></object>

Easy right? Now you're gonna install CyanogenMod into your Nexus One. Follow the steps below to get into Amon Ra recovery image and flash CyanogenMod:
<ol>
	<li>Copy your downloaded <a href="http://forum.cyanogenmod.com/index.php?/forum/8-nexus-one/">CyanogenMod zip file &amp; Google Apps</a> into the root directory of your Nexus One's SD Card.</li>
	<li>Turn Off your phone.</li>
	<li>Turn it back on by pressing &amp; holding the <strong>Volume Down</strong> button first and pressing the power button.</li>
	<li>Navigate to RECOVERY with the the VOLUMEDOWN-key.</li>
	<li>Press the POWER-key to select.</li>
	<li><strong>WIPE</strong> everything first using the Wipe menu.</li>
	<li>Backup you're current ROM first if needed.</li>
	<li>Choose <strong>Flash Zip From SD Card</strong> and first choose to flash CyanogenMod and Google Apps afterwards.</li>
	<li>Reboot and cross your fingers.</li>
</ol>
Enjoy!