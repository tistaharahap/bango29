+++
author = "Batista Harahap"
categories = ["automated", "favorite", "machine learning", "nlp", "nltk", "organic", "python", "tweet", "twitter"]
date = 2013-08-03T10:35:05Z
description = ""
draft = false
slug = "machine-favorited-tweets-organically-improve-followers-count"
tags = ["automated", "favorite", "machine learning", "nlp", "nltk", "organic", "python", "tweet", "twitter"]
title = "Machine Favorited Tweets - Organically Improve Followers Count"

+++


Last night, I read about <a href="http://blog.jmoz.co.uk/increase-your-twitter-followers/" target="_blank">James Moriss' blog post</a> on how to gain more followers by favoriting other tweets relevant to your own tweets or some other keywords you are interested in. The downside was, you still have to input the keywords yourself. So I hacked up some codes let the codes figure out what keywords are proper. My first try into <a href="http://nltk.org" target="_blank">Python's NLTK</a>.

<strong>WARNING:</strong> The codes below are not production ready codes. These are only proof of concepts and therefore should not be used in production environments without proper knowledge.

So now the warning is out of the way, let's hack some codes. Here is the the original code from James Morrison.

<script src="https://gist.github.com/jmoz/6135716.js"></script>

As you can see, the codes are pretty much the building blocks of what I'm trying to achieve. I made my own modifications to produce the codes below.

<script src="https://gist.github.com/tistaharahap/6145960.js"></script>

Since I want to the codes to scan my own tweets, the <code>my_tweets()</code> function was introduced. I also introduced 2 regex patterns to filter URLs and @screen_name as a variable, hence <code>twitter_namespace</code>.

The next step was to figure out what to do with my last tweets. Over the years, I have grown in favor of <code>TF-IDF</code> to filter out keywords against its own document set and also against a larger part collection of documents. Using this analysis, 5 of Urbanesia's articles are always on out Top 10 traffic by pageviews. You can read more about the topic <a href="https://en.wikipedia.org/wiki/Tf%E2%80%93idf" target="_blank">here</a>.

Sadly, Python's NLTK does not have a TF-IDF module. It's not too difficult to implement but a quick search brings me to <a href="https://gist.github.com/AloneRoad/1605037" target="_blank">this Github Gist</a>. It was almost all that I needed except that I don't want to do Keywords VS Doc VS Docs comparison, I just want important keywords either singles, bigrams and up until trigrams. So the codes need some refactoring which results to codes below.

<script src="https://gist.github.com/tistaharahap/6145996.js"></script>

For the codes to run, you need to install NLTK's Stopwords module. Here's how:
<pre lang="bash">
$ python
>> nltk.download()
</pre>

It will show up either in the terminal or a GUI if you're on a GUI environment. Since I also tweet in Bahasa Indonesia, so also need stopwords for it. I got from <a href="https://github.com/pebbie/pebahasa" target="_blank">Pebahasa Github repo</a>. Put the gist below into your <code>~/nltk_data/corpora/stopwords/indonesian</code>

<script src="https://gist.github.com/tistaharahap/6146013.js"></script>

Now after you're done with that, we're stitch the whole thing. Before continuing, let me remind you that I want to create a self sufficient Twitter favoriter which will favorite tweets of others which are relevant to things that I tweet about everyday. So here goes.

<script src="https://gist.github.com/tistaharahap/6146029.js"></script>

The code will run forever so I suggest you use some daemonizing magic like <a href="http://supervisord.org/" target="_blank">Supervisor</a> to manage the process.

As you can see, you can always do some altercations with the interval. I've set it to one hour so it won't take to long for my tweets to be processed the codes and yet it won't put a shitload of requests to Twitter.

May I remind you that this is a for fun codes. Use the codes responsibly, nobody likes spam. That being said, would like to know how your mileage ran with the codes.