+++
author = "Batista Harahap"
categories = ["unraid", "roon", "audiophile", "flac", "home"]
date = 2020-03-09T17:58:38Z
description = ""
draft = false
image = "/images/2020/03/Screen-Shot-2020-03-10-at-07.35.03-1.png"
slug = "roon-audiophiles-favorite"
tags = ["unraid", "roon", "audiophile", "flac", "home"]
title = "Roon - Audiophile's Favorite"

+++


I love music and not only I listen to it, [I write music too](https://open.spotify.com/artist/6Nn2qZBx1PYKgh88LvxfN8). Now I think there's only 1 way of listening to music: loud. Listening loud to immerse myself in those high frequency hi hats, lower frequency bass line or kicks. Just recently, I moved my monitor speaker from the studio to my working desk. While I love Plex, it caters the mass, I want something specific for music.

Before finding for other solutions, I did give [PlexAmp](https://plexamp.com/) a try. Stuck myself on it for a week.

![PlexAmp](/content/images/2020/03/Screen-Shot-2020-03-10-at-07.15.13.png)

While Plex's metadata to fill the album art, lyrics, etc is second to none, this morning I was heavily disappointed by PlexAmp's audio quality. I can't hear the differences when playing on my Apple Homepod, it all changes when I plugged in my monitor speaker to my Hackintosh. For starters, volume is lower sacrificing all the details of my FLAC collection. This is the deal breaker for me.

## Roon

Now check this out.

![Roon Welcome Screen](/content/images/2020/03/roonfront.jpg)

And this.

![Roon source and output](/content/images/2020/03/Screen-Shot-2020-03-10-at-07.28.20.png)

The second picture actually hooked me. Then I found out about this.

![Roon DSP Functions](/content/images/2020/03/Screen-Shot-2020-03-10-at-07.33.40.jpg)

Double hooked! Oh and 1 more.

![Roon Transfer Zone](/content/images/2020/03/Screen-Shot-2020-03-10-at-07.35.03.png)

Just look at it! I can transfer the playback to other locations or outputs. After some digging, I also found out [Roon Bridge](https://kb.roonlabs.com/RoonBridge), its output software can be installed on a Raspberry Pi. Sick right?

![Roon Remote on my iPhone](/content/images/2020/03/IMG_2441.jpg)

Did I tell you I can use my iPhone to remote control the playback? Yes I can.

## Installation

I use [my Unraid box](https://bango29.com/supernas-with-unraid-at-home/) and set up a VM for Roon Server. There are Docker containers but the last updates were years ago. Since setting up a VM is painless in Unraid, I opted for this.

When creating the VM, I tagged an Unraid share with the tag `music` so I can mount easily within the VM.

```
$ sudo mkdir /mnt/music
$ sudo vim /etc/fstab
# Add the line below
music	/mnt/music	9p	trans=virtio	0 0
$ sudo mount -a
```

Now we're ready to install.

```
$ sudo apt-get install libasound2 ffmpeg cifs-utils
$ wget http://download.roonlabs.com/builds/roonserver-installer-linuxx64.sh
$ chmod +x roonserver-installer-linuxx64.sh
$ sudo ./roonserver-installer-linuxx64.sh
```

## Verdict

Roon is not free. It costs $119/year or $699 for a lifetime membership, comes with a 14 days trial. Yes it's expensive, the trial period is going to determine if I'm going to shell out the subscription price or not. My first impressions are positive.

All my favorite features are on the screenshots above. My last notes would be this screenshot.

![Roon iOS looking for connections](/content/images/2020/03/IMG_2442.jpg)

The screenshot above will happen I you're not on your home network. Unlike Plex with your medias following you wherever you are, Roon only works where your Roon Core server is at. Since this isn't Roon's purpose, it'a apple to orange comparing to Plex. For the creative blooded engineer, we can always VPN to where the Roon Core is located. But that's a story for another blog post.
