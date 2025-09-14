+++
author = "Batista Harahap"
date = 2025-09-14T17:49:21+04:00
image = "/content/images/2025/09/omarchy.png"
categories = ["omarhcy", "linux", "desktop", "machine"]
tags = ["omarhcy", "linux", "desktop", "machine"]
title = "Customizing My Omarchy"
slug = "customizing-my-omarchy"
description = ""
draft = false

+++

It's Sunday and tomorrow is the start of a new week. With that, I'm telling myself to completely spend the week off of my Mac Mini M4 and 100% into my Omarchy machine. I'm customizing Omarchy to my liking and this is the beauty of it. Some I did myself while some I asked Claude Code to do for me.

## Machine Specs

My gaming PC laid dormant for the majority of the time, I use it only when I'm playing games. Proton in Linux is making waves but for most of the games I played, I'd rather play it in Windows, I want the games to just work. On the other hard, a spare NVMe drive on this machine paved the way for Omarchy.

- AMD Ryzen 7800X3D
- 32 GB DDR5 RAM
- AMD Radeon 7800XT GPU
- 7x Noctua NF-A12x25 Chromax Black 120 mm
- NZXT X73 AIO Watercooler
- 1x 2 TB Corsair Gen4 NVMe - Windows
- 1x 1 TB Crucial Gen4 NVMe - Omarchy
- OWC Aquantia 10 GBe NIC
- NZXT H6 Flow Casing
- Silverstone 1000 Watts PSU
- Samsung OLED G8 1440P Ultrawide @ 175 Hz

[Geekbench Result](https://browser.geekbench.com/v6/cpu/13812142)

I want this PC to be whisper quiet and I can say I'm successful at that. The fans only picks up when there are intense CPU workloads which is almost never. Of all the components in the PC, the only thing I'm inclined to upgrade is the RAM but Omarchy has so far negate that idea, it just runs so smooth.

## Development Environment

We have a small team in Zest Equity where I work today, a team of 2 backend engineers and 2 web frontend engineers. We dwell in the WWW exclusively. I don't really need beefy hardware to do my development, built Zest Equity from scratch with a Macbook Air M1 at the beginning as prove.

My development environment is a mix of backend and frontend stacks. I code the backend mainly in Python but background services are written in TypeScript and RXJS although since finding about [dramatiq](https://dramatiq.io/), more service are written in Python. LLM related background services are exclusively written in Python, I mean [Pydantic AI](https://ai.pydantic.dev/) man, the DX is _chef's kiss_.

The biggest RAM hog is Pycharm and Android Studio, and of course Chrome. Omarchy is making me more eager to try out other alternatives but not anytime soon. I dabble in Android to write apps just for me, usually apps that uses LLMs to make me enjoy my time better.

## The Display

Out of the box, Omarchy gave me a 60 Hz refresh rate. It was ok until I switched to my Windows to play games, what have I been missing? Fixing this apparently was easy, I asked Claude Code to correctly change the refresh rate to 175 Hz. Although if I had spent some time to read Omarchy's manual, this was a no brainer.

The other thing I wanted the screen to behave is scaling. I'm 40+ so my eyes hate small UI elements and I'd rather lose real estate than productivity. This was apparently so easy to tweak with.

```conf
# ~/.config/hypr/monitors.conf
env = GDK_SCALE,1.067
monitor = DP-3,3440x1440@175,auto,1.067
monitor = HDMI-A-1,1920x1080@60,auto-center-down,1
```

The twist came with another monitor I recently use. It's a 1080P 14" monitor I dedicate for Claude Code. Getting it to center and to the bottom of the main display was a bit of an effort. That is until Claude Code figured out `auto-center-down`, worked like a charm.

[Hyprland's monitor config](https://wiki.hypr.land/Configuring/Monitors/) is not that much of a learning curve. With Omarchy, any changes to the config file gets implemented immediately after I save the file, neat!

On my keyboard to make changes to the config, I'd just `Option + Command + Space` then select `Setup > Monitors` and an `nvim` window pops up with the config to play with. This is what peak DX look like for an OS optimized for software engineers.

## The RAM

So the RAM is one of those RGB sticks, I hate colorful RGB with a passion, it screws up the whole aesthetics of the PCs I build. However, the right color (or no color) works for me. Now I need to turn the RAM RGB off so I googled it and downloaded an `appimage` file for [OpenRGB](https://openrgb.org/).

```bash
mkdir ~/openrgb
mv OpenRGB*.AppImage ~/openrgb
cd ~/openrgb
chmod +x OpenRGB*.AppImage
open .
```

The last command is going to pop a file manager into the UI and all I have to do is double click the `appimage` file to run it. Unfortunately it did not detect my RAM so I had to do more.

```bash
sudo pacman -S i2c-tools
sudo usermod $USER -aG i2c
sudo modprobe i2c-dev
```

This was enough to make my RAM detected and I can immediately do what I needed, turning off the RGB. To make the kernel module stick after rebooting:

```bash
sudo vim /etc/modules-load.d/i2c.conf
# type this: i2c-dev then save
sudo cat /etc/modules-load.d/i2c.conf
# should print out below:
i2c-dev
```

That was not as straightforward to do but not that big of a deal to decode.

## The Terminal

[Warp Terminal](https://www.warp.dev/) has been my go to terminal for quite a while now. It's available on all the platforms I work with and it's sleek. To install is straightforward:

```bash
yay -S warp-terminal-bin
```

I don't enjoy Warp's sudden recommendation to edit a test file when there's a failing test, but something I can tolerate. For Claude Code though, Warp Terminal is great. I have the secondary screen with Warp Terminal always there all the time.

Alacritty that came with Omarchy is great when I needed to do something quick like installing a package because it loaded almost instantenously.

## Waybar

I'm in love, I'm in love. Never have I experienced a taskbar that is configurable, nothing stopping me from making it exactly how I want it to look like. I don't have to do this on my own as a bonus, I just ask Claude Code to things for me. The config file is located at:

`~/.config/waybar/config.jsonc`

I can edit this by `Option + Command + Space` then going to `Setup > Config > Waybar` which will pop an `nvim` window to edit the config. When I looked at it the first time I was smiling ear-to-ear, they're all just Unicode characters and a little bit of HTML!

I asked Claude Code to give me CPU use in %, the CPU frequency and up/down traffic on my ethernet port. The icons are all just Unicode characters, I haven't said this before right? It's so simple and elegant!

Seriously this is so beautiful, here's a link for the complete reference to the config file:

[Waybar Wiki](https://github.com/Alexays/Waybar/wiki/Configuration)

Oh and changes to the config file gets executed as soon as the file is saved.

## Web Apps

You should know how icky it is to do this in macOS and Windows, there's no way to do this easily. This is one of those things that you don't you'll love until you have it. In Omarchy, to do this is simple `Option + Command + Space` then going to `Install > Web App` afterwards just follow the instructions.

It's so straightforward and easy to do this. The newly created Web App will be immediately available when you `Command + Space`. First website I did for was `Netflix` since I binge watching while working is so satisfying.

---

I'm sure I will have more use cases to talk about in the future but for now these tweaks suit my needs.

The single most influential thinking to switch to Omarchy is the fact that I can use ANY x86_64 machine. This means the control goes back to myself as the software engineer. I can choose my own hardware at my own pace, no Apple tax. It even runs on an old 2018 Intel NUC.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Tiny but does not feel sluggish at all. <a href="https://t.co/EQd0yAG3vR">pic.twitter.com/EQd0yAG3vR</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1960286431743496406?ref_src=twsrc%5Etfw">August 26, 2025</a></blockquote>

I can't stress how valuable it is to choose the hardware I want for my own workstation. It's liberating and I hope the PC industry don't go into SoCs anytime soon. I want to build my own PC with my own hands, just for me!

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
