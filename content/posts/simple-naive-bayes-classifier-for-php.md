+++
author = "Batista Harahap"
categories = ["bayes", "bayesian", "github", "handlersocket", "mongodb", "mysql", "naive bayes classifier", "naive bayesian classifier", "opensource", "php", "probability"]
date = 2012-02-27T19:00:03Z
description = ""
draft = false
slug = "simple-naive-bayes-classifier-for-php"
tags = ["bayes", "bayesian", "github", "handlersocket", "mongodb", "mysql", "naive bayes classifier", "naive bayesian classifier", "opensource", "php", "probability"]
title = "Simple Naive Bayes Classifier for PHP"

+++


Recently Hacker News is flooded with numerous articles discussing or at least mentioning Naive Bayes Classifier algorithm. It's a basic algorithm to classify a set of words into a certain category (set) based on prior learning of words and its probabilities. It sounds simple enough but without actual technical guide book, it's quite trivial since most of the information out there regarding it is too messy for newbies like myself.

Just today, there was an article by <a href="https://github.com/alexandru" target="_blank">Alexandru Nedelcu</a> about Naive Bayes Classifier <a href="http://bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html" target="_blank">here</a> which is exactly what I am looking for. It's simple, to the point and most importantly outlines the benefit of using the algorithm with practical examples. The codes are in Ruby but I think the article is finely written, you don't have to look at the source code.

So I somewhat forked and ported the idea into PHP and voila, the PHP counterpart is available at <a href="https://github.com/tistaharahap/Simple-Naive-Bayes-Classifier-for-PHP" target="_blank">https://github.com/tistaharahap/Simple-Naive-Bayes-Classifier-for-PHP</a>. It's still very basic, just a prove of concept with MySQL as its persistent storage. The Store is abstracted so you can write your own Store with any database you'd like.

My focus is creating codes that will scale for big documents, and yes MySQL won't be a definite winner here for scalability but I'm using it now to make learning easier. I'm planning on creating a HandlerSocket Store as well as a MongoDB Store.

The codes at the repository for now is not ready for prime time, however, feel free to fork, port or anything you feel right with the codes. Have a great time ;)