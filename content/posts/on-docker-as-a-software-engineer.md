+++
author = "Batista Harahap"
categories = ["digital ocean", "jenkins", "continuous integration", "docker", "orchestration", "simple", "deployment"]
date = 2015-11-25T11:05:34Z
description = ""
draft = false
slug = "on-docker-as-a-software-engineer"
tags = ["digital ocean", "jenkins", "continuous integration", "docker", "orchestration", "simple", "deployment"]
title = "On Docker - As A Software Engineer"

+++


Last week, I went for the ocassional time a geek gets to down a few bottles of beer with other geeks. The conversations started with the usual "How are you"s but being geeks it led to various talks about tech. One of it was me telling everyone about [Docker](https://www.docker.com/).

One of the reactions about Docker was *why am I willing to complicate myself when the scale isn't there yet?* A valid argument.

When I read about the Docker, the first thing that caught my attention is the tagline: **Build, Ship, and Run** - *An open platform for distributed applications for developers and sysadmins*. Developers and Sysadmins?

After finishing a few more readings about Docker, I came across to [CoreOS](https://coreos.com/). It's a Linux distro that doesn't have any package manager at all. WTF right? As it turns out, Docker is its package manager. Apps are ran in containers, no clutter to the main OS. It really hit me.

## Laptop To Production

Often times, software engineers don't give the slightest care about environments other than their own laptop. This usually leads to complexity for the sysadmins. Ex: *it's working fine on my laptop, why isn't it working as expected on the production environment?*

The symptom above can be avoided by foolproofing configs, matching the OS on the production with the laptop, making sure all the dependencies are the exact version, etc. This is hard work! Even the slightest discrepancy can be responsible for intermittent defects within the software.

This is where Docker shows its most valuable power: **Consistency**.

A few lines of `Dockerfile` is enough to gift you good night sleeps. How you ask? The long explanation is well written [here](https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images) at DigitalOcean. Get it?

If I have to be explicit then here goes. Docker uses a layered file system called [Union File System](https://docs.docker.com/engine/introduction/understanding-docker/#union-file-systems). So each time there's a change to the filesystem, it gets layered into the filesystem which then enable a versioning-like capability on the filesystem level.

Getting back to the `Dockerfile`, it basically tells Docker that the base image for this container is let's say `ubuntu:latest`, update the `apt` & install these packages, get all the dependecies for my app and run it. That's it.

Of course you can do more by [linking containers together](http://rominirani.com/2015/07/31/docker-tutorial-series-part-8-linking-containers/). Pretty powerful to share config values between containers.

Docker enables simple orchestration with a relatively simple from concept to implementation. Best of all, you get consistency between your laptop to the production environment.

## Source Code Changes

Being a Pythonista, I enjoy simple solutions for complex and even complicated problems. Updating source code is one of them.

With Docker you worry more about writing code and or managing the infrastructure than the small things that hurts you a lot. WTF? When your source code include a `Dockerfile`, you can be sure that an update means it's just `$ docker build .` away. Docker comes with [Docker Hub](https://hub.docker.com/).

You can commit changes to Docker Hub which will then can either act as a repo for your changes or get your Continous Delivery mechanism going with Automated Builds. I won't discuss the details since the road to hell is paved with good intentions. On a high level, Docker Hub is like Github powered by Jenkins.

## Scale

Docker comes with [Swarm](https://docs.docker.com/swarm/).

> Docker Swarm is native clustering for Docker. It allows you create and access to a pool of Docker hosts using the full suite of Docker tools. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.

Basically you can combine multiple docker daemons running on different machines to form a single cluster. You can even [span multiple data centers](http://blog.weave.works/2014/10/08/i-just-created-a-cassandra-cluster-that-spans-3-different-network-domains-by-using-2-simple-shell-commands-how-cool-is-that/) with just a few lines of shell commands.

I haven't scaled Docker to this order of magnitude but when I do need to, I'm comfortable that Docker manages to keep its abstraction as simple as possible.

## Network Separation

Every container you run will run on a different network from its host. You can instead use a bridge to run it on the same network of course. But I think by running it of a different network by default gives an extra layer of complexity in the event that an attacker compromises your application.

I run Docker on Digital Ocean, I miss AWS' VPC but I get it for free with Docker (sort of).

The only thing you expose to the public is the API container. Other than that, it stays private.

---

The 4 points above are what drives me to implement Docker from early with Coral. Using Docker is like stacking Legos. It keeps your way of thinking simple. I've always liked complexity more than complication, Docker is exactly it.

As a footnote, I haven't written in a while and it's great to write about something disruptive. If you like what you're reading, there are plenty more of this on [Coral](http://www.coralshop.co.id), hit me up on `tista _%at%_ coral-inc.com` to have a conversation.