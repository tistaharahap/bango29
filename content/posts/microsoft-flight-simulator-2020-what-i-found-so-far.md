+++
author = "Batista Harahap"
categories = ["flightsim", "msfs", "2020"]
date = 2021-03-11T19:06:22Z
description = ""
draft = false
image = "/images/2021/03/stripes.jpg"
slug = "microsoft-flight-simulator-2020-what-i-found-so-far"
tags = ["flightsim", "msfs", "2020"]
title = "Microsoft Flight Simulator 2020 - What I Found So Far"

+++


Since the game launched in August 2020, this has been the game I spent time the most with over than 463 hours logged so far. Becoming a pilot was what I wanted to be before I knew how to code, learning to fly is nothing like coding, bugs are fatal. This write up sums up what I've found about the game so far I wish I knew before playing the game.

## In Game Performance Tuning

I tried playing the game [with an i7-8700K, Ryzen 3700X and Ryzen 5600X paired with an Nvidia RTX 3080](https://bango29.com/microsoft-flight-simulator-8700k-3700x-5600x-with-an-rtx-3080/). Then I sold the 3080 and instead bought an XFX Merc 319 Radeon 6900XT Black Edition. The 3080 was a lower powered AIB card, it wasn't performing as I would expected a 3080 would be.

My final build and suggestion is to go AMD all the way to get the best experience. Turn on [Smart Access Memory](https://www.techspot.com/article/2178-amd-smart-access-memory/) from BIOS, tune the card (OC) and get a 3600MHz RAM at the minimum.

### XFX Merc 319 Radeon 6900XT Black Edition

Here are my recommended settings to tune (OC) this card, might or might not work for other 6900XT cards. These recommendations are based on Microsoft Flight Simulator 2020 with the March 2021 patch.

With these settings, on rainy weathers I got an average of 45 FPS while for clear skies, it's 50+ FPS.

The other benefit of going AMD is Crossfire (MultiGPU in a single system) doesn't need an adapter. Just plug another GPU, change some settings and it's a go.

Also, make sure to get a 1000W PSU for the GPU, I used to use a 850W PSU and I get random shutdowns because of this. On paper, the power usage is said to be around 320W and on average this might be true. However, there are random spikes in power, just like its predecessor the Nvidia RTX 3080.

The above would be even more important if you use a higher powered CPU like Ryzen 5900X/5950X.

#### AMD Control Center

Manual GPU performance tuning with these settings:

* Core clock: 2400-2575 MHz
* Memory Timing: Fast Timing
* Memory Clock: 2150 MHz
* Fans: Default
* Power: 15%

#### In Game Settings

Everything Ultra is fine with these exceptions:

* Clouds: High
* Render Scale: 80
* LOD: 100

### AMD Ryzen 5000 Series + 500 Series Chipset

Be careful with AIO coolers. Make sure the Windows application that comes with the AIO to control the fans and pumps are installed and configured for performance. I once had immediate shutdowns mid-flight because I didn't install NZXT CAM for my NZXT X72 AIO cooler.

RAM speed matters a lot. Only recently I've been using a 3600MHz RAM, it gives a very different experience compared with a 3200MHz RAM. The difference is most apparent with less sttuterings and frame times. I actually bought a 4000MHz RAM but was unable to tune the FCLK bus because my Ryzen 5600X just couldn't handle it, bad sillicon.

![Not a silicon lottery winner](https://pics.me.me/that-moment-when-you-realize-win-the-you-didnt-lottery-53758116.png)

For the smoothest experience, might wanna pair a Ryzen 5800X or 5900X with a 4000MHz FCLK and RAM speed. BUT, in reality until Microsoft releases a patch for the game to upgrade from DirectX 11 to DirectX 12, CPU's with a thread count more than 12 will be used sparingly.

The games loves IPC, the more the IPC of the CPU, the more performant the game.

### Resolution

The reason why I choose to go AMD Radeon is because when I tried the game with Nvidia's RTX 3080, the performance didn't scale well in lower resolutions. The FPS in 4K is not much different than 1440P. I was and still contemplating on getting a 1440P high refresh rate display and going AMD Radeon is a safe bet.

However, the game is best enjoyed in 4K I believe. It's why I never got myself a 1440P screen after contemplating for a while anyways.

### Upgrade Path

For me, the more important path is upgrading the CPU to something that can sustain a 4000MHz FCLK. My older 3700X handled that frequency so I'm assuming a 5800X would also be sufficient. With this I'm sure I can get FPS to nearer to 60 FPS.

If 60 FPS is unattainable with the above upgrade, I would choose to add another 6900XT GPU and Crossfire it. Crossfire setups are not consistent, some games receive significant boost in performance while some don't. For this though, I'm not so sure my 1000W PSU would be enough, a more prudent upgrade would be a 1200-1600W PSU.

## Addons

The de facto destination for addons must be [FlightSim.to](https://flightsim.to/). You can find anything you can think of here. The [Scenery Map](https://flightsim.to/scenery-map) will help find sceneries using a world map, you'll love it.

For paid addons, just checkout the game's Marketplace. I bought a local Jakarta airport there Halim Perdanakusuma (WIHH).

### Project Megapack

The destination to find free Liveries and Aircrafts:

* Livery Megapack - [link](https://www.projectmegapack.com/liveries/)
* Aircraft Megapack - [link](https://www.projectmegapack.com/aircraft/) - Released aircrafts include these:
  * Airbus A321-200 ported from FSX
  * Airbus A330-300 built from scratch

## Aircraft Realism

First of all, I was a Boeing fan. Have flown in Boeing 737 simulators before with a real pilot teaching me how to do things. I was exempted of much of the knowledge on those experiences though, the AP, flight plan and most of the flight management were handled by the pilot. I wished I asked about LNAV or VNAV on those simulator sessions.

However in this game, the most real aircraft is the Airbus A320 Neo since there is no Boeing 737 aircraft available yet, at least none that is study level yet.

### Airbus A320 Neo

I learned how to use Autopilot, insert flight plans, departure/arrival management, etc on the A320 Neo. This is made possible by the fantastic work of the people from [FlyByWire](https://flybywiresim.com/) team who built the [A32NX](https://github.com/flybywiresim/a32nx) mod. They are also working on an Airbus A380 too, oh yeah!

<blockquote class="twitter-tweet"><p lang="und" dir="ltr"><a href="https://t.co/gXpnyWojo2">pic.twitter.com/gXpnyWojo2</a></p>&mdash; FlyByWire Simulations (@FlyByWireSim) <a href="https://twitter.com/FlyByWireSim/status/1369078858109116419?ref_src=twsrc%5Etfw">March 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

People say it's not as real as it can be yet but with each iteration it's becoming more and more real. If you're just starting to play the game and flight simulator in general, this mod must be your first destination. Learning to fly the most popular and most sold aircraft in history comes with its own goodies.

#### Liveries

Simply second to none in terms of quantity. Even carriers that isn't flying the A320 would be available. These are links for Indonesian airlines:

* Garuda Indonesia - [link](https://flightsim.to/file/3357/8k-garuda-indonesia)
* Citilink - [link](https://flightsim.to/file/7359/poslaju-citilink-garuda)
* Batik Air - [link](https://flightsim.to/file/7444/batik-air-8k-pk-azo)
* Lion Air - [link](https://nl.flightsim.to/file/5301/lion-air)
* Sriwijaya Air - [link](https://flightsim.to/file/6077/sriwijaya)
* Air Asia Indonesia - [link](https://nl.flightsim.to/file/7395/airasia-indonesia-8k-pk-azo)
* JNE Express - [link](https://fr.flightsim.to/file/5237/jne-express)

In Flightsim.to, you can find many other liveries not listed in Liveries Megapack.

#### Educational Materials

An Airbus aircraft is relatively easier to understand in my believe when you're trying to get a grip of how this flight sim thing works. To get Autopilot working, there is only 1 button, it's like an iPhone, has only 1 button to navigate. There are also plentiful resources in Youtube to learn about the aircraft. Let me put a few channels that helped me get up on my feet. Also, learning to fly an A320 will also enable you to fly other Airbus aircrafts easier.

* Easyjet Sim Pilot - [link](https://www.youtube.com/channel/UCoOgf1QDun4PGN-d_X2b_1g)
* Drawyah Flight Simulator tutorial - [link](https://www.youtube.com/playlist?list=PL66UOo0xjl6OtIlggRtXbp98fN8Gl2Qtu)
* 320 Sim Pilot - [link](https://www.youtube.com/user/filanjix)

I spent a lot of hours watching their videos. However, there's a caveat here. Some of the videos are posted with earlier versions of the game, the changes from the earlier versions to the current version are noticeable. Especially on flight dynamics and button & knobs on the default planes.

## Overall Realism

The harder part of my educational journey is learning when to flare. The easier part is learning how to use the onboard computer, it's data entry but with each aircraft, there's a difference. 

Real pilots when they learn how to fly always have a more experienced pilot as an instructor, flight simmers learn everything on their own. Don't get me wrong, this is not an inhibition, for me this means filtering noises and focusing on the fundamentals without much theoretical hours. As an example, I learned how to use a rudder on an A320 and A330 while real pilots would learn it using a smaller aircraft.

Also, since first time flight simmers are limited by clicks and mouse scroller actions, it's hard to learn or do something that is trivial like adjusting trims. Having hardware that closely mimics the buttons and knobs of a real aircraft will help significantly although not necessary to be able to start learning.

So long as my monitor acts as a cockpit instead of displaying sceneries, realism is far. After spending more than 463 hours on the flight sim, I still consider myself as a total noob. I'm still clumsy in the fundamentals like TOD calculations, trimming, flaring and using the rudder properly. Much of it can be blamed because I started with just a joystick, a rather horrendous one too. But in hindsight, that's actually a good thing, I now know how to invest time and money without going over my understandings of how flight dynamics are.

I tell myself this to motivate my learnings: "Can I land any aircraft in case there's an emergency in a flight I'm in?". It's far fetched I know but it's a life and death situation, it's always good to be prepared. To answer the question, I focus my learnings into key pieces outlined below.

### On Board Computer

The on board computer is a helper, not a pilot. The pilot decides based on indicators provided by the computer. Although much of the flying is just sitting in a cockpit, learning how to interpret data provided by the computer is _numero uno_ and would mean the difference when figuring out the root cause of a failure.

Other than acting as an indicator (like in trading), the computer accept inputs from the pilot. These inputs directs the computer to show data or manages the attitude of the aircraft. On Airbus aircrafts in the `PERF` section of the MCDU, before taking off we can input V1, VR and V2 speed, these inputs determine when to rotate and tells the computer to show V1 and VR bugs in the PFD. The computer will also say verbally V1 on takeoff rolls, notifying the pilot to focus on rotation speed on the PFD if committed or slam the breaks if not. Data entry which is something trivial from a software engineer's perspective becomes the difference between life or death, if not the pilot's then the other people on board.

Most of my flights would be spent either in an Airbus or a Boeing aircraft, learning how to enter data and intrepret results for both are my key focus. However in the game at the moment, only Airbus aircrafts are simulating reality closer than Boeing aircrafts. Since both manufacturer's flight models are likely similar between different aircrafts, learning each in a specific aircraft would enable learning other aircrafts with the same manufacturer.

### Landings

I can understand why pilots enjoy landings. Articulation of knowledge gained is always a proud and also artistically impressive expression. Landing buttery smooth with under -100FPM vertical speed is not always the most impressive expression in real life. Consider a short runway with a wet surface, pilots would want to touchdown on the TDZ and not worry about buttery landings. Flaring just enough to not make the landing not harded than it needed to be.

Learning when to flare is difficult, concurrently a pilot's eyes are focused on the widening runway while maintaining an acceptable vertical speed. At least for me, this is something I will never stop learning. Because it's in a simulator, trying to land no matter what and not going around which is a safer choice is still where I'm at.

More to this, different aircraft behaves differently when it's about to land. An A320 flares at around 50-75 feet while that too late for an A330, or at least that's what I learned so far. The A330 is a bigger and heavier aircraft, when it gets that low, gravity will pull the aircraft more than an A320 but too much flare will make it float for far too long missing the TDZ.

On this landing I missed the TDZ, I was visual and turned of AP way before it's needed to because the ILS heading was broken for the airport. Only followed the vertical PFD bug. But coordinating between a slight left rudder combined with correcting course and altitude translated into panic when it touches down. I should've touched down sooner and when it's down, I should've ease the left rudder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AREct3IjRg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

My point is, this part of a flight is when articulation is everything. I'm sure with more hours I will develop confidence to trust my judgement so I won't get distracted by the number of things that can go wrong. Like when you see a Susi Air pilot telling his peer that their committed to landing then nothing can distract him from getting that plane down safely. I must develop a mental model of where I want the plane to land on the runway and how to get there (the attitude and heading) between minimums and flaring.

An experienced pilot if reading this part of the blog post, please tell me what I'm doing wrong [on Twitter](https://twitter.com/tista).

---

I still have much to learn, I know what the focuses are, also know where to look for guidance but still weak in fundamentals of flying. My TOD calculator is either using the EFB's calculator in the A32NX mod or measure roughly which basically means when I'm 150-175 miles from the destinations, start descending at 1500FPM and adjust vertical speed when halfway of the descent.

Although learning independently has always been my thing like with programming, I'm not convinced that's the best way to learn how to fly. But this is all I know how now. One day, I'll check that item on my bucket list to become a pilot, flying in the real world. Before that day comes, I'm learning to fly now.