+++
author = "Batista Harahap"
categories = ["form", "http", "ios", "iphone", "objective c", "post", "url encode", "urlencode"]
date = 2011-08-16T00:43:28Z
description = ""
draft = false
slug = "urlencode-with-objective-c-the-oauth-way"
tags = ["form", "http", "ios", "iphone", "objective c", "post", "url encode", "urlencode"]
title = "URLEncode With Objective C - The OAUTH Way"

+++


Coming from a PHP background, we should all be thankful to rawurlencode() from PHP! Here's an Objective C version with OAUTH v1.0a requirements.

<pre lang="objc" line="1">
- (NSString *)urlencode:(NSString *)text {
    NSString *temp = @"";

    for(int i=0, max=[text length]; i<max; i++) {
        char t = [text characterAtIndex:i];
        int b = (int) t;
        
        if(
           t == (char) '.' ||
           t == (char) '_' ||
           t == (char) '-' ||
           t == (char) '~' ||
           t == (char) '#' ||
           (b>=0x30 && b<=0x39) ||
           (b>=0x41 && b<=0x5A) ||
           (b>=0x61 && b<=0x7A)
            ) {
            temp = [temp stringByAppendingFormat:@"%c", t];
        } else {
            temp = [temp stringByAppendingString:@"%"];
            if (b <= 0xf) temp = [temp stringByAppendingString:@"0"];
            temp = [NSString stringWithFormat:@"%@%X", temp, b];
        }
    }
    
    return temp;
}
</pre>