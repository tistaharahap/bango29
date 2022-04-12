+++
author = "Batista Harahap"
categories = ["mac", "studio", "desktop", "machine"]
date = 2022-04-12T16:14:00Z
description = ""
image = "/content/images/2022/04/mac-studio.webp"
draft = true
slug = "mac-studio-perfect-for-me"
tags = ["mac", "studio", "desktop", "machine"]
title = "Mac Studio: Perfect For Me"

+++

After ~4 years of using a hackintosh as my main work machine, and coupled with Apple's impending deprecation of the `x86` architecture, I think Mac Studio is the best machine for me. I bought the base model and it serves me exactly how I need it to. I didn't spend a crazy amount of money and for the performance, it was worth every Dirham. Bonus point for me, when I'm going back to Indonesia in a few more months, I can easily carry the computer with me.

## Specs

The complete spec is [here](https://www.apple.com/ae/mac-studio/).

Before the Mac Studio, I am [coming from an Intel i5 11400 (6 core/12 threads) hackintosh with 32GB of memory](https://bango29.com/hackintosh-virtualized-vs-bare-metal/). This served me well, it's faster than my [i7 8700K hackintosh](https://bango29.com/hackintosh-pro/).

The Mac Studio comes with the M1 Max 10 core/10 threads and 32GB of really fast DDR5 memory integrated in the SoC. This ain't a gimmick, this combination is true power/performance for my use case. Nothing in my use case brings this machine to the edge of its capability.

What I don't like about the base model is it comes with only 512GB of storage. It's not a deal breaker, I still have ~300GB of free space but there is FOMO of some sort from [having non-upgradeable storage](https://youtu.be/8IHqntr8FjY?t=305). Yes I do have an Unraid machine for long term storage which proved to be useful, but with only this small of a storage, it's preventing me to pursue more creative workflows like music creation. Fortunately storage is expandable with Thunderbolt, such as with this [Sonnet Tech Dual NVMe Dock](https://www.sonnettech.com/product/echo-dual-nvme-thunderbolt-dock/overview.html).

## Form Factor

I said before that as a bonus, because of its small footprint, I can easily carry this machine with me when I go home to Indonesia later in the summer. I have not found any other PC equivalent with this form factor this powerful, power efficient and this quiet, none. With the latest Macbook Pros and this Mac Studio, Apple is.. well Apple; industry leader.

The hackintosh it's replacing was huge in comparison. I couldn't put it on my table, didn't fit. The Mac Studio though sits perfectly just under my monitor. You can really go for a minimalist look for your desk if you want to.

Something to note also, the front USB-C ports are appreciated, I don't have to reach to the back to plug in a cable to do transactions with my Ledger Nano X for example. It only took like 17 years for Apple to come up with front ports *sigh.

Less ergonomic is the placement and feel of the power button. It's placed in the back, just like a Mac Mini which forces me to reach and the feel the back chassis because the button is quite flush with the body. I find myself sometimes having to pull the machine towards me to press the button.

Have I told you that it's quiet? Oh yes I did, it's impossibly quiet under load. I managed to get CPU usages to 100% on all cores during testing of a few work related things and I can't hear the fans, I'm about a meter away from the machine. I also tried to export a 5120x1440 HDR video of me flying in Flight Simulator 2020 using Final Cut Pro, it was still quiet.

## Software Engineering

The community is catching up with Apple's M1, this is a fact. Official Docker images now mostly have ARM64 arch. Some of the Python libraries I needed to work with for work were also available with `aarch64` wheels. I used to have to compile some libs which makes building Docker images longer on my M1 machines, hence why I still stick with the hackintosh before.

For Python, my IDE of choice is Pycharm, it's a memory hog but I couldn't find anything else that helps me write Python with such ease. Small things like PEP8 integration is out-of-the-box and more complex use case like refactoring. The Mac Studio didn't break a sweat with Docker running Kubernetes in the background. I think this is a testament to how good macOS Monterey is prioritizing the performance cores for foreground apps and efficiency core for background apps. I didn't experience any slowdown in the UI.

Memory bandwidth is also stupendously plenty at 400GB/s for the M1 Max. This is evident for me comparing it with my Macbook Air M1's 68GB/s memory bandwidth. Switching between memory hogging apps like browsers, electron apps and Docker is seamless in the Mac Studio.

As a software engineer who primarily writes Python and NodeJS codes, I have no complaints for the Mac Studio. It's perfect. I can't push the machine to its limit with my use case.

## Quirks

Plex is transcoding HEVC content to H264 in any browser I use on the Mac Studio. The eventual quality of the transcoding is horrible. I'm not 100% sure why. My hackintosh didn't have this problem, it's marked as `Direct Play` in Plex's dashboard. The Unraid machine is using a Quadro P620 GPU to do the transcoding. This could be caused by my Unraid GPU is just not sufficient for the task. As an alternative, I downloaded Plex iPad app on my Mac Studio, unfortunately the app didn't open. H264 content are `Direct Play` though so that's a reprieve.

My Mac Studio outputs 5120x1440@120Hz or 5120x1440@60Hz with HDR on to my Samsung Odyssey Neo G9 only if connected through DisplayPort. The max resolution I get through HDMI either through the onboard HDMI 2.0 port or a Thunderbolt HDMI 2.1 dongle is 3840x1080@120Hz. What a shame! But the bigger shame is Samsung only providing 1 DisplayPort in the Neo G9 while its previous generation G9 provided 2 DisplayPorts. This limitation forces me to connect my gaming PC to the monitor using HDMI 2.1 therefore limiting me to 5120x1440@144Hz with HDR on. It's still butter smooth at 120Hz or 144Hz compared to 60Hz but my display is capable of 240Hz.

For all M1 macs, to be able to recognize a 1440P monitor as HiDPI, the alternatives are:

* BetterDummy - [link](https://github.com/waydabber/BetterDummy) - This creates a virtual display that will be mirrored to the monitor. The downside is the virtual display's max refresh rate is 60Hz, doesn't work for my use case.
* SwitchResX - [link](https://www.madrau.com/) - This works with a catch, you have to disable System Integrity Protection the first time you set SwitchResX up. I can live with this and it outputs to the max supported macOS refresh rate which is 120Hz in my case.

Translated `x86` or Intel apps runs well until you find an app or two that's just horrible. In my case those are:

* Microsoft Teams - in truth, running this on a native platform also sucks.
* Whatsapp - not worth installing, nothing changes since I first tried it on my Macbook Air M1

I suspect all Intel apps that runs on top of Electron or the likes will suck. There are alternatives like for Microsoft Teams, I run this as a Microsoft Edge app, it runs butter smooth but will lack some native features. While for Whatsapp I resorter to [Flotato](https://www.flotato.com/).

---

Apple Silicon is impressive and Mac Studio is my perfect machine. Still plagued by quirkiness that I can still live with. I wish the Macbook Air form factor will get an upgrade with an M1 Pro SoC though. That would be my perfect laptop; lightweight, powerful and the battery lasts long.

If you can justify Mac Studio's price tag, I think the machine will be a great investment for the next 2-3 years.

![Mac Studio](/content/images/2022/04/mac-studio.webp)
