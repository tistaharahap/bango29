+++
author = "Batista Harahap"
categories = ["base station", "blackberry", "cell tower", "cid", "gps", "jde", "lac", "lbs", "location", "location base", "location based", "Mac", "urbanesia"]
date = 2011-08-04T18:28:12Z
description = ""
draft = false
slug = "blackberry-coordinates-from-cell-tower"
tags = ["base station", "blackberry", "cell tower", "cid", "gps", "jde", "lac", "lbs", "location", "location base", "location based", "Mac", "urbanesia"]
title = "Blackberry Coordinates From Cell Tower"

+++


I'm beginning to like coding in Blackberry since now an official JDE for Mac is available. Then I decided to have a look and prepare myself for some rather annoying but pleasant surprise from Blackberry's JDE. To be honest, I don't like Blackberry's behavior of complicating simple things. But then I learned a lot from the codes.

Urbanesia is a location based service and therefore location is very important. I've been trying out a few ways to get the device's location and after all the things I've tried, I resorted into plain GMM solution. Blackberry's location API was too slow to get a fix on the device's location. Nevertheless, the codes are included as well.

The codes should work well from Blackberry OS 5.0 upwards. Haven't tried with older OS. You might want to wrap calling the methods inside a Thread so it won't block the UI. My 2 cents about Threading in Blackberry, extend the Thread class, makes life easier.

<pre lang="java" line="1">
package com.urbanesia.api;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import javax.microedition.io.Connector;
import javax.microedition.io.HttpConnection;
import javax.microedition.location.Criteria;
import javax.microedition.location.Location;
import javax.microedition.location.LocationException;
import javax.microedition.location.LocationProvider;

import net.rim.device.api.system.GPRSInfo;

import com.urbanesia.utils.Log;

public class CellTowerLocation {
	protected static final int LOOKUP_TIMEOUT = 5000;
	protected static final int LOOKUP_TOLERANCE = 500;
	
	public static final boolean FORCE_LOCATION_UPDATE = true;
	public static final boolean DONT_FORCE_LOCATION_UPDATE = false;
	
	public static String getLocation() {
		Criteria ct = new Criteria();
		ct.setHorizontalAccuracy(1000);
		ct.setVerticalAccuracy(1000);
		ct.setCostAllowed(true);
		ct.setPreferredResponseTime(LOOKUP_TIMEOUT);
		ct.setPreferredPowerConsumption(Criteria.POWER_USAGE_LOW);
		
		String coords = "";
		try {
			LocationProvider lp = LocationProvider.getInstance(ct);
			Location loc = lp.getLocation(LOOKUP_TIMEOUT + LOOKUP_TOLERANCE);
			
			String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
			String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
			
			coords = lat+","+lon;
			Log.out("Coordinates - Exact Location: " + coords);
		} catch (LocationException e) {
			Location loc = LocationProvider.getLastKnownLocation();
			String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
			String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
			
			coords = lat+","+lon;
			Log.out("Coordinates - Using last known location: " + coords);
		} catch (InterruptedException e) {
			Location loc = LocationProvider.getLastKnownLocation();
			String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
			String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
			
			coords = lat+","+lon;
			Log.out("Coordinates - Using last known location: " + coords);
		}
		
		Log.out("Coordinates: " + coords);
		return coords;
	}
	
	public static String getLocation(boolean force) {
		if(force) {
			Criteria ct = new Criteria();
			ct.setHorizontalAccuracy(1000);
			ct.setVerticalAccuracy(1000);
			ct.setCostAllowed(true);
			ct.setPreferredResponseTime(LOOKUP_TIMEOUT);
			ct.setPreferredPowerConsumption(Criteria.POWER_USAGE_LOW);
			
			String coords = "";
			try {
				LocationProvider lp = LocationProvider.getInstance(ct);
				Location loc = lp.getLocation(-1);
				
				String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
				String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
				
				coords = lat+","+lon;
			} catch (Exception e) {
				Location loc = LocationProvider.getLastKnownLocation();
				String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
				String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
				
				coords = lat+","+lon;
			}
			
			Log.out("Coordinates: " + coords);
			return coords;
		} else {
			return getLocation();
		}
	}
	
	public static String getLocationGMM() {
		String coords = "0,0";
		int cellID = GPRSInfo.getCellInfo().getCellId();
		int lac = GPRSInfo.getCellInfo().getLAC();
		
		String urlString = "http://www.google.com/glm/mmap" + ConnString.getConnectionString();
		
		try {
			HttpConnection conn = (HttpConnection) Connector.open(urlString);
			OutputStream os = null;
			InputStream in = null;
			
			conn.setRequestMethod(HttpConnection.POST);
			conn.setRequestProperty("Content-Type","application/x-www-form-urlencoded"); 
			conn.setRequestProperty("If-Modified-Since","29 Oct 1999 19:43:31 GMT");
			conn.setRequestProperty("User-Agent","Urbanesia Jajan Blackberry v1.0");
			conn.setRequestProperty("Content-Language", "en-US");
			
			os = conn.openOutputStream();
			WriteData(os, cellID, lac);
			
			in = conn.openInputStream();
			DataInputStream dataInputStream = new DataInputStream(in);
			dataInputStream.readShort();
			dataInputStream.readByte();
			int code = dataInputStream.readInt();
			if (code == 0) {
				double lat = (double) dataInputStream.readInt() / 1000000D;
			    double lng = (double) dataInputStream.readInt() / 1000000D;
			    dataInputStream.readInt();
			    dataInputStream.readInt();
			    dataInputStream.readUTF();
			    
			    coords = Double.toString(lat) + "," + Double.toString(lng);
			    Log.out("Coordinates - Got from GMM: " + coords);
			} else {
				Location loc = LocationProvider.getLastKnownLocation();
				String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
				String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
				coords = lat+","+lon;
				Log.out("Coordinates - Using last known location: " + coords);
			}
		} catch (Exception e) {
			Location loc = LocationProvider.getLastKnownLocation();
			String lat = String.valueOf(loc.getQualifiedCoordinates().getLatitude());
			String lon = String.valueOf(loc.getQualifiedCoordinates().getLongitude());
			coords = lat+","+lon;
			Log.out("Coordinates - Using last known location: " + coords);
		}
		
		return coords;
	}
	
	private static void WriteData(OutputStream out, int cellID, int lac) throws IOException  {
		DataOutputStream dataOutputStream = new DataOutputStream(out);
		dataOutputStream.writeShort(21);
        dataOutputStream.writeLong(0);
        dataOutputStream.writeUTF("en");
        dataOutputStream.writeUTF("Android");
        dataOutputStream.writeUTF("1.0");
        dataOutputStream.writeUTF("Web");
        dataOutputStream.writeByte(27);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(3);
        dataOutputStream.writeUTF("");

        dataOutputStream.writeInt(cellID);  
        dataOutputStream.writeInt(lac);     

        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.flush();
	}	
}
</pre>