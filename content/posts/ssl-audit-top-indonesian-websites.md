+++
author = "Batista Harahap"
categories = ["audit", "indonesia", "ssl", "websites"]
date = 2013-06-26T21:42:24Z
description = ""
draft = false
slug = "ssl-audit-top-indonesian-websites"
tags = ["audit", "indonesia", "ssl", "websites"]
title = "SSL Audit - Top Indonesian Websites"

+++


I came across <a title="Qualys SSL Labs" href="http://www.ssllabs.com" target="_blank">Qualys SSL Labs</a> a few minutes ago while reading through Hacker News. Immediately triggered my interest to question how secure top websites in Indonesia when it comes to their SSL.

<h3>Urbanesia</h3>
Since I am at Urbanesia, the first goto is clear. Typed in Urbanesia.com and the initial audit result was needs more work.

So the audit results came back as a <strong>B</strong>. The server didn't mitigate BEAST attack and that's the main reason the grade was dropped. After a little digging up, the ciphers were the culprit and to mitigate the problem, nginx needs to be configured like below.

<script src="https://gist.github.com/tistaharahap/5871541.js"></script>

As it turs out, after putting the configuration at play, Urbanesia was still getting a B due to BEAST non-mitigation. The resources out there implies the above configuration so I'll have to settle for B until further digging.

<h3>Top Websites</h3>

So I was curious how other websites in Indonesia grades. Went ahead to do more testing and the report as of 27 June 2013 03:53:00 GMT+7 after this paragraph.

<h3>Kaskus</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=kaskus.co.id
Domain: kaskus.co.id
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>80</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<h3>Detik</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=detik.com
Domain: detik.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Detik Connect</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=connect.detik.com
Domain: connect.detik.com
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>80</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<h3>Kompas</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=kompas.com
Domain: kompas.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Kompas Logins</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=login.kompas.com
Domain: login.kompas.com
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<strong>Update 28 June 2013:</strong> Kompas has since fixed this and now getting a big A. But there is one more thing they can do is to update their OpenSSL library to support a newer TLS version. Overall, fast response and decisive A factoring actions.

<h3>TokoBagus</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=tokobagus.com
Domain: tokobagus.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Berniaga</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=berniaga.com
Domain: berniaga.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Tokopedia</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=tokopedia.com
Domain: tokopedia.com
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>80</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated

<strong>Updated 27 June 2013 13:28:00</strong>: <a href="https://twitter.com/liamtanu">William</a> responded in Facebook and reworked Tokopedia's SSL implementation to upgrade their score from B to A. Swift and precise measures, the others should make Tokopedia as an example (including Urbanesia).

<h3>Bhinneka</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=bhinneka.com
Domain: bhinneka.com
Grade: <strong>F</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>0</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<h3>LivingSocial</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=livingsocial.co.id
Domain: livingsocial.co.id
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>80</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated
Note: Does not support TLS 1.2

<h3>Disdus</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=disdus.com
Domain: disdus.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Lazada</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=lazada.co.id
Domain: lazada.co.id
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated
Note: Does not support TLS 1.2

<h3>Blibli</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=blibli.com
Domain: blibli.com
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<h3>Tiket</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=tiket.com
Domain: tiket.com
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated

<strong>UPDATE 28 July 2013:</strong> Tiket.com now scores an A with 100/90/90/90 across the board.

<h3>Tiket2</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=tiket2.com
Domain: tiket2.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Lion Air</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=secure2.lionair.co.id
Domain: secure2.lionair.co.id
Grade: <strong>C</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>40</strong>
Cipher Strength: <strong>60</strong>
BEAST: Mitigated

<h3>Garuda Indonesia</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=booking.garuda-indonesia.com
Domain: booking.garuda-indonesia.com
Grade: <strong>F</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>87</strong>
Key Exchange: <strong>0</strong>
Cipher Strength: <strong>80</strong>
BEAST: Mitigated

<h3>Air Asia</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=airasia.com
Domain: airasia.com
Grade: <strong>C</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>40</strong>
Cipher Strength: <strong>60</strong>
BEAST: Non-mitigated

<h3>KlikBCA</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=ibank.klikbca.com
Domain: ibank.klikbca.com
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated

<h3>Bank Mandiri</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=ib.bankmandiri.co.id
Domain: ib.bankmandiri.co.id
Grade: <strong>A</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated
Note: Does not support TLS 1.2

<h3>CIMB Clicks</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=www.cimbclicks.co.id
Grade: <strong>A</strong>
Domain: www.cimbclicks.co.id
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Mitigated

<h3>Veritrans</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=payments.veritrans.co.id
Domain: payments.veritrans.co.id
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>90</strong>
Key Exchange: <strong>90</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated

<h3>iPaymu</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=my.ipaymu.com
Domain: my.ipaymu.com
Grade: <strong>B</strong>
Certificate: <strong>100</strong>
Protocol Support: <strong>85</strong>
Key Exchange: <strong>80</strong>
Cipher Strength: <strong>90</strong>
BEAST: Non-mitigated
Note: Checked the domain for iPaymu's API transaction

<h3>Doku</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=doku.com
Domain: doku.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

<h3>Finpay</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=portalfinpay.com
Domain: portalfinpay.com
Grade: SSL Certificate Mismatch
Certificate: SSL Certificate Mismatch
Protocol Support: SSL Certificate Mismatch
Key Exchange: SSL Certificate Mismatch
Cipher Strength: SSL Certificate Mismatch
BEAST: SSL Certificate Mismatch

<h3>Midazz</h3>

SSLLabs Report: https://www.ssllabs.com/ssltest/analyze.html?d=midazz.com
Domain: midazz.com
Grade: No SSL Support
Certificate: No SSL Support
Protocol Support: No SSL Support
Key Exchange: No SSL Support
Cipher Strength: No SSL Support
BEAST: No SSL Support

So as the results above says, it's quite the risky business for E-Commerce consumers in Indonesia. <a href="http://www.alexa.com/topsites/countries;2/ID" target="_blank">Bhinneka ranking 58</a> according to Alexa.com scores an <strong>F</strong>. Tiket.com is using an older set of daemon/SSL Ciphers, they need to harden while Tiket2 needs to buy an SSL certificate. Other E-Commerce websites like TokoBagus, Disdus and Berniaga doesn't even support SSL.

On the other hand, websites scoring an A were mostly banks which are KlikBCA, Bank Mandiri and CIMB. Applause for Lazada for also scoring an A.

What I found most disappointing were payment gateways except for Veritrans. Veritrans implements a rather secure API mimicking OAuth's flow requiring all requests to be signed with a secret key, they also scored a B.

iPaymu was scoring a B but after going through their <a href="https://ipaymu.com/dokumentasi-api" target="_blank">API Documentation</a>, it was appalling to say the least. All of the requests to their API doesn't need any public/private token pair, in fact just a plain token. Definitely needs more attention to their security practice.

For Doku and Finpay, I don't know their API endpoints if any but a check to their root domain names yield disappointing results as well. Doku does not support SSL while Finpay has an SSL certificate mismatch. Not what you expected from a payment gateway. I'm out of <code>-(superlatives)</code> for these two. Midazz is pretty much exactly like Doku, they don't understand the needs for SSL.

Airlines have the worst SSL audit of all the other websites. Lion Air and Air Asia got a C while Garuda Indonesia got an F! Airlines especially Garuda Indonesia needs to find better resources in securing their customer's transactions on their websites. <strong>Totally unacceptable!</strong> How can you pay hundreds of millions of dollars on airplanes and fail miserably at this?

So there you go, Top Indonesia websites awareness for SSL.