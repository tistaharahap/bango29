+++
author = "Batista Harahap"
categories = ["code", "end", "fun", "javascript", "means", "php", "python"]
date = 2013-06-21T06:04:39Z
description = ""
draft = false
slug = "means-to-an-end"
tags = ["code", "end", "fun", "javascript", "means", "php", "python"]
title = "Means To an End"

+++


It has been quite a while since my first Hello World in BASIC and I have since absorbed a few more languages to my liking. Back in college, C and C++ were 2 of the primary languages taught which is fine. But then, there's this junior who asked me: "<em>Why do I have to learn something nobody can see?</em>".

That guy asked a very valid question. For some, crunching codes into you favorite editor with only you and the machine communicating is of the utmost fun but for others, it's not as fun. So with this particular question, one can conclude that either you're gonna code more in backend or frontend is pretty much answered, but that's topic for another day.

There's <a href="https://twitter.com/chazzuka" title="Ariel Komang" target="_blank">this guy</a> I also know, he codes in every language he deemed interesting (which your fingers can't keep count) while also mastering both backend, frontend whether it's native, interpreted or scripted. He is a full stack developer and by stack, I meant stacks. The skills he picked up is not just average, he mastered every single one of them and most of the codes end up in production machines somewhere on the Internet.

Another case is a guy I work with in Urbanesia. He focuses his efforts as a Frontend Developer and his high standards with a unique eye for details come from his insatiable hobby as a photographer. Packed with his knowledge in development, he ventures himself into panoramic photography. You know, that photography technique to create 360x180 degrees stitched images enabling viewers as if they are there. Below is an example of his work, follow him <a href="https://twitter.com/trisrmdh" target="_blank" title="Tris Ramadhan">here</a>.

<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,28,0" height="300" width="640"><param name="movie" value="http://static-10.urbanesia.com/flash/krpano/krpano.swf"><param name="flashvars" value="xml=http://static-10.urbanesia.com/flash/krpano/xml/sentul/sentul.xml"><param name="allowFullScreen" value="true"><embed pluginspage="http://www.macromedia.com/go/getflashplayer" height="300" width="640" allowFullScreen="true" src="http://static-10.urbanesia.com/flash/krpano/krpano.swf" flashvars="xml=http://static-10.urbanesia.com/flash/krpano/xml/sentul/sentul.xml" /></object>

Let's move on to something else.

I have an interesting puzzle quiz. It's simple to be done in less than 5 minutes but also deceptive enough to filter script kiddies.

<code>1 2 * 3 4 5 * 6 7 * 8 9 10 * 11 12 * 13 14 15 * 16 17...1000</code>

The puzzle quiz is to code that specific pattern in various languages. Let's start from the most inefficient way of doing it in PHP.

<script src="https://gist.github.com/tistaharahap/5825378.js"></script>

The codes above will yield a correct pattern. To make it interesting, let's redo the code with the least lines of code possible like below.

<script src="https://gist.github.com/tistaharahap/5825425.js"></script>

There is something else we can do to further optimize this piece of code. Instead of using 2 variables, let's just use 1.

<script src="https://gist.github.com/tistaharahap/5825561.js"></script>

Ok now that we've got the most efficient logic to recreate the pattern, let's try indulging ourselves into various languages. Let's start off with JavaScript.

<script src="https://gist.github.com/tistaharahap/5825597.js"></script>

There's not much difference in the syntax as we compare it with the PHP codes right? Time for some <a href="http://coffeescript.org" target="_blank">CoffeeScript</a> below.

<script src="https://gist.github.com/tistaharahap/5825979.js"></script>

Consider the JavaScript equivalent of the above CoffeeScript code generated from CoffeeScript in-browser compiler:

<script src="https://gist.github.com/tistaharahap/5825996.js"></script>

From the example above, subjectively I feel the CoffeeScript code is more beautiful to comprehend. Its support for <a href="http://coffeescript.org/#loops" target="_blank">Array Comprehension</a> makes the code equivalent to a mathematic expression and the operators available in CoffeeScript is there to be read like reading plain English.

However as you can see the resulting JavaScript codes, it uses more variables and more lines of code. Browsers will have to download more bytes. Since <a href="https://developers.google.com/speed/articles/gzip" target="_blank">GZIP compression for web pages</a> is available in most modern browsers and daemons, sacrificing bytes for clarity I believe will save development time in the future. Again, this is subjectively speaking, your mileage may vary.

Let's venture into another language, Python.

<script src="https://gist.github.com/tistaharahap/5826164.js"></script>

My first impression after doing the codes above is the codes were like New Year's day. It's old and new at the same time. So let's spice it a little bit to adhere with <a href="http://lukasz.langa.pl/8/single-dispatch-generic-functions/" target="_blank">PEP443 - Single Dispatch Generic Functions</a>.

<script src="https://gist.github.com/tistaharahap/5829056.js"></script>

Now the code got more lines, more variables but if you noticed, it's a lot more readable (verbose) and ready to be extended if deemed necessary. So for fun's sake, let's output differently depending on the modulus result.

<script src="https://gist.github.com/tistaharahap/5829123.js"></script>

The backend developer in me is happier with the last codes. It gives me flexibility and verbosity instantly. Python's nature to uphold conventions over configurations is also a different approach to what is out there.

As you can see, implementation varies in various languages and yet all of it do the same thing: To recreate the pattern and output it. 

This brings me to the title of this blog post: Means To an End.

Coding is always the easy part, the hard part is to set your mind on how to code and be ready for changes post coding. We developers live in a world where the word obsolete keeps getting redefined. After all, we are always 1/10th behind of the present. Don't believe me? There's a video for it below.

<iframe width="560" height="315" src="http://www.youtube.com/embed/LaQzYn500E8?rel=0" frameborder="0" allowfullscreen></iframe>