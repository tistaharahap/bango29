+++
author = "Batista Harahap"
categories = ["roon", "raspberry pi", "airplay"]
date = 2020-04-03T08:03:05Z
description = ""
draft = false
image = "/images/2020/04/mixer-1.jpg"
slug = "raspberry-pi-for-roon-bridge-and-airplay-receiver"
tags = ["roon", "raspberry pi", "airplay"]
title = "Raspberry Pi for Roon Bridge and Airplay Receiver"

+++


I love [Roon](https://roonlabs.com/)! After [trying it out](https://bango29.com/roon-audiophiles-favorite/) for 14 days, I bought the subscription. It's just so easy to manage my FLAC library with Roon. The number one feature I love is Roon's attention to high quality output and flexibility to play music to any receiver. My receiver is a Raspberry Pi.

A few days ago I set up my Raspberry Pi to act as a [Roon Bridge](https://kb.roonlabs.com/RoonBridge). I plugged my USB mixer to my Raspberry Pi allowing me to listen to music even if my Hackintosh is turned off. It's a simple [Behringer Xenyx Q502USB](https://www.behringer.com/Categories/Behringer/Mixers/Analog/Q502USB/p/P0ALL#googtrans(en|en)). Before using this mixer, I plugged a [Behringer UMC202HD](https://www.behringer.com/Categories/Behringer/Computer-Audio/Interfaces/UMC202HD/p/P0BJZ#googtrans(en|en)) but was disappointed by the loudness, but then it's powered from the USB bus so fair play to it. Plugging to the small mixer made a world of difference in loudness.

![My small mixer](/content/images/2020/04/mixer.jpg)

Please ignore the cabling mess in the back.

What I don't like by this setup, now my Hackintosh reverted back my [Jabra 510 USB](https://www.apac.jabra.com/business/speakerphones/jabra-speak-series/jabra-speak-510) for its audio output. I wanted a way for me to still output to those studio monitor speakers. A few years back, I remembered I used a Cubieboard to act as an Airplay receiver for audio. That led me [here](https://pimylifeup.com/raspberry-pi-airplay-receiver/). Followed it to install `shairport-sync`.

By default the Pi will output to its onboard sound card. We need to disable it. Follow [here](https://raspberrypi.stackexchange.com/questions/80072/how-can-i-use-an-external-usb-sound-card-and-set-it-as-default) to do so. After disabling the sound card, reboot.

```
$ sudo shutdown -r now
```

When we're back, let's start the Airplay service and crank the volume up.

```
$ sudo systemctl start shairport-sync # Will persist every reboot
$ alsamixer # Press up to crank the volume
```

Now from my Hackintosh, I went to `System Preferences / Sound / Output` and chose `Raspberrypi` as the output. If you want to change that name, it's actually the hostname of the Pi. You can change it by using `raspi-config`.

Both my Hackintosh and Raspberry Pi are connected by LAN connections. There will be delays when playing back audio from the Hackintosh to the Pi. The reason for this is the Airplay receiver needs to sync the timing with my Hackintosh, hence the name `sync` name for the receiver. I can live with that.