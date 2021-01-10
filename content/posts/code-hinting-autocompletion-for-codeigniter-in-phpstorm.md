+++
author = "Batista Harahap"
categories = ["autocompletion", "codeigniter", "phpstorm", "Technology"]
date = 2012-02-06T09:29:12Z
description = ""
draft = false
slug = "code-hinting-autocompletion-for-codeigniter-in-phpstorm"
tags = ["autocompletion", "codeigniter", "phpstorm", "Technology"]
title = "Code Hinting & Autocompletion for CodeIgniter in PHPStorm"

+++


Finally, moving back and forth between models, views and controllers is just too distracting and time consuming. I had to find another way to navigate my way between codes. I tweeted asking about alternative IDEs in Mac OS X to achieve this. Turns out there is a way!

I got a tip from <a href="http://twitter.com/LuisFAlonso" target="_blank">@LuisFAlonso</a> (THANK YOU!) to check out instructions from a blog <a href="http://valid-webs.com/346/code-completion-for-codeigniter-in-phpstorm/" target="_blank">here</a>. I followed the instructions and restarted PHPStorm afterwards. Sadly, it didn't work :(

I did a Google search and was happy to read a blog post <a href="http://www.grafikkaos.co.uk/blog/article/104-getting-autocomplete-for-codeigniter-2.0-with-phpstorm" target="_blank">here</a>. But it didn't work (again). The instructions was to copy paste lines of comments directly to the <code>system/core/Controller.php</code> and <code>system/core/Model.php</code>. The thing is, my system folder is outside the public folder. So I copy pasted the Controller part to <code>application/core/MY_Controller.php</code>. It WORKED!

Now I'm happy with a new IDE and Code hinting + Autocompletion!