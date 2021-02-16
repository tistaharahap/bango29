+++
author = "Batista Harahap"
categories = ["airplay", "pi", "raspberry", "hifi"]
date = 2021-02-08T03:14:00Z
description = ""
image = "/content/images/2021/02/audio-setup.png"
draft = false
slug = "airplay-on-raspberry-pi-hifi-setup"
tags = ["airplay", "pi", "raspberry", "hifi"]
title = "Airplay On Raspberry Pi - Hifi Setup"

+++

I've had this setup for a year now, it's useful if you don't have optical out from your devices like your laptop or your phone. Why optical out? Because analog out from computers are noisy. Noisy as in electrical noises. Without even cranking up the volume the hiss and garbled noise is unbearable. From that point on, I will only output digitally and will only output analog from either a DAC or a mixer.

DAC and mixers can be very expensive or just the opposite. I like high quality music listening but I'm not that particular, as long as I can subjectively enjoy the listening experience, I'm fulfilled. So the connections are arranged and pictured in the diagram below.

![Audio Setup](/content/images/2021/02/audio-setup.png)

The important hardware are below:

* Cheap IDR 150k DAC - Optical receiver to output analog stereo out
* Raspberry Pi
* Behringer Xenyx Q502 USB Mixer
* Yamaha HS8 Speakers
* Yamaha HS8S Subwoofers

My motherboard outputs an optical connection to the cheap DAC. The problem is, my [new Macbook Air M1](https://bango29.com/macbook-air-m1-experience-for-a-software-engineer/) doesn't have an optical output. Analog output would be too noisy for sure. I don't use it too often to play music since [i'm using Roon for music](https://bango29.com/roon-favorite-features/), Youtube sounds better with my studio monitors though.

The diagram above would be self explanatory I think. My Raspberry Pi hosts both the Roon Bridge and Shairport Sync. Roon Bridge is to accept audio coming from Roon Core while Shairport Sync is to accept audio stream using Airplay. My iOS and Apple devices can stream audio using Airplay to the studio monitors. Nothing fancy, just a consumer here of great pieces of tech.

I won't repeat what's already out there about compiling and installing Shairport Sync, here's [a great read to do so](https://www.hackster.io/opcode/apple-airplay-on-raspberry-pi-in-7-easy-steps-c7ff40).

The cons of playing audio directly using Airplay is I won't be enjoying the audio with my Roon equalizer settings. To `centralize` the equalizer I would need to have an equalizer device sitting between the mixer and the studio monitors. I haven't found a system wide parametric equalizer I'm comfortable with for a Raspberry Pi, not yet.

Some reading [here](https://www.hifiberry.com/docs/software/guide-adding-equalization-using-alsaeq/) tells me it's doable with a simple ALSA mixer. Could be something to try later in the future.