+++
author = "Batista Harahap"
categories = ["flightsim", "microsoft", "fs2020", "ryzen", "i7", "performance"]
date = 2020-12-05T22:09:22Z
description = ""
draft = false
image = "/images/2020/12/HORAS.jpg"
slug = "microsoft-flight-simulator-8700k-3700x-5600x-with-an-rtx-3080"
tags = ["flightsim", "microsoft", "fs2020", "ryzen", "i7", "performance"]
title = "Microsoft Flight Simulator - 8700K, 3700X & 5600X with an RTX 3080"

+++


As I said [here](https://bango29.com/microsoft-flight-simulator-2020-beta-testing-using-your-customers/) and [here](https://bango29.com/the-case-of-pairing-3700x-and-3080/), Microsoft Flight Simulator 2020 is beautiful. Been flying non-stop the past few months, to this day I've logged 229 hours of game time. Flying virtually made me remember moments and also an opportunity to learn something new. This blog post is about what you get in the game with combinations of CPU's I've tested it on and RTX cards namely 2070 Super and 3080.

The combinations are all feeding a 4K60 monitor with HDR turned on.

TLDR; get yourself a Ryzen 5000 series CPU to run this game smoothly, the single core performance of it blew all the other CPU's out of the water. More about it below.

## Intel Core i7 8700K + RTX 2070 Super

This is the worst combination of all (which is expected). At the time, this CPU was my most performant CPU for games. Simply put, I can't run 4K, the most I can run is at 1440P with all settings between medium to high for a +30 FPS experience.

Playing at resolutions lowers than 4K on a 4K monitor is troubling for the eyes. The game is not meant to be an eye sore. Had to upgrade.

Specs:

* Intel Core i7 8700K
* MSI Z370 Gaming M5
* 32GB DDR4 3200 MHz
* Samsung 960EVO NVMe
* Corsair H115i AIO CPU Cooler
* EVGA 2070 Super KO
* NZXT H710i Case

## Intel Core i7 8700K + RTX 3080

With the RTX 3080, 4K in any game I play is a reality, it's beautiful. Games like Red Dead Redemption 2 and Flight Simulator 2020 are just BEAUTIFUL, especially when HDR is turned on.

Game performance in 4K was adequate, it's decent but not good and definitely not great. The biggest experience breaker is the stuttering that will happen often. My assumption is there is just not enough IPC being processed on time by the CPU. Frame rates are not as bad but it wasn't a pleasant experience.

Since my assumption is there wasn't enough CPU room to process more instructions, I wondered how it will perform on a Ryzen 3000 build. A Ryzen 3000 CPU will not be as great in delivering frame rates like an i7 8700K but at least the Infinity Fabric can offer more headroom.

Specs:

* Intel Core i7 8700K
* MSI Z370 Gaming M5
* 32GB DDR4 3200 MHz
* Samsung 960EVO NVMe
* Corsair H115i AIO CPU Cooler
* Palit RTX 3080 Gaming Pro OC
* NZXT H710i Case

## AMD Ryzen 3700X + RTX 3080

Stutterings were reduced significantly. Running the Infinity Fabric in a 1:1 ratio with the memory clock definitely brings more to the table.

I think I won the silicon lottery with my Ryzen 3700X, I overclocked the memory to 3800MHz with a 1:1 ratio for the Inifinity Fabric @ 1900MHz. To my surprise, everything were stable at this clock. Benchmark tools really like the memory OC but it only contributed marginal improvement in Flight Simulator 2020, was not worth the risk of frying my memory.

Although stutterings were reduced, areas where photogrammetry data was dense or heavy weather (clouds) were still stuttering. The bus had a lots of seats but it was only driving 120 KM/h on a 300 KM/h highway. At this time, Ryzen 5000 series was launched.

Specs:

* AMD Ryzen 3700X
* AsRock X570 Taichi
* 32GB DDR4 3200 MHz
* Samsung 960EVO NVMe
* Corsair H115i AIO CPU Cooler
* Palit RTX 3080 Gaming Pro OC
* 2x 120mm Noctua fans under the GPU
* 1x 140mm Noctua fan under the double 120mm fans
* NZXT H710i Case

One thing to note, installing 2x 120mm & 1x 140mm Noctua fans in the PCIe slot just below the GPU affected the GPU temperature. Without the Noctua fans, temperatures were in the lower to mid 70s C while with the fans, temperatures were in the mid 60s C.

Further more it's quieter with the Noctua fans installed, the GPU fans didn't need to work as hard and stayed at around 40%.

### AMD Ryzen 5600X + RTX 3080

Best of the bunch.

Specs:

* AMD Ryzen 5600X
* AsRock X570 Taichi
* 32GB DDR4 3200 MHz
* Samsung 960EVO NVMe
* NZXT X72 AIO CPU Cooler
* Palit RTX 3080 Gaming Pro OC
* 2x 120mm Noctua fans under the GPU
* 1x 140mm Noctua fan under the double 120mm fans
* NZXT H710i Case

I switched the AIO CPU Cooler to a 360mm radiator because I wanted to get more airflow. I figured 3x 120mm fans would bring more air in than 2x 140mm fans.

Ryzen 5000 series is a leap in gaming performance indeed. Any game I threw at it at 4K were running +60 FPS at High-Ultra settings except for Flight Simulator 2020 of course. However, stutterings were once again greatly reduced. You'd see true 20 FPS without stutters if that makes sense :D.

It's still not possible to run Flight Simulator 2020 at 4K with Ultra settings. Had to tone down the settings to achieve an acceptable trade off between performance and quality. I ended up with these settings and for now it's enough for me.

![Microsoft Flight Simulator 2020 - Settings 1](/content/images/2020/12/20201206094610_1.jpg)

![Microsoft Flight Simulator 2020 - Settings 2](/content/images/2020/12/20201206094623_1.jpg)

![Microsoft Flight Simulator 2020 - Settings 3](/content/images/2020/12/20201206094648_1.jpg)

Clouds and heavy weather impacted the overall performance dramatically, especially when flying airliner jets. General Aviation planes tends to perform better. My benchmark would be comparing A320 Neo with Icon A5.

## Thoughts

Until Flight Simulator 2020 is updated with DX12, I think performance gains would only be marginal. An RTX 3090 is not worth the money spent for the performance it promises I believe. The game is CPU bound for now, the latest and greatest Ryzen 5000 series will still be brought to its knees with DX11.

Why DX12? Multicore performance. Although multicore performance has increased from when the game was first released, it still wasn't enough. While writing this blog post, I'm flying from WIII (CGK) to WARR (SUB) and here's a look at the CPU usage graph. I switched between the cockpit and external views to show minimum and maximum usages.

![Cockpit Views - Microsoft Flight Simulator 2020](/content/images/2020/12/cockpit.png)
*Cockpit Views - Microsoft Flight Simulator 2020*

![External View - Microsoft Flight Simulator 2020](/content/images/2020/12/external.png)
*External View - Microsoft Flight Simulator 2020*

As you can see, the External View eats up more threads. However both views only maximized as much as 5 threads only out of 12. Hopefully DX12 would enable the game to maximize all the remaining threads, when that time comes, the higher end Ryzen 5000 series would be an interesting choice.

Another area for performance for me would be to get a faster memory. A 4000MHz DDR4 memory with low latency would be nice.

---

[Mention me on Twitter](https://twitter.com/tista) if you want to talk about Flight Simulator 2020 performance.

Cheers!