+++
author = "Batista Harahap"
categories = ["bayes", "classifier", "io", "machine learning", "mongodb", "mysql", "naive bayes classifier", "node.js", "php", "redis", "socket", "websocket"]
date = 2012-10-16T11:26:29Z
description = ""
draft = false
slug = "naive-bayes-classifier-revisited"
tags = ["bayes", "classifier", "io", "machine learning", "mongodb", "mysql", "naive bayes classifier", "node.js", "php", "redis", "socket", "websocket"]
title = "Naive Bayes Classifier - Revisited"

+++


During the last week, I've been following up work with a side project to do machine learning with Urbanesia's comprehensive data. A lot of late night reading and fiddling with foreign codes were the highlights of my last week. Wanted to elaborate my implementations and how several kinds of technologies affect benchmarks particularly with classification performance.

The repo for the codes is at Github <a title="Simple Naive Bayes Classifier for PHP" href="https://github.com/tistaharahap/Simple-Naive-Bayes-Classifier-for-PHP" target="_blank">here</a>.

During time span of the first batch of codes until now, I have made lots of changes to the codes and also the data store. I wasn't sure at first, which database will bring the best performance. I'm testing on a fairly low spec hardware which is a Macbook Air Late 2011 with 4 GB DDR3, SSD and Intel Core i5 1.7GHz, this is nothing compared to a real server relatively. By the way, although relatively low spec, she's got a name, it's <strong>Claire</strong>.

My first challenge was to abstract data stores and deal with the algorithm later. To keep things familiar and easy, MySQL was the first store I dealt with. After getting the tables ready, I coded the algorithm with help from <a href="http://bionicspirit.com/pages/about.html" target="_blank">Alexandru Nedelcu</a>'s excellent <a href="http://bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html" target="_blank">Hacker News posting to implement Naive Bayes Classifier in Ruby</a>. The alpha version was produced.

The alpha sucks really bad in terms of performance, it took +1000 seconds to classify a single word. MySQL was expectedly not up for the task. Since the data is actually a collection of words, I was intrigued to use MongoDB as the data store. Since the abstraction layer is already there, I wrote a MongoDB store quite painless and hoping to get better results. The codes were done and the benchmark showed with MongoDB, it only took +400 seconds to classify a single word. Still not good enough, I wasn't prepared to write scheduled backend services which will explode the servers with +50.000 users at least and not to mention the 200.000+ businesses we have, it's gonna be a Sys Admin's nightmare.

Real work was catching up with side projects so I decided to take a break until last week, I managed to get some time to write more codes. So I read along Hacker News to look for the perfect NoSQL database to work with the data we have. I remembered a friend of mine <a href="http://twitter.com/dondyb" target="_blank">Dondy Bappedyanto</a> talking about Redis and how it is a superset of Memcache. So I went straight to <a href="http://redis.io" target="_blank">Redis.io</a> and compiled the source code.

Disclaimer: I knew the algorithm wasn't optimized as I would have liked it to be with the MySQL and MongoDB store, wanted to focus on macro optimizations and do micro optimizations afterwards.

Redis is quite unique because it's <em>"Memcache-like"</em> storing data as key values, the logic changes dramatically and further learning of Redis' data types will help a lot. My aim was to study Redis while doing the project so I opted to do the codes with primitive data types first and optimize along the way. So with a lousy algorithm and a not-so-optimized data model in Redis, I classfied a keyword and it was instant love. It only took ~1 second to do it.

So in my mind, I already got the optimization I wanted on a macro level, it's time to get dirty now. Being my nature of enjoying new stuffs as they come up, I researched other implementations of Naive Bayes Classifier in other languages. I was thinking about implementing a <a href="http://nodejs.org" target="_blank">Node.js</a> + <a href="http://socket.io" target="_blank">Socket.io</a> proxy to do the JavaScript communication with our V2 client side codings and was interested to know more about Node.js.

A quick google introduced me to several Node.js modules to do the job. One that I was particularly interested was <a href="https://github.com/harthur/classifier" target="_blank">Classifier</a> by <a href="http://twitter.com/harthvader" target="_blank">Heather Arhur</a>. I read through the source code and finding some clever methods to speed up things, get all the data first and do the calculations afterwards. But, I was curious about Node.js and wanted to learn to code with it. So I did a more optimized of my previous algorithm in PHP and implemented it in JavaScript. Wanted to know how my codes will perform against the Classifier Node.js module. Both codes were using Redis as the data store.

The quick answer is that both my codes and the Classifier module achieved sub second performance, classifying single keywords in ~300Â milliseconds. This was a great morale boost but the fun only lasted a while. It turns out that sometimes both implementations won't spit out results in medium to large datasets. Being a newbie with Node.js, I didn't know what to do. My guess it's got something to do with memory because the both implementions didn't emit the finish events. Could be a Node.js problem or rather the redis and hiredis node modules.

This makes me code in PHP again. Heavily modified the implementation in PHP to get the data first and calculate later. I was surprised with the result. It took only ~0.01 second to classify a single keyword after the optimization was done. This gives me an idea to do the calculation in PHP and using Node.js + Socket.io as a frontend to JavaScript clients.

Since it was really painless to do WebScoket with Socket.io, it took only a few minutes to produce the Node.js frontend available <a href="https://github.com/tistaharahap/nbc-nodejs-php" target="_blank">here</a>. During a subjective benchmark, it took 68 milliseconds to classify and deliver the result to JavaScript clients. This was a near realtime result and I found my solution.

Last night was full with fiddling around with the algorithm, trying to get the best accuracy from it and during last night and today, the PHP implementation is now at <a href="https://github.com/tistaharahap/Simple-Naive-Bayes-Classifier-for-PHP/tags" target="_blank">version 0.3.0</a>. A coding session this afternoon led to a helper to produce blacklist/stopwords from a collection of text. I couldn't just import the most frequent words to the blacklist collection because it's really subjective depending on languages. Urbanesia's data is a mix of Indonesian and English so it will take more time to analyze. If there's an acceptable automation method, I will share it at the repo.

The conclusion of this project was to think less and do more. Algorithms to do machine learning is available through out the Internet, I mean smart and talented developers before and after us will keep finding new ways to organize data, it's the implementation that counts. Each problems has its own domain and I'm sure my codes will not cater all problems. However, learning by doing is also an excellent experience.

Naive Bayes Classifier is a probability calculation of each keyword being independent to the other keywords classified so it's really suited to mine preferences, related content, etc but in some cases when a group of keyword is actually what we want to know about, Naive Bayes Classifier's accuracy won't be so great. This calls for another solution, if you have any ideas about this, please do comment, would love to know what you think.

Cheers!