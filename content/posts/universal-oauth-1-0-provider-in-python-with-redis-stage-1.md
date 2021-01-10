+++
author = "Batista Harahap"
date = 2013-06-04T09:19:27Z
description = ""
draft = false
slug = "universal-oauth-1-0-provider-in-python-with-redis-stage-1"
title = "Universal OAuth 1.0 Provider in Python with Redis - Stage 1"

+++


Just a few days ago, I had a pretty long geektalk with <a href="http://twitter.com/dondyb" target="_blank">Dondy</a> about OAuth. He wanted to talk about which OAuth version is best for his needs. Long story short, the answer was OAuth 1.0. He was the one who '<em>introduced</em>' me into Python and I instantly got an itch to have a try in building an OAuth 1.0 Provider in Python.

First of all, I have no plans at the moment to support 3 legged authentications. I want to just go out there and code, make it work and refactor later to support things that are not supported initially.

The purpose of this provider is so that anyone can extends everything easily while still maintaining compatibility with <a href="http://tools.ietf.org/html/rfc5849" target="_blank">RFC5849</a>. At the current v0.1.1 version, the only available URI is <code>'oauth/access_token'</code>. This is to get XAuth working first. To provide authentication, modify or extend <code><a href="https://github.com/tistaharahap/oauth1-provider-redis-py/blob/v0.1.1/oauth1-provider/oauth1.py#L98" target="_blank">_verify_xauth_credentials and</a></code> suit your needs.

The next step is to abstract and provide decorators to initialize the provider in Flask.

Why Redis? Because Redis is unmatched in performance with atomic CRUDs. It's lightning fast, CPU friendly and it's basically a key/value store.

I am still new to Python, would love for some best practice pointers with the project. Forks and Pull Requests are welcomed.

The source code is available here at <a href="https://github.com/tistaharahap/oauth1-provider-redis-py" target="_blank">https://github.com/tistaharahap/oauth1-provider-redis-py</a>

A test using <a href="http://urbanesia.github.io/oauthnesia-py" target="_blank">Urbanesia's OAuthnesia for Python</a> is imported below.

<script src="https://gist.github.com/tistaharahap/5704712.js"></script>