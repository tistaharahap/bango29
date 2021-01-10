+++
author = "Batista Harahap"
categories = ["ios", "ipad", "iphone", "oauth", "oauthnesia", "objective c", "urbanesia", "urbanesia api", "xauth"]
date = 2011-08-14T09:19:47Z
description = ""
draft = false
slug = "oauthnesia-client-for-objective-c"
tags = ["ios", "ipad", "iphone", "oauth", "oauthnesia", "objective c", "urbanesia", "urbanesia api", "xauth"]
title = "OAUTHnesia Client for Objective-C"

+++


Okay for the last few hours, I've been learning how to code in Objective-C and the first result is an OAUTH client for Urbanesia. I haven't tested thoroughly though. The class basically wraps POST &amp; GET requests to Urbanesia with OAUTH requirements.

Instantiating the class, you will have to provide Consumer Key &amp; Secret obtained from Urbanesia. The current implementation requires User Key &amp; Secret for every requests too. Future release of OAUTHnesia will include non Use Key/Secret methods and XAUTH.

You will have to do the HTTP connection yourselves with your own codes, OAUTHnesia only wraps the request with proper OAUTH requirements.

Base64Transcoder.h
<pre lang="c" line="1">
/*
 *  Base64Transcoder.h
 *  Base64Test
 *
 *  Created by Jonathan Wight on Tue Mar 18 2003.
 *  Copyright (c) 2003 Toxic Software. All rights reserved.
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 *
 */

#include <stdlib.h>
#include <stdbool.h>

extern size_t EstimateBas64EncodedDataSize(size_t inDataSize);
extern size_t EstimateBas64DecodedDataSize(size_t inDataSize);

extern bool Base64EncodeData(const void *inInputData, size_t inInputDataSize, char *outOutputData, size_t *ioOutputDataSize);
extern bool Base64DecodeData(const void *inInputData, size_t inInputDataSize, void *ioOutputData, size_t *ioOutputDataSize);
</pre>
Base64Transcoder.c
<pre lang="c" line="1">
/*
 *  Base64Transcoder.c
 *  Base64Test
 *
 *  Created by Jonathan Wight on Tue Mar 18 2003.
 *  Copyright (c) 2003 Toxic Software. All rights reserved.
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 *
 */

#include "Base64Transcoder.h"

#include <math.h>
#include <string.h>

const u_int8_t kBase64EncodeTable[64] = {
	/*  0 */ 'A',	/*  1 */ 'B',	/*  2 */ 'C',	/*  3 */ 'D', 
	/*  4 */ 'E',	/*  5 */ 'F',	/*  6 */ 'G',	/*  7 */ 'H', 
	/*  8 */ 'I',	/*  9 */ 'J',	/* 10 */ 'K',	/* 11 */ 'L', 
	/* 12 */ 'M',	/* 13 */ 'N',	/* 14 */ 'O',	/* 15 */ 'P', 
	/* 16 */ 'Q',	/* 17 */ 'R',	/* 18 */ 'S',	/* 19 */ 'T', 
	/* 20 */ 'U',	/* 21 */ 'V',	/* 22 */ 'W',	/* 23 */ 'X', 
	/* 24 */ 'Y',	/* 25 */ 'Z',	/* 26 */ 'a',	/* 27 */ 'b', 
	/* 28 */ 'c',	/* 29 */ 'd',	/* 30 */ 'e',	/* 31 */ 'f', 
	/* 32 */ 'g',	/* 33 */ 'h',	/* 34 */ 'i',	/* 35 */ 'j', 
	/* 36 */ 'k',	/* 37 */ 'l',	/* 38 */ 'm',	/* 39 */ 'n', 
	/* 40 */ 'o',	/* 41 */ 'p',	/* 42 */ 'q',	/* 43 */ 'r', 
	/* 44 */ 's',	/* 45 */ 't',	/* 46 */ 'u',	/* 47 */ 'v', 
	/* 48 */ 'w',	/* 49 */ 'x',	/* 50 */ 'y',	/* 51 */ 'z', 
	/* 52 */ '0',	/* 53 */ '1',	/* 54 */ '2',	/* 55 */ '3', 
	/* 56 */ '4',	/* 57 */ '5',	/* 58 */ '6',	/* 59 */ '7', 
	/* 60 */ '8',	/* 61 */ '9',	/* 62 */ '+',	/* 63 */ '/'
};

/*
 -1 = Base64 end of data marker.
 -2 = White space (tabs, cr, lf, space)
 -3 = Noise (all non whitespace, non-base64 characters) 
 -4 = Dangerous noise
 -5 = Illegal noise (null byte)
 */

const int8_t kBase64DecodeTable[128] = {
	/* 0x00 */ -5, 	/* 0x01 */ -3, 	/* 0x02 */ -3, 	/* 0x03 */ -3,
	/* 0x04 */ -3, 	/* 0x05 */ -3, 	/* 0x06 */ -3, 	/* 0x07 */ -3,
	/* 0x08 */ -3, 	/* 0x09 */ -2, 	/* 0x0a */ -2, 	/* 0x0b */ -2,
	/* 0x0c */ -2, 	/* 0x0d */ -2, 	/* 0x0e */ -3, 	/* 0x0f */ -3,
	/* 0x10 */ -3, 	/* 0x11 */ -3, 	/* 0x12 */ -3, 	/* 0x13 */ -3,
	/* 0x14 */ -3, 	/* 0x15 */ -3, 	/* 0x16 */ -3, 	/* 0x17 */ -3,
	/* 0x18 */ -3, 	/* 0x19 */ -3, 	/* 0x1a */ -3, 	/* 0x1b */ -3,
	/* 0x1c */ -3, 	/* 0x1d */ -3, 	/* 0x1e */ -3, 	/* 0x1f */ -3,
	/* ' ' */ -2,	/* '!' */ -3,	/* '"' */ -3,	/* '#' */ -3,
	/* '$' */ -3,	/* '%' */ -3,	/* '&' */ -3,	/* ''' */ -3,
	/* '(' */ -3,	/* ')' */ -3,	/* '*' */ -3,	/* '+' */ 62,
	/* ',' */ -3,	/* '-' */ -3,	/* '.' */ -3,	/* '/' */ 63,
	/* '0' */ 52,	/* '1' */ 53,	/* '2' */ 54,	/* '3' */ 55,
	/* '4' */ 56,	/* '5' */ 57,	/* '6' */ 58,	/* '7' */ 59,
	/* '8' */ 60,	/* '9' */ 61,	/* ':' */ -3,	/* ';' */ -3,
	/* '<' */ -3,	/* '=' */ -1,	/* '>' */ -3,	/* '?' */ -3,
	/* '@' */ -3,	/* 'A' */ 0,	/* 'B' */  1,	/* 'C' */  2,
	/* 'D' */  3,	/* 'E' */  4,	/* 'F' */  5,	/* 'G' */  6,
	/* 'H' */  7,	/* 'I' */  8,	/* 'J' */  9,	/* 'K' */ 10,
	/* 'L' */ 11,	/* 'M' */ 12,	/* 'N' */ 13,	/* 'O' */ 14,
	/* 'P' */ 15,	/* 'Q' */ 16,	/* 'R' */ 17,	/* 'S' */ 18,
	/* 'T' */ 19,	/* 'U' */ 20,	/* 'V' */ 21,	/* 'W' */ 22,
	/* 'X' */ 23,	/* 'Y' */ 24,	/* 'Z' */ 25,	/* '[' */ -3,
	/* '\' */ -3,	/* ']' */ -3,	/* '^' */ -3,	/* '_' */ -3,
	/* '`' */ -3,	/* 'a' */ 26,	/* 'b' */ 27,	/* 'c' */ 28,
	/* 'd' */ 29,	/* 'e' */ 30,	/* 'f' */ 31,	/* 'g' */ 32,
	/* 'h' */ 33,	/* 'i' */ 34,	/* 'j' */ 35,	/* 'k' */ 36,
	/* 'l' */ 37,	/* 'm' */ 38,	/* 'n' */ 39,	/* 'o' */ 40,
	/* 'p' */ 41,	/* 'q' */ 42,	/* 'r' */ 43,	/* 's' */ 44,
	/* 't' */ 45,	/* 'u' */ 46,	/* 'v' */ 47,	/* 'w' */ 48,
	/* 'x' */ 49,	/* 'y' */ 50,	/* 'z' */ 51,	/* '{' */ -3,
	/* '|' */ -3,	/* '}' */ -3,	/* '~' */ -3,	/* 0x7f */ -3
};

const u_int8_t kBits_00000011 = 0x03;
const u_int8_t kBits_00001111 = 0x0F;
const u_int8_t kBits_00110000 = 0x30;
const u_int8_t kBits_00111100 = 0x3C;
const u_int8_t kBits_00111111 = 0x3F;
const u_int8_t kBits_11000000 = 0xC0;
const u_int8_t kBits_11110000 = 0xF0;
const u_int8_t kBits_11111100 = 0xFC;

size_t EstimateBas64EncodedDataSize(size_t inDataSize)
{
    size_t theEncodedDataSize = (int)ceil(inDataSize / 3.0) * 4;
    theEncodedDataSize = theEncodedDataSize / 72 * 74 + theEncodedDataSize % 72;
    return(theEncodedDataSize);
}

size_t EstimateBas64DecodedDataSize(size_t inDataSize)
{
    size_t theDecodedDataSize = (int)ceil(inDataSize / 4.0) * 3;
    //theDecodedDataSize = theDecodedDataSize / 72 * 74 + theDecodedDataSize % 72;
    return(theDecodedDataSize);
}

bool Base64EncodeData(const void *inInputData, size_t inInputDataSize, char *outOutputData, size_t *ioOutputDataSize)
{
    size_t theEncodedDataSize = EstimateBas64EncodedDataSize(inInputDataSize);
    if (*ioOutputDataSize < theEncodedDataSize)
        return(false);
    *ioOutputDataSize = theEncodedDataSize;
    const u_int8_t *theInPtr = (const u_int8_t *)inInputData;
    u_int32_t theInIndex = 0, theOutIndex = 0;
    for (; theInIndex < (inInputDataSize / 3) * 3; theInIndex += 3)
	{
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_11111100) >> 2];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_00000011) << 4 | (theInPtr[theInIndex + 1] & kBits_11110000) >> 4];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex + 1] & kBits_00001111) << 2 | (theInPtr[theInIndex + 2] & kBits_11000000) >> 6];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex + 2] & kBits_00111111) >> 0];
        if (theOutIndex % 74 == 72)
		{
            outOutputData[theOutIndex++] = '\r';
            outOutputData[theOutIndex++] = '\n';
		}
	}
    const size_t theRemainingBytes = inInputDataSize - theInIndex;
    if (theRemainingBytes == 1)
	{
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_11111100) >> 2];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_00000011) << 4 | (0 & kBits_11110000) >> 4];
        outOutputData[theOutIndex++] = '=';
        outOutputData[theOutIndex++] = '=';
        if (theOutIndex % 74 == 72)
		{
            outOutputData[theOutIndex++] = '\r';
            outOutputData[theOutIndex++] = '\n';
		}
	}
    else if (theRemainingBytes == 2)
	{
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_11111100) >> 2];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex] & kBits_00000011) << 4 | (theInPtr[theInIndex + 1] & kBits_11110000) >> 4];
        outOutputData[theOutIndex++] = kBase64EncodeTable[(theInPtr[theInIndex + 1] & kBits_00001111) << 2 | (0 & kBits_11000000) >> 6];
        outOutputData[theOutIndex++] = '=';
        if (theOutIndex % 74 == 72)
		{
            outOutputData[theOutIndex++] = '\r';
            outOutputData[theOutIndex++] = '\n';
		}
	}
    return(true);
}

bool Base64DecodeData(const void *inInputData, size_t inInputDataSize, void *ioOutputData, size_t *ioOutputDataSize)
{
    memset(ioOutputData, '.', *ioOutputDataSize);
    
    size_t theDecodedDataSize = EstimateBas64DecodedDataSize(inInputDataSize);
    if (*ioOutputDataSize < theDecodedDataSize)
        return(false);
    *ioOutputDataSize = 0;
    const u_int8_t *theInPtr = (const u_int8_t *)inInputData;
    u_int8_t *theOutPtr = (u_int8_t *)ioOutputData;
    size_t theInIndex = 0, theOutIndex = 0;
    u_int8_t theOutputOctet;
    size_t theSequence = 0;
    for (; theInIndex < inInputDataSize; )
	{
        int8_t theSextet = 0;
        
        int8_t theCurrentInputOctet = theInPtr[theInIndex];
        theSextet = kBase64DecodeTable[theCurrentInputOctet];
        if (theSextet == -1)
            break;
        while (theSextet == -2)
		{
            theCurrentInputOctet = theInPtr[++theInIndex];
            theSextet = kBase64DecodeTable[theCurrentInputOctet];
		}
        while (theSextet == -3)
		{
            theCurrentInputOctet = theInPtr[++theInIndex];
            theSextet = kBase64DecodeTable[theCurrentInputOctet];
		}
        if (theSequence == 0)
		{
            theOutputOctet = (theSextet >= 0 ? theSextet : 0) << 2 & kBits_11111100;
		}
        else if (theSequence == 1)
		{
            theOutputOctet |= (theSextet >- 0 ? theSextet : 0) >> 4 & kBits_00000011;
            theOutPtr[theOutIndex++] = theOutputOctet;
		}
        else if (theSequence == 2)
		{
            theOutputOctet = (theSextet >= 0 ? theSextet : 0) << 4 & kBits_11110000;
		}
        else if (theSequence == 3)
		{
            theOutputOctet |= (theSextet >= 0 ? theSextet : 0) >> 2 & kBits_00001111;
            theOutPtr[theOutIndex++] = theOutputOctet;
		}
        else if (theSequence == 4)
		{
            theOutputOctet = (theSextet >= 0 ? theSextet : 0) << 6 & kBits_11000000;
		}
        else if (theSequence == 5)
		{
            theOutputOctet |= (theSextet >= 0 ? theSextet : 0) >> 0 & kBits_00111111;
            theOutPtr[theOutIndex++] = theOutputOctet;
		}
        theSequence = (theSequence + 1) % 6;
        if (theSequence != 2 && theSequence != 4)
            theInIndex++;
	}
    *ioOutputDataSize = theOutIndex;
    return(true);
}
</pre>
OAUTHnesia.h
<pre lang="objc">#import 

@interface OAUTHnesia : NSObject {
@protected
    NSString *CONSUMER_KEY;
    NSString *CONSUMER_SECRET;
    NSString *API_BASE_URL;
}

@property(nonatomic, retain) NSString *CONSUMER_KEY;
@property(nonatomic, retain) NSString *CONSUMER_SECRET;
@property(nonatomic, retain) NSString *USER_KEY;
@property(nonatomic, retain) NSString *USER_SECRET;
@property(nonatomic, retain) NSString *API_BASE_URL;
@property(nonatomic, retain) NSString *POST_URL;
@property(nonatomic, retain) NSString *POST_DATA;

- (id)initWithKey:(NSString *)cons_key secret:(NSString *)cons_secret;
- (void) setUserKey: (NSString *)user_key;
- (void) setUserSecret: (NSString *)user_secret;
- (NSString *) encodeForOauth: (NSString *) postget;
- (NSString *) getNonce;
- (NSString *) getTime;
- (NSString *) generateBaseSignature: (NSString *) base_sig uri:(NSString *) uri;
- (NSString *) hmacsha1: (NSString *)text key:(NSString *)secret;
- (NSString *) md5: (NSString *)text;
- (NSString *) urlencode: (NSString *)text;

- (void) oAuth:(NSString *)oUri oPost:(NSString *)oPost oGet:(NSString *)oGet;

@end</pre>

OAUTHnesia.m
<pre lang="objc">#import "OAUTHnesia.h"
//
//  OAUTHnesia.m
//  Jajan
//
//  Created by Batista Harahap on 8/14/11.
//  Copyright 2011 Urbanesia.com. All rights reserved.
//

#import "OAUTHnesia.h"
#include "Base64Transcoder.h"
#import <CommonCrypto/CommonHMAC.h>
#import <CommonCrypto/CommonDigest.h>

@implementation OAUTHnesia
@synthesize CONSUMER_KEY, CONSUMER_SECRET, USER_KEY, USER_SECRET, API_BASE_URL, POST_URL, POST_DATA;

- (id)initWithKey:(NSString *)cons_key secret:(NSString *)cons_secret {
    if (self = [super init]) {
        self.CONSUMER_KEY = cons_key;
        self.CONSUMER_SECRET = cons_secret;
        self.API_BASE_URL = @"http://api1.urbanesia.com/";
        self.POST_URL = self.POST_DATA = @"";
    }
    
    return self;
}

- (void)oAuth:(NSString *)oUri oPost:(NSString *)oPost oGet:(NSString *)oGet {
    // Post yang pasti harus ada!
    NSString *postIncludes = [NSString stringWithFormat:
        @"oauth_consumer_key=%@&oauth_nonce=%@&oauth_signature_method=HMAC-SHA1&oauth_timestamp=%@&oauth_token=%@&oauth_version=1.0",
        self.CONSUMER_KEY, self.getNonce, self.getTime, self.USER_KEY];
    
    // Cek ada POST ga di request?
    if([oPost isEqual:@""]) {
        oPost = postIncludes;
    } else {
        oPost = [NSString stringWithFormat:@"%@&%@", oPost, postIncludes];
    }
    
    // Cek ada GET ga di request?
    if(![oGet isEqual:@""]) {
        oGet = [NSString stringWithFormat:@"&%@", oGet];
    }
    
    // Encode for OAUTH & Generate Base Signature
    NSString *base_sig = [self generateBaseSignature:[self encodeForOauth:[NSString stringWithFormat:@"%@%@", oPost, oGet]] uri:oUri];
    
    // OAUTH Signature
    NSString *signature = [self hmacsha1:[NSString stringWithFormat:@"%@&%@", self.CONSUMER_SECRET, self.USER_SECRET] key:base_sig];
    
    // POST URL
    self.POST_URL = [NSString stringWithFormat:@"%@%@?oauth_signature=%@%@", self.API_BASE_URL, oUri, signature, oGet];
    
    // POST DATA
    self.POST_DATA = oPost;
}

- (void)setUserKey:(NSString *)user_key {
    self.USER_KEY = user_key;
}

- (void)setUserSecret:(NSString *)user_secret {
    self.USER_SECRET = user_secret;
}

- (NSString *)getNonce {
    NSTimeInterval timePassed_ms = [[NSDate date] timeIntervalSinceNow] * -1000.0;
    return [self md5:[NSString stringWithFormat:@"%@", timePassed_ms]];
}

- (NSString *)getTime {
    NSTimeInterval timePassed_ms = [[NSDate date] timeIntervalSinceNow] * -1000.0;
    return [NSString stringWithFormat:@"%@", timePassed_ms];
}

- (NSString *)generateBaseSignature:(NSString *)base_sig uri:(NSString *)uri {
    NSString *dest = [NSString stringWithFormat:@"%@%@", self.API_BASE_URL, uri];
    dest = [self urlencode:dest];
    base_sig = [self urlencode:base_sig];
    return [NSString stringWithFormat:@"POST&%@&%@", dest, base_sig];
}

- (NSString *)encodeForOauth: (NSString *)postget {
    // Explode to array
    NSArray *par = [postget componentsSeparatedByString:@"&"];
    
    // Sort by array keys
    par = [par sortedArrayUsingSelector:@selector(localizedCaseInsensitiveCompare:)];
    
    NSString *ret = @"";
    
    for(int i=0, j=0, max=par.count; i<max; i++) {
        if(j==1)
            ret = [NSString stringWithFormat:@"%@&", ret];
        
        NSArray *temp = [[par objectAtIndex:i] componentsSeparatedByString:@"="];
        NSString *k = (NSString *)[temp objectAtIndex:0];
        k = [self urlencode:k];
        NSString *v = (NSString *)[temp objectAtIndex:1];
        v = [self urlencode:v];
        ret = [NSString stringWithFormat:@"%@%@=%@", ret, k, v];
        
        j = 1;
    }
    
    return ret;
}

- (NSString *)urlencode:(NSString *)text {
    return [text stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding];
}

- (NSString *)md5:(NSString *)text {
    const char* str = [text UTF8String];
    unsigned char result[CC_MD5_DIGEST_LENGTH];
    CC_MD5(str, strlen(str), result);
    NSMutableString *ret = [NSMutableString stringWithCapacity:CC_MD5_DIGEST_LENGTH*2];
    for(int i = 0; i<CC_MD5_DIGEST_LENGTH; i++) {
        [ret appendFormat:@"%02x",result[i]];
    }
    return ret;
}

- (NSString *)hmacsha1:(NSString *)text key:(NSString *)secret {
    NSData *secretData = [secret dataUsingEncoding:NSUTF8StringEncoding];
    NSData *clearTextData = [text dataUsingEncoding:NSUTF8StringEncoding];
    unsigned char result[20];
	CCHmac(kCCHmacAlgSHA1, [secretData bytes], [secretData length], [clearTextData bytes], [clearTextData length], result);
    
    char base64Result[32];
    size_t theResultLength = 32;
    Base64EncodeData(result, 20, base64Result, &theResultLength);
    NSData *theData = [NSData dataWithBytes:base64Result length:theResultLength];
    
    NSString *base64EncodedResult = [[NSString alloc] initWithData:theData encoding:NSUTF8StringEncoding];
    
    return base64EncodedResult;
}

@end
</pre>