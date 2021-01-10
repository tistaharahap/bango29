+++
author = "Batista Harahap"
categories = ["hmac", "hmac sha1", "ios", "ipad", "iphone", "oauth", "oauthnesia", "objective c", "sha1", "twitter", "urbanesia", "urbanesia api", "xauth"]
date = 2011-08-16T16:32:48Z
description = ""
draft = false
slug = "hmac-sha1-base64-result-with-objective-c"
tags = ["hmac", "hmac sha1", "ios", "ipad", "iphone", "oauth", "oauthnesia", "objective c", "sha1", "twitter", "urbanesia", "urbanesia api", "xauth"]
title = "HMAC-SHA1 Base64 Result With Objective-C"

+++


A few days of hard done nights were all inspired by faulty encodings. Talk about "Hello World" experiences LOL. Keeping things in mind, to really smooth things up between Objective-C and PHP, in any Objective-C functions needing to encode/decode strings like PHP, here's the encoding type:

<pre lang="objc">
NSASCIIStringEncoding
</pre>

Do not interchange this with any other or things will go wrong :( Here are snippets to generate HMAC-SHA1 hashes in its Base64 form encoded correctly for OAUTH v1.0a authentication.

<script src="https://gist.github.com/1202963.js"></script>

The Base64Transcoder library is the work of Jonathan Wright, available at <a href="http://code.google.com/p/oauth/">http://code.google.com/p/oauth/</a>. Cheers!