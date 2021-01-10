+++
author = "Batista Harahap"
categories = ["oauth", "provider", "python", "redis", "xauth"]
date = 2013-06-10T19:42:27Z
description = ""
draft = false
slug = "universal-oauth-1-0-provider-in-python-with-redis-stage-2"
tags = ["oauth", "provider", "python", "redis", "xauth"]
title = "Universal OAuth 1.0 Provider in Python with Redis - Stage 2"

+++


Been doing some more work with this OAuth 1.0 Provider and as it turns out, my implementation so too lean. Having said that, it's exactly what I aimed for in the beginning: A simple lean OAuth 1.0 Provider implementation without getting buried over the concept of OAuth itself.

This iteration still have more things to be introduced. As pointed by <a href="http://geektalk.in/users/kuvMNkNSCrYSqeCov" target="_blank">willhn</a> at <a href="http://geektalk.in" target="_blank">GeekTalk.in</a> <a href="http://geektalk.in/posts/3KekGYJdRjoxbCjo9/comment/9v48RxJzeaWPejnhr" target="_blank">here</a>, OAuth 1.0 allow the OAuth authorization data to be passed through HTTP Authorization Header and POST. RFC 5849 documentation states the standard <a href="https://tools.ietf.org/html/rfc5849#section-3.5" target="_blank">here</a>. At the current <a href="https://github.com/tistaharahap/oauth1-provider-redis-py/tree/v0.3.0" target="_blank">0.3.0 version</a>, Authorization data are picked up only from Authorization Header.

My immediate goal for this project is to create an OAuth reverse proxy, carrying all valid requests into some other language independent backend be it in Python, PHP, Node.js or any other languages. For that, Stage 2 has accomplished the reverse proxy nature.

Stage 3 will be adding POST support for Authorization headers and to implement a reverse proxy to a publicly available API somewhere. I have a few in mind and the <a href="http://www.icndb.com/" target="_blank">Internet Chuck Norris Database</a> will make a great candidate :D

Talk is cheap, so here is an example of an endpoint implementation.

<script src="https://gist.github.com/tistaharahap/5751575.js"></script>