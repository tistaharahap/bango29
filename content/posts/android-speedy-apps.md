+++
author = "Batista Harahap"
date = 2013-07-28T14:09:35Z
description = ""
draft = false
slug = "android-speedy-apps"
title = "Android Speedy Apps"

+++


The first time I coded for Android was with Eclair (2.1). Bought a Nexus One to develop some apps with it. Nowadays, Android has gone a long way but still, most fundamentals to make your apps snappy still applies. I'm going down memory lane to post some of the optimizations producing effective and efficient codes.

<h2>Static Method &amp; Properties</h2>

Like in any platform, memory is the key to performance. The better we utilize memory, the better the performance. With Android, utilizing memory is as simple as defining the right static class properties and methods. When you set a static property or method, it will always be referenced once at run time. Hence, all the references are already in the memory before you call any of them.

I usually have a <code>Utils</code> class defined with all my Android apps. Every property and method are static. Android comes with a pretty handy <code>Log</code> class to log to <code>stdout</code>. The first parameter for most of the methods is a String tag. It gets in the way for me. So here's an example.

<pre lang="java">
public class Utils {
	public static String TAG = "APP_NAME";
	public static void logger(String msg) {
		Log.v(TAG, msg);
	}
}
</pre>

<h2>Interface (Listeners)</h2>

When I first learned about Java Interfaces, I fell in love at first sight. It allows me to create a very neat way of communicating between classes, activities, etc. I am building a Finance application to talk with Yahoo Finance through <a href="http://developer.yahoo.com/yql/console/?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)&env=store://datatables.org/alltableswithkeys" title="Yahoo Finance YQL" target="_blank">YQL Queries</a>.

Here's an example from an unfinished code I'm working on.
<pre lang="java">
package com.bango.yql;

import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

import android.app.Activity;
import android.content.Context;

import com.bango.stocksquotes.DBHelper;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

public class YQLFinance {

    private static String BASE_URL = "http://query.yahooapis.com/v1/public/yql";
    private static String QUERY = "select * from yahoo.finance.quote where symbol in (%s)";

    private static AsyncHttpClient http = new AsyncHttpClient();

    private static QuotesResponseListener caller;

    public static interface QuotesResponseListener {
        void onQuotesResponseSuccess(List<Long> ids);

        void onQuotesResponseFailure(Throwable e);

        Context getContext();
    }

    public static void attach(Activity act) {
        if (act instanceof QuotesResponseListener) {
            caller = (QuotesResponseListener) act;
        } else {
            throw new ClassCastException("The calling activity must implement YQLFinance.QuotesResponseListener");
        }
    }

    public static List<String> getQuoteSymbols() {
        if (caller == null)
            throw new ClassCastException("The calling activity must implement YQLFinance.QuotesResponseListener");

        DBHelper helper = new DBHelper(caller.getContext());
        return helper.getQuoteSymbols();
    }

    public static void getQuotes(List<String> quotes) throws
            IllegalArgumentException, ClassCastException {
        if (caller == null)
            throw new ClassCastException("The calling activity must implement YQLFinance.QuotesResponseListener");

        RequestParams params = new RequestParams();
        params.put("format", "json");
        params.put("env", "store://datatables.org/alltableswithkeys");

        if (quotes.size() == 0)
            throw new IllegalArgumentException("Quotes must have some value please.");
        else {
            String q = "";
            for (String quote : quotes) {
                q += "'" + quote + "',";
            }
            q = q.substring(0, (q.length() - 1));
            String yql = String.format(QUERY, q);
            params.put("q", yql);
        }

        http.get(BASE_URL, params, quotesHandler);
    }

    private static JsonHttpResponseHandler quotesHandler = new JsonHttpResponseHandler() {
        @Override
        public void onSuccess(JSONObject res) {
            if (caller == null)
                throw new ClassCastException("The calling activity must implement YQLFinance.QuotesResponseListener");

            DBHelper helper = new DBHelper(caller.getContext());
            List<Long> ids = new ArrayList<Long>();

            JSONArray quotes = res.optJSONObject("query").optJSONObject("results").optJSONArray("quote");
            for (int i = 0; i < quotes.length(); i++) {
                JSONObject row = quotes.optJSONObject(i);
                if (row != null) {
                    String symbol = row.optString("symbol", "");
                    float price = Float.parseFloat(row.optString("LastTradePriceOnly", "0"));
                    ids.add(helper.addNewQuote(symbol, price));
                }
            }

            caller.onQuotesResponseSuccess(ids);
        }

        @Override
        public void onFailure(Throwable e, JSONObject res) {
            if (caller == null)
                throw new ClassCastException("The calling activity must implement YQLFinance.QuotesResponseListener");

            caller.onQuotesResponseFailure(e);
        }
    };

}
</pre>

YES, I also hate having to do the same code over and over like what I'm doing to always null-check the <code>caller</code> property. Could've done a static method to do this but verbosity wins this time. I want to be verbose more than not being redundant because it train my mind to always watch out for danger.

<h2>Use Native UI</h2>

A few days ago, <a href="https://developer.android.com/about/versions/jelly-bean.html" target="_blank">Android Jellybean 4.3</a> was launched at Google I/O 2013. With every new Android release, Google updates their <a href="https://developer.android.com/tools/support-library/index.html" target="_blank">Android Support Library</a> to include certain UI Components needing backward compatibilities. Of all the latest UI components I used, only the <code>ActionBar</code> component is still needing other alternative (hint: <a href="http://actionbarsherlock.com/" target="_blank">ActionBarSherlock</a>).

Native UI components offer you consistent codes throughout all Android versions meaning that you can worry more about what your app do than what versions of Android support component X. This is fresh air for developers, thanks to Google for making lives easier.

Here are a few Native UI Components I used before with Android Support Library:
<ul>
<li><a href="https://developer.android.com/guide/components/fragments.html" target="_blank">Fragments</a></li>
<li><a href="https://developer.android.com/design/patterns/navigation-drawer.html" target="_blank">NavigationDrawer</a></li>
<li><a href="https://developer.android.com/reference/android/support/v4/view/ViewPager.html" target="_blank">ViewPager</a></li>
</ul>

<h2>AsyncTask</h2>

For any task that your codes do that will block the UI in any way, delegate to <code><a href="https://developer.android.com/reference/android/os/AsyncTask.html" target="_blank">AsyncTask</a></code>. With every subclass, you can always override <code>onPreExecute()</code> and <code>onPostExecute</code> to meddle the UI a bit before and after your task is executed.

I have a few tutorials here for that matter:
<ul>
<li><a href="http://www.bango29.com/go/blog/2011/android-asynctask-is-a-beauty-part-1" target="_blank">Part 1</a></li>
<li><a href="http://www.bango29.com/go/blog/2011/android-asynctask-is-a-beauty-part-2" target="_blank">Part 2</a></li>
</ul>

<h2>Final Words</h2>

So to wrap things up, by adhering to these design patterns when developing on Android, I always get that speedy and snappy Android app illusion for users. Speed like in web development is an expensive illusion but you can pay it by doing some vertical scaling. It's hard to scale horizontally because Android devices hardware is on the mercy of manufacturers.