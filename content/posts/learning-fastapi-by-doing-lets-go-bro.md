+++
author = "Batista Harahap"
categories = ["python", "fastapi", "travel"]
date = 2021-01-02T05:17:14Z
description = ""
draft = false
image = "/images/2021/01/123-let39s-go-imaginary-text.jpg"
slug = "learning-fastapi-by-doing-lets-go-bro"
tags = ["python", "fastapi", "travel"]
title = "Learning FastAPI By Doing - Let's Go Bro!"

+++


A few days ago I published a Python Sanic backend and an Android app of a weekend project I did a few years ago. The project was simply directing people to a random cheapest return flights from where they are, set a budget and just press `Go`. It was written when async Python was beginning to mature. So I thought why not learn something new (FastAPI) and compare it with Sanic.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is the Android app <a href="https://t.co/bA2cBt7SyS">https://t.co/bA2cBt7SyS</a></p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1344566520307884032?ref_src=twsrc%5Etfw">December 31, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Let's Go Bro!

Here's a link to [the repository](https://github.com/tistaharahap/letsgobro-api). The `README.md` covers how to run the API while here I wanna focus on the journey. As I write this, the end result is not even 24 hours old so memory is still fresh.

### PyDantic

[PyDantic](https://pydantic-docs.helpmanual.io/) is foundation of FastAPI. Request/Response are modeled with it including with validations. That said, it's reusable across the entire codebase which makes responses consistent. **BIG PLUS!**

I made a typical noob mistake with it.

```python
class Airport(BaseModel):
    iata = str
    name = str
```

```python
class Airport(BaseModel):
    iata: str
    name: str
```

Saw which one is wrong? Took me a bit to get used to modeling with native python types. I like it!

### Routing

Coming from Flask and Sanic, when building APIs, I'm used to declaring endpoints explicitly. In FastAPI, it's just another (decorated) function or at least that's how it seems.

```python
Airports = APIRouter()


@Airports.get('/airports', response_model=List[AirportResponse])
async def airports(latitude: float, longitude: float, max_distance_in_km: int = 50):
    await connect_to_mongodb()

    nearest_airports = await Airport.find_nearest_airport(latitude=latitude,
                                                          longitude=longitude,
                                                          max_distance_in_km=max_distance_in_km)

    await disconnect_mongodb()

    return nearest_airports
```

Looking at the flow of the codes, this is pretty much how it flows too when I code backends with RxJS. Since FastAPI is still new, there are not much libraries out there yet. Had the choice of using [Motor](https://docs.mongodb.com/drivers/motor) but I stuck with [MongoEngine](http://mongoengine.org/) since I wanted to learn about FastAPI first. Had to be careful to code database connection and queries correctly using a sync library on an async environment.

The codes above are for `GET` requests with query parameters, let's see how a `POST` request looks like.

```python
@Flights.post('/flights', response_model=FlightSearchResponse)
async def flights(request: FlightSearchRequest):
    await connect_to_mongodb()

    min_distance_in_km, max_distance_in_km = get_distances_from_budget(budget=request.budget)
    destinations = await Airport.find_destinations(origin=request.origin,
                                                   min_distance_in_km=min_distance_in_km,
                                                   max_distance_in_km=max_distance_in_km)

    def _build_destination(origin: str, destination: dict, departure_date: str, returning_date: str, adults: int,
                           children: int, infants: int):
        forward_link = forward(origin=origin,
                               destination=destination.get('iata'),
                               departure_date=departure_date,
                               returning_date=returning_date,
                               adults=adults,
                               children=children,
                               infants=infants)
        return {
            'airport': destination,
            'origin': origin,
            'destination': destination.get('iata'),
            'link': forward_link
        }

    destinations = [_build_destination(origin=request.origin,
                                       destination=row,
                                       departure_date=request.outbound_date,
                                       returning_date=request.inbound_date,
                                       adults=request.adults,
                                       children=request.children,
                                       infants=request.infants) for row in destinations]

    await disconnect_mongodb()

    return {
        'budget': request.budget,
        'outbound_date': request.outbound_date,
        'inbound_date': request.inbound_date,
        'adults': request.adults,
        'children': request.children,
        'infants': request.infants,
        'destinations': destinations
    }
```

It's so simple right? The function focuses on the flow only. Could've hidden some complexity out of the function though.

## Flight Search

Let's take a look what the client needs to do to get flight recommendations.

### Find Nearest Airport

![Find Nearest Airport](/content/images/2021/01/Screen-Shot-2021-01-02-at-19.05.16.png)

I acknowledge that the closest might not be the most suitable. The request above is made with Monas coordinates. There are more options from `CGK` compared to `HLP` so the choice of airport is at the client's discretion.

### Get Flight Recommendations

![Flight Recommendations - IDR 1.5 mio](/content/images/2021/01/Screen-Shot-2021-01-02-at-19.08.50.png)

With IDR 1.5 mio, most of the recommendations are local destinations. What happens with IDR 5 mio? Let's have a look!

![Flight Recommendations - IDR 5 mio](/content/images/2021/01/Screen-Shot-2021-01-02-at-19.10.37.png)

I chose `SUB` as the origin, there isn't much international flight destinations from there but then the API still shows up non-direct routes. The flight recommendations works on a radius based on the budget. Here are the codes.

```python
def get_distances_from_budget(budget: int):
    distances = (100, 1000)

    if 0 < budget <= 1500000:
        distances = (100, 1000)
    elif 1500000 < budget <= 2000000:
        distances = (800, 1250)
    elif 2000000 < budget <= 3000000:
        distances = (1000, 1750)
    elif 3000000 < budget <= 4000000:
        distances = (1500, 2250)
    elif 4000000 < budget <= 5000000:
        distances = (2000, 2750)
    elif 5000000 < budget <= 6000000:
        distances = (2500, 3250)
    elif 6000000 < budget <= 7000000:
        distances = (3000, 3750)
    else:
        distances = (3500, 15000)

    return distances
```

It's just a rule engine but an effective one. The logic above was coded 4 years ago and still rings true today.

## Try it!

```shell
$ git clone git@github.com:tistaharahap/letsgobro-api.git
$ cd letsgobro-api
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ MONGO_USER=user MONGO_PASSWORD=password MONGO_HOST=host MONGO_DB=db python scripts/airports.py # seed mongodb, only needed once
$ MONGO_USER=user MONGO_PASSWORD=password MONGO_HOST=host MONGO_DB=db python app.py
```

I used MongoDB Atlas' Free tier since this is just a weekend project. You should try too.

---

Thinking about doing a frontend for it but I don't think I will. A REST client will do the job for me when I need recommendations.