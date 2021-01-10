+++
author = "Batista Harahap"
categories = ["Android", "custom rom", "htc", "htc sensation", "rom", "root", "s-on", "sensation", "virtuous inquisition", "xda-developers"]
date = 2012-07-08T14:23:51Z
description = ""
draft = false
slug = "rooting-and-installing-custom-rom-on-s-on-htc-sensation"
tags = ["Android", "custom rom", "htc", "htc sensation", "rom", "root", "s-on", "sensation", "virtuous inquisition", "xda-developers"]
title = "Rooting and Installing Custom ROM on S-ON HTC Sensation"

+++


At the moment, I'm doing some weekend project coding in Android and since a Galaxy Tab does not qualify as a phone, I switched gadget. An iPhone for an HTC Sensation with my uncle. One thing I quickly miss is iPhone's Retina Display, however the performance of the Sensation is sensational compared to my iPhone. Was happy until the battery keeps on dying out too soon. I figured HTC Sense played a big part, so I went hunting to get a Sense-less ROM.

The HTC Sensation I have on me is already running Ice Cream Sandwich, was updated OTA. This is good news for me because from some readings <a href="http://forum.xda-developers.com/showthread.php?t=1613295" target="_blank">here</a>, virgin ROMs are easy to be rooted. For the sake of clarity, here are some links that you'd find most useful in doing the we're about to do.
<ul>
	<li>Stock ROMs to revert back to factory defaults, <a href="http://forum.xda-developers.com/showthread.php?t=1749789" target="_blank">here</a>.</li>
	<li>HTC Sensation/XE/4G AIO Tool (Windows based), <a href="http://forum.xda-developers.com/showthread.php?t=1668276" target="_blank">here</a>.</li>
	<li>Virtuous Inquisition ROM, <a href="http://forum.xda-developers.com/showthread.php?t=1408351" target="_blank">here</a>.</li>
	<li>Fastboot, just Google this.</li>
</ul>
Because we're rooting and installing Custom ROMs with S-ON, there is a limitation on what is possible and what is not. First of all, you can only use ROMs that are based on HTC firmwares meaning that you <strong>CANNOT</strong> use ROMs that are coming from AOSP, CyanogenMod or any of those sort. However, there are some tricks you can try but I'm not responsible for any wrongdoings.

Before anything else, you should root and install a custom recovery. If you're lucky enough to have your hboot version less then 1.18 then you should go ahead and visit <a href="http://revolutionary.io/" target="_blank">Revolutionary.io</a>, follow the steps there and you even get S-OFF and therefore the limitation in the previous paragraph does not apply to you. However if you're not that lucky, use the AIO tool from the links above and run it to root your device.

You could actually do S-OFF with the AIO tool BUT you'd have to do it my meddling with some hardware. Since this is a borrowed unit, I'm not doing it. Now that you have root and custom recovery installed, you can go ahead and install a ROM.
<ol>
	<li>Download an HTC based ROM like the one I put above at the links section.</li>
	<li>Copy the ROM to the root directory of your device's SD Card.</li>
	<li>Turn off the device.</li>
	<li>Unplug the battery and replug after a few seconds.</li>
	<li>Hold down <strong>Volume Down + Power</strong> buttons until it shows a white screen.</li>
	<li>Press Volume Down to select <strong>RECOVERY</strong>.</li>
	<li>Once you're in the Custom Recovery, choose <strong>Install from a ZIP</strong></li>
	<li>Select the ZIP file you downloaded earlier.</li>
	<li>Confirm the ROM installation</li>
	<li>Next you must <strong>Wipe Data</strong> and <strong>Wipe Cache + Dalvik</strong></li>
</ol>
Now for the next part, since we're still S-ON, the ROM script to overwrite boot.img will not work, it's still protected by the device. What you can do now is to repeat steps 3 to 5 above. In your laptop/computer, unzip the ROM's zip file and copy the file boot.img from kernel/pyramid/boot.img to somewhere you're comfortable.
<ol>
	<li>On the device, select <strong>FASTBOOT</strong> by pressing the Power Button.</li>
	<li>If your device is properly connected with your laptop, the device will say <strong>FASTBOOT USB</strong>.</li>
	<li>Open up a terminal and do <strong>fastboot flash boot /path/to/boot.img</strong></li>
	<li>Restart the device by doing <strong>fastboot reboot</strong></li>
</ol>
Now you have an S-ON device with a custom ROM :)