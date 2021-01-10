+++
author = "Batista Harahap"
categories = ["Mac", "Hackintosh", "windows", "iso", "usb"]
date = 2020-03-16T05:41:48Z
description = ""
draft = false
image = "/images/2020/03/burn-iso.png"
slug = "burn-windows-10-iso-to-a-usb-drive-from-a-mac"
tags = ["Mac", "Hackintosh", "windows", "iso", "usb"]
title = "Burn Windows 10 ISO To A USB Drive From A Mac"

+++


I'm on [a hackintosh](https://bango29.com/hackintosh-2019-2020-msi-z370-gaming-m5/), it gets tricky when trying to burn a Windows 10 ISO to a USB drive. Google comes up with a variety of different ways, none worked until I come across a Super User post [here](https://superuser.com/questions/1503238/create-windows-10-install-usb-on-macos-catalina). It's great but the actual burning process is slower than it should.

The post tells you to output `dd` to a buffered `/dev/diskX` device. This means there will be processing overhead from the OS to write to that device. So for everyone out there trying to do this, here's a faster way of doing it. This will work on any Mac regardless of it being a Hackintosh or not.

```
# Pretend that the ISO is at ~/Downloads/Win10_1909_EnglishInternational_x64.iso
$ cd ~/Downloads
$ hdiutil convert -format UDRW -o win10.img Win10_1909_EnglishInternational_x64.iso
$ mv win10.img.dmg win10.img
$ diskutil list
# Take note where your USB drive is at, should be /dev/diskX
$ diskutil unmountDisk /dev/diskX # Replace X with your drive location
$ sudo dd if=win10.img of=/dev/rdiskX bs=1m # Replace X with your drive location
```

What's different is instead of writing to `/dev/diskX`, you are writing to the unbuffered device `/dev/rdiskX`. This will be at least an order of magnitude faster than the original command.

In Mac's `dd` you can check for progress on the terminal by pressing `Ctrl + T`. Mine looked something like this.

```
$ sudo dd if=win10.img of=/dev/rdisk3 bs=1m
Password:
load: 1.54  cmd: dd 2501 uninterruptible 0.00u 0.02s
81+0 records in
80+0 records out
83886080 bytes transferred in 4.130995 secs (20306507 bytes/sec)
load: 1.50  cmd: dd 2501 uninterruptible 0.00u 0.04s
174+0 records in
173+0 records out
181403648 bytes transferred in 18.447054 secs (9833746 bytes/sec)
load: 1.62  cmd: dd 2501 uninterruptible 0.00u 0.05s
206+0 records in
205+0 records out
214958080 bytes transferred in 22.525669 secs (9542806 bytes/sec)
load: 1.69  cmd: dd 2501 uninterruptible 0.00u 0.41s
1787+0 records in
1786+0 records out
1872756736 bytes transferred in 243.519404 secs (7690380 bytes/sec)
load: 1.34  cmd: dd 2501 uninterruptible 0.00u 0.71s
3240+0 records in
3239+0 records out
3396337664 bytes transferred in 446.496814 secs (7606634 bytes/sec)
5172+1 records in
5172+1 records out
5424252928 bytes transferred in 715.032572 secs (7586022 bytes/sec)
```

The command finished in 715 seconds or 12 minutes. The write speed of course will depend on the USB flash drive's quality and the USB port's speed. On mine it took that long.