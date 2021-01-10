+++
author = "Batista Harahap"
categories = ["Android", "commtiva", "compile", "cyanogenmod", "gingerbread", "lion", "Mac", "nexian journey", "os x", "z71"]
date = 2011-10-22T03:41:26Z
description = ""
draft = false
slug = "building-android-gingerbread-cyanogenmod-7-1-for-nexian-journey-mac-os-x-lion"
tags = ["Android", "commtiva", "compile", "cyanogenmod", "gingerbread", "lion", "Mac", "nexian journey", "os x", "z71"]
title = "Building Android Gingerbread CyanogenMod 7.1 for Nexian Journey - Mac OS X Lion"

+++


Owkay, this is my first shot at compiling and building CyanogenMod 7.1 for Nexian Journey. Been trying to do so for the last 8 hours with only now I'm seeing some light on how to do it properly with Mac OS X Lion.

Before starting, you should check out these resources to gain some grasp about the whole process:
<ul>
	<li><a href="http://source.android.com/source/initializing.html" target="_blank">Google's official documentation</a></li>
	<li><a href="http://wiki.cyanogenmod.com/wiki/Commtiva_Z71:_Compile_CyanogenMod_%28OS_X%29" target="_blank">CyanogenMod official instructions for Commtiva Z71</a></li>
	<li><a href="http://twitter.com/#!/markogargenta" target="_blank">Marko Gargenta</a>'s fabulous screencast <a href="http://www.youtube.com/watch?v=1_H4AlQaNa0" target="_blank">part 1</a> and <a href="http://www.youtube.com/watch?v=rFqELLB1Kk8" target="_blank">part 2</a></li>
<li>Modaco's tips &amp; trick compiling CyanogenMod in OS X Lion <a href="http://android.modaco.com/topic/343919-compiling-cm-on-os-x-lion/page__view__findpost__p__1788918" target="_blank">here</a></li>
	<li>The Nexian Journey <strong>MUST</strong> already be rooted, steps are located <a href="http://www.bango29.com/go/blog/2010/upgrade-nexian-journey-to-froyo-cyanogen-mod-6-1" target="_blank">here</a></li>
	<li>Coffee and about 3+ hours to spend when building the first time</li>
</ul>
From here on, the road will be bumpy and I warn you, your Internet bandwidth is gonna play a big part in finishing up all the necessary steps. You're gonna be downloading around 7 Gigs of source codes so make sure you're up for this.
<blockquote>Credits are all reserved for the guys at Google and CyanogenMod for all the steps written below. I'm merely compiling all the information into a single blog post to save time.</blockquote>
Before you start anything, READ this lifesaving blog post <a href="http://rootzwiki.com/entry.php?104-How-To-Compile-CM7-on-OS-X-Lion" target="_blank">here</a> from <em>rootzwiki</em> to hack a bit of Darwin's C libraries to cope with Android's needs.

FYI: I'm compiling on a Macbook Pro Early 2011 Core i5 with Mac OS X Lion 10.7.2 and Xcode 4.2

<strong>0:</strong> Ditch your current MacPorts in favor for a fresh install just to be safe
<pre lang="bash">$ sudo port -fp uninstall --follow-dependents installed
$ sudo rm -rf \
    /opt/local \
    /Applications/DarwinPorts \
    /Applications/MacPorts \
    /Library/LaunchDaemons/org.macports.* \
    /Library/Receipts/DarwinPorts*.pkg \
    /Library/Receipts/MacPorts*.pkg \
    /Library/StartupItems/DarwinPortsStartup \
    /Library/Tcl/darwinports1.0 \
    /Library/Tcl/macports1.0 \
    ~/.macports</pre>
<strong>1:</strong> Install a fresh MacPorts from the official website and download the OS X Lion version <a href="http://guide.macports.org/chunked/installing.macports.html">here</a>

<strong>2:</strong> Follow the rootzwiki steps below to teleport String errors at compile time
<pre lang="bash">$ sudo vi /opt/local/etc/macports/sources.conf
* Press ]]
* Press i
* Append # at the beginning of the line 
* Press Enter and copy paste the following lines:

file:///Users/Shared/dports
rsync://rsync.macports.org/release/ports/

* Press Esc 
* Press :wq</pre>
<strong>3:</strong> Update Macports and install the necessary packages and revert <em>gmake</em> to 3.81 - GONNA TAKE A LOOOONG TIME
<pre lang="bash">$ sudo port selfupdate
$ POSIXLY_CORRECT=1 sudo port install -f python27 +universal
$ POSIXLY_CORRECT=1 sudo port install gmake libsdl git-core gnupg gsed curl libiptcdata xorg-libX* pngcrush findutils
$ sudo ln -s /opt/local/bin/gsed /opt/local/bin/sed
$ sudo ln -s /opt/local/libexec/gnubin/find /opt/local/bin/find
$ vi /opt/local/etc/macports/sources.conf
$ mkdir /Users/Shared/dports
$ cd /Users/Shared/dports
$ svn co --revision 50980 http://svn.macports.org/repository/macports/trunk/dports/devel/gmake/ devel/gmake/
$ portindex /Users/Shared/dports
$ sudo port install gmake @3.81
</pre>
<strong>4:</strong> We're going to comment a line in one of Darwin's C Library to get rid of compile time errors
<pre lang="bash">$ sudo vi /usr/include/string.h

* Press :143
* Press i
* Append //
* Press Esc
* Press :wq!</pre>
<strong>5:</strong> Next up is to add a symlink for 10.5 SDKs
<pre lang="bash">$ sudo ln -s /Developer/SDKs/MacOSX10.6.sdk /Developer/SDKs/MacOSX10.5.sdk</pre>
<strong>6:</strong> Creating a sparseimage with a Case Sensitive FS for our sandbox
<pre lang="bash">* Open Disk Utility application
* Click on +New Image
* Save it as "cm7.sparseimage" preferrably in your HOME folder with the following parameters:
    * Name: gingerbread
    * Size: >= 15 GB
    * Format: Mac OS Extended (CASE-SENSITIVE, Journaled)
    * Encryption: none, Partition - Single Apple Partition Map
    * Image Format: Sparse Disk Image
* Double click the file and it will mount on /Volumes/gingerbread
* FYI: A sparseimage file although we have set the maximum size to be 15 GB but it will only get larger when you actually use all the space so it won't eat up your hard drive space yet</pre>
<strong>7:</strong> Macports version of <em>e2fsprogs</em> will fail to compile, download the source and compile it yourself
<pre lang="bash">$ mkdir -p ~/src
$ cd ~/src
$ git clone http://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git
$ cd e2fsprogs
$ ./configure --prefix=/opt/local
$ make -j4 && sudo make install</pre>
<strong>8:</strong> Set up the pre-requisites for CyanogenMod to compile, there are
<pre lang="bash">$ cd /Volumes/gingerbread
$ mkdir -p bin
$ curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > bin/repo
$ chmod a+x bin/repo
$ mkdir -p android/system/
$ PATH=${PATH}:/Volumes/gingerbread/bin:
$ echo "PATH=\${PATH}:/Volumes/gingerbread/bin:" >> ~/.profile</pre>
<strong>9:</strong> Clone CyanogenMod repository into our sparseimage - GONNA TAKE A LOOOONG TIME
<pre lang="bash">$ cd /Volumes/gingerbread/android/system
$ repo init -u git://github.com/CyanogenMod/android.git -b gingerbread
$ repo sync</pre>
<strong>10:</strong> Now we need to get all closed source binaries from the device and into our Z71 build folder
<pre lang="bash">$ cd /Volumes/gingerbread/android/system/device/commtiva/z71/
$ ./extract-files.sh</pre>
<strong>11:</strong> <em>ROMManager</em> is a requirement for CyanogenMod, I haven't excluded any of the standard packages
<pre lang="bash">$ /Volumes/gingerbread/android/system/vendor/cyanogen/get-rommanager</pre>

<strong>12:</strong> Get a binary out from your Rooted CM Nexian Journey. Plug in the device using USB.
<pre lang="php">
$ cd /Volumes/Gingerbread/android/system/vendor/commtiva/z71/proprietary/bin/
$ adb pull /system/bin/hostapd .
</pre>

<strong>13:</strong> Tweak a few more settings to fit OS X Lion's shortcomings
<pre lang="bash">
$ cd /Volumes/gingerbread/android/system/
$ vi external/qemu/Android.mk

* Press i
* Append # to every line without in preceeding it
* Press Esc
* Press :wq
</pre>

<strong>14:</strong> Now here comes the real fun, let's compile CyanogenMod and enable Compiler cache so future recompiles will take less time
<pre lang="bash">$ cd /Volumes/gingerbread/android/system/
$ cp ./vendor/cyanogen/products/cyanogen_z71.mk ./buildspec.mk
$ . build/envsetup.sh
$ lunch cyanogen_z71-eng
$ make -j`sysctl -an hw.logicalcpu` bacon
$ export USE_CCACHE=1
$ export CCACHE_DIR=/tmp/.ccache
$ prebuilt/darwin-x86/ccache/ccache -M 20G
</pre>

<strong>15:</strong> After the long process is done, your build is located at the following folder
<pre lang="bash">/Volumes/gingerbread/android/system/out/target/product/z71/update.cm-XXXXX-signed.zip</pre>
<strong>16:</strong> Flash the build!
<pre lang="bash">* Copy the zip file from Step 13 to your device's SDCARD root directory
* Reboot into recovery
* Flash it!</pre>

My build is still compiling and this wraps up the steps needed. Comment on this blog post or mention me <a href="http://twitter.com/tista" target="_blank">@tista</a> in Twitter if you need help. Good luck ;)