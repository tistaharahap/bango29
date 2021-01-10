+++
author = "Batista Harahap"
categories = ["2.2", "Android", "Boston", "clockwork", "cmlmod", "cyanogen mod", "froyo", "journey", "nexian", "nexian journey", "RUT", "Vibo"]
date = 2010-11-10T09:56:56Z
description = ""
draft = false
slug = "upgrade-nexian-journey-to-froyo-cyanogen-mod-6-1"
tags = ["2.2", "Android", "Boston", "clockwork", "cmlmod", "cyanogen mod", "froyo", "journey", "nexian", "nexian journey", "RUT", "Vibo"]
title = "Upgrade Nexian Journey to Froyo - Cyanogen Mod 6.1"

+++


The first Cyanogen Mod build for Nexian Journey is quite the rush. By default, the CPU is forced to run at 800 MHz, that's more than the 600 MHz capability of the phone. Luckily, the next build now defaults to 600 MHz and that's the build I'm upgrading my phone with.

The requirements to upgrade is the following:
<ol>
	<li>Upgrade your phone to Eclair if you're not already in Eclair. Steps to do so after the break. Download CMLMod 1.3 <a href="http://r.bango29.com/adYMkW" target="_blank">here</a> for some Eclair love.</li>
	<li>You will need Clockwork recovery image after flashing CMLMod 1.3, download <a href="http://r.bango29.com/cEdGhF" target="_blank">here</a>.</li>
	<li>This is the best part, Cyanogen Mod 6.1 Build 7 for your Journey, download <a href="http://r.bango29.com/9OB4DR" target="_blank">here</a>. <strong>[UPDATE] Stable Release 6.1.1 <a href="http://r.bango29.com/eXvqQw" target="_blank">here</a>.</strong></li>
	<li>Google Apps - MDPI <a href="http://r.bango29.com/cFNsTq" target="_blank">here</a>.</li>
	<li>A decent laptop/pc or a Mac with Parallels and Windows XP will do.</li>
	<li>Android Rom Upgrade Tools (RUT) and Drivers for 32 bit windows <a href="http://r.bango29.com/9criMA" target="_blank">here</a>, 64 bits windows <a href="http://r.bango29.com/ddNZGq" target="_blank">here</a> or both <a href="http://r.bango29.com/cx9wZi" target="_blank">here</a>.</li>
	<li>Fastboot windows, download <a href="http://r.bango29.com/bGUKe3" target="_blank">here</a>.</li>
</ol>
Nowadays, rooting is a very easy task. It's already built into the recovery image, what else can you ask?

Sorry I couldn't give picture-by-picture step to upgrade your Journey, you'll have to make do with plain text. Tweet me <a href="http://r.bango29.com/aacYxl" target="_blank">@tista</a> if you need assistance. So here are the steps:
<ol>
	<li>Skip to step 7 if you're already in eclair. If not, backup everything precious located on your phone's memory and let's begin.</li>
	<li>*<strong>UPDATE*</strong> Before plugging in to RUT, power off your phone and press HANG UP soft button, VOLUME UP and POWER to enter Download mode. Fire up the RUT you downloaded earlier above, click on NEXT until you find the dialog asking you to specify the ROM you're gonna flash. Point it to your CMLMod 1.3 .nb0 file.</li>
	<li>Power off your Journey and power it back on by pressing CAMERA, VOLUME UP and POWER. Now plug the USB cable in and RUT will detect your phone. Point it to the drivers you've downloaded before.</li>
	<li>Follow all the steps until your phone finally boots to CMLEclair 1.3.</li>
	<li>When you're in, power the phone off again. Bring it back on by pressing CAMERA, VOLUME UP and POWER to reenter recovery mode. Now look for the option to ENABLE ROOT. Scroll with your trackball, select by pressing the trackball and confirm by pressing the HOME soft-button.</li>
	<li>When you're done rooting, turn it off again.</li>
	<li>Power on the phone by pressing RED/HANG UP, VOLUME DOWN and POWER to enter Fastboot mode.</li>
	<li>Windows will ask for drivers and point it to the android drivers you downloaded earlier.</li>
	<li>Open up a command prompt and go to the folder where you downloaded fastboot. To keep it simple, I put fastboot and Clockwork recovery image on C:\</li>
<pre>cd \
fastboot-windows flash recovery clockwork-z71.img
fastboot-windows reboot</pre>
	<li>Your phone will reboot. Once you're in, copy the Cyanogen Mod ROM file and Google Apps to your SD Card then power off your phone again and bring it back on by pressing CAMERA, VOLUME UP and POWER.</li>
	<li>Once you're in RECOVERY MODE, scroll to INSTALL ZIP FROM SDCARD by using the VOLUME UP or VOLUME DOWN button. Please note that when you press and release the volume buttons, it'll be counted as 2 scrolls. Press the trackball to make your choice.</li>
	<li>Select the Cyanogen Mod zip file and confirm flashing.</li>
	<li>Select Google Apps zip and confirm flashing.</li>
	<li>Use the BACK soft-button to go back to where you started, select WIPE DATA/FACTORY RESET and confirm.</li>
	<li>Select WIPE CACHE PARTITION.</li>
	<li>Select ADVANCED &gt;&gt; FIX PERMISSIONS</li>
	<li>Back to the beginning, select ENABLE ROOT to live on the edge ;)</li>
	<li>REBOOT!</li>
</ol>
<p style="text-align: center;"><a href="http://www.bango29.com/go/wp-content/uploads/2010/11/nexianfroyo.jpg"><img class="aligncenter size-medium wp-image-508" title="nexianfroyo" src="http://www.bango29.com/go/wp-content/uploads/2010/11/nexianfroyo-300x225.jpg" alt="" width="300" height="225" /></a>Nexian Journey Froyo moment :)</p>
Congratulations! Now you're a Froyo owner :)