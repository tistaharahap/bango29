+++
author = "Batista Harahap"
categories = ["graph", "machine learning", "nlp", "nltk", "textblob", "word graph", "wordgraph"]
date = 2013-08-11T20:36:27Z
description = ""
draft = false
slug = "wordgrapher-build-a-graph-from-words-and-documents"
tags = ["graph", "machine learning", "nlp", "nltk", "textblob", "word graph", "wordgraph"]
title = "WordGrapher - Build A Graph from Words and Documents"

+++


Just recently (last night), <a title="Steven Loria" href="https://twitter.com/sloria1" target="_blank">Steven Loria</a> updated <a title="TextBlob" href="http://textblob.readthedocs.org/" target="_blank">TextBlob</a> to v0.5.0. The module enabled a relatively easy way to do Natural Language Processing in Python. NLTK is a dependency so it's familiar turfs with an easier getting started part. Based on this, I did also did an easy way to parse a set of words and documents to measure important keywords based on <a title="TF-IDF" href="https://en.wikipedia.org/wiki/Tf–idf" target="_blank">TF-IDF</a> algorithm.

A few minutes ago I uploaded the module to PyPi and tagged it as v0.1.0. It's still rough and what it does is just plain TF-IDF for now. The next version will incorporate the said graph building feature.

Basic use will be using it to create an Google-like autocomplete feature when you do a search but that's a topic for another day. For now, I am using it to analyze my own tweets and to favorite other tweets relevant with my own tweets <a href="http://www.bango29.com/go/blog/2013/machine-favorited-tweets-organically-improve-followers-count" target="_blank">automatically</a>.

Head on to <a href="http://tistaharahap.github.io/WordGraph/" target="_blank">http://tistaharahap.github.io/WordGraph/</a> for some action.