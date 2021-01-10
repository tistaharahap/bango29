+++
author = "Batista Harahap"
categories = ["bancakan", "Me.java", "sell yourself", "StartupLokal"]
date = 2010-07-29T22:28:19Z
description = ""
draft = false
slug = "sell-yourself-by-being-yourself"
tags = ["bancakan", "Me.java", "sell yourself", "StartupLokal"]
title = "Sell yourself by being yourself!"

+++


YOU are your own Startup!

<div style="width:425px" id="__ss_4873796"><strong style="display:block;margin:12px 0 4px"><a href="http://www.slideshare.net/tistaharahap/bancakan-v5-selling-me" title="Bancakan v5 - Selling Me">Bancakan v5 - Selling Me</a></strong><object id="__sse4873796" width="425" height="355"><param name="movie" value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=bancakan-100730121442-phpapp02&stripped_title=bancakan-v5-selling-me" /><param name="allowFullScreen" value="true"/><param name="allowScriptAccess" value="always"/><embed name="__sse4873796" src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=bancakan-100730121442-phpapp02&stripped_title=bancakan-v5-selling-me" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object><div style="padding:5px 0 12px">View more <a href="http://www.slideshare.net/">presentations</a> from <a href="http://www.slideshare.net/tistaharahap">Batista R. Harahap</a>.</div></div>

<pre lang="java">
package me.myself;

import humility.*;
import geekdom.*;
import google.*;
import experience.*;
import vision.*;

public class Me extends Myself throws NegativityException {
	public String me = "Batista Harahap";
	
	public Humility humble;
	public Geekdom geek;
	public Experience exp;
	
	private Ideas idea;
	public Vision v;
	
	Handler h = new Handler() {
		@Override
		public void handleMessage(Message msg) {
			switch(msg.what) {
				case GOT_EXPERIENCE:
					exp.open();
					break;
				case BRANDED:
					vision.add();
					break;
			}
		}
	};
	
	public Me() {
		humble = new Humility(me);
		geek = new Geekdom(me);
		exp = new Experience(me);
		
		while(1) {
			new Thread() {
	            public void run() {
		            try {
		            	String s = geek.learn("l33t");
						exp.add(s);
		            } catch (StupidException e) {
		            	e.printStackTrace();
		            }
		            
		            Message msg = new Message();
		            msg.what = GOT_EXPERIENCE;
		            h.sendMessage(msg);
	            }
		    }.start();
			
			new Thread() {
	            public void run() {
		            try {
		            	geek.branding();
		            } catch (StupidException e) {
		            	e.printStackTrace();
		            }
		            
		            Message msg = new Message();
		            msg.what = BRANDED;
		            h.sendMessage(msg);
	            }
		    }.start();
		}
	}
	
	public Vision getVision() {
		return v;
	}
	
	public int setVision(Vision w) {
		if( v.gotFoundation() && 
			v.greatProduct() && 
			v.coolFeatures() &&
			v.isMonetizable() ) {
			v = w;
			return 7;
		} else {
			return -1;
		}
	}
	
	public Ideas getIdea() {
		return idea;
	}
	
	public int setIdea(Ideas s) {
		if( s.feasible() ) {
			idea = s;
			return 7;
		} else {
			return -1;
		}
	}
	
	public String encourage(Ideas idea) {
		Vision vision = new Vision(idea);
		
		return vision.fastForwardToEnd(idea);
	}
	
	public String encourage(Startup startup) {
		Vision vision = new Vision(startup);
		
		return vision.fastForwardToEnd(startup);
	}
}
</pre>