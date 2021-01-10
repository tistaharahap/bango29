+++
author = "Batista Harahap"
categories = ["cubieboard", "classifier", "performance", "python", "redis", "server", "benchmark", "digital ocean", "cluster", "low end"]
date = 2014-01-16T12:35:36Z
description = ""
draft = false
slug = "squeezing-cubieboard-for-performance"
tags = ["cubieboard", "classifier", "performance", "python", "redis", "server", "benchmark", "digital ocean", "cluster", "low end"]
title = "Squeezing Cubieboard for Performance"

+++


For the past month, I've been pleasantly hacking my Cubieboard to try out several different things. This time, I wanna know how performant Cubieboard is. Benchmarks are configured in such a way to replicate a real Web Application.

## Preparing

Here are the specs for my Cubieboard:

- AllWinner A10 ARM Single Core CPU
- 1 GB DDR3 @ 480 MHz
- 5V / 2A = 10 Watts
- SATA HD - 5400 RPM
- Cubian r7 - [http://cubian.org](http://cubian.org)
- 2 GB Swapfile (SATA HD)
- US$ 49

I've written a tutorial on how to install Cubian to a SATA HD [here](http://bango29.com/cubieboard-part-3-sata-install-with-cubian/). The main reason why I'm doing a SATA HD Install for this is to preserve my micro-SD's lifetime. We're gonna be compiling and doing I/O intensive tasks so it's best to delegate off the micro-SD card.

Other than preserving the micro-SD, these cheap ARM boards have limited I/O performances so a SATA 5400 RPM HD might be better but ultimately an SSD should be used because it's pitted against SSD opponents. I don't have a spare SSD so this will have to do.

### Benchmarking

The Cubieboard is pitted against my Macbook Pro and [Digital Ocean's](https://www.digitalocean.com/?refcode=2bac813f3a2d) lowest spec VM.

A Macbook Pro will reflect how the Cubieboard perform compared with a typical development machine while the Digital Ocean VM is a real world server.

**DISCLAIMER**: This is not an apple to apple comparison, please keep in mind that between the 3 systems there are gaps in specs. The benchmarks served here are good only for references.

#### Macbook Pro

- Early 2011
- Dual Core i5 @ 2.3 GHz
- 8 GB DDR3 @ 1333 MHz
- SSD HD
- OS X Mavericks 10.9.1
- US$ 1199

#### Digital Ocean

- Single Core
- 512 MB Memory
- SSD HD
- Ubuntu 12.04 LTS
- 2 GB Swapfile
- US$ 5/month

### Compiler

We need to install a build system so that the Cubieboard will be able to do the benchmarks.

<pre>
$ sudo -i
$ apt-get install -y build-essential git gcc-arm-linux-gnueabihf python-dev
</pre>

## Redis

Surprisingly the Cubieboard compiled [Redis](http://redis.io) successfully! I wasn't hoping much for this piece of hardware but then it's not just a toy, it's a full blown computer with a very small form factor.

### Compile, Configure & Install

For this blog post, I'm compiling Redis 2.8.4. Let's go ahead.

<pre>
$ wget http://download.redis.io/releases/redis-2.8.4.tar.gz
$ tar xfz redis-2.8.4.tar.gz
$ cd redis-2.8.4
$ make
$ mkdir -p /usr/local/redis/bin
$ mkdir -p /usr/local/redis/conf
$ cp src/redis-{benchmark,check-aof,check-dump,cli,sentinel,server} /usr/local/redis/bin
$ cp redis.conf /usr/local/redis/conf
$ ln -s /usr/local/redis/bin/redis-{benchmark,check-aof,check-dump,cli,sentinel,server} /usr/local/bin/
$ ln -s /usr/local/redis/conf/redis.conf /etc/redis.conf
</pre>

Now that it's compiled and installed appropriately, let's go ahead and change some configurations to our needs.

<pre>
$ vim /etc/redis.conf
</pre>

Use/modify the file reflecting the below values and leave the rest on their default values.

<pre>
daemonize yes
bind 127.0.0.1
</pre>

Now let's start the server.

<pre>
$ redis-server /etc/redis.conf
</pre>

### redis-benchmark

`redis-benchmark` comes with the Redis we will compile. It will basically benchmark throughputs for various Redis commands. The ones that I'm particularly interested are `GET`, `SET` and `INCR`. Those 3 are the commands I would normally used within a web application.

For this benchmark, I'm gonna test using 1, 2, 3, 4, 8 and 20 concurrent connections. The results are CSVs.

<pre>
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 1 > reds-bench-1.csv
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 2 > reds-bench-2.csv
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 3 > reds-bench-3.csv
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 4 > reds-bench-4.csv
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 8 > reds-bench-8.csv
$ redis-benchmark -h 127.0.0.1 -p 6379 -n 1000 --csv -c 20 > reds-bench-20.csv
</pre>

#### Results

##### Cubieboard

The higher the better.

![Cubieboard Results](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Cubieboard&chd=s:svxz44,twx595,svxyzx&chco=00ff00,0000ff,ff0000&chdl=SET|GET|INCR&chxl=0:|c1|c2|c3|c4|c8|c20|1:|8196.72%20rps|&chxt=x,t,r)

[Full Results CSV &raquo;](https://gist.github.com/tistaharahap/8446289)

##### Macbook Pro

The higher the better.

![Macbook Pro Results](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Macbook%20Pro&chd=s:QYgr66,QWky49,QWdu69&chco=00ff00,0000ff,ff0000&chdl=SET|GET|INCR&chxl=0:|c1|c2|c3|c4|c8|c20|1:|45454.55%20rps|&chxt=x,t)

[Full Results CSV &raquo;](https://gist.github.com/tistaharahap/8446340)

##### Digital Ocean

The higher the better.

![Digital Ocean Results](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Digital%20Ocean&chd=s:gqsz41,fqvu90,jmr03z&chco=00ff00,0000ff,ff0000&chdl=SET|GET|INCR&chxl=0:|c1|c2|c3|c4|c5|c6|1:|28571.43%20rps|&chxt=x,t)

Full Results CSV - Pending Upload

#### Conclusion

This benchmark stresses the raw CPU power of the device and its memory bandwidth. 

The Cubieboard is obviously the under achiever which is expected. However, with a very low power usage, I believe ARM processors do have a market for low end servers.

The worst performer here I think is Digital Ocean. It is performing at around 60% of my Macbook Pro's performance and only roughly 3 times as fast as my Cubieboard.

### BayesRedis

This is a small Python library I developed to train and classify sets of text. It is available on Github [here](https://github.com/tistaharahap/python-bayes-redis). Installation for Cubieboard is a bit tricky because Cubian doesn't come with `pip` by default. We will have to install it manually.

#### Installation

For your Cubieboard follow the steps below, other platforms may skip should you have `pip` already installed.

<pre>
$ cd /usr/local/src
$ wget https://pypi.python.org/packages/source/s/setuptools/setuptools-2.1.tar.gz#md5=2044725530450d0517393882dc4b7508
$ tar xfz setuptools-2.1.tar.gz
$ cd setuptools-2.1
$ python setup.py install
$ cd ..
$ wget https://pypi.python.org/packages/source/p/pip/pip-1.5.tar.gz#md5=6969b8a8adc4c7f7c5eb1707118f0686
$ tar xfz pip-1.5.tar.gz
$ cd pip-1.5
$ python setup.py install
</pre>

BayesRedis is written in Python but upon installation it will be compiled natively. Here are the steps.

<pre>
$ pip install redis hiredis bayesredis
</pre>

If you take a look at the Github repo, there's a `test.py` file at the root directory. I've made a Github Gist of the file so let's go ahead and customize it to our needs.

<pre>
$ wget https://gist.github.com/tistaharahap/8446592/raw/ac7350b7e7e17c07c7beff89affd7c3766633077/test.py
$ vim test.py
</pre>

As you can see, the training examples are all commented out, for our first run we must uncomment them by removing the triple single quotes `'''` before and after the examples.

#### Benchmarking

Now let's run the benchmark.

<pre>
$ redis-cli flushdb # This will truncate all your Redis data, use with care
$ python test.py
</pre>

#### Results

The lower the better.

![BayesRedis Results](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Cubieboard&chd=s:jouz49,LNOQRS,JKKLMN&chco=00ff00,0000ff,ff0000&chdl=Cubieboard|Macbook%20Pro|Digital%20Ocean&chxl=0:|k1|k2|k3|k4|k5|k6|1:|0.00379%20second|2:|Keywords|&chxt=x,t,r)

If we see the chart above, Cubieboard is definitely miles apart. This particular benchmark stresses the memory bandwidth of the system. A wider memory bandwidth is key to this benchmark success.

This kind of benchmark is actually computed by servers everyday around the world. It's synthetic but it can explain how the real world would exploit the hardware beneath. 

A more familiar implementation example would be recommending you items to purchase by analyzing your purchase history.

As you can see, the Cubieboard is not ready for real world use by seeing the result of this benchmark. The Cubieboard is practically limited by its memory bandwidth.

## nginx - Static Files

[`nginx`](http://nginx.org) is on the rise right now. It's steadily dominating web servers around the world. The most obvious reason why nginx is so successful in simply because it's lightning fast.

Just by reverse proxying traffic with nginx in front, I have seen at least 30% performance increase. The nature of handling requests asynchronously with a very lightweight memory footprint makes nginx the de facto choice for performance hungry websites.

### Compile, Configure & Run

For this benchmark we only want to test synthetic raw performances. There are many factors in the real world that will influence a web server's perceived speed with network latency as the usual suspect.

Benchmarks will be executed from another machine on the same network.

#### Compile

Our `nginx` installation is gonna be located at `/usr/local/nginx`. The only dependency we're gonna need is `libpcre3-dev`.

<pre>
$ cd /usr/local/src
$ wget http://nginx.org/download/nginx-1.4.4.tar.gz
$ tar xfz nginx-1.4.4.tar.gz
$ cd nginx-1.4.4
$ apt-get install -y libpcre3 libpcre3-dev
$ ./configure --prefix=/usr/local/nginx
$ make && make install
</pre>

#### Configure & Run

We're gonna benchmark using only the default parameters of `nginx.conf`. As an addition, I want to benchmark image serving.

<pre>
$ /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
$ cd /usr/local/nginx/html
$ wget http://nginx.org/nginx.gif
</pre>

Check if `nginx` is running by opening up a web browser and type in the IP of your Cubieboard.

### Benchmark

This benchmark will be executed by 2 application which are:

- [`ab`](http://httpd.apache.org/docs/2.2/programs/ab.html) - Apache's benchmarking tool
- [`wrk`](https://github.com/wg/wrk) - A rather modern evolution of HTTP benchmarking

#### HTML

<pre>
$ ab -n 10000 -c 10 http://192.168.1.134/
$ ab -n 10000 -c 100 http://192.168.1.134/
$ ab -n 10000 -c 250 http://192.168.1.134/
$ ab -n 10000 -c 500 http://192.168.1.134/
$ ab -n 10000 -c 1000 http://192.168.1.134/
$ wrk -r 10000 -t 1 -c 10 http://192.168.1.134/
$ wrk -r 10000 -t 1 -c 100 http://192.168.1.134/
$ wrk -r 10000 -t 1 -c 250 http://192.168.1.134/
$ wrk -r 10000 -t 1 -c 500 http://192.168.1.134/
$ wrk -r 10000 -t 1 -c 1000 http://192.168.1.134/
</pre>

##### Results

The higher the better.

![Cubieboard HTML Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Cubieboard%20HTML&chd=s:YomcM,AAAAT,wvz92,AAAFP&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|2639.39%20rps|&chxt=x,t)

The higher the better.

![Macbook Pro HTML Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Macbook%20Pro%20HTML&chd=s:EGCCA,AAAmm,89655,AAABD&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|15981.36%20rps|&chxt=x,t)

The higher the better.

![Digital Ocean HTML Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Digital%20Ocean%20HTML&chd=s:cfbXa,AAAAG,3942z,AAAAA&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|8347.89%20rps|&chxt=x,t)

#### Image

<pre>
$ ab -n 10000 -c 10 http://192.168.1.134/nginx.gif
$ ab -n 10000 -c 100 http://192.168.1.134/nginx.gif
$ ab -n 10000 -c 250 http://192.168.1.134/nginx.gif
$ ab -n 10000 -c 500 http://192.168.1.134/nginx.gif
$ ab -n 10000 -c 1000 http://192.168.1.134/nginx.gif
$ wrk -r 10000 -t 1 -c 10 http://192.168.1.134/nginx.gif
$ wrk -r 10000 -t 1 -c 100 http://192.168.1.134/nginx.gif
$ wrk -r 10000 -t 1 -c 250 http://192.168.1.134/nginx.gif
$ wrk -r 10000 -t 1 -c 500 http://192.168.1.134/nginx.gif
$ wrk -r 10000 -t 1 -c 1000 http://192.168.1.134/nginx.gif
</pre>

##### Results

The higher the better.

![Cubieboard Image Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Cubieboard%20Image&chd=s:PbacO,AAAAA,o9877,AAAEM&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|3907.59%20rps|&chxt=x,t)

The higher the better.

![Macbook Pro Image Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Macbook%20Pro%20Image&chd=s:EIGBA,AAjjj,54595,AAABD&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|17491.20%20rps|&chxt=x,t)

The higher the better.

![Digital Ocean Image Result](http://chart.apis.google.com/chart?chs=700x300&cht=bvg&chtt=Digital%20Ocean%20Image&chd=s:aecfU,AAAAH,15996,AAAAA&chco=00ff00,ff0000,0000ff,ff00ff&chdl=ab|ab%20err|wrk|wrk%20err&chxl=0:|c10|c100|c250|c500|c1000|1:|7876.61%20rps|&chxt=x,t)

### Cubieboard as a Web Server

The results are in and Cubieboard proved a resilient piece of hardware. It is outperformed in every tests by its opponents but surprisingly when compared with my Macbook Pro, the Cubieboard is proving to be a reliable machine with fewer HTTP response errors.

OS tuning is a factor why my Macbook Pro is spitting out lots of HTTP response errors. I tested as is without any OS tuning to my Macbook Pro and the other opponents. 

On this benchmark my Macbook Pro is giving the highest throughput against the other opponents up until 250 concurrent connections when HTTP response errors are building up.

The Digital Ocean server stood very well only spitting out HTTPS response errors at 1000 concurrent connections. It's definitely a web server.

## Conclusion

The Cubieboard is great at handling CPU intensive tasks. Not so great when memory is vital to performance. I can see myself rigging a cluster of Cubieboards to do data science. And do it cheap with only 10 watts of power usage and US$ 49 price tag per board.

A typical unbranded server here in Indonesia can cost upwards of US$ 1000 per server which amounts to 20 Cubieboards. When adding up the electricity costs of let's say a 450 Watts PSU, monthly usages is more cost efficient with a Cubieboard cluster.

To be fair, a Cubieboard configured as a server would at least cost US$ 49 + US$ 50 for a SATA HD - 5400 RPM. If SSD is an option, it could wind up to US$ 165 for a 64GB SSD totalling to US$ 224 per rig.

All and all, I am pleased with the benchmark results for my Cubieboard and in the future, I believe an ARM board such as the Cubieboard is performant enough and cost efficient to be a cluster of data science computing.

<script type="text/javascript">
var amzn_assoc_placement = "adunit0";
var amzn_assoc_search_bar = "true";
var amzn_assoc_tracking_id = "bango29-20";
var amzn_assoc_ad_mode = "manual";
var amzn_assoc_ad_type = "smart";
var amzn_assoc_marketplace = "amazon";
var amzn_assoc_region = "US";
var amzn_assoc_title = "Buy Now";
var amzn_assoc_linkid = "37ddc99aabea4f2a5b575620b01a230c";
var amzn_assoc_asins = "B00JUG7R60,B00ISKS416,B00KCS8ZUC,B010Q57T02";
</script>
<script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>