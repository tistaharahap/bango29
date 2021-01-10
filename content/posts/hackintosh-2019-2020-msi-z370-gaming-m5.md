+++
author = "Batista Harahap"
date = 2020-01-02T15:47:26Z
description = ""
draft = false
slug = "hackintosh-2019-2020-msi-z370-gaming-m5"
title = "Hackintosh 2019/2020 - MSI Z370 Gaming M5"

+++


Just after NYE 2020, I upgraded my Hackintosh to Catalina 10.15.2. Long story short, it blew up. It won't boot and this was my main work machine. Considered using my laptop but I knew my Dual Core Macbook Pro 13" with 16 GB memory wouldn't be able to handle it. To be honest, I don't think my Macbook Pro can handle 2 4k displays comfortably with only Intel's integrated GPU.

I had to make this work.

## Specs

I googled for my motherboard and it seemed that no one has tried to build a Hackintosh out of it. So this blog post is for people who wants to. Before anything else, here is the spec for my machine.

[PCPartPicker Part List](https://pcpartpicker.com/list/9n8TzN)

<style>
table.pcpp-part-list th {
  text-align: left;
}
table.pcpp-part-list td, table.pcpp-part-list th {
  padding: 0 10px;
}
</style>
<table class="pcpp-part-list">
  <thead>
    <tr>
      <th>Type</th>
      <th>Item</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="pcpp-part-list-type">CPU</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/sxDzK8/intel-core-i7-8700k-37ghz-6-core-processor-bx80684i78700k">Intel Core i7-8700K 3.7 GHz 6-Core Processor</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">CPU Cooler</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/RH2rxr/corsair-cpu-cooler-cw9060027ww">Corsair H115i 104.65 CFM Liquid CPU Cooler</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Motherboard</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/T3VBD3/msi-z370-gaming-m5-atx-lga1151-motherboard-z370-gaming-m5">MSI Z370 GAMING M5 ATX LGA1151 Motherboard</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Memory</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/nfWfrH/kingston-hyperx-fury-16-gb-1-x-16-gb-ddr4-3200-memory-hx432c18fb2k216">Kingston HyperX Fury 16 GB (1 x 16 GB) DDR4-3200 Memory</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Memory</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/nfWfrH/kingston-hyperx-fury-16-gb-1-x-16-gb-ddr4-3200-memory-hx432c18fb2k216">Kingston HyperX Fury 16 GB (1 x 16 GB) DDR4-3200 Memory</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Storage</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/Ykbkcf/samsung-960-evo-500gb-m2-2280-solid-state-drive-mz-v6e500">Samsung 960 EVO 500 GB M.2-2280 NVME Solid State Drive</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Video Card</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/9ZmxFT/asus-radeon-rx-580-8gb-rog-strix-video-card-rog-strix-rx580-o8g-gaming">Asus Radeon RX 580 8 GB ROG STRIX Video Card</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Case</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/6qPKHx/cooler-master-masterbox-mb500-atx-mid-tower-case-mcb-b500d-kgnn-s00">Cooler Master MasterBox MB500 ATX Mid Tower Case</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Power Supply</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/2HbwrH/corsair-rmx-2018-650w-80-gold-certified-fully-modular-atx-power-supply-cp-9020178-na">Corsair RMx (2018) 650 W 80+ Gold Certified Fully Modular ATX Power Supply</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Monitor</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/HKL7YJ/lg-24ud58-b-238-3840x2160-60hz-monitor-24ud58-b">LG 24UD58-B 23.8" 3840x2160 60 Hz Monitor</a></td>
    </tr>
    <tr>
      <td class="pcpp-part-list-type">Monitor</td>
      <td class="pcpp-part-list-item"><a href="https://pcpartpicker.com/product/HKL7YJ/lg-24ud58-b-238-3840x2160-60hz-monitor-24ud58-b">LG 24UD58-B 23.8" 3840x2160 60 Hz Monitor</a></td>
    </tr>
  </tbody>
</table>

## Pre Requisites

I created the USB stick for installation using my Macbook. I'm at a loss if you don't have an already running Mac to do this with.

### BIOS

Upgraded to the latest version as of this writing which is **7B58v18**. You can download the BIOS from the link below.

[https://www.msi.com/Motherboard/support/Z370-GAMING-M5](https://www.msi.com/Motherboard/support/Z370-GAMING-M5)

Use a blank `MS-DOS` formatted USB stick and put the downloaded BIOS in the root directory of the USB stick. Go into your BIOS and use `M-Flash` to flash to a newer BIOS.

### Olarila

The community here made Hackintosh installs even easier. I found it while googling for problems when trying to install using conventional methods (downloading Catalina from System Preferences). I went nowhere trying to do it conventionally for 1.5 days.

Olarila's community provides easily flashable images for USB sticks. I opted to go this route. I know the risks but I had to make this work. The provided images are inclusive of an EFI partitions with Clover. Find it in the link below.

[https://olarila.com/forum/viewtopic.php?f=51&t=10412](https://olarila.com/forum/viewtopic.php?f=51&t=10412)

You will need to register to be able see the links within Olarila. Please consider donating to the community if you find them useful.

Next for post installation, you would need an EFI folder for your Hackintosh. The link is below.

[https://olarila.com/forum/viewtopic.php?t=8222](https://olarila.com/forum/viewtopic.php?t=8222)

### Utilities

* Clover Configurator - [here](https://mackie100projects.altervista.org/download-clover-configurator/)
* Etcher, to flash to your USB stick - [here](https://www.balena.io/etcher/)

## Installation

After downloading Olarila's Catalina image, you'd find the file is compressed. Double click on it to decompress, you'd find a `.img` file you can flash to your USB stick.

### Flash to USB Stick

1. Open `balenaEtcher`
2. Select the `.img` file as the input
3. Select your USB stick as the output
4. Flash

### Catalina

1. Put the USB stick into an available front USB port
2. Turn on your Hackintosh
3. Go into the BIOS
4. Boot to USB Stick as the first priority
5. Save & Exit - Will Restart
6. Clover shows up - Select `Install Catalina`
7. When the Catalina installer shows up, select `Disk Utility`
8. Format the target drive using `APFS` filesystem and `GUID Partition Table`
9. Close `Disk Utility`
10. Continue installing Catalina

### Post Install

When restarting after installing Catalina, **don't unplug the USB Stick yet**, we still need it to boot to your Catalina install. When you get to the desktop, follow these steps.

1. Open `Clover Configurator`
2. On the left hand sidebar, choose `Mount EFI`
3. Select your Catalina install drive
4. Click `Mount Partition`

At this point, you would need to decompress the EFI folder you downloaded earlier from Olarila.

1. Copy the `EFI` folder to your `EFI partition`
2. Fire up `Disk Utility`
3. Eject the `EFI partition`
4. Restart

When restarting, go into your BIOS before starting up and select your Catalina install as your first boot priority. Unplug the USB Stick.

Enjoy Catalina.

## ACPI Patches

I haven't done this at all, will post this as a separate post.

---

After 1.5 days without this Hackintosh, I finally have a fully working machine. Contemplated installing Windows 10 and or Ubuntu on it but I'm a spoiled brat, I like macOS just fine.

I missed that big 3% Bitcoin drop train since I don't want to trade with an uncomfortable setup. Dual monitors is a must although 3 monitors is my dream setup. Sadly with my GPU, only 2 Display Ports are available, the third one would need to go through HDMI.