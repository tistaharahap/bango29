+++
author = "Batista Harahap"
categories = ["llm", "openwebui", "ai", "saas", "hosting", "litellm", "coolify"]
date = 2025-04-25T06:37:16Z
description = "This is a writing about getting things done more than it is a showcase of a new business and the tech empowering it. Within this, an attempt to explain the why will also be written. But before all that, I'm going to try to look cool first so get ready for some cringe moments."
draft = false
slug = "sleekchat-research-to-production-in-1-week"
tags = ["llm", "openwebui", "ai", "saas", "hosting", "litellm", "coolify"]
title = "SleekChat: Research to Production in 1 Week"

+++

This is a writing about getting things done more than it is a showcase of a new business and the tech empowering it. Within this, an attempt to explain the why will also be written. But before all that, I'm going to try to look cool first so get ready for some cringe moments.

## Vibe Coding

Hell yeah! But not in a way most will vibe with. Being a backend guy, giving up control is not my nature although the web frontend is vibed. As with any experiments, it started with an idea then proof of concept, hit walls then pushed through. Here are the core tech stack to build SleekChat:

1. [Open WebUI](https://x.com/OpenWebUI) - of course
2. [Coolify](https://x.com/coolifyio) - yes, it's so 🆒
3. [Clerk](https://x.com/clerkdev) - simple auth
4. [Polar](https://x.com/polar_sh) - payments, so simple
5. [MongoDB](https://x.com/mongodb) - my favorite
6. [Redis](https://x.com/redisinc) - key values are enough
7. [Anthropic](https://x.com/AnthropicAI) Claude 3.7 - best pairing buddy so far
8. [FastAPI](https://x.com/fastapi) - the most macro of the micros
9. [NextJS](https://x.com/nextjs) - in an effort to be cool
10. [Pydantic](https://x.com/pydantic) - modeling is more better here
11. [Typescript](https://x.com/typescript) - modeling is more better here?
12. Python - don't have words to describe this gem
13. [Hetzner](https://x.com/hetzner_online) - another effort to be 🆒
14. [Pycharm](https://x.com/pycharm) - is there anything else for Python?
15. [Visual Studio Code](https://x.com/code) - swiss army knife

More about the tech stuffs later.

## Open WebUI

I've been using Open WebUI since their 0.1.x release, the way the contributors pushed through the bleeding edge is admirable. I would go as far as to say, they're an inspiration. They release features with much fuss, they just do it, the train keeps going forward. All my LLM/AI research started with Open WebUI, I developed and experimented there first before writing codes.

Having the ability to create my own models based on Claude, ChatGPT, Gemini, Ollama and everything else in between is helpful if not fundamental. It made me realize, non-tech people wouldn't be able to enjoy the power of Open WebUI without someone like me helping them.

## Motivation

In the last month I've been struck with a realization that doing work to empower others has a non zero chance to be a blessing and I mean this in the sincerest way possible. You will see this with the pricing which I will write about later on here.

Then comes a question that became an itch:

> Why would something like Open WebUI that has helped me upskill myself to be only confined to those who can install it and get it working?

I googled and I can't find any hosting service built for Open WebUI. Why? Is it technically hard or impossible? It's a Dockerized HTTP app, why wouldn't anyone do this?

A probable answer could be that not enough people experienced Open WebUI like how I experienced it? I think so. If enough people thought about it the same way like I do, I'm sure there's someone out there that has done it. Most of the services that do offer hosting for it are cold, they don't seem to actually use the software, it's just another Docker app for them.

One of the promise of LLMs or AI is to bring prosperity to the world so I thought; an infrastructure to create prosperity would be a shovel that won't stop giving. Let's see how this age but fundamentally, this should hold true even if SleekChat won't be the number one option for hosting Open WebUI.

There's a business to be built here I thought.

Spent an hour with @kresnahendri to talk about this and we both came to the same conclusion: someone has to do it. It became more than just building a business, it became more like a mission for us. Especially when we look at the pricing of AI products, it's absurd. It's fair game to cash out on the AI boom of course, I mean look at Nvidia, they basically screwed over gamers who made them big in the first place? I suppose the premium is carried forward from the fundamental to the end user.

We (Kresna and I) think because of LLMs, knowledge will be extremely personal and enriching of what you already know. The advent of the Internet many years ago have made knowledge almost universal, you just have to know where to look. Hence, the rise of Google. But with LLMs, knowledge is as universal as it is personal. Open WebUI enables that with its core features.

We built SleekChat with Open WebUI and Claude 3.7, is this an "inception" the movie moment? Let me try to explain how we do it so that you can do something like this too.

## Build Mode

There have been a few other products that Kresna and I have built from scratch, him on the frontend and me on the backend. But none of them were built as a business for both of us. We knew that getting things done is our strength but to be able to do it in a week? That's epic.

![The catalyst](/content/images/2025/04/catalyst.png)

The screenshot above is a model I created in Open WebUI, here's a link to the system prompt I use for the model:

[https://gist.github.com/tistaharahap/8231027f0a8ec41db16ead993e365f27](https://gist.github.com/tistaharahap/8231027f0a8ec41db16ead993e365f27)

This `Hosted OpenWebUI` model is then empowered with what Open WebUI called Knowledge. Here are the documents I uploaded for it.

![Knowledge documents for pair programming](/content/images/2025/04/knowledge.png)

These documents are txt files generated from their corresponding Github repository below:

* [Polar SDK Python source code](https://github.com/polarsource/polar-python)
* [Clerk Python SDK source code](https://github.com/clerk/clerk-sdk-python)
* [Docker Docs](https://github.com/docker/docs)
* [Coolify Docs](https://github.com/coollabsio/coolify-docs)
* [Open WebUI source code](https://github.com/open-webui/open-webui)
* [LiteLLM source code](https://github.com/BerriAI/litellm)

To convert these repositories into txt files, I used this excellent Github repository:

[https://github.com/abinthomasonline/repo2txt](https://github.com/abinthomasonline/repo2txt)

Because I use this over and over, I ended up deploying it in my home lab's Coolify server. An AMD Ryzen 3700X goes a long way, has had this CPU since before the pandemic and it's still going strong!

![Web Search Tool](/content/images/2025/04/knowledge.png)

Another thing I make use of from Open WebUI is called `Tools`. With it, we have the capability of extending the LLMs we use in chats to interact with the outside world. This is usually known as `function calling` and Open WebUI has a marketplace for this.

I have my own locally deployed [SearxNG](https://x.com/searxng) installation and using this means the search results comes from search engines I've configured it with. Think of it as an aggregator of search results.

The cool kids might see this like an MCP (Model Context Protocol) and it's half right. The difference being this is not a standardized like how MCP is. Sweat not, Open WebUI does support MCP servers and SleekChat plans to support them too down the road in a way that is plug n play for the common users (or not).

Now the tools at my disposal to build is complete. Here's a screenshot of my first conversation:

![First conversation to BUILD](/content/images/2025/04/fuel.png)

Did I mention that SleekChat is powered by Coolify? Yes it is! This was the fuel that burned the first fire 🔥🔥🔥

At this point in time, there's no other complete self hosting solution out there covering production use cases the way Coolify does. At least not as polished. Sure there are bits and pieces that'll improve quality of life but then Coolify is built on top of other open source software that are just as powerful and extensible. I'll get to this later.

Since that first conversation, I have had more conversations and I try to keep the context as specific as possible. The first is for Coolify, the other one is for Polar, etc. But I need all of them from 1 knowledge base only as context to the LLM.

There's a party trick I learned from one of the conversations which is Coolify's lack of container status notifications (webhooks) to services. Since Coolify is built on top of Docker, the LLM suggested me to instead tap into Docker for container status updates. That became this repository that is now live in production:

[https://github.com/sleek-inc/coolify-docker-statuses](https://github.com/sleek-inc/coolify-docker-statuses)

Vibe coded much of the codebase in the conversation with me still copy pasting or correcting the codes on my own. Even though I like LLM Agents doing the work for me, I still want to understand what the codes are doing. I still did the wiring myself and refactored some of the codes to better suit my needs.

LLMs are getting better at coding but it's still early. To go to production, it's still going to take some time before an LLM agent can be fully autonomous to the point where all we have to do is supervise. What I do like about the generated codes is that the codes are commented well, it's not hard to built a mental model of what it's doing provided that it's a well used/known library/software you're dealing with. Try telling an LLM to use MarbleJS, io-ts and fp-ts to build an API? Nope, no go, I've tried.

There are times though when the LLM hallucinates even though I've set the temperature to 0.0. There are certain Coolify API endpoints that it told me that weren't there. I still had to go to Coolify's docs and confirm. But I can confidently say, LLMs got me to at least 60% with the remaining 40% wiring everything together.

The longest time was spent in getting the provisioning mechanism for new subscribers to work. There are integrations with third parties (Clerk for auth, Polar for payment, etc) and their Python SDK is less documented. Reading source codes became a neccessity.

Figuring out how to receive payouts also takes time. Polar uses Stripe for payouts and that means I have to have a special license here in Dubai to be eligible. After discussing back and forth with Kresna, we agreed we'll tackle this later when we get to a certain revenue threshold. The cool thing about Polar, the payout does not stop money coming in, we can go into production early.

The staging server was previously deployed at my home lab. It's just an LXC installed with Coolify running on my beefiest machine. My first sense of achievement is when I successfully configured the staging machine to be able to accept *.sleekchat.net into it. Coolify's docs here fits 1:1 to SleekChat's needs.

For every new subscribed instance, we assign it a subdomain. Imagine making DNS changes for every instance, [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) solves for this. Following the Coolify guide, all unnamed subdomains are routed to the staging server. This means my staging server never needs a public IP to be exposed to the Internet which is good for obvious reasons.

![Open WebUI instances deployed in Coolify](/content/images/2025/04/instances.png)

The subdomain assigned for instances is named after the Coolify application name. We keep the naming slugified and I use this Python library:

[https://github.com/fkapsahili/random-slugs](https://github.com/fkapsahili/random-slugs)

With over than 6 million unique combinations, if this ever breaks uniqueness, that'll be a happy problem to solve later on. I tried vibe coding a similar solution but I just don't have enough words to generate from and I'm not going to be wasting LLM tokens for this.

Once the provisioning mechanism was solved for, the rest of the work is integrating with the frontend. This was actually almost a smooth process thanks to FastAPI's built in OpenAPI docs generator. The surprise was not that, it was when I found out that I can't mount Docker volumes programmatically through Coolify's API without deploying apps using the Docker Compose build pack.

Coolify's docs says there multiple endpoints to create a new application. Boy did I struggle to figure out which is relevant for SleekChat's use case. I needed to mount a Docker volume for each of the Open WebUI instances to persist storage. The docs did not clearly say which API endpoint to aim to. This was yesterday before we went live to production today.

I started by choosing the `POST /applications/dockerimage` endpoint. To my surprise though, adding volumes for applications created in that manner is only applicable using the UI. So I tried another approach to instead use Docker Compose `POST /applications/dockercompose` which surprisingly did not create an application, it created a service. The volume defined in the Docker Compose yaml was created but there's no way to assign a domain to it programmatically using the API.

Remember when I said 40% of the time was spent in getting the provisioning mechanism to work? This was 80% of the 40%. There were little documentation about the behavior I posted on the previous paragraph noted in the docs site. So I thought why not read the source code directly?

[https://github.com/coollabsio/coolify/blob/v4.x/app/Http/Controllers/Api/ApplicationsController.php#L224](https://github.com/coollabsio/coolify/blob/v4.x/app/Http/Controllers/Api/ApplicationsController.php#L224)

When I read the source code above, it dawned on me that I didn't need to use the Docker Image/Compose endpoints. I just needed to use the regular `POST /applications/public` or `POST /applications/private` endpoints depending on the source itself whether it's on a public or private Github repository. Keyword there being the `build_pack` field.

To be fair, the docs site does include the `build_pack` field and I had assume that in the Docker Image/Deploy endpoints it was for the `build_pack` field. I was wrong and I'm glad I took the time to read the source code. My mind was triggered differently when reading source codes.

I made some tests and that turns out to be the right way of provisioning apps. But then, there's another quirk that didn't bother me much but worth mentioning. There are a few of them actually:

1. docker-compose.yaml - this takes precedence if the file is present in a source code repository. Even if you write your own yaml, it won't matter for Docker Compose build packs. Trick is to just create a public repo on Github containing only the Docker Compose yaml you want.
2. Coolify auto deployment only works on source codes based apps. Makes total sense, the webhooks are coming from Github and if you're deploying a Docker image, there's no webhooks configured from the Docker repository. Coolify does provide a webhook endpoint for apps to trigger an update.

Above said, I don't think LLMs alone can build SleekChat from scratch but I am rooting for LLMs to be able to do so in the future. This will shave away a significant part of writing software: time. In my head, my practical use case for a modular monorepo style development is for LLMs to write the libs (or otherwise known as modules) and I write the apps wiring the modules together. This is achievable today, I am honestly looking forward for LLMs to write the wiring codes but not today, yet.

## Audience

The mission is to make Open WebUI usable by non-tech people. We believe there are more steps to be done to get to that state. In general, I think these are the things that needs to happen:

1. Take away the complexity of deploying an Open WebUI instance - done
2. Write better documentations for SleekChat focusing on real world use cases, you don't know what you don't know - hasn't started
3. Enrich Open WebUI with more capabilities such as connecting to MCP servers as an addon using [mcpo](https://github.com/open-webui/mcpo) - hasn't started
4. LiteLLM as an addon to enable multiple models from different LLM providers to be used in Open WebUI - hasn't started
5. Bundle add ons with Open WebUI for subscriptions - hasn't started
6. Community oriented features - hasn't started

For audiences comfortable with the command line, SleekChat might not be the best option. But what I can tell you is that SleekChat just works, period.

Regardless of tech or non-tech audiences, I think SleekChat should inspire people to be able to use Open WebUI the way it has upskilled Kresna & I and changed our day-to-day. When we get SleekChat to that point, that's success right there. This brings us to the next section; pricing.

## Pricing Model

Right now, there are only 2 plans: monthly at $11.99 and yearly at $99.9. This is the base pricing for just the Open WebUI instance. This kind of pricing gives us approximately ~85% of profit margin. Most SaaS will optimize this to be more than 90% but we'll stay at ~85% for the forseeable future.

We want to lower the barrier of entry to drive people to use Open WebUI. There will be add ons as I wrote in the previous sections. These add ons would not only will be a quality of life enhancements but would also prove to be crucial to make use of Open WebUI effectively. Those add ons would also get bundled with Open WebUI later on to further reduce prices when subscribed together.

I can tell you this, I configured, launched and make use of Open WebUI and its add ons on my home lab by myself. To add to that, I deployed them in production at my day job to be used for various AI use cases. I know where it hurts when you manage them on your own and I plan to change that. This will be something I would also like to use myself.

## Doubts, Questions & Not Knowing

I don't know if SleekChat will be successful as a business or not but I do know that both Kresna and I wants to contribute back to the community. At the very least, there is now an option for a hosted Open WebUI service to advance the use of Open WebUI to more people, we make it simple.

But Open WebUI itself is quite technical? Wouldn't people need to configure it with API keys from LLM providers? Do people know how to do that?

I don't know, there's not enough feedback right now to answer the questions. I could also argue that the add ons that are going to be added might themselves become the hero. I just don't know yet and that's the fun part of doing this.

This is true; we don't know enough but we dove in head first because we can, why wouldn't you?

## Wrapping Up

To celebrate the launch, here's a discount code for you to try SleekChat for free for the first month:

`EIHAK9VY`

OR better yet, here's a link to checkout directly:

[https://buy.polar.sh/polar_cl_Qbyk0Yu8m8qxgUhFeAP3xtUVhsEvOtkqQPpXZ00vfyK](https://buy.polar.sh/polar_cl_Qbyk0Yu8m8qxgUhFeAP3xtUVhsEvOtkqQPpXZ00vfyK)

Your feedback will go a long way in getting SleekChat better, we're always open for it and we're not shy to #buildinpublic. Mention [@sleekchat_ai](https://x.com/sleekchat_ai) [@tista](https://x.com/tista) or [@kresnahendri](https://x.com/kresnahendri) for help or feedbacks.
