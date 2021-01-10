+++
author = "Batista Harahap"
categories = ["Hackintosh"]
date = 2020-09-15T10:11:19Z
description = ""
draft = false
image = "/images/2020/09/workstation-1.jpg"
slug = "small-upgrade-for-the-hackintosh"
tags = ["Hackintosh"]
title = "Small Upgrade For The Hackintosh"

+++


My [last post](https://bango29.com/ryzen-3700x-hackintosh-2020/) about my hackintosh is when I was still on Ryzen 3700X/X570 pair. It was overkill for my day to day work, instead I built a new PC just for the hackintosh and used the higher end pair for gaming. It was a great decision, introduced me to the microATX form factor.

For a work computer (trading and programming), a microATX board fits my use case. It's small but it's big enough to host all my peripherals. I started with this spec.

* AMD Ryzen 3500 - 6 Core w/ 65W TDP
* 16GB 3200MHz RAM
* 500GB Samsung 960 Evo
* MSI B450M Pro-VDH Plus
* MSI Armor RX570 8GB
* Cooler Master MasterLiquid Lite 120 AIO
* Cooler Master Masterbox MB400L
* Corsair RM750 PSU
* Bluetooth Dongle

Opted for a 6 core lower TDP Ryzen because the PC is always on everyday. Peak CPU temperature while on heavy CPU load is 65-67C, a 120mm AIO is enough.

I use Geekbench 5 to benchmark, hackintosh always performs lower compared to benchmarking in Windows with the same hardware. The difference is about 1-2% per run which is negligible for the kind of work I'm doing.

Everything ran smoothly with 1 catch, hooking up the audio to my Yamaha HS8 studio monitor speakers always end up with noise, which is expected. Unfortunately the motherboard I chose didn't come with an optical out interface. Listening audio through a conference speakerphone is unbearable after a while.

Time for an upgrade then. Here's the spec afterwards.

* AMD Ryzen 3500 - 6 Core w/ 65W TDP
* 16GB 3200MHz RAM
* 500GB Samsung 960 Evo
* Asrock B550M Steel Legend
* MSI Armor RX570 8GB
* Cooler Master MasterLiquid Lite 120 AIO
* Cooler Master Masterbox MB400L
* Corsair RM750 PSU
* Bluetooth Dongle
* Fenvi TV919 PCIe Wifi

Hooked up the PCIe Wifi card so I can receive calls on the hackintosh. After setting the whole thing up, this microATX form factor grew more on me. There were no wastage of PCIe ports.

The motherboard comes with heaps of PWM pins and the PC does not take up a lot of space on my desk. Airflow is not a problem:

* 2 x 120mm front fans - cool air in
* 1 x 120mm backside fan - cool air in
* 1 x 140mm top fan ~~or 2 x 120 mm top fans~~ - hot air out

Heat is mostly coming from the GPU driving 3 4k monitors. I might need to reapply thermal paste and check on its thermal pads.

---

![Workstation](/content/images/2020/09/workstation.jpg)


I really like building my own hardware for work or pleasure, should stay that way for the future, I hope. Dumb terminals is not my cup of tea.