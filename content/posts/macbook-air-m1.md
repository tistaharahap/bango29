+++
author = "Batista Harahap"
categories = ["mac", "macbook", "air", "apple", "m1", "laptop"]
date = 2021-02-01T11:34:00Z
description = ""
image = "/content/images/2021/02/spongebobair.png"
draft = false
slug = "macbook-air-m1-experience-for-a-software-engineer"
tags = ["mac", "macbook", "air", "apple", "m1", "laptop"]
title = "Macbook Air M1 Experience for a Software Engineer"

+++

In short, **It's GREAT!** What can I say more other than it's just a fantastic machine to play with. At the moment I have a Macbook Pro 16" i9 top of the line, a Ryzen 5600X gaming PC and this new laptop. The i9 16" is just not in the same league as this M1 Air. But that's not all I have to say, I'm looking at this from a software engineer's point of view.

## Apps for M1

Everything works as of now although some of them with an asterisk:

* Docker - Only technical preview builds are available, it's fine for my limited use case of spinning up just database daemons
* Pycharm (and other IntelliJ based IDE) - M1 builds are official
* Homebrew - M1 builds are official
* Python 3 - M1 builds are official
* NodeJS - No M1 builds yet
* Firefox - M1 builds are official
* Visual Studio Code - M1 builds in beta, running x86 build with Rosetta 2 is not a great experience
* iTerm2 - M1 builds are official

To put things short, anything not built for M1 will work using Rosetta 2 but the experience would be degraded. Apps that are ran with Rosetta 2 will suffer from text manipulation sluggishness. Whenever I try to block a text or copy paste, there is a significant delay interrupting my flow. I guess this is Apple's way of saying to developers to provide M1 builds.

Go [here](https://ported2m1.com/) to check if M1 builds for your apps are available.

## CPU/RAM Experience

I bought the 256GB Air with 8GB of RAM, it's enough. It's **NOT** slow at all.

![8 Gigs of RAM](/content/images/2021/02/8gigs.png)

A lot of apps is running including Pycharm along with the Photos app curating my photos. All that took 47% of memory with ~30% CPU usage. I can still do a lot, I code without any sluggishness at all. Oh and Docker is running a MongoDB container.

![](/content/images/2021/02/docker-8gigs.png)

The SoC temperature is sitting between high 30s and mid 40s degrees Celcius. Also, there are no fans, it's quiet. To be fair, I'm not coding mobile apps so resource usages are not demanding. Xcode is obviously native M1 while Android Studio still don't have an M1 build yet. [Here's a good read](https://blog.metaobject.com/2020/11/m1-memory-and-performance.html) about Apple's choice in opting for Reference Counting instead of Garbage Collection dramatically increasing the whole user experience while for developers, the implementation is no different (yes apples to oranges, almost literally) programmatically.

```
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">fun fact:  retaining and releasing an NSObject takes ~30 nanoseconds on current gen Intel, and ~6.5 nanoseconds on an M1</p>— David Smith  (@Catfish_Man) <a  href="https://twitter.com/Catfish_Man/status/1326238434235568128?ref_src=twsrc%5Etfw">November 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js"  charset="utf-8"></script> 
```

The tweet above taken from the article I linked. With almost 5x faster in doing atomic functions, the effect in the whole user experience of an M1 hardware is a departure from the old incremental performance improvements pioneered by Intel.

Single core performance of this laptop is faster than my high end gaming PC with a Ryzen 5600X CPU according to Geekbench.

```
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">MacBook Air M1’s  single core score outperforms my gaming rig, crazy af <a  href="https://t.co/TUvpiiiYXs">https://t.co/TUvpiiiYXs</a></p>— Batista Harahap (@tista) <a  href="https://twitter.com/tista/status/1356531756887756802?ref_src=twsrc%5Etfw">February 2, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js"  charset="utf-8"></script> 
```

Coming from an Intel machine, even this Air is pro level experience that I don't get with a top of the line 16" i9 MacBook Pro. All this with a price substantially cheaper than a Pro machine. Imagine how a true Pro Apple Sillicon machine will give us!

## Coding

No complaints, for now.

### Docker

Before writing this paragraph, Docker just quit unexpectedly. It's a preview build so it's tolerable for now. Restarted Docker and the MongoDB container without a problem. This might not be a great experience if let's say you're planning to run a full Kubernetes stack, who knows what would get corrupted.

Other than the above, since my use case is limited, I'm pleased to have Docker running. I can also build container images like I would on an Intel Mac although CI/CD usually will do that for you.

### Python

As I said in the preface of this blog post, Python is available natively for M1 hardware. I installed through `Homebrew` with a simple `$ brew install python@3.9`. I did have to adjust my `PATH` to use the binaries from `Homebrew` but that's also what I would've done on an Intel Mac. My flow to use Python is like below:

```
$ brew install python@3.9
$ echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/tista/.zprofile
$ vim ~/.zprofile
# Use Homebrew's Python
export PATH=/opt/homebrew/opt/python@3.9/libexec/bin:$PATH
$ source ~/.zprofile
$ python3 -m pip install virtualenv
$ cd path/to/python/project
$ virtualenv env
$ . env/bin/activate
```

Haven't tested libraries without M1 wheels, do we need to compile from source? As I'm writing this, I'm trying to install `numpy`. While it's building, my SoC temperature is at mid 50s degress Celcius, how awesome is that? And no fans.

The build failed with this message.

```
ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly
```

What it's actually saying is that there are no wheels for `numpy` intended for M1 hardware. [Someone succesfully built from source](https://stackoverflow.com/questions/65336789/numpy-build-fail-in-m1-big-sur-11-1) but another trick is [to open iTerm2 with Rosetta 2](https://alexslobodnik.medium.com/apple-m1-python-pandas-and-homebrew-20f14828ccc7) if you're ok with an 80% near native performance. In time, popular libraries will have wheels for M1.

### MongoDB

Used Docker for this, don't get any simpler.

```
$ docker run --name mongo -v /path/to/local/dir:/data/db -d -p 27017:27017 -d mongo:4
$ docker ps # Make sure mongo is running
$ docker logs mongo | tail # Make sure mongo is running properly
```

### Pycharm

Worked like a charm. An M1 build is available, everything is snappy, and it just works. Starting up the app is as fast as it is on an Intel Mac with beefy hardware, I couldn't tell the difference.

### Visual Studio Code

The experience is not even good. Since text manipulation in Rosetta 2 is disruptive to my flow, I can't code in it. But there's an `Insider's Build` built for M1 which you can [download here](https://code.visualstudio.com/insiders). Haven't spent enough time with it though, not much to say.

### iTerm2

An M1 build is available so it just works out of the box. Installed it through `Homebrew`.

```
$ brew install iterm2
```

---

For now I'm ending this blog post with as a satisfied software engineer. It's the kind of pro experience any pro user would expect from a Mac device. The given expectation of getting a pro machine from Apple being an actual pro machine is now real again after a long long long wait period thanks to Intel's monkey business. Don't forget this is a MacBook Air, not a Pro, no fans FTW!

One more thing, battery life is indisputedly the best I've ever owned.

![Sponge Bob Agrees](/content/images/2021/02/spongebobair.png)
