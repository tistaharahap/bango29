+++
author = "Batista Harahap"
categories = ["boot132", "Hackintosh", "install", "Mac"]
date = 2010-05-10T10:18:15Z
description = ""
draft = false
slug = "a-hackintosh-for-everyone-hehe-part-1"
tags = ["boot132", "Hackintosh", "install", "Mac"]
title = "A #hackintosh for everyone hehe - Part 1"

+++


Today was a loooong day. Started the day with a meeting with <a href="http://twitter.com/farry" target="_blank">@farry</a> till late in the afternoon and went back to the office to do some more work for Android. Coupled with 3 very bad experiences in 1 day from XL, it's a long and complete day. I thought why not make some fun by building a hackintosh?

I have 2 unused PCs at home and I'm not wasting them. I decided to make a hackintosh from one of them. The specs for the PC I'm using are:
<ul>
	<li>ASUS P5QL SE Motherboard</li>
	<li>2 x 2 GB DDR2-800 RAM</li>
	<li>Onboard PCIe Gigabit LAN</li>
	<li>Nvidia Geforce 9400 GT 1024 MB DDR2</li>
	<li>ALC 662 Onboard Sound</li>
	<li>Benq 18.5" LCD</li>
</ul>
That's just about it. What worried me the first time was the motherboard. Only 1 posting I know in <a href="http://www.insanelymac.com" target="_blank">InsanelyMac.com</a> forum that uses an ASUS and it's not the motherboard I'm using. For this project to happen, you will need some files which are:
<ol>
	<li>Retail Snow Leopard DVD - <strong>BUY IT!</strong> I have 2 of them actually. One for my laptop and the other for my hackintosh. Buy the upgrade version, it's <strong>IDR 300.000</strong>. Well worth every Rupiahs you spend - <strong>Restore the DVD to an external hard drive</strong>.</li>
	<li>Boot132 CD - get it from <a href="http://www.insanelymac.com/forum/index.php?showtopic=129834" target="_blank">here</a>. Follow the forum posting directions and you'll be fine.</li>
	<li>USB Keyboard and Mouse. You can use PS2 but it will be easier when you don't.</li>
	<li>A spare hard drive will be convenient - for this case i'm using just that.</li>
	<li>Free time to tinker.</li>
</ol>
The real steps are here:
<ol>
	<li>First off, insert your Boot132 CD and boot from your DVD drive. With my motherboard, when the bootup ASUS logo appeared, just press F8.</li>
	<li>Plug your external USB hard drive.</li>
	<li>When you get to the OS choosing screen, choose your USB hard drive labeled <strong><em>Mac OS X Install Disc</em><span style="font-weight: normal;">.</span></strong></li>
	<li>When you put the cursor on it, press the bolded characters <strong>-v -x -f </strong>and press <strong>Enter</strong>. It's telling to boot verbosely so you can see all the console outputs, boot into safe mode (no kexts loaded) and force full reload off all the available kexts.</li>
	<li>Wait until you get into the Installation routine.</li>
	<li>When you do get to the Installation routine, don't start yet. Click the <strong>Utilities</strong> menu on your top bar. Choose Disk Utility.</li>
	<li>You will see your hard drives listed on the left menu. Choose the Hard Drive you want to restore to.</li>
	<li>On the right panel, choose <strong><em>Partition</em><span style="font-weight: normal;"> and </span>1 Partition </strong>at the Volume Scheme drop down box. Just below the hard drive space box, click on <strong>Options </strong>and choose <strong>GUID Partition</strong>.</li>
	<li>Close Disk Utility and now you're back on your installation routine.</li>
	<li>Click NEXT all the way until it starts to install. Grab a coffee, it's gonna take some time.</li>
	<li>The installation will say it failed installing Mac OS X in the end. Don't worry, just reboot with the Boot132 CD still in the drive.</li>
</ol>
Ok that's just about it for our Part 1 of the tutorial. Leave a comment :)