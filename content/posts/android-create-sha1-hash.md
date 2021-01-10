+++
author = "Batista Harahap"
categories = ["Android", "api", "hash hmac sha1", "hmac sha1", "oauth", "sha1", "urbanesia"]
date = 2010-12-23T19:51:10Z
description = ""
draft = false
slug = "android-create-sha1-hash"
tags = ["Android", "api", "hash hmac sha1", "hmac sha1", "oauth", "sha1", "urbanesia"]
title = "Android - Create SHA1 Hash"

+++


I've been toying with Urbanesia's OAuth provider API calls in Android these few hours regretting why it is so complicated in Java compared to PHP hehehe. Since OAuth's requirement to generate a signature is using HMAC SHA1 to sign the whole POST &amp; GET requests, I had to find a way to do it in Android's Java.

So I scour Google to look for answers but sadly the results isÂ surprisinglyÂ scarce. I wanted to make a standardize OAuth client for Urbanesia's API but the standard libraries provided by the Android SDK is not what I've expected. For this to work, will need to download Apache Commons Codec Library <a href="http://r.bango29.com/eBzz8a">here</a>. So without further ado, here are the codes.

<pre lang="java">
	private String sha1(String s, String keyString) throws 
		UnsupportedEncodingException, NoSuchAlgorithmException, 
			InvalidKeyException {
		
		SecretKeySpec key = new SecretKeySpec((keyString).getBytes("UTF-8"), "HmacSHA1");
		Mac mac = Mac.getInstance("HmacSHA1");
		mac.init(key);
		
		byte[] bytes = mac.doFinal(s.getBytes("UTF-8"));
		
		return new String( Base64.encodeBase64(bytes) );
	}
</pre>