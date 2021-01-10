+++
author = "Batista Harahap"
categories = ["android", "notetoself", "camera"]
date = 2015-04-13T08:46:06Z
description = ""
draft = false
slug = "androids-camera-preview"
tags = ["android", "notetoself", "camera"]
title = "Android's Camera Preview"

+++


This is a _note to self_ post. Today I've been figuring out to have my own custom Camera Activity. A newbie mistake made the Activity to block the UI when initializing. Here's the problem and the fix.

I started `camera.startPreview()` at `surfaceCreated(SurfaceHolder holder)`. When I moved to `surfaceChanged(SurfaceHolder holder, int format, int width, int height)`, everything turns out as expected. Here's the full class with an explanation below.

<script src="https://gist.github.com/tistaharahap/5ad6ff038f4062cf8ede.js"></script>

To made matters worse, I called `camera.startPreview()` both when on both methods. The explanation on [SurfaceHolder.Callback](http://developer.android.com/reference/android/view/SurfaceHolder.Callback.html)'s documentation was crystal clear.

`surfaceCreated(SurfaceHolder holder)`

_This is called immediately after the surface is first created._

`surfaceChanged(SurfaceHolder holder, int format, int width, int height)`

_This is called immediately after any structural changes (format or size) **have been made to the surface**._

The emphasis is the key.