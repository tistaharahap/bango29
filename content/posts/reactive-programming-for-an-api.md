+++
author = "Batista Harahap"
categories = ["rxjs", "node.js", "reactive", "frp", "functional", "tech", "codes"]
date = 2017-11-26T07:53:54Z
description = ""
draft = false
image = "/images/2017/11/687474703a2f2f692e696d6775722e636f6d2f634c344d4f73532e706e67.png"
slug = "reactive-programming-for-an-api"
tags = ["rxjs", "node.js", "reactive", "frp", "functional", "tech", "codes"]
title = "Reactive Programming for an API"

+++


I have to admit, when I first heard about Reactive, Rx, Linq, etc I was reluctant to learn it. All kinds of materials were mostly theoretical and I failed to get a grasp of the whole thing. Well I still am, I still can't explain what a `monad` is. That said, this blog post is all about practicality of a pragmatist.

[PRISM](https://www.prismapp.io) is not more than just a product, building it have brought more opportunities. One of it dictates the necessity to do multiple external API requests in order to produce a response. This made me think, how can I make this concurrent if not parallel with a codebase that is relatively `easy` to understand for anyone interested in contributing?

One of our tech lead has actually wrote his API with Rx. So I had a conversation with him to know more about it. I talked for 15-20 minutes and spent another 3 hours to produce these line of codes:

```javascript
import createResponse from '../response'

const rootHandler = (requestObservable) => {
  return requestObservable.map((it) => {
    return createResponse(it.response)
  })
}

export default rootHandler
```

After getting that `aha` moment, it felt like lightning has struck me. Before continuing, here are the tech stack I choose to learn about Rx.

```
* NodeJS 8.9.x
* Koa 2.4.x
* Full ES6
```

Please let me advise you to use [Visual Studio Code](https://code.visualstudio.com/) for this practice. It saved me a lot of time to get to code in best practice with NodeJS.

---

First and foremost of my enlightening is to think of data as streams. Those streams can be just an object or a collection of objects. This is crucial in my learning, this means I can convert anything into an `Observable` to manipulate.

```javascript
const observableJson = Rx.Observable.of({ name: 'Tista' })
const observableArray = Rx.Observable.from([{ name: 'Tista' }, { name: 'Harahap' }])
```

Second, avoid mutability at all costs, even within a lambda's scope. This will empower your codes to have no unintended side effects. An example of intended side effects is logging, it does not warrant a seat within the code.

```javascript
const anApiCallObservable = (from, to) => {
  const opts = {
    url: config.apiUrl,
    form: {
      to,
      from,
    },
  }

  return Rx.Observable.fromPromise(request.post(opts))
    .do(() => {
      logger.info(`Making API call from ${opts.form.from} to ${opts.form.thru}`)
    })
}
```

Third is everything is composable. Take a moment to imagine this correctly. The next line of codes should explain itself pretty clearly.

```javascript
const concurrentObservable = Rx.Observable.from(requestBody)
    .switchMap((body) => {
      const [originObservable, destinationObservable] =
        createOriginDestinationObservable(body.origin, body.destination)

      return Rx.Observable.zip(originObservable, destinationObservable)
        .map((result) => {
          const originResults = result[0].hits.hits.map(x => x._source).slice(0, 3)
          const destinationResults = result[1].hits.hits.map(x => x._source).slice(0, 3)

          return [originResults, destinationResults]
        })
        .switchMap((results) => {
          const [originResults, destinationResults] = results
          return anApiCallObservable(originResults[0], destinationResults[0])
        })
        .map((results) => {
          return JSON.parse(results)
        })
    })
```

The codes above is composed of codes from the second example: `anApiCallObservable()` and another one called `createOriginDestinationObservable()`. Now this is reusability without the baggage of threading. You don't even have to worry about implementation pitfalls. NodeJS is single threaded which makes concurrency as the only option.

RxJs have these schedulers, [link](https://github.com/ReactiveX/rxjs/blob/master/doc/scheduler.md):

* `null` - By not passing any scheduler, notifications are delivered synchronously and recursively. Use this for constant-time operations or tail recursive operations.
* `Rx.Scheduler.queue` - Schedules on a queue in the current event frame (trampoline scheduler). Use this for iteration operations.
* `Rx.Scheduler.asap` - Schedules on the micro task queue, which uses the fastest transport mechanism available, either Node.js' process.nextTick() or Web Worker MessageChannel or setTimeout or others. Use this for asynchronous conversions.
* `Rx.Scheduler.async` - Schedules work with setInterval. Use this for time-based operations.

---

I'm still learning about the power of Reactive Programming, this quick intro is already enough for me to start imagining API calls to and from as just another data source. Have a read about [what an operator is](https://github.com/ReactiveX/rxjs/blob/master/doc/operators.md), this will bring happy experiences.

Cheers!
