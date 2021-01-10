+++
author = "Batista Harahap"
categories = ["flask", "mongodb", "python", "root", "monitor", "android"]
date = 2013-12-27T14:58:08Z
description = ""
draft = false
slug = "monitoring-android-with-flask"
tags = ["flask", "mongodb", "python", "root", "monitor", "android"]
title = "Monitoring Android with Flask"

+++


This blog post is a mirror and a more detailed representation of the materials I'm talking about at [Kopi Darat Python Indonesia - December 2013](http://www.python.or.id/2013/11/kopi-darat-python-indonesia-desember.html). Slides can only say so much, here is where the intimacy starts.

## Warning

Any and all of the information including source code available here are for educational purposes. Please use them responsibly. That being said, all codes are basic implementations only. Please get your hands dirty.

All codes are tested on the following configuration (specs):

* Python 2.7.2 on OS X Mavericks 10.9.1
* Google Nexus 4 - __rooted__ - Kitkat 4.4 ROM
* MongoDB 2.4.6

## Materials & Repo Access

All of the source code are available on the following Github repos.

* Ngintipbot - https://github.com/tistaharahap/ngintipbot
* ngintipd - https://github.com/tistaharahap/ngintipd

## Android

[Android](http://source.android.com/) as most of us know (or not) is an OS for a wealthy option of gadgets, embedded devices and also [laptops](http://www.theverge.com/2013/10/18/4852104/lenovo-announces-a10-android-laptop). Long story short, Android is Linux based with Java as its frontend exposed through its SDK. 

However, not everything is Java. Android has what it's called [Java Native Interface (JNI)](http://developer.android.com/training/articles/perf-jni.html). So we can do things in Java, C/C++ and vice versa. Head on to [Android NDK](http://developer.android.com/tools/sdk/ndk/index.html) for more info.

The part of Android I'm talking about is not necessarily about native C/C++ developments on Android. It's a nice to know knowldge to get a bigger picture of Android's internals. Here's a great Youtube video about the matter.

<iframe width="100%" height="315" src="//www.youtube.com/embed/MlxiQNijniQ" frameborder="0" allowfullscreen></iframe>

## Rooting Android

This part is for you to figure out. But, if you happen to be using a Nexus 4, you can go [here](http://nexus4root.com/nexus-4-root/how-to-root-nexus-4-windowsmac-osxlinuxubuntu/).

Rooting your phone is required in order to try out the codes.

## Introducing Ngintipbot

Ngintipbot is an iconless (supposedly) Android app. Its main purpose is to monitor the items I would want to be monitored which are the items below.

* Line - `root` required
* Whatsapp - `root` required
* Remote Upload of Data - `root` required
* Call Recording - `root` required
* SMS
* Location
* Phone Logs
* Contacts
* Remote Mic Activation

### How Ngintipbot Works

Here's a quick generals on how Ngintipbot works and how it doesn't.

1. Install Ngintipbot's APK
2. Run it with one of 2 ways, the icon from the launcher or a specific SMS format
3. Eitherway, it will start Ngintipbot's Service and make it a `STICKY` service
4. The service will create a `PendingIntent` which will set off `AlarmBroadcastReceiver` to be invoked every 1 hour
5. When `AlarmBroadcastReceiver` is invoked, Ngintipbot will try to passively sense the device's current location
6. After getting a lock on location, Ngintipbot will read contents from Line, Whatsapp and SMS, pack it and send the whole data to a `ngintipd` instance somewhere on the Internet

All of the juicy stuffs are at `Utils.java`. The methods to read contents from Line, Whatsapp and SMS are defined there.

### The Main Activity

The main activity contains nothing. Consider it as a placeholder only.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/IntipbotActivity.java"></script>

There's nothing there right? Why? A simple answer is because Activities does not have a predictable lifetime. You can't keep Activities to always run on the background. That's why most of the logic are delegated into Services.

## Intipbot Service

This particular class interest is with stated before which is about starting the Service as a `STICKY` service. In particular is with the source code below.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/IntipbotService.java?slice=23:32"></script>

By returning `Service.START_STICKY` we are simply making the Service to be constantly recreated if needed. A better explanation from Android's documentation is available [here](http://developer.android.com/reference/android/app/Service.html#START_STICKY).

### Broadcast Receivers

The Service above is actually started from one of three possibilities which are a direct launch of the app, a specific SMS or when the device is booted. All of these are possible by registering a `BroadcastReceiver` into the manifest like below.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/AndroidManifest.xml?slice=37:42"></script>

The receiver which is `StartupReceiver` simply triggers an `Intent` invocation to start `IntipbotService`.

## Sensing Location

I guess this is relatively the easy part. Tutorials to do this are plentiful so I won't talk much about this. My implementation after we get a lock on a location is where the more interesting action happens.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/Utils.java?slice=155:193"></script>

## Reading & Receiving SMS

In order for us to be able to read & receive SMSes, the app must declare the permission to do so.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/AndroidManifest.xml?slice=17:18"></script>

### Reading SMS

I like `JSON` and this is why my implementation is actually read SMSes and convert them into `JSONArray`s which will then return its `String` representation to be `POST`ed later on.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/Utils.java?slice=42:69"></script>

### Receiving SMS

The current implementation doesn't actually parse the content of any SMS. It simply just invoke `StartupReceiver`. This can be a good after hours tinkering don't you think?

## Privileged Process Running

Next step is to gain privileged rights. I implemented this at `Utils.java` statically. There's nothing special about this. One thing to keep in mind is to do proper error parsing if it so happens the app didn't get privileged rights.

My implementation does not have that particular error management. Please do so.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/Utils.java?slice=118:153"></script>

## Reading Line & Whatsapp

Both of these apps are actually storing their message database in an `SQLite` flat file database. If you're interested in extracting the databases without the app, the path is below.

* `/data/data/jp.naver.line.android/databases/naver_line*`
* `/data/data/com.whatsapp/databases/msgstore*`

Now with the app, I'm actually `tar`-ring the databases, create a directory called `.goog` on the SDCARD, upload to `ngintipd` and delete the `.goog` directory afterwards.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipbot/blob/master/src/com/bango/ngintipbot/Utils.java?slice=71:116"></script>

## ngintipd

Okay __ngintip__ is Indonesian for peeking so it's only right to name the daemon `ngintipd`. As the name implies, this daemon is always ready to receive data from `Ngintipbot`. Written in Python and at the current development state, acts only as a storage. Further development should process `SQLite` databases and manipulate.

Again there are nothing special yet, it's basically a one file daemon.

<script src="http://gist-it.appspot.com/github/tistaharahap/ngintipd/blob/master/ngintipd"></script>

## EOF

This concludes the talk. Codes and implementations are still minimum but I believe it's ready to be a foundation of something more ambitious so to speak. Cheers!