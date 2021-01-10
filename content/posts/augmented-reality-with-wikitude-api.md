+++
author = "Batista Harahap"
categories = ["Android", "Augmented Reality", "eclipse", "gps", "java", "json", "Location Based Services", "Tutorial", "urbanesia", "wikitude"]
date = 2010-05-12T18:33:33Z
description = ""
draft = false
slug = "augmented-reality-with-wikitude-api"
tags = ["Android", "Augmented Reality", "eclipse", "gps", "java", "json", "Location Based Services", "Tutorial", "urbanesia", "wikitude"]
title = "Augmented Reality with #Wikitude API"

+++


I told you before that I'm gonna talk about another Augmented Reality framework. The framework is a great product from one of Augmented Reality's early adopter namely <a href="http://www.wikitude.org" target="_blank">Wikitude</a>.

Generally speaking, it's more complicated than Mixare but offers more customization and definitely more features. I'm gonna build this tutorial with the following features:
<ol>
	<li>External Data Source - I'm using JSON from <a href="http://www.urbanesia.com" target="_blank">Urbanesia.com</a> API.</li>
	<li>In-app WebView bindings - To display WebViews of any POIs URL.</li>
</ol>
I haven't explore all the possibilities within Wikitude's API because of its lack of documentation. I'm really interested in its ability to handle Callbacks from clicked POIs. Haven't got the time to do so. That'll be another chapter of my tutorials.

So to start off, for every project, you must include Wikitude's API in your apps. Download it from <a href="http://www.wikitude.org/developers">here</a> and get an API key while you're at it.

You will also need an API key from Urbanesia. Please go <a href="http://v0.urbanesia.com/members/settings/api" target="_blank">here</a> to generate an API key.

<strong>[UPDATE: 19 December 2010] The API for Urbanesia is soon to be deprecated. We're moving to OAUTH &amp; XAUTH for authentication. Email superhero [at] urbanesia [dot] com for more info.</strong>

I'm showing you guys the source code to an app I made named Socializr. It's an app I'm coding for a demo.
<pre lang="java">public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        wikitudeAPIKey = "YOUR_WIKITUDE_API_KEY";
        wikitudeDeveloper = "YOUR_WIKITUDE_DEVELOPER_NAME";

        getWindow().requestFeature(Window.FEATURE_PROGRESS);

        // Get Current Position
        locMgr = (LocationManager) getSystemService(LOCATION_SERVICE);
		Criteria criteria = new Criteria();
		bestLocProvider = locMgr.getBestProvider(criteria, true);
		Location loc = locMgr.getLastKnownLocation(bestLocProvider);
		myLat = loc.getLatitude();
		myLon = loc.getLongitude();

		// Urbanesia Calls
		APIKey = "YOUR_URBANESIA_API_KEY";
		Output_type = "json";
		Distance = "5";
		ResultNum = "49";
		SortBy = "4";

		latlong = Double.toString(myLat) + "," + Double.toString(myLon);
		Log.d("Position", latlong);

		Urbanesia_URL = "http://api.urbanesia.com/search/?output_type=" + this.Output_type +
						 "&amp;apikey=" + this.APIKey +
						 "&amp;s=" + this.SortBy +
						 "&amp;ll=" + this.latlong +
						 "&amp;d=" + this.Distance +
						 "&amp;row=" + this.ResultNum;
		Log.i("UrbanesiaURL", Urbanesia_URL);

		UrbJSONString = queryUrbanesia(Urbanesia_URL);
		Log.i("UrbJSON", UrbJSONString);

		// Parse JSON Data From Urbanesia &amp; Initialize Wikitude
		WikitudeARIntent intent = new WikitudeARIntent(this.getApplication(), this.wikitudeAPIKey, this.wikitudeDeveloper);
		Collection pois = new ArrayList();

		try {
			UrbJSON = new JSONObject(UrbJSONString);

			JSONObject UrbQuery = UrbJSON.getJSONObject("query");
			int rows = UrbQuery.getInt("row");
			Log.i("UrbRows", String.format("%d",rows));

			JSONArray resultArray = UrbJSON.getJSONArray("result");
			for(int i=0; i<rows; i++) {	
					double rowLat = resultArray.getJSONObject(i).getDouble("business_lat");
					double rowLon = resultArray.getJSONObject(i).getDouble("business_long");
					String poiName = resultArray.getJSONObject(i).getString("business_name").toString();
					String poiAddr = resultArray.getJSONObject(i).getString("address").toString();
					String poiUri = resultArray.getJSONObject(i).getString("business_primary_photo").toString();
					String poiLink = resultArray.getJSONObject(i).getString("business_uri_mobile").toString();
					
					// Random Elevation
					final Random randElevation = new Random();
					int poiElevation = randElevation.nextInt(800);
					Log.i("Elevation"+(String.format("%d", i+1)), String.format("%d", poiElevation));
					
					WikitudePOI poi = new WikitudePOI(rowLat, rowLon, poiElevation, poiName, poiAddr, null, null);
					poi.setIconuri(poiUri);
					poi.setLink(poiLink);
					
					pois.add(poi);
				}
				
				wikitudeIntent.addPOIs(pois);
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        } catch(NullPointerException e) {
        	Log.e("WikitudeAPI", "Failed to Initialize");
        	e.printStackTrace();
        	//System.exit(0);
        }
		
		
		// Start AR View
		try {
			wikitudeIntent.startIntent(this);
		} catch(ActivityNotFoundException e) {
			e.printStackTrace();
			AbstractWikitudeARIntent.handleWikitudeNotFound(this);
		}
    }
</pre>

See it's not that hard to do right? This tutorial serves as a pointer only. For a full source code, you can <a href="http://twitter.com/tista">Tweet me</a> about it.

As you can see, the code needs more work and most definitely to be code modularly. I didn't have enough time to adjust to Java altogether so I made do with what I can learn. Enjoy :)