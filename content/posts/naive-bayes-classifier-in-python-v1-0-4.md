+++
author = "Batista Harahap"
categories = ["bayes", "cython", "Open Source", "pypi", "python", "redis"]
date = 2013-06-07T07:42:14Z
description = ""
draft = false
slug = "naive-bayes-classifier-in-python-v1-0-4"
tags = ["bayes", "cython", "Open Source", "pypi", "python", "redis"]
title = "Naive Bayes Classifier in Python v1.0.4"

+++


Just finished work on a Naive Bayes Classifier in Python. Was interested to benchmark Python performance with large data sets. Also had the chance to get to know more about <a href="http://cython.org/" target="_blank">Cython</a>. Indeed as a C extension, it increased performance.

So this project all started from my own implementation in PHP <a href="https://github.com/tistaharahap/Simple-Naive-Bayes-Classifier-for-PHP" target="_blank">here</a>. As it turns out, PHP is more performant than Python as of <a href="https://github.com/tistaharahap/python-bayes-redis/tree/v1.0.4" target="_blank">version 1.0.4</a> of this library. But there are differences.

The Python module redis available at PyPi is not compiled as a C extension while the PHP counterpart is definitely a C extension. So the bottleneck here I suspect is with the Redis client. Expect some more enhancements to the Redis clients in future versions.

So long story short, why not give it a go atÂ <a href="https://github.com/tistaharahap/python-bayes-redis" target="_blank">https://github.com/tistaharahap/python-bayes-redis</a>. Would love for feedbacks on how to further optimize the codes. Still very fresh with Python at the moment.