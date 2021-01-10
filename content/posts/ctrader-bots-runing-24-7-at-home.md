+++
author = "Batista Harahap"
categories = ["trading", "bots", "ctrader", "forex"]
date = 2020-11-01T23:43:52Z
description = ""
draft = false
image = "/images/2020/11/ResizerImage1344X1078-1.jpg"
slug = "ctrader-bots-runing-24-7-at-home"
tags = ["trading", "bots", "ctrader", "forex"]
title = "cTrader Bots - Runing 24/7 At Home"

+++


Lately I've been indulging myself in learning more about trading much more than cryptocurrency. During the last 2 weeks I jumped head first into Forex and Precious Metals. It's different, volume is always high, unlike Bitcoin. Gained a new perspective, while other people might see as manipulation, I see how market maker moves as just another day at the office. Anyways, I learned how to automate some parts of the tradings, here's what I experienced.

## cTrader Highlights

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Coding for an indicator in cTrade is awesome. Native C# means I have full control! While Trading View’s Pinescript is easy, it lacks features. There’s no way you can do recursive functions and for what I’m doing, it’s a nice refresh 😍</p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1321772508652003328?ref_src=twsrc%5Etfw">October 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

My broker gave me cTrader and I liked it in an instant. Although MetaTrader is widely used, I dislike the UI, period. While both these software employs some implementation of black UI/X pattern designed to make people lose money, I think cTrader is still the better alternative. Both are horrible at charting, TradingView wins by a long shot here. Here are screenshots of the same indicator I wrote running on both cTrader and TradingView.

![cTrader Chart](/content/images/2020/11/ElgAk1kUcAAFzOk.jpg)

![TradingView Chart](https://www.tradingview.com/x/Gyx4d21e/)

With TradingView's ease of use to write indicators in Pinescript comes also its inability to do more. cTrader indicators and bots are written in C# which is in itself very powerful. We can leverage the power of the .NET framework right on our indicators. We can use Visual Studio and also cTrader's built in editor to write codes.

I didn't have a lot of C# coding experiences but since my first try years ago, I always knew if I ever get serious in it, I'll be happy with it and boy did I was. Suddenly I can do network IO, create a pipeline for external apps to access my bot and much more, I mean the sky is the limit.

However what really got me hooked was cTrader's Backtesting and Optimization feature. I used to do this separately but now I can do this within the trading software. Also, cTrader's data resolution is up to the tick! Now any indicator or bot I write will be very fast in reacting to changes.

## cTrader 24/7 Setup

I've [written about Unraid](https://bango29.com/unraid-case-motherboard-upgrade-and-some-more/) numerous times here in my blog, this is another one. I just recently decided to use a larger case for my Unraid box, in it runs a Core i7 8700K with 32GB of RAM.

![Unraid Box](/content/images/2020/11/ResizerImage1344X1078.jpg)

Had to run it with the front fans exposed since it's not an airflow case. Used to use the case for my main rig.

cTrader runs on Windows, my plan is to run a Windows 10 VM on the Unraid box. After trying the first time, here are some things your might wanna do or consider first:

1. Windows takes a LOT of RAM, I added another 16GB of RAM to compensate but to be fair, most of the RAM is eaten up by cTrader.
2. [VirtIO](https://wiki.libvirt.org/page/Virtio) is required to run Windows, make sure to download it in your Unraid dashboard. Go to *Settings > VM Manager > Download*.
3. While creating the VM, make sure to mount the VirtIO ISO into a DVD drive, Windows will need the storage driver to be able to see the virtual disk.
4. If you plan to access the VM through RDP, make sure you install Windows 10 Pro.

I'm being optimistic here running cTrader from my home lab. After looking into various cloud providers, I was dumbfounded by how much it costs, it's a different environment from where I'm coming from. Also, I have a 6 Core/6 Thread CPU I can leverage from.

After getting the VM successfully installed with Windows 10, open up Explorer and go to the VirtIO DVD drive, there run the installer to install the other remaining drivers. I run the VM on a 64 bit CPU so I choose the x64 installer.

## Backtesting

Before cTrader, I backtest using TradingView while a separate bot runs with the parameters I've backtested. It's not a bad setup but it's also not efficient. I had to code twice for each indicator I use. Now I don't have to.

Over the weekend I focused on learning about backtesting and optimization using cTrader. For my style of trading, I find the optimization part being the pivot. The rules I developed are below:

1. Optimize using 3 days of data (H Minus 2, H Minus 1 and First 4 hour of today) for today.
2. Run bots after the first 4 hour candle closes on the start of the week.
3. Try to not have any positions open during the weekend.
4. Concurrent positions should be backtested, useful to hedge especially on bots with breakout strategies.

While the kind of data I'm using are like below:

1. Optimize with tick data so that spreads are factored in the optimization accurately.
2. Backtest with tick data too.
3. Backtest using 3 days of data from the Optimization windows first, make sure it's performing close to the Optimization results.
4. Backtest using today's data after the first 4 hour candle closed. If there are no losses, run the bot.
5. I tend to choose optimization passes with the lowest number of trades with the highest amount of profits.

### Backtesting to Trading

Simple. Copy paste all the parameters from my main rig I use to backtest to the Windows 10 VM.

### Backtesting CPU Usages

Favor a CPU with most amount of cores/threads? At the moment there is no GPU support in cTrader so CPU it is. My Ryzen 7 3700X (8 core/16 thread) CPU is not the best to do this. But then cTrader is not maxing out my CPU usages as shown on the screenshot below.

![cTrader CPU Usage](/content/images/2020/11/Screenshot-2020-11-02-131229.png)

The above is with the optimization granted 100% CPU usage. I think a high core count CPU with excellent single core performance will do better. Gives me a reason to take a look at Ryzen 5000 series haha.

To be fair, all the cores in my 3700X are saturated so the argument of having a higher count CPU is valid. As for the usage of its core, well that's an optimization case for cTrader. More about this [here](https://ctrader.com/forum/calgo-support/11535).

The CPU usage graph above also shows only 2 of my cores are being utilized above average compared to the other cores. I think this is Ryzen's Precision Boost Overdrive working, it selected the best cores to boost. In this Ryzen generation, the 32MB L3 cache is being split into 2 CCX, each with 16MB. The 5000 series changes this by having a multiple of 8 core per CCX which means the Ryzen 5800X would have 32MB for all its cores. Gives me very compelling reason to upgrade.

---

As of last week, I made the switch to Windows final. I don't own a Mac anymore and my Hackintosh's SSD has been repurposed to store games. A fun fact, switching from a SATA SSD to an NVMe SSD to store my games didn't give me the speed ups I was hoping for, if any it was marginal. Until games implements `DirectStorage`, a SATA SSD is the best choice I think.

Switching to Windows for the last 2 weeks reminded me how great it is to choose your own hardware. As with the case of trading here, my CPU is not the best but it's enough. If ever I want to spend less time waiting for optimization results, I have the option to go put a 16 Core/32 Thread beast of a CPU later.

It's a great time in the PC world, everything just got cheaper and more performant thanks to AMD's impact in both CPU and GPU.



