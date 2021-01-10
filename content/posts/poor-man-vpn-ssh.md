+++
author = "Batista Harahap"
date = 2017-05-14T08:49:46Z
description = ""
draft = false
slug = "poor-man-vpn-ssh"
title = "Poor Man VPN - SSH"

+++


Baru-baru ini gw mau ga mau mesti terima kalo koneksi internet di rumah (bukan Jakarta) mesti gunain telco karena landline nya masih belum siap. Apa yang terjadi? Same shit, same smell, HTTP connection gw dibajak jadi sebuah `iframe` yang isinya kata XL untuk bantu track quota usage gw. Bull shit!

![Ada XL di kiri bawah](/content/images/2017/05/Screen-Shot-2017-05-14-at-10.17.53-PM.jpg)

Gw udah [sering bicarain](http://bango29.com/tag/xl/) praktek menjijikkan seperti ini dari XL dan telco lain. Mereka ga berhak melakukan ini, detilnya bisa baca di blog post gw sebelum-belumnya.

Sekarang gw mau nulis tentang caranya untuk hindarin praktek semacam ini.

---

## SSH Endpoint

Long story short, gw punya komputer di rumah di Jakarta yang selalu nyala 24 jam. Komputer ini adalah sebuah Ubuntu Server yang selalu setia hadir untuk membuat hidup gw lebih nyaman kalo di luar kota. Salah satunya adalah SSH Socks Proxy.

Nah supaya gw bisa SSH ke komputer rumah, gw pake service dari `ngrok`, cek [disini](https://ngrok.com). Memudahkan untuk gw punya tunnel yang dari internet bisa kontak yang di dalem jaringan rumah. Sangking kerennya dan kepake melulu, gw bayar langsung setahun, gw saranin lo juga.

## Action

Setiap kali bikin koneksi ke `ngrok`, akan di assign sebuah port dan sebuah DNS address. Karena gw biasanya di Indonesia dan sekitarnya, gw pilih region AP (Asia Pacific). Untuk menggunakan SSH connection sebagai SOCKS Proxy, demikian perintahnya:

```
$ ssh -ND 1234 tista@0.tcp.ap.ngrok.io -p 12345
```

`tista`: That's me.

`-ND`: Setelah terjadi koneksi, ga perlu masuk shell lalu langsung buat SOCKS Proxy di port `1234`.

`-p`: Lakukan koneksi SSH ke server melalui port `12345`.

## Proxy Setup

Langsung meluncur ke `System Preferences > Network > [Your Network Adapter] > Advanced > Proxies`. Centang `SOCKS Proxy` dan masukin host `127.0.0.1` dan port `1234`.

---

Sekarang, jangan biarin XL bikin lo jadi objek iklan dengan mengintip semua web visits HTTP lo. Be smart, lo udah bayar, masa lo mau dikerjain kaya begini?