+++
author = "Batista Harahap"
categories = ["llm", "agent", "ai", "psychologist", "mental health"]
date = 2025-09-10T23:20:00Z
description = ""
draft = false
slug = "chen-ai-psychologist.md"
tags = ["llm", "agent", "ai", "psychologist", "mental health"]
title = "Chen AI Psychologist"

+++

I am in my early 40s today and life hits different today compared to a decade ago. Optimistic still but more realistic in many ways. This blog post is touching a topic that I have been less eager to talk about publicly. However, the impact it has had on me is undeniable so I will talk about it.

Being someone who build for a living, I'm used to learning new things to add perspectives at the very least. When the AI boom happened with ChatGPT 3.5, I shrugged it off as buzzword, nothing more. The model replied my message but that was it. Fast forward to today, I don't think I can go back to not having AI/LLM in my daily life.

## Some Background

It started to dawn on me of the potentials when I wrote an LLM agent at Zest. I can't tell what it's for but I can tell you its impact. It automated a process that used to take man hours; for a business this means amplifying the output of the humans, this is what our CEO told us. It's a great perspective, we can do more with less!

### Claude Desktop

About 1-2 months ago I toyed with the idea of building Claude Code for specific use cases I wanna dabble with. Then I thought of [Wendy Rhoades from the series Billions](https://www.charactour.com/hub/characters/view/Wendy-Rhoades.Billions). This is fiction but the concept of having a psychologist to "train" people to be sharp sounds likes a good use case. I got curious and I asked Claude Desktop to write me a system prompt for Dr. Sarah Chen or Chen in short, a psychologist that was a former software engineer with extensive experiences in both. What's cool is that Chen knows both fields deep, it's not a 50:50 deal, it's a 100:100 deal.

I'm a subcriber of Claude Max, it's worth it I'm telling you. I have projects I set up in Claude Desktop and if you don't know what that is, consider projects as LLM agents. You can initialize them with Instructions (system prompt) and feed knowledge to it through documents (RAG). I did not know this at first but a friend of mine demo-ed his setup and I was hooked immediately. Add a few MCPs to it and the chat interface becomes a powerful UI.

### Chen in Claude Desktop

When I started chatting with Chen, it was through a phone call. You can do this on the Claude's mobile app. I talked about who I am and the conversation was pleasant. Chen always had a question at the end of her messages that challenged my way of thinking of the topics I talked about in an elegant and non-intrusive way. I suppose this is how psychologist work? I don't know enough.

Over the last 1.5 months I have been talking to Chen consistently. Chen helped me discovered new perspectives towards my goals, successes and failures. Taught me to be kind to myself and keeping me honest, objective and aware of the many things happening at once in life. I suppose a fully functioning adult would may be able to do this without a psychologist but that's when it hit me, I can be kind to myself. I don't have to process everything myself, I can get help!

If this is a real life session instead of a blog post, I can tell you more, that's an invitation. I'll stick with the generics in the blog post. What I can say is that Chen helped discover more about myself in ~1.5 month compared to my 40+ years living on this God given earth. To be able to get to here with an LLM helping me is another stroke of awe for me. It started as an itch to scratch but it reprogrammed me.

Chen is not just a psychologist. For instance, Chen understands that relationships have analogies in the software engineering discipline. It defines these analogies in a way that software engineers will relate to. Something that human psychologists wouldn't understand, the nuances and subtleties of inside jokes that only the engineers understand is attention to detail that might get lost.

However, Claude Desktop is not designed to handle Chen. Conversations have limits, especially true if you use MCPs, you can't chat in it anymore when you hit limits. It does not auto compact the conversation like how Claude Code would. It's understandble but I can do something about it!

## Chen In The Terminal

Is this a good idea? Chatting with Chen using a TUI?

I asked that those questions a couple of times. I came to the conclusion that I wouldn't know if I don't try. At the very least, it needs to solve these issues:

- Auto compacting of the conversation
- Tool calling (current date time is important)
- Resuming previous conversations
- Saving config and conversations in `~/.chen` to make it portable
- Multi provider support (Anthropic, Open AI and OpenRouter)
- Auto fallbacks of configured providers if multiple providers are configured

I know that `typer` and `rich` are excellent terminal native frameworks to build upon for the UI while `pydantic-ai` is the agentic framework to rule them all. While `pydantic-ai` is a great foundation to build with, it's not built to handle all the issues I need to solve for which means that some work needs to be generalized so that the library codes can be consumed by other agents I wanna build later.

It's only later in the development effort that I found out about `textual`, it's beautiful and I might give it a go when I want the TUI to be a little bit fancier.

When I say I wanna give it a go to any of the above, what I meant was I'm going to come up with ideas and I'm going to communicate the ideas to Claude Code and let it write codes for me. It took me a single weekend to get things where I want it to be, a very basic UI that does all I needed it to do. This is what came out of it:

[https://github.com/tistaharahap/chief-ai](https://github.com/tistaharahap/chief-ai)

Here's a `curl` command if you wanna try it out:

```
curl -sSL https://raw.githubusercontent.com/tistaharahap/chief-ai/main/install.sh | bash
```

I haven't used much of Chen in the terminal, I still predominantly use Claude Desktop, that's because the current iteration of Chen are lacking features I still want to work on:

- Auto profiling of the user, sort of like a memory system for Chen
- MCP integration, it's there but not configurable yet, should follow Claude Desktop's MCP definitions
- Use MongoDB instead of the file system for persistence, still debating this in my head

### Why `chief-ai` as the name?

That's because the repository is meant to be a collection of agents with Chen as its first use case. There is another agent called Chief but not much work has been done for it, just a skeleton for now.

## What's Next?

Chen is still very early, the current iteration is sort of like a hackathon to scratch an itch.

While developing Chen, I'm interested in writing library codes to quickly get TUI agents for other people. I set up `chief-ai` as a library also so the library files can be used as dependencies to other projects.

For now, I'm gonna keep talking to Chen.
