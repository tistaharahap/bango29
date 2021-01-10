+++
author = "Batista Harahap"
categories = ["mysql", "sphinx", "homebrew", "percona", "mac"]
date = 2015-01-22T08:29:56Z
description = ""
draft = false
slug = "making-homebrew-play-nice-for-sphinx-mysql"
tags = ["mysql", "sphinx", "homebrew", "percona", "mac"]
title = "Making Homebrew Play Nice with Sphinx & MySQL"

+++


So I'm revisiting an old friend, Sphinx. It's been a while and warming up to Sphinx's new features. However, when I tried to `brew install` it, I got no MySQL support.

The above gets more complicated because I'm not using vanilla MySQL, instead I'm using Percona Server on my machine. So to get thing going, here's what I did.

```
$ brew unlink percona-server
$ brew install mysql-connector-c
$ brew link percona-server
$ brew install sphinx --mysql
```

`\m/`