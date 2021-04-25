+++
author = "Batista Harahap"
categories = ["mac", "windows", "laptop", "change"]
date = 2021-04-18T16:14:00Z
description = ""
draft = true
slug = "mac-to-windows-in-2021"
tags = ["mac", "windows", "laptop", "change"]
title = "Mac To Windows In 2021"

+++


I made the switch. Not sure if this is going to last but I'm here nevertheless. This blog post is discussing the why and what happened afterwards. The switch came in the form of a Dell XPS 15 9500, supposedly a premium Windows laptop for the mass. Content creators love it, let's see if the same sentiment echoes with me.

## Why?

Because [my Macbook Air M1](https://bango29.com/macbook-air-m1-experience-for-a-software-engineer/) is still not in a good place for programming. Although all the usuals in modern programming tools are catching up, I still need to write production codes.

Running a mac terminal in Rosetta 2 mode is not a pleasant day to day experience, it's sluggish. Further more, I find myself needing to have a k8s mini cluster running and although that Macbook Air M1 has blown away my expectations, 8GB RAM is just not enough. Swapping to disk made the whole experience of computing not pleasant.

I didn't buy the right machine for my development needs. But, here in Indonesia it's too much of a premium to get a 32GB top up in RAM. Also, I'm convinced it's only a matter of months before Apple gives us real Pro machines. Their experiment with the M1 machines of now is a success.

Again I reiterate, I still need to write production codes.

## Choices

There are plenty of Windows laptops out there. I want a laptop that is upgradable. RAM, Thunderbolt and if possible an extra NVMe slot would be desirable. I watched a LOT of reviews of different laptops. My choices were narrowed down to Dell XPS 15 9500 and LG Gram 17 2021. Another thing I wanted is to be able to run Linux. Both laptops are not recognized for being trivial in configuring them for Linux.

Between the 2 choices, they both have all the hardware requirements I wanted. The Dell XPS 15 9500 has a bonus in the shape of an Nvidia 1650 Ti GPU while the LG Gram 17 2021 is unbelieavably light. Since both are not the best laptops for Linux, I chose the lesser of the 2 evil; Dell XPS 15 9500. The LG Gram doesn't come with upgradable RAM.

## PopOS 20.10

I installed an extra NVMe drive and installed PopOS 20.10 into it.

Before committing to buying a laptop, I installed PopOS 20.10 into my gaming PC. I customized to whole experience to how I want it since muscle memory after 13 years in the Mac ecosystem won't wear off easily. It was a **GREAT** experience! I didn't miss my Mac at all! Everything just works without anything much from me to do.

An entirely different experience with the laptop. PopOS offers these GPU options for the laptop:

* Integrated Graphics
* Nvidia Graphics
* Hybrid Graphics
* Compute Graphics

I never tried Compute Graphics since I don't have a use case yet. From the other 3, only `Nvidia Graphics` works well. The other options left me with acute screen tearing and my mouse flickering to the point I once can't find where my mouse pointer is. This is vanilla PopOS Nvidia experiece, I didn't do anything to alter that.

Closing the lid of the laptop and then opening it would take a fair amount of time to show the login screen. Coming from an M1 with instant on when opening the lid, this is just not vibing well with me. It's a reminder how the small things that matter, matters. The kind of things an Apple device will give you. But to be fair, the same experience was also present in Windows, not a Linux issue.

Battery life is not the best. Dell equipped the laptop with a 130W USB-C charger, I should've noticed this earlier. Clearly the combination of an Intel CPU and an Nvidia GPU is not kind to the batteries. But, this is not a negative for me since the M1 is on a league of its own.

The graphics in the laptop screen and an external 4K monitor are not smooth. I mentioned about screen tearing but it doesn't stop there. When Fractional Scaling is active, I can notice I'm not getting 60Hz refresh rate. When I move a window side to side, it's evident. To be fair, the Display Settings said Fractional Scaling will cause performance issues but this is sub par against Windows and Mac experiences. What I haven't tried is using Nvidia's proprietary drivers.

## Windows

Windows Hello was welcomed very much! It's so convenient to just continue where I left off.

The best experience with the laptop is of course with Windows. My day to day work happens from here. WSL is up to the task of being a usable runtime for programming tasks. To be honest, everything that a Linux machine can offer, WSL can too. WSL is not a full blown Linux but it gets the job done where a software engineer needs most. Full props to Microsoft for understanding.

The one thing disappointing is memory usage. I got myself a 32GB upgrade because at 16GB with all the apps I needed open, it was already eating 14GB of RAM. WSL also needs to be contained with its memory usage, [here](https://blog.simonpeterdebbarma.com/2020-04-memory-and-wsl/) is a great guide how.

One thing that is funny when I got this laptop is the RAM setup. It was configured with a single stick 16GB DDR4 2666 which basically runs the RAM in single channel. But then also a blessing in disguise, I only needed to buy another stick of 16GB DDR4 2666 which I did. Was doubtful it will run stable with different RAM manufacturers but then it is. I had no stability problem whatsoever.

The main thing that is bothering me is muscle memory, I'm so used to macOS keyboard shortcuts. There are solutions like [autohotkey](https://www.autohotkey.com/) and [kinto.sh](http://kinto.sh) but they're still hacks on top of a different OS, there are some circumstances when the hack is not the best. My left `Ctrl` button is mapped to Cortana for instance, I can't duck in CS:GO because of this.

CS:GO ran 100-150FPS in 4K with the Nvidia 1650Ti. This is the one game I always have regardless of OS. That's the only game I tried anyways.

Windows Terminal is more pleasant visually than the Command or Powershell apps. Just have to configure the WSL to start at Ubuntu's home directory by changing the executable path for WSL to:

```
wsl.exe ~ -d Ubuntu-20.04
```

## Build Quality

I like the combination between aluminium and carbon surfaces, looks great. My only complaint is heat spots. When the CPU needs to work hard, the left part of the keyboard and also the spot where your left palm rests are warmer. To be fair I rarely use the onboard keyboard, at home I always use an external keyboard. I can say it's warmer than I'm used to. Since this is an Intel laptop, it's part of the deal.

The keyboard though when used is a pleasure to type on with. Compared to a Macbook Pro 16" keyboard, I love this keyboard more.

Speakers though, it's another story. Not the best. Pumping the volume to 50% or more, it sounds like a blown speaker although not so blown. The internal mic is also not the best, I have found a number of times I got complains from people conferencing with me that my voice is not being heard. I had to come close to the laptop more than I had to usually.

