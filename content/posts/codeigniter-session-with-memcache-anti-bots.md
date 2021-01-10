+++
author = "Batista Harahap"
categories = ["bots", "ci", "codeigniter", "memcache", "mongodb", "session", "urbanesia"]
date = 2011-04-26T20:30:03Z
description = ""
draft = false
slug = "codeigniter-session-with-memcache-anti-bots"
tags = ["bots", "ci", "codeigniter", "memcache", "mongodb", "session", "urbanesia"]
title = "CodeIgniter Session With Memcache + Anti Bots!"

+++


Last night was a thrilling change of routine. Urbanesia was crippled because of theÂ unprecedentedÂ growth of our MongoDB databases. I must admit that MongoDB is like Memcache with steroids, well it overdosed. MongoDB doesn't have any mechanism to limit its memory usages, the only limit we can define is the size of its individual files. Therefore, something must be done!

The second flaw was with CodeIgniter by design. By default, CodeIgniter uses its own Session handling mechanism either by using cookie and or database. The database types supported were limited to drivers available for CodeIgniter. Well we hacked it to use MongoDB a few months ago.

The boomerang was that CodeIgniter again by default does not filter bots for its session mechanism. Urbanesia is very attractive to bots and therefore all of our sessions were mostly bots, this equals junk data. The garbage collector for sessions was also very primitive. We had to do something about this.

We wanted a fast and simple yet elegant solution to tackle the problems above. MySQL is out of the question of course, Insert/Update activities will surely lock tables and we can't afford it. So we turned to Memcache. The most important built in feature with Memcache was its ability to limit memory usage and therefore giving us a garbage collector for stale sessions without extra codes at all!

There are no known Memcache session handling available with CodeIgniter as to my knowledge, so I went ahead and did a whole redo of our MY_Session library to accomodate Memcache as our Session storage engine.  The first thing to do was to filter bots that frequently visit Urbanesia and deny them sessions, instead a cookie will do them just fine.
<pre>function __detectVisit() {
       $this-&gt;CI-&gt;load-&gt;library('user_agent');
       $agent = strtolower($this-&gt;CI-&gt;input-&gt;user_agent());

       $bot_strings = array(
           "google", "bot", "yahoo", "spider", "archiver", "curl",
           "python", "nambu", "twitt", "perl", "sphere", "PEAR",
           "java", "wordpress", "radian", "crawl", "yandex", "eventbox",
           "monitor", "mechanize", "facebookexternal", "bingbot"
       );

       foreach($bot_strings as $bot) {
               if(strpos($agent, $bot) !== false) {
                       return "bot";
               }
       }

       return "normal";
}</pre>
Yes it's quite primitive but it works and it satisfied our needs to filter the most frequent bots.Â The next step was to build namespaces adjusted with some of CodeIgniter's built in Session handling mechanisms.
<pre>function __build_namespace($sess_id, $ip_addr = 0, $user_agent = '') {
	$this-&gt;namespace .= $sess_id;
	if($this-&gt;sess_match_ip == TRUE &amp;&amp; $ip_addr &gt; 0)
		$this-&gt;namespace .= '#'.ip2long($ip_addr);
	if($this-&gt;sess_match_useragent == TRUE &amp;&amp; $user_agent != '')
		$this-&gt;namespace .= '#'.md5($user_agent);
}</pre>
The 3 parameters accepted are all components within a standard CodeIgniter Session. Since CodeIgniter gave us options like sess_match_ip and sess_match_useragent, it's important to adjust the namespace as a filter of its own actually.  One of the most difficult part was to decide whether to use JSON or serialized array to store custom user data. I decided to use JSON in the end. Here's a code snippet of setting a session value to Memcache.
<pre>$this-&gt;CI-&gt;memsess-&gt;set($this-&gt;namespace, json_encode($this-&gt;userdata), $this-&gt;sess_expiration);</pre>
FYI, I used another library called memsess, short of Memcache Sessions lol to let me shard Memcache arrays. I wanted an exclusive Memcache instance solely be used to store sessions. The main reason was to keep session data as tidy as possible meaning that there are no other data that will push the sessions data away unless we tell them to. This makes the Memcache instance far more predictable.  Most of the codings were derived from CI_Session and modified to use Memcache as storage. I will not go into the full details of the library, instead I'm gonna give the code for the sess_read() method. I'm pretty sure it's enough for you to experiment on your own.
<pre>function sess_read() {
	// Kick out bots!
	if($this-&gt;is_bot) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	$session = $this-&gt;CI-&gt;input-&gt;cookie($this-&gt;sess_cookie_name);

	if($session === FALSE) {
		return FALSE;
	}

	if ($this-&gt;sess_encrypt_cookie == TRUE) {
		$session = $this-&gt;CI-&gt;encrypt-&gt;decode($session);
	} else {
		$hash	 = substr($session, strlen($session)-32);
		$session = substr($session, 0, strlen($session)-32);

		if ($hash !==  md5($session.$this-&gt;encryption_key)) {
			$this-&gt;sess_destroy();
			return FALSE;
		}
	}

	$session = $this-&gt;_unserialize($session);

	if (
		!is_array($session)
		OR ! isset($session['session_id'])
		OR ! isset($session['ip_address'])
		OR ! isset($session['user_agent'])
		OR ! isset($session['last_activity'])
	) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	if (($session['last_activity'] + $this-&gt;sess_expiration) &lt; $this-&gt;now) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	if ($this-&gt;sess_match_ip == TRUE AND $session['ip_address'] != $this-&gt;CI-&gt;input-&gt;ip_address()) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	if (
		$this-&gt;sess_match_useragent == TRUE
		AND trim($session['user_agent']) != trim(substr($this-&gt;CI-&gt;input-&gt;user_agent(), 0, 50))
		) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	// Build namespace!
	$this-&gt;__reset_namespace();
	$this-&gt;__build_namespace($session['session_id'], $session['ip_address'], $session['user_agent']);

	$query = $this-&gt;CI-&gt;memsess-&gt;get($this-&gt;namespace);
	if(empty($query)) {
		$this-&gt;sess_destroy();
		return FALSE;
	}

	$row = json_decode($query);
	if(isset($row-&gt;user_data) AND $row-&gt;user_data != '') {
		$custom_data = $this-&gt;_unserialize($row-&gt;user_data);
		if(is_array($custom_data)) {
			foreach($custom_data as $key =&gt; $val) {
				$session[$key] = $val;
			}
		}
	}

	$this-&gt;userdata = $session;
	unset($session);

	return TRUE;
}</pre>
There you go, a glimpse into Session management in CodeIgniter with Memcache. This is a product of experiment because of needs. I'm sure it can be done in smarter ways, the sky is the limit ;)