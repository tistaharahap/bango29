+++
author = "Batista Harahap"
categories = ["bitcoin", "bots", "trading", "tradingview"]
date = 2020-08-20T11:55:49Z
description = ""
draft = false
image = "/images/2020/08/LogoMakr_6eW7Qa.png"
slug = "building-a-bitcoin-trading-bot-with-sanic"
tags = ["bitcoin", "bots", "trading", "tradingview"]
title = "Building A Bitcoin Trading Bot With Sanic"

+++


For the longest time, I've been wanting to write a trading bot to leverage on [TradingView](https://www.tradingview.com/gopro/?share_your_love=tista)'s alert system. For any indicator or strategy you use, you can set up alerts which will then send the notification to various destinations including a webhook. They have a strict 3 second must reply rule which is not trivial the first time I thought about it. Persistence and a lot of codes later wins though, found a way.

My first try was to decouple all the components by using RabbitMQ as its vein for messages.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My own <a href="https://twitter.com/tradingview?ref_src=twsrc%5Etfw">@tradingview</a> alerts <a href="https://twitter.com/hashtag/btc?src=hash&amp;ref_src=twsrc%5Etfw">#btc</a> trading bot for <a href="https://twitter.com/binance?ref_src=twsrc%5Etfw">@binance</a> running on my own hardware thanks to <a href="https://twitter.com/UnraidOfficial?ref_src=twsrc%5Etfw">@UnraidOfficial</a>&#39;s excellent product. Covers all the use cases of any geek 😍Source codes are open source, early days still need more work but here it is <a href="https://t.co/l8ezHHR8m9">https://t.co/l8ezHHR8m9</a> <a href="https://t.co/uxOepZdN21">pic.twitter.com/uxOepZdN21</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1295816830485794816?ref_src=twsrc%5Etfw">August 18, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Notice that the bot is becoming complex before it's even being utilized? I admit I did some over engineering but by nature it was too complex, I had trouble running the bot initially, had to have a note for the services and its IP addresses. So I said fuck it, there must be an easier way. And there was, I stumbled into this post.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Love this <a href="https://t.co/W4vmnkox6s">https://t.co/W4vmnkox6s</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1296254451674562560?ref_src=twsrc%5Etfw">August 20, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Been writing asynchronous Python codes for a while now and my hunch about [Sanic](https://github.com/huge-success/sanic) was justified. It's basically an `asyncio` loop, we can do concurrent tasks by nature. Now that the building block is set, it's time to code.

## GoingFast

I learned how to trade with the community, people in the community taught me everything I had to know. That said, it's only pertinent that I share this with the community. All source codes are published below.

[https://github.com/tradebro/goingfast](https://github.com/tradebro/goingfast).

The `README` needs some work which I will try to write some of it here.

### Concept

Select an indicator/strategy in TradingView. Note that all strategies comes with alerts while indicators don't necessarily so. Check out my indicators [here](https://www.tradingview.com/u/tista/#published-scripts), all of them provide alerts.

Create an alert and fill in the values like below.

![Alerts in TradingView](/content/images/2020/08/Screen-Shot-2020-08-21-at-01.09.42.png)

More about the JSON payload is below:

```
[POST] /webhook

+ Request (application/json)

        {
            "close": 11382.11,
            "indicator": "Bayesian SMI Oscillator",
            "exchange": "Coinbase",
            "pair": "BTCUSD",
            "action": "Long"
        }

+ Response 200
```

Fill in the `Webhook URL` with your own deployment of the bot.

### Bot Flow

I'll try to detail the bot's decision process below. For any request whether the request is valid or not, the bot will always respond with a `200` HTTP status code.

1. Webhook is triggered, validation of the webhook's payload is done
2. Spawn a new background task for trade orders then immediately reply the webhook and close the client's connection

The trading part right now is only implemented for [Bybit](https://bybit.com), I only actively trade there. Trades are implemented using [CCXT](https://github.com/ccxt/ccxt), a multi exchange client library. Although for my implementation, I avoid its "universal" API and instead uses exchange implicit methods. Using CCXT mostly because I don't wanna do request signing logic myself.

The trading part flow is below.

1. Check if there is an open position, only trade if there no open position
2. Cancels all orders if any
3. Entry as a taker
4. Exit as a maker both for take profit and stop loss orders

### Deployment

The Github repository will automatically push Docker images to its Docker hub equivalent [here](https://hub.docker.com/r/tistaharahap/goingfast). I would suggest to deploy using Docker, it's way simpler.

```
$ docker -d --name goingfast -p 8080:8080 \
-e APP_HOST="0.0.0.0" \
-e APP_PORT="8080" \
-e APP_DEBUG="0" \
-e TELEGRAM_TOKEN="your_telegram_bot_token" \
-e TELEGRAM_CHAT_ID="your_telegram_chat_id" \
-e STOP_DELTA="100" \
-e TP_DELTA="100" \
-e CAPITAL_IN_USD="100" \
-e API_KEY="your_api_key" \
-e API_SECRET="your_api_secret" \
-e TRADER="bybit" \
-e LEVERAGE="10" \
tistaharahap/goingfast:latest
```

#### Env Vars

I'll discuss important env vars here, the rest are self explanatory I believe.

##### Stop Delta

`STOP_DELTA` is the delta from your entry price for the stop order.

##### TP Delta

`TP_DELTA` is the delta from your entry price for the take profit order.

##### Capital In USD and Leverage

`CAPITAL_IN_USD` for leveraged exchanges should be based on your actual capital and leverage. If you have $1000 worth of Bitcoin, you can trade $100 with a 10x leverage while maintaining a 1% risk, you will only use $10 worth of Bitcoin for the trade.

### Future Ideas

Some ideas I have for the bot.

1. The current logic is pretty primitive. It basically mimics spot trading with the main difference of being able to short the market. Leveraged exchanges are position oriented so in the future, we can optimize for positions taking in small profits but often. More like how market makers bots work.
2. Implement spot exchanges. Due to spot exchanges stop order nature, I decided to not implement this initially. Spot exchanges require you to cancel all orders explicitly while on leveraged exchanges you can do `Reduce Only` orders meaning that it will only be executed if there is an open position.

---

I'm lucky I live where my ISP gives me a public IP with all ports open for me. I run my bot from home on my [Unraid Box](https://bango29.com/unraid-case-motherboard-upgrade-and-some-more/). It's scary to expose my home network to the internet, had to go do more work to secure it but that's for another blog post.

Open to any feedbacks for the bot, [mention me](https://twitter.com/tista) on Twitter.