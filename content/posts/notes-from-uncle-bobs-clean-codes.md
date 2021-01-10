+++
author = "Batista Harahap"
categories = ["quote", "uncle bob"]
date = 2014-05-15T10:45:27Z
description = ""
draft = false
slug = "notes-from-uncle-bobs-clean-codes"
tags = ["quote", "uncle bob"]
title = "Notes from Uncle Bob's Clean Codes"

+++


I've been reading a book by [Robert C. Martin](http://www.amazon.com/Robert-C.-Martin/e/B000APG87E/) titled [Clean Code: A Handbook of Agile Software Craftsmanship](http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship-ebook/dp/B001GSTOAM). It's a great book talking about writing clean, readable, functional and best practice patterns codes. This book is based on Java but the implementation of any of the concepts is language agnostic.

This blog post serves as important points I extracted from the book. Some will contain codes but some will only be plain English. Here goes.

---

> The only valid measurement of code quality: **WTFs/minute**.

[...] And specifying requirements in such detail that a machine can execute them is programming. Such a specification is *code*.

The total cost of owning a mess is: *zero productivity*.

Most managers want the truth, even when they don’t act like it.

The *only* way to make the deadline—the only way to go fast—is to keep the code as clean as possible at all times.

[...] So too being able to recognize clean code from dirty code does not mean that we know how to write clean code!

Grady Booch:
>*Clean code is simple and direct. Clean code reads like well-written prose. [...]*

Dave Thomas:
>*[...] It provides one way rather than many ways for doing one thing. [...] Code should be literate since depending on the language, not all necessary information can be expressed clearly in code alone.*

Michael Feathers:
>*[...] Clean code always looks like it was written by someone who cares. There is nothing obvious that you can do to make it better. [...]*

Ron Jeffries:
>*[...] Of these, I focus mostly on duplication. When the same thing is done over and over, it’s a sign that there is an idea in our mind that is not well represented in the code. [...]*

Ward Cunningham:
>*[...] You can call it beautiful code when the code also makes it look like the language was made for the problem.*

[...] Of course there’s no way to write code without reading it, so *making it easy to read actually makes it easier to write.*

The Boy Scout Rule:
>*Leave the campground cleaner than you found it.*

---

Choosing names that reveal intent can make it much easier to understand and change code.

Spelling similar concepts similarly is *information*. Using inconsistent spellings is *disinformation*.

If names must be different, then they should also mean something different.

---

`EOF` for First Part.

