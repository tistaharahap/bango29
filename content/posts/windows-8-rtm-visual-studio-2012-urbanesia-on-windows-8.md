+++
author = "Batista Harahap"
categories = ["microsoft", "rtm", "urbanesia", "visual studio", "visual studio 2012", "windows", "windows 8"]
date = 2012-10-07T19:40:36Z
description = ""
draft = false
slug = "windows-8-rtm-visual-studio-2012-urbanesia-on-windows-8"
tags = ["microsoft", "rtm", "urbanesia", "visual studio", "visual studio 2012", "windows", "windows 8"]
title = "Windows 8 RTM & Visual Studio 2012 - Urbanesia on Windows 8"

+++


My first experience with Hello Worlds was through an old 8088XT that shows up a primitive BASIC IDE to hack on codes. Well now with the Urbanesia team and also past members of the team, we've created a native Windows 8 app for Urbanesia. We were in it from the start when Windows 8 was seeded as a Developer Preview. Our first IDE was Visual Studio 11 Beta that is now Visual Studio 2012.

Urbanesia is a BizSpark member and therefore, we gained benefits such as being the first to enjoy Microsoft products that has yet been released publicly. Our MSDN account enables us to download almost all of Microsoft's commercial, development and enterprise products to be used without any complicated and expensive expenses for 3 years. I downloaded Windows 8 Pro and Visual Studio 2012 Ultimate.

<a href="http://www.bango29.com/go/blog/2012/microsoft-windows-8-bootcamp-bandung" target="_blank">Our Windows 8 Bootcamp</a> back in August taught us the core of coding for Windows 8. It's relatively easy and stress free if you're accustomed to Open Source flavours previously. We created a basic application in a few hours and learned how to effectively structure your web services data. Gained all of that knowledge really quick and mostly painless.

Windows 8 is now approaching its launch date and we were given an ARM tablet by Microsoft installed with WinRT to test our development efforts. To be honest, the tablet is great but we didn't know what to do with it. We used it mostly to test our upcoming iteration of Urbanesia's frontend web face. I got a Windows laptop with a really low spec and decided to install Windows 8 there and do some development work for our app.

Let me tell you this, to develop for Windows 8, you must install Visual Studio 2012 on a Windows 8 device. Trying to develop for Windows 8 on versions less than Windows 8 will give you a friendly warning that you're fucked. This friendly warning made me download a Windows 8 ISO image from Microsoft. It turns out that our MSDN subscription was loaded with Windows 8 RTM and I followed through.

I installed Windows 8 on that crappy Windows laptop without any trouble and finding the performance of the laptop acceptable when I logged in. It wasn't the same case with the Windows 7 installation. Microsoft did a great job with their new OS, really.

When Visual Studio 2012 was installed, I wasn't expecting any trouble with our source code, but nothing great is produced without first encountering problems right? To keep it simple, the application didn't work at all. Spent the better part of my Sunday to scour Google for answers. Before the Manchester United game (that they won), I can't find what's not working.

FYI, we are coding in C# for our Windows 8 application.

After the game, I was gonna give up but then inspiration usually comes when you're about to give up. I hacked my way again into the source code and below is a list of gotchas you should pay attention when you're gonna convert older Visual Studio 11 Beta projects to a Visual Studio 12 project:
<ul>
	<li>After you realize that you're fucked, close the solution for the project you're working and create another project.</li>
	<li>Close that new project you've just created and open up the primary project.</li>
	<li>Copy paste your Common\StandardStyles.xaml file somewhere.</li>
	<li>Open up explorer and navigate your way to the new project.</li>
	<li>Go to the Common folder and copy paste everything to your primary project's Common folder.</li>
	<li>Now open up the newly pasted Common\StandardStyles.xaml and copy paste all of your previously created custom DataTemplate from your old copy.</li>
	<li>Go to <a href="http://blogs.microsoft.co.il/blogs/shair/about.aspx" target="_blank">Shair Raiten's</a> excellent guide to upgrade Metro apps from Beta to RC <a href="http://blogs.microsoft.co.il/blogs/shair/archive/2012/06/03/upgrade-metro-app-from-beta-to-rc.aspx" target="_blank">here</a>.</li>
	<li>As you can see, there are a number of changes to naming conventions for classes, XAML styles and static class methods. For each XAML style items, do a Find/Replace, yes it sucks but it works. The same goes to classes and static class methods if you use any in your codes.</li>
	<li>Clean your solution and be hopeful. Run it now.</li>
</ul>
So what does this taught me? Microsoft is getting it right over time but they don't really like early adopters. They make us bleed with the current <strong>BREAKING</strong> changes with Visual Studio 2012 and offering us only white papers that I don't like to read. This is done with even the Microsoft Indonesia dev team is not aware of. A sad fact but it's true.

However, I got help from Pak Risman, Microsoft Indonesia's Developer &amp; Platform Director. He taught me the right way to do things with codes, this is something I'd understand.

To wrap things up, I'll be submitting the app to Windows Store soon and hopefully satisfy the QA team over at Microsoft. Cheers!