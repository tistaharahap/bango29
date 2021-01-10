+++
author = "Batista Harahap"
categories = ["acer", "acerid", "Android", "asynctask", "hdpi", "java", "ldpi", "magpierss", "mdpi", "php", "phpthumb", "rss", "sourceforge", "Tutorial", "xhdpi"]
date = 2011-05-26T17:26:04Z
description = ""
draft = false
slug = "android-asynctask-is-a-beauty-part-1"
tags = ["acer", "acerid", "Android", "asynctask", "hdpi", "java", "ldpi", "magpierss", "mdpi", "php", "phpthumb", "rss", "sourceforge", "Tutorial", "xhdpi"]
title = "Android - AsyncTask Is A Beauty - Part 1"

+++


Since last weekend, I've been coding more on Android and although the topic about AsyncTask is nothing new, I just wanna bring it up again to appreciate its simplicity and more importantly in real world usable best practice. So I decided to create an RSS client from FeedBurner and this time to get feeds from <a href="http://www.acerid.com">AcerID.com</a>.

The application basically loads all the feeds with its first Activity, show it with the second activity and another helper Activity to send direct emails for questions related with Acer products. Do mind the layout, it's quite plain but it's usable nonetheless. So before going on with the tutorial, I'm gonna show some screenshots from and MDPI emulator running Eclair and XHDPI emulator running HoneyComb.

<strong>MDPI</strong>

<a href="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-AcerID.png"><img class="size-thumbnail wp-image-675" title="mdpi-AcerID" src="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-AcerID-150x150.png" alt="mdpi-AcerID" width="150" height="150" /></a>

<a href="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-Hacktivate.png"><img class="size-thumbnail wp-image-676" title="mdpi-Hacktivate" src="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-Hacktivate-150x150.png" alt="mdpi-Hacktivate" width="150" height="150" /></a>

<a href="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-webview.png"><img class="size-thumbnail wp-image-677" title="mdpi-webview" src="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-webview-150x150.png" alt="mdpi-webview" width="150" height="150" /></a>

<a href="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-Ask.png"><img class="size-thumbnail wp-image-678" title="mdpi-Ask" src="http://www.bango29.com/go/wp-content/uploads/2011/05/mdpi-Ask-150x150.png" alt="mdpi-Ask" width="150" height="150" /></a>

<strong>XHDPI</strong>

<a href="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-AcerID.png"><img class="alignnone size-thumbnail wp-image-679" title="xhdpi-AcerID" src="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-AcerID-150x150.png" alt="xhdpi-AcerID" width="150" height="150" /></a> <a href="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Hacktivate.png"><img class="alignnone size-thumbnail wp-image-680" title="xhdpi-Hacktivate" src="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Hacktivate-150x150.png" alt="" width="150" height="150" /></a> <a href="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Webview.png"><img class="alignnone size-thumbnail wp-image-681" title="xhdpi-Webview" src="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Webview-150x150.png" alt="" width="150" height="150" /></a> <a href="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Webview1.png"><img class="alignnone size-thumbnail wp-image-682" title="xhdpi-Webview" src="http://www.bango29.com/go/wp-content/uploads/2011/05/xhdpi-Webview1-150x150.png" alt="" width="150" height="150" /></a>

The first task before everything else must be the core function of this tiny application to read RSS feeds, that is why I started out by doing it both in PHP and Java. I have a reserved hatred towards XML and its derivative, it makes codes messy, that's why I'm doing the messy stuff with PHP and outputting it into a more "civil" JSON for the app to process.

Luckily for me, processing RSS in PHP is a breeze with this simple library <a title="MagpieRSS" href="http://magpierss.sourceforge.net" target="_blank">MagpieRSS</a>. I incorporated the library to do less code and efficiency. Since RSS feeds is self contained with images in its original sizes, I will need to generate thumbnails to make it better looking with Android mobile phones, for this purpose I incorporated <a title="PhpThumb" href="http://phpthumb.sourceforge.net" target="_blank">PhpThumb</a>. Here is the final PHP source code.
<pre lang="php" line="1">// index.php
require_once 'rss_fetch.inc';

$url = (isset($_GET['url']) && $_GET['url'] != '') ? $_GET['url'] : 'http://feeds.feedburner.com/acerid';
$rss = fetch_rss($url);

foreach($rss->items as &$r) {
	// Parse image
	$doc = new DOMDocument();
	@$doc->loadHTML($r['content']['encoded']);
	$tags = $doc->getElementsByTagName('img');
	$first = true;
	foreach($tags as $tag) {
		$root = "http://bango29.com/rss/";

		if($first) {
			$r['image'] = $root . "thumb/phpThumb.php?zc=1&w=150&h=150&src=" . $tag->getAttribute('src');
			$r['content']['encoded'] = str_replace($tag->getAttribute('src'), $r['image'], $r['content']['encoded']);
			$first = false;
		} else {
			$rep = $root . "thumb/phpThumb.php?w=150&amp;src=" . $tag->getAttribute('src');
			$r['content']['encoded'] = str_replace($tag->getAttribute('src'), $rep, $r['content']['encoded']);
		}
	}
	$r['body'] = base64_encode($r['content']['encoded']);

	unset($r['content']);
	unset($r['wfw']);
	unset($r['slash']);
	$r['link'] = $r['feedburner']['origlink'];
	unset($r['feedburner']);
	unset($r['summary']);
	unset($r['atom_content']);
	unset($r['comments']);
	unset($r['pubdate']);
	$r['writer'] = $r['dc']['creator'];
	unset($r['dc']);
	unset($r['category']);
	$r['date_friendly'] = date("l, j F Y G:i:s", $r['date_timestamp']);
}

$out['rss'] = $rss->items;

echo json_encode($out);</pre>

If you see from the code above, I put an extra effort to Base64 encode the actual article content. I did it for a very obvious reason to keep the data free from encoding and or character sets problems. Now that the server side coding is done, I will need to do the client side coding and created a class named RssDownloader.java. It basically reads out all the RSS contents and returns either a String or a JSONObject.

<pre lang="java" line="1">
package com.bango.acerid;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONException;
import org.json.JSONObject;

public class RssDownloader {
	
	private String url;
	
	public RssDownloader(String url) {
		this.setUrl(url);
	}
	
	public JSONObject getRssJson() throws ClientProtocolException, IOException, JSONException {
		String response = this.sendRequest(getUrl(), "");
		return new JSONObject(response);
	}
	
	public String getRssString() throws ClientProtocolException, IOException {
		return this.sendRequest(getUrl(), "");
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public String getUrl() {
		return url;
	}
	
	private String sendRequest(String url, String postString)
		throws ClientProtocolException, IOException {
		HttpClient client = new DefaultHttpClient();
		
		if (postString.compareTo("") != 0) {
			// GET & POST Request
			HttpPost post = new HttpPost(url);
		
			// Create POST List
			List<NameValuePair> pairs = new ArrayList<NameValuePair>();
			String[] exp = postString.split("&");
			int max = exp.length;
			for (int i = 0; i < max; i++) {
				String[] kv = exp[i].split("=");
				pairs.add(new BasicNameValuePair(kv[0], kv[1]));
			}
			post.setEntity(new UrlEncodedFormEntity(pairs));
		
			// Get HTTP Response & Parse it
			HttpResponse response = client.execute(post);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				InputStream instream = entity.getContent();
				String result = convertStreamToString(instream);
				// Log.i("HTTPError", "Result of conversion: [" + result + "]");
		
				instream.close();
				return result;
			}
		} else {
			// GET & POST Request
			HttpGet get = new HttpGet(url);
		
			// Get HTTP Response & Parse it
			HttpResponse response = client.execute(get);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				InputStream instream = entity.getContent();
				String result = convertStreamToString(instream);
				//Log.v("HTTPError", "Result of conversion: [" + result + "]");
		
				instream.close();
				return result;
			}
		}
		
		return "";
	}

	private String convertStreamToString(InputStream is) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(is));
		StringBuilder sb = new StringBuilder();
		
		String line = null;
		try {
			while ((line = reader.readLine()) != null) {
				sb.append(line);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				is.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return sb.toString();
	}

}
</pre>

Since now the app is ready to consume RSS feed, it's now time to do our first activity AcerID which essentially download RSS feeds using AsyncTask and pass the data to another activity. Here are the codes.

<pre lang="java" line="1">
package com.bango.acerid;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;

public class AcerID extends Activity {
	protected final static String FEED_URL = "http://bango29.com/rss/index.php?url=http://feeds.feedburner.com/acerid";
	private String res = "";
	private RssDownloader rss;
	
    /** Called when the activity is first created. */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        // waku
        execStreamDownload();
    }
    
    private void execStreamDownload() {
    	rss = new RssDownloader(FEED_URL);
        new RssDownload().execute(rss);
    }
    
    protected void onResume(Bundle icicle) {
    	super.onResume();
    	if(res == null || res == "")
    		execStreamDownload();
    	else
    		hacktivate(res);
    }
    
    protected void onRestart() {
    	super.onRestart();
    	if(res == null || res == "")
    		execStreamDownload();
    	else
    		hacktivate(res);
    }
    
    private class RssDownload extends AsyncTask<RssDownloader, Void, String> {
    	private String ret = "";
    	
		@Override
		protected String doInBackground(RssDownloader... params) {
			DeviceInfo d = new DeviceInfo(AcerID.this);
			d.prefCheck();
			d = null;
			
			try {
				ret = params[0].getRssString();
				Thread.sleep(1000);
			} catch (ClientProtocolException e) {
				return "error";
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			return ret;
		}
		
		protected void onPostExecute(String ret) {
			Log.v("RssDownloadTask", ret);
			AcerID.this.hacktivate(ret);
		}
    	
    }
    
    private void hacktivate(String ret) {
    	setRes(ret);
    	Intent i = new Intent(this, Hacktivate.class);
    	i.putExtra("listData", ret);
    	startActivity(i);
    }

	public void setRes(String res) {
		this.res = res;
	}

	public String getRes() {
		return res;
	}
	
	public void onBackPressed() {
		moveTaskToBack(true);
	}
}
</pre>

As you can see, the codes above basically speaks for itself with AsyncTask doing exactly what it's meant to do without much change. This activity is inclusive of a onResume() and onRestart() to check whether the RSS data has is still there or not due to the Android's Garbage Collector behavior, we can't know for sure if the data is still there.

There is also another class I created called DeviceInfo.java to gather unique information about devices using this application. However that particular class is not finished yet so the source code is still not final.

This wraps up the first part of this tutorial and will continue to discuss Hacktivate activity for a further more creative way to hack up AsyncTask. Stay tuned!