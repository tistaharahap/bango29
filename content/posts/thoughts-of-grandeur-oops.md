+++
author = "Batista Harahap"
categories = ["betanesia", "friday", "grandeur", "morning glory", "urbanesia"]
date = 2010-10-29T01:01:05Z
description = ""
draft = false
slug = "thoughts-of-grandeur-oops"
tags = ["betanesia", "friday", "grandeur", "morning glory", "urbanesia"]
title = "Thoughts of Grandeur - OOPS"

+++


Okay the title is a WTF right? To be honest, this blog post is inspired by one of the earliest episode of Heroes when Nathan and his Mom told Peter that he is having illusions of grandeur. Evidently, Peter became one of the most talented and gifted mutant of them all, he figured out how to gain any power he wants without killing the subject unlike Sylar lol.

Well subjectively I must say that thinking BIG is a blessing. It gives you vision and therefore a purpose in whatever you are trying to achieve in the future. The right sense of purpose can bring you anywhere you want to be at any point in your lives. Everyone's is welcomed to debate this point anytime :)

Now to put into perspective, building and maintaining Urbanesia almost from scratch is a BIG thing. Grandeur is a requirement for everyone involved and may I say subjectively (again), the kind of thought that our Web Developer team must have. Because of the nature of Urbanesia, it is important for each one of us developers to have a firm grasp of the bigger picture. Some things are just NOT a bargain.

This is why I imposed a new policy which is also one of the principle I withhold: <strong>LESS IS MORE</strong>! As developers, we all know our biggest enemy, it's that thirst for doing everything efficiently. The strength of a developer and also the weakest of any. I don't know, maybe because efficiency is interpreted differently with different developers. For me efficiency means less load and to achieve that, the codebase should be as slim as possible.

We achieved a big performance gain with our new v1.0 by streamlining the MY_Controller part of our Codeigniter Framework to less than 800 lines of codes. We love Object Oriented Programming (OOP) but we hate overusing OOP to a point where it should be abbreviated as <em>OOPS</em>.

For most of mid to advanced developer, OOP is a comfort zone and as with any comfort zone, it's NOT good in the long run. Now why do I say such a <strong>BOLD</strong> statement? Because instantiating a class takes a lot of memory and CPU cycles! Codeigniter itself is a giant in disguise, it basically wraps all the MVC into one big object. This is a liability and surely you will notice heavy memory usage.

Now how do Urbanesia solve this dilemma? As I said before, Less is More and therefore make everything as simple as possible. From hundreds of controllers, we slimmed down to only 33 controllers. Why do we optimized the controllers first? That's the million dollar question. Simple, it's where all the logic happens, it's where CPU cycles are heavy and most importantly by slimming down to just 33 controllers, we saved significant amount of overheads by NOT instantiating too many classes.

How about the Views you asked? Well we love views but we also hate views. Views are always generated dynamically and therefore, it's NOT the most efficient way to display contents. Views also contains iterations and loops to display data. This is a resource hogger too. So what should we do? A lot!

First of all, cache it! Yes we love cache, without cache, Urbanesia won't be as fast as it is right now. Disk cache is of great importance. We are building static HTML files of every dynamically generated content of Urbanesia. Now you ask why we do this when we have Memcached? Because I'd rather have Disk I/O rather than CPU Cycles. Our servers are already using the fastest SAS Harddrives available, why not make us of it to the max!

Another gem is HTML5. After Google DevFest earlier this month, the team was inspired to built an SVN like mechanism in JavaScript for visitors to fetch increments instead of the whole website. This will be a significant boost towards productivity load-wise. By only serving increments, we are projecting of cutting down more than 30-40% of the entire load. Non-HTML5 browsers are already accounted.

O yea by the way, our team of Superhero Geeks are named Betanesia, follow us <a href="http://twitter.com/Betanesia" target="_blank">@Betanesia</a>. We are always in Beta that's for sure. Prepping for the next innovation and optimization for Urbanesia. Just recently, we rolled out Panoramic View into Urbanesia. You can view it <a href="http://www.urbanesia.com/profile/taman-mini-indonesia-indah" target="_blank">here</a>.

It is amazing that in the last 3 months, Urbanesia have produced tons of achievements in terms of codes, marketing activities and overall productivity. It's back to this blog post's title: Thoughts of Grandeur. Each one of us has a purpose in life, a bigger one I might add and why not experience and achieve it together? Just by supporting as a direct effort to <strong>EMPOWER</strong> others, just try it, I keep getting amazed by it :p

Well it's 7:57 AM right now and I'm thirsty for more action, I'm gonna start my Friday with a #FF on Twitter. Thanks for reading, I'm leaving you with a quote.
<blockquote><em>You're <span style="text-decoration: underline;">GREAT</span>! Get used to it!</em></blockquote>