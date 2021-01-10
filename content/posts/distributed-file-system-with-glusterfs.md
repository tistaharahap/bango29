+++
author = "Batista Harahap"
categories = ["linux", "ubuntu", "glusterfs", "filesystem", "distributed", "torrent", "deluge"]
date = 2014-03-23T15:59:34Z
description = ""
draft = false
slug = "distributed-file-system-with-glusterfs"
tags = ["linux", "ubuntu", "glusterfs", "filesystem", "distributed", "torrent", "deluge"]
title = "Distributed File System with GlusterFS"

+++


Recently I had an itch about my 3 unused VMs. Each of them only has 512 MB RAM, 1 vCore and 10 Gigs of SSD. It's limited in resource but this is what you get for US$ 1/month. From the 10 Gigs SSDs, I had approximately 21 Gigs of free space combined. This got me thinking.

What if I could combine all the free space and have a mega volume?

---

After some readings, I settled for [GlusterFS](http://glusterfs.org). It was the simplest to understood and also to install & configure. It took some trials & errors to figure out which operating mode suit my needs. I settled for a __Distributed Striped Volume__.

> Distributed striped volumes are very much similar to striped volume, with an added advantage that you can distribute the stripes across more number of bricks on more nodes. In other words, you can distribute data with 4 stripes onto 8 servers.

As a note: I'm doing this with 3 VMs installed with Ubuntu 12.04.3 LTS.

---

#### Step 1

Edit `/etc/hosts` on **all the VMs**.

```
$ sudo vim /etc/hosts
# Add Below
192.168.23.1 bt1 # Node 1
192.168.23.2 bt2 # Node 2
192.168.23.3 bt3 # Node 3
```

Call the nodes whatever you want. Be sure to use the same exact names on all the VMs.

On each VMs, create directories to be distributed.

```
$ sudo mkdir /bt1 # bt1 for Node 1, bt2 for Node 2 and bt3 for Node 3
```

#### Step 2

Let's install `glusterfs-server` on **all the VMs**.

```
$ apt-get install -y glusterfs-server
```

The daemon will automatically be started after each installs.

#### Step 3

After all the VMs are installed, it's time to pick a VM as a leading role. For brevity, I'm using `bt1` or `192.168.23.1` as the leading VM.

```
$ sudo -i
$ gluster peer probe bt2 # Adding Node 2 as peer
$ gluster peer probe bt3 # Adding Node 3 as peer
```

Next up we're going to create a new volume.

```
$ sudo -i
$ gluster create volume bt-vol stripe 3 bt1:/bt1 bt2:/bt2 bt3:/bt3
```

As I said earlier I want to create a Distributed Stripe Volume. I would need to add 3 more peers/shares to expand the volume. 

**Why striping though?**

First reason will be because I tried plain Distributed and it didn't work for some reason. The other reasons below:

* More performance with more clients accessing the same volume
* Little chunks of the same file are distributed on different peers so in my case the throughput triples (network/IO bound per VM) because the chunks are spread into 3 peers
* If any of the peer experiences down time, data integrity is lost. I'm not too concerned because the data there are low value.

#### Step 4

After creating the volume, we would need to start and mount the volume.

```
$ sudo -i
$ gluster volume start bt-vol
$ mkdir -p /media/bt-vol
$ mount.glusterfs bt1:/bt-vol /media/bt-vol
```

There you have it. Check the mount point doing the below commands.

```
$ mount
or
$ df -h
```

---

**What's next?**

For me it's simple. I want a Torrent downloader with a huge and flexible space I can shrink and expand anytime. I opted for `deluge-webui`. That's topic for another blog post.

Another idea is to use the replicating nature of `GlusterFS` and implement a highly available filesystem. This will work wonders for all kinds of use. From a centralized source code repository to CDNs, you can do a lot.