+++
title = "Blogging With Hugo"
author = "Batista Harahap"
draft = false
date = 2021-01-11T19:45:56+07:00
image = "/content/images/2021/01/simple.jpg"
slug = "blogging-with-hugo"
tags = ["blog", "hugo", "writing"]
categories = ["blog", "hugo", "writing"]

+++

Before this post, my blog was a self hosted [Ghost](https://ghost.org/) installation. I hardly update the installation, it's been at its `0.11.x` install for quite a while. It's not quite straightforward it seems to update to the latest Ghost version. I didn't want to use MySQL as it's not needed for my scale, couldn't get it to work with sqlite3 unfortunately. So I went shopping and immediately liked [Hugo](https://gohugo.io).

## Pre Migration

Going to talk more about what led me to Hugo. It started with [Pico](http://picocms.org/) but was immediately discouraged because the website is not served throught HTTPS and although I have nothing against PHP, it's still PHP. Dug deeper about static file blogging platforms, wanted a [Python alternative](https://blog.getpelican.com/) to find that it's not great, it's too bland for my taste and most importantly it looks old (sorry..).

Hugo was next on the list and I never looked back.

Just looking at the themes already built for Hugo, that's enough reason to make the switch. Incidentally, a Ghost to Hugo migration tools is available, [link here](https://github.com/jbarone/ghostToHugo).

## Migration

Not hard at all for the markdown files. A bit more work for assets and url routes.

### Export/Import

1. Login to Ghost
2. Go here `Labs > Export`
3. Download the JSON
4. Use `ghostToHugo` to migrate

When it's migrated, it will create a Hugo site, if at this points you don't have a Hugo binary, do this.

```shell
$ brew install hugo
```

### Adapting to Hugo

Next is to download all the assets.

On the server side.

```shell
$ cd your/ghost/install/directory
$ tar cfz ~/ghost-content.tgz content/
```

On your local.

```shell
$ scp user@yourserver:~/ghost-content.tgz .
$ tar xfz ghost-content.tgz
$ mv content your-new-hugo-site/static
```

The problem with my Ghost install was that it was referencing images from these directories:

```
images/
content/images/
```

I chose `content/images` as the absolute path. Next is to do some URL rewriting in Nginx, as simple as adding this into the Virtual Host:

```
rewrite ^/images/(.*)$ /content/images/$1 redirect;
rewrite ^/tag/(.*)$ /tags/$1 redirect;
```

There's another rewrite rule for tags. Ghost uses a singular route while Hugo uses a plural route. I'm with Hugo on this.

## Themes

Hugo recommends using git submodules for this but I don't really like it since ideally I'd need to fork a new repo for it. Forking something I don't work on frequently means it will not get much pulls from the origin which is no different than just downloading a zip and extracting it. 

### Colors

Settled with [Beautiful Hugo](https://github.com/halogenica/beautifulhugo), it's simple. The one global change I want was to have a darker toned theme, the theme was `#fff` heavy I have to say. So I did a little bit CSS editing to have a more `off white` color. Other than that, I kept the CSS as is.

### Activating Theme Features

This is somewhat confusing at the start, there wasn't much resource I googled that explains this succintly. It was around 1AM last night and I was too much of a pragmatist at that hour to read the docs. Ended up looking into other people's blogs and observing how they did it. It wasn't that difficult. At writing, this is how my `config.toml` looks like.

```toml
baseURL = "http://localhost:5000"
disablePathToLower = true
languageCode = "en-us"
title = "Batista Harahap"
theme = "bhugo"
DefaultContentLanguage = "en"
disqusShortname = "bango29"
pygmentsCodeFences = true
pygmentsUseClasses = true

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true

[permalinks]
  posts = "/:slug"

[Author]
  name = "Batista Harahap"
  email = "b@tista.me"
  twitter = "tista"
  github = "tistaharahap"
  linkedin = "tista"
  soundcloud = "tistaharahap"

[Params]
  useHLJS = true
  logo = "/content/images/tista.jpg"
```

## CI/CD Thoughts

Haven't thought about this much but the general flow is like below:

1. Push to repo
2. Push triggers a Github action
3. Action issues a trigger through SSH for my VM to pull changes, build and deploy

Thought I could use Docker but then it's a static site, why the complexity? So from the get go I choose to host my blog traditionally. I can just create a `service` account on my server for step 3.

---

From contemplating of migrating to Hugo to execution, I wanted it to be dead simple and that's exactly what I got. I'm now writing my blog post in VS Code which is new but welcomed. I acknowledge that assets would need to be uploaded manually (copy paste to the right folder) but that's still simple. On the server side also it's much simpler, no database needed, it's just static files.

Oh, one more thing..

Hugo supports live preview while you write your blog post, while writing just do this:

```shell
$ hugo serve -D
```

Changes will be updated automagically.

Happy with Hugo, now my thoughts are versioned in Github.