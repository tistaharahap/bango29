+++
author = "Batista Harahap"
categories = ["acer", "acerid", "Android", "asynctask", "hdpi", "java", "ldpi", "magpierss", "mdpi", "php", "phpthumb", "rss", "sourceforge", "Tutorial", "xhdpi"]
date = 2011-05-26T18:14:36Z
description = ""
draft = false
slug = "android-asynctask-is-a-beauty-part-2"
tags = ["acer", "acerid", "Android", "asynctask", "hdpi", "java", "ldpi", "magpierss", "mdpi", "php", "phpthumb", "rss", "sourceforge", "Tutorial", "xhdpi"]
title = "Android - AsyncTask Is A Beauty - Part 2"

+++


Here goes the second part of a short tutorial of how beautiful AsyncTask is, the first tutorial is <a href="http://r.bango29.com/ixjpHR">here</a>. Now that we're moving up to our second activity which is Hacktivate, a brief description about it is that this activity essentially puts all the data retrieved previously and populate a custom layout ListView.

To make reading and understanding easier, here are the codes first before anything else.

<pre lang="java" line="1">
package com.bango.acerid;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.jsoup.Jsoup;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.AdapterView.OnItemClickListener;

public class Hacktivate extends Activity {
	private String jsonStr = "";
	private JSONObject json;
	private List<String> images = new ArrayList<String>();
	private List<String> titles = new ArrayList<String>();
	private List<String> writers = new ArrayList<String>();
	private List<String> dates = new ArrayList<String>();
	private List<String> links = new ArrayList<String>();
	private List<String> body = new ArrayList<String>();
	private List<String> description = new ArrayList<String>();
	private ArticleAdapter adapter = new ArticleAdapter();
	private List<ListData> l = new ArrayList<ListData>();
	
	@Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.hacktivate);
        
        Bundle the = getIntent().getExtras();
        jsonStr = (the != null) ? the.getString("listData") : "";
        parseJson(jsonStr);
        
        ListView articleList = (ListView) findViewById(R.id.list);
        articleList.setAdapter(adapter);
        
        final Intent i = new Intent(this, PostViewer.class);
        
        articleList.setOnItemClickListener(new OnItemClickListener() {
			public void onItemClick(AdapterView<?> parent, View v, int position,
					long id) {
				i.putExtra("wvUrl", links.get(position));
				i.putExtra("wvBody", body.get(position));
				Hacktivate.this.startActivity(i);
			}	
        });
    }
	
	private void parseJson(String j) {
		try {
			json = new JSONObject(j);
			JSONArray rss = json.getJSONArray("rss");
			
			int max = rss.length();
			for(int i=0; i<max; i++) {
				JSONObject post = rss.getJSONObject(i);
				titles.add(post.getString("title"));
				writers.add(post.getString("writer"));
				dates.add(post.getString("date_friendly"));
				links.add(post.getString("link"));
				body.add(new String(Base64.decode(post.getString("body"))));
				images.add(post.getString("image"));
				description.add(post.getString("description"));
			}
		} catch (JSONException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	private class ListData {
		private int position;
		private View v;
		private Bitmap bitmap;
		
		public ListData(int position, View v) {
			setPosition(position);
			setView(v);
		}
		
		public void setPosition(int position) {
			this.position = position;
		}
		public int getPosition() {
			return position;
		}
		public void setView(View v) {
			this.v = v;
		}
		public View getView() {
			return v;
		}

		public void setBitmap(Bitmap bitmap) {
			this.bitmap = bitmap;
		}

		public Bitmap getBitmap() {
			return bitmap;
		}
	}
	
	private class ArticleAdapter extends BaseAdapter {
		ImageManager imgMan;

		public int getCount() {
			return titles.size();
		}

		public Object getItem(int arg0) {
			return null;
		}

		public long getItemId(int arg0) {
			return arg0;
		}
		
		private class DownloadImage extends AsyncTask<ListData, Void, ListData> {
			private ImageView img;
			
			@Override
			protected ListData doInBackground(ListData... l) {
				int pos = l[0].getPosition();
				View v = l[0].getView();
				Bitmap ret;
				
				try {
					String imgStr = images.get(pos);
					imgMan = new ImageManager(imgStr);
					
					img = (ImageView) v.findViewById(R.id.articleImage);
					
					if(imgMan.fileExists()) {
						ret = imgMan.getImage();
					} else {
						ret = imgMan.saveImage();
					}
					
					ListData ll = new ListData(pos, v);
					ll.setBitmap(ret);
					
					return ll;
				} catch(Exception e) {
					e.printStackTrace();
					return null;
				}
			}
			
			@Override
			protected void onPostExecute(ListData ret) {
				if(ret != null) {
					img.setImageBitmap(ret.getBitmap());
					if(l.get(ret.getPosition()).getBitmap() == null) {
						l.get(ret.getPosition()).setBitmap(ret.getBitmap());
					}
				}
			}
			
		}

		public View getView(int position, View v, ViewGroup vg) {
			LayoutInflater inflater = getLayoutInflater();
			v = inflater.inflate(R.layout.articlerow, vg, false);
			
			TextView title = (TextView) v.findViewById(R.id.articleTitle);
			TextView desc = (TextView) v.findViewById(R.id.articleDesc);
			
			title.setText(titles.get(position));
			String d = Jsoup.parse(description.get(position)).text() + "\n\nBy " + writers.get(position) + " on " + dates.get(position);
			desc.setText(d);
			
			// Lazy load images
			try {
				ListData tmp = l.get(position);
				
				ImageView img = (ImageView) v.findViewById(R.id.articleImage);
				img.setImageBitmap(tmp.getBitmap());
			} catch(IndexOutOfBoundsException e) {
				ListData lst = new ListData(position, v);
				l.add(lst);
				new DownloadImage().execute(l.get(position));
			}
			
			return v;
		}
		
	}
	
	public void onBackPressed() {
		moveTaskToBack(true);
	}
	
	public void askDoctor(View v) {
		Intent i = new Intent(this, Ask.class);
		startActivity(i);
	}
	
	public boolean onCreateOptionsMenu(Menu menu) {
		MenuInflater inflater = getMenuInflater();
	    inflater.inflate(R.menu.menu, menu);
		return true;
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch(item.getItemId()) {
			case R.id.menuIcon:
				return true;
			case R.id.menuRefresh:
				Intent i = new Intent(this, AcerID.class);
				startActivity(i);
				return true;
			case R.id.menuExit:
				moveTaskToBack(true);
				return true;
			default:
				return true;
		}
	}
	
}
</pre>

You might noticed that instead of extending ListActivity, I choose to simply extend Activity. My reason is to carve out expected behaviors of a ListActivity like the standardized naming conventions for its ListView and the default row layout.

For this activity, I incorporated an external library called <a href="http://jsoup.org">JSOUP</a>. It's a very useful library to deal with HTML or even HTML fragments. Most importantly to correctly decode HTML entities generated by server side languages.

The next interesting technique is to incorporate an SD Card to save downloaded thumbnails to only use bandwidth when required only. I created a separate class called ImageManager.java to do exactly that. Here is the source code.

<pre lang="java" line="1">
package com.bango.acerid;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.Environment;

public class ImageManager {
	protected final static String STORAGE_PATH = Environment.getExternalStorageDirectory().toString();
	private String imgUrl;
	private String fn;
	private String basepath = STORAGE_PATH + "/AcerID/";
	
	public ImageManager(String imgUrl) {
		this.setImgUrl(imgUrl);
		fn = md5(imgUrl) + ".jpg";
	}
	
	protected Drawable getImageFromURL(String url) {
		try {
			InputStream is = (InputStream) new URL(url).getContent();
			Drawable d = Drawable.createFromStream(is, "src name");
			is.close();
			return d;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}
	}
	
	public boolean fileExists() {
        return new File(basepath+fn).exists();
	}
	
	public static String md5(String s) {
		try {
			// Create MD5 Hash
			MessageDigest digest = java.security.MessageDigest
					.getInstance("MD5");
			digest.update(s.getBytes());
			byte messageDigest[] = digest.digest();

			// Create Hex String
			StringBuffer hexString = new StringBuffer();
			for (int i = 0; i < messageDigest.length; i++)
				hexString.append(Integer.toHexString(0xFF & messageDigest[i]));
			return hexString.toString();

		} catch (NoSuchAlgorithmException e) {
			//e.printStackTrace();
			return s;
		}
	}
	
	public Bitmap getImage() {
		return BitmapFactory.decodeFile(basepath+fn);
	}
	
	public Bitmap saveImage() {
		Bitmap b = ((BitmapDrawable) getImageFromURL(imgUrl)).getBitmap();
		FileOutputStream out;
		
		// Create dir
		File dir = new File(basepath);
		if(!dir.exists()) {
			dir.mkdirs();
		}
		
		try {
			File output = new File(dir, fn);
			out = new FileOutputStream(output);
			
			b.compress(Bitmap.CompressFormat.JPEG, 90, out);
			out.flush();
			out.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return b;
	}

	public void setImgUrl(String imgUrl) {
		this.imgUrl = imgUrl;
	}

	public String getImgUrl() {
		return imgUrl;
	}
	
}
</pre>

Since I'm using PhpThumb to generate the thumbnails, it's quite complicated to parse only the filename of the image downloaded. This is why I choose to use an MD5 hash of the whole image URL as its filename and all formats are in JPEG converted by the within the saveImage() method. This class is actually needing more conditions to check whether an external storage is available or not. I'm gonna leave this to your creativity.

To give a better user experience, I lazy loaded all the thumbnails and put in a default image for every thumbnails before it is displayed. The condition checks if that particular is already available or not, if not then it will execute the AsyncTask assigned for this download job.

The interesting part about the AsyncTask in this activity is that it detoured Java's deficiency to pass by reference and instead pass data by value. I made a special class called ListData to contain the data I need to pass. My particular interest is with this line of code:

<pre lang="java" line="1">
l.get(ret.getPosition()).setBitmap(ret.getBitmap());
</pre>

Looks a bit messy but it's an elegant method chaining way to exactly do what I want which is to return and finally set the downloaded image into each rows. Without it, everytime you scroll down and back up vice versa, the image will continuously be downloaded by AsyncTask.

<pre lang="java" line="1">
			// Lazy load images
			try {
				ListData tmp = l.get(position);
				
				ImageView img = (ImageView) v.findViewById(R.id.articleImage);
				img.setImageBitmap(tmp.getBitmap());
			} catch(IndexOutOfBoundsException e) {
				ListData lst = new ListData(position, v);
				l.add(lst);
				new DownloadImage().execute(l.get(position));
			}
</pre>

So this wraps up AsyncTask's beauty and completes the tutorial. The application I made will soon be introduced into Android Market, still have to do a bit more codes. Thanks for tuning in!