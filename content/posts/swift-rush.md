+++
author = "Batista Harahap"
categories = ["apple", "ios", "programming", "swift"]
date = 2014-06-03T10:23:53Z
description = ""
draft = false
slug = "swift-rush"
tags = ["apple", "ios", "programming", "swift"]
title = "Swift Rush"

+++


Incidentally, yesterday I reconverted myself as an iPhone user once again. Just in time for Apple WWDC. I thought I was gonne be one of those late buyers who'll regret what they just bought when not very long, a "better" phone/hardware introduced. On the contrary, this was my most "on time" purchase of an iPhone ever.

These couple of years, I've limit myself from coding in iOS. I genuinely don't like Objective-C just like I don't like Ruby. My dislike doesn't mean I didn't try to at least a Hello World but each time I do it, it just reaffirms everything I don't like about Objective-C. No bashing is intended but I really think a top platform should have top tools.

Take for example how well Microsoft treated their developer ecosystem by providing them with the best IDE I've tried so far: Visual Studio. I acknowledge that this is subjective but you should try building software with only Make files and a plain text editor. Visual Studio is expensive yes and I'm grateful for Bizspark.

Last night when I was watching the WWDC keynote about Swift, it was like Deja Vu. A few years ago, Microsoft did the same with [WinRT](http://en.wikipedia.org/wiki/Windows_Runtime) and Windows 8. Excerpts from Wikipedia below:

> Windows Runtime, or WinRT, is a platform-homogeneous application architecture on the Windows 8 operating system. WinRT supports development in C++/CX (Component Extensions, a language based on C++) and the managed languages C# and VB.NET, as well as JavaScript and TypeScript. 

> WinRT applications natively support both the x86 and ARM architectures, and also run inside a sandboxed environment to allow for greater security and stability. WinRT components are designed with interoperability between multiple languages and APIs in mind, including native, managed and scripting languages.

When diving in head first with WinRT, I was utterly impressed. It was straightforward and relatively easy to learn and practiced.

---

So what's going on with Apple and its new flagship programming language **Swift**? After asking that question in my head, more questions follow.

1. Smells like Microsoft-esque vendor lock in?
2. Is my resentment towards Objective-C is more on the framework or the language itself?
3. Will coding in Swift save me more lines of codes like it did when I learned Python?
4. If the third is true, will my productivity increases just by learning a language, again like when I learned Python?

To answer the questions, I will need to read more about Swift.

---

Here's what Apple thinks about Swift, taken from [here](https://developer.apple.com/library/prerelease/ios/documentation/swift/conceptual/swift_programming_language/index.html#//apple_ref/doc/uid/TP40014097-CH3-XID_0).

> Swift is a new programming language for iOS and OS X apps that builds on the best of C and Objective-C, without the constraints of C compatibility. Swift adopts safe programming patterns and adds modern features to make programming easier, more flexible, and more fun. 

> Swift’s clean slate, backed by the mature and much-loved Cocoa and Cocoa Touch frameworks, is an opportunity to reimagine how software development works.

Reading through the page, I'm noting below various code snippets I fell in love with instantly.

---

```
let apples = 3
let oranges = 5
let appleSummary = "I have \(apples) apples."
let fruitSummary = "I have \(apples + oranges) pieces of fruit."
```

Say good bye to the `@` literal in strings and say hello to smart String formatting.

---

```
var shoppingList = ["catfish", "water", "tulips", "blue paint"]
shoppingList[1] = "bottle of water"
 
var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
]
occupations["Jayne"] = "Public Relations"
```

Will need to get used using brackets `[]` for dictionaries.

---

```
let emptyDictionary = Dictionary<String, Float>()
```

You see Java? No it's Swift.

---

```
var optionalString: String? = "Hello"
optionalString == nil
```

You see Ruby or Coffeescript? No it's Swift.

---

```
let vegetable = "red pepper"
switch vegetable {
	case "celery":
    	let vegetableComment = "Add some raisins and make ants on a log."
	case "cucumber", "watercress":
    	let vegetableComment = "That would make a good tea sandwich."
  case let x where x.hasSuffix("pepper"):
      let vegetableComment = "Is it a spicy \(x)?"
  default:
      let vegetableComment = "Everything tastes good in soup."
}
```

Elegance.

---

```
let interestingNumbers = [
    "Prime": [2, 3, 5, 7, 11, 13],
    "Fibonacci": [1, 1, 2, 3, 5, 8],
    "Square": [1, 4, 9, 16, 25],
]
var largest = 0
for (kind, numbers) in interestingNumbers {
    for number in numbers {
        if number > largest {
            largest = number
        }
    }
}
largest
```

You see Python? No it's Swift.

---

You are welcomed to take a look at the online documentation or download the ebook to taste more Swift.

After some more thinking, I'm prepared to answer the questions.

1. Yes.
2. The language.
3. Yes.
4. Yes.

### Vendor Lock In

Apple is innovating by copying yet again. I'm not saying this is bad, look at what they did before with Xerox and look at how they are right now. Hell, take a look at your iOS 7. They say imitation is the highest form of flattery but I argue that this ain't flattery at all.

Over the course of Apple's remarkable history, Apple innovates by making better and great products with emphasis on UX and quality. The rest of the gang ended up mimicking what Apple innovated over and over. They invent things and profit.

What's that gotta do with Vendor Lock in? Here are some more excerpts about the new tech Apple is showcasing last night.

#### [Home Kit Framework](https://developer.apple.com/library/prerelease/ios/documentation/HomeKit/Reference/HomeKit_Framework/index.html)

> Home Kit provides seamless integration between accessories that support Apple's Home Automation Protocol and iOS devices, allowing for new advances in home automation. By promoting a common protocol for home automation devices and making a public API available for configuring and communicating with those devices, Home Kit makes possible a marketplace where the app a user controls their home with doesn’t have to be created by the vendor who made their home automation accessories, and where home automation accessories from multiple vendors can all be integrated into a single coherent whole without those vendors having to coordinate directly with each other.

Me as an engineer loves the Homekit idea. I fell in love with mobile phones first but true love is with embedded systems. There are so many ARM development boards available as a platform of innovation. However, they lack standards. What Apple is offering is just stupid to say no to.

Airplay is what I consider a prequel of Home Kit. It just **works**.

#### [Carplay](http://www.apple.com/ios/carplay/)

> [...] Just plug in your iPhone and go.

You see? Again it just works. 

#### Locked In

You don't have to be a rocket scientist to `*play`. Apply this to their development community and voila. A relatively easy way of bulding products with the high standards Apple is famous for.

### The Language

I don't like Objective-C, C, C++ or anything like the trio. Period.

### Swift is (not) Python

Swift is Swift of course. The expressive nature of Swift is what attracts me. 

I've always thought that programming language is just another language. It's a [means to an end](http://bango29.com/means-to-an-end/). But, the art of any language is the poetries. By being expressive I believe best practices, clean codes and design patterns are implemented as the highest importance.

---

So, Swift reinvigorates my interest towards iOS and Apple in general. Here's something from Ice House HQ to further interest you in Swift.

![Swift Craze](/content/images/2014/Jun/2x.jpg)