+++
author = "Batista Harahap"
categories = ["Android", "animation", "boot animation", "flash", "nexian journey", "splash screen"]
date = 2011-10-23T16:13:11Z
description = ""
draft = false
slug = "create-your-own-android-splash-screen-and-boot-animation"
tags = ["Android", "animation", "boot animation", "flash", "nexian journey", "splash screen"]
title = "Create Your Own Android Splash Screen and Boot Animation"

+++


So far my experience compiling my own version of Android using CyanogenMod 7.1 <a href="http://www.bango29.com/go/blog/2011/building-android-gingerbread-cyanogenmod-7-1-for-nexian-journey-mac-os-x-lion" target="_blank">here</a> is as sharp as it can be. I'm running it smoothly on my Nexian Journey and it's time to do some changes to CM's default theme to show my own.

Either creating the splash screen or the boot animation, each of the tasks have its own complication. I'm gonna start off by creating a boot animation.

I created my boot animation using Adobe Photoshop CS4. Create the animation just like creating a GIF animation. First you need to know the LCD resolution of the device you're gonna implement it with. Mine is 320x480 and that's gonna be the base here.
<pre lang="bash">1. Create a new file on Photoshop and adjust the width &amp; height dimension to you device's
2. Do all the required animation framing using Photoshop's Animator (Window / Animation)
3. Now you must logically part the animation into 2 sections. The first will be the initial non loop animation while the second will be the animation that's gonna be looped forever
4. Convert to Frame Animation
5. Flatten Animation to layers
6. Okay this gonna sound silly, I saved all the layers one by one. For the first animation section, save it anywhere under the folder part0 -&gt; You gotta save it into PNG 8 Bit with any file name as long as it's numerical according to its sequence. Ex: bango_001.png bango_002.png bango_003.png
7. Do the same for the second animation section continuing the file naming sequence from the first part and save all the frames under part1
8. Within the same folder where the part0 and part1 is located, create a new text file desc.txt
9. The content will be:
   320 480 24
   p 1 0 part0
   p 0 0 part1
10. Still in the same folder as step 9, do the following:
    $ zip -r0 bootanimation.zip *
11. Voila</pre>
Now to create a splash image is quite more challenging doing it on a MAC but thanks to <a href="http://forum.xda-developers.com/showthread.php?t=683303" target="_blank">this thread</a> in <a href="http://forum.xda-developers.com" target="_blank">XDA Developers</a>, we're all set. I'm merely copy pasting the steps on the thread, all credits should go to the author of the thread.

You will need to create a new executable BASH file with the contents below:
<pre lang="bash">#!/bin/bash
prog_header() {
	echo "###############################"
	echo "####### EleGoS's FFMPEG #######"
	echo "# G1/Sapphire/MyTouch3G/Magic #"
	echo "### Splash Screen converter ###"
	echo "###############################"
	echo "version 1.0"
	echo ""
}

if [ "$1" == "--help" ] || [ "$1" == "-h"  ]; then
	prog_header
	echo "Usage"
	echo "$0 your_image_file"
	exit 0
fi

warning() {
	printf "\e[0;31m$1\e[0m \n"
}

check_ok() {
	printf "\e[0;32m$1\e[0m \n"
}

ffmpeg_check=$(which ffmpeg)
size_check=307200
size_desc="320x480"

if [ "$ffmpeg_check" != "" ]; then
	OUTPUT=$(echo "$1" | cut -d'.' -f1).raw565
	clear
	prog_header
	ffmpeg -i $1 -f rawvideo -pix_fmt rgb565 $OUTPUT
	clear
	prog_header
	FILESIZE=$(cat $OUTPUT | wc -c)
	if [ $FILESIZE -eq $size_check ]; then
		check_ok "$OUTPUT is ready to be flashed."
	else
		rm $OUTPUT
		warning "$OUTPUT filesize mismatches! Wrong image size ($size_desc)? Aborted."
		exit 0
	fi
	echo "In order to flash this image you have to plug your phone in fastboot mode."
	read -p "Flash it now? (y/n) "
	if [ "$REPLY" == "y" ] || [ "$REPLY" == "Y" ]; then
		fastboot devices | grep -q "fastboot"
		if [ $? -ne 0 ]; then
			warning "The USB cable is not plugged, or the device is not in fastboot mode."
			echo "To flash the splash screen, manually execute this command once in fastboot mode:"
			echo "fastboot flash splash1 $OUTPUT"
			exit 0
		else
			fastboot flash splash1 $OUTPUT
		fi
	else
		echo "To flash the splash screen, execute this command once in fastboot mode:"
		echo "fastboot flash splash1 $OUTPUT"
		exit 0
	fi
else
	warning "ffmpeg not found! Please install it before running this script!\ni.e. (DEBIAN) apt-get install ffmpeg / (OSX) sudo port install ffmpeg"
fi</pre>
Now again my device's resolution is 320x480 so I have created a file called splash.bmp in Photoshop within the same folder of the script above. Before continuing, you must have MacPorts installed by going <a href="http://www.macports.org/" target="_blank">here</a>. If your device's screen resolution is not the same as mine, you must change the following lines on the script above to match yours.
<pre lang="bash">size_check=307200
size_desc="480x800"</pre>
<pre lang="bash">$ vi splash
  * Press i
  * Copy paste the above script
  * Press :wq
$ chmod +x splash
$ sudo port install ffmpeg
$ ./splash splash.bmp</pre>
That's it! To flash both the boot animation and the splash screen, I'm sure a quick search in Google will come up a few pages explaining the steps. Enjoy!