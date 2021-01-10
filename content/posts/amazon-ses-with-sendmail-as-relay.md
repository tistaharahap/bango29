+++
author = "Batista Harahap"
categories = ["amazon", "aws", "cloud", "email", "relay", "sendmail", "ses", "simple email service"]
date = 2012-01-25T09:54:32Z
description = ""
draft = false
slug = "amazon-ses-with-sendmail-as-relay"
tags = ["amazon", "aws", "cloud", "email", "relay", "sendmail", "ses", "simple email service"]
title = "Amazon SES with Sendmail as Relay"

+++


Over and over, <code>sendmail</code> keeps getting whacked out of configuration and it's puzzling why this keeps happening. I followed everything at Amazon SES' instruction <a href="http://docs.amazonwebservices.com/ses/latest/DeveloperGuide/Scripts.MTAs.Sendmail.html">here</a> with no luck.

So to set things straight once for all, here are the steps to make the changes permanent.
<ol>
	<li>Open up <code>sendmail.mc</code> typically located at <code>/etc/mail</code></li>
	<li>Add <code>FEATURE(`mailertable')dnl</code> below where all the <code>FEATURE()</code> codes are</li>
	<li>Add the lines below at the end of file</li>
<ul>
	<li><code>MAILER_DEFINITIONS
Maws-email, P=/etc/aws/ses-send-email.pl, F=mDFMuXn, U=mail, S=EnvFromSMTP/HdrFromSMTP, R=EnvToSMTP, A=ses-send-email.pl -r -k /etc/aws/aws-credentials -e https://email.us-east-1.amazonaws.com -f $f $u</code></li>
</ul>
	<li>Save the file</li>
	<li>Generate <code>sendmail.cf</code> by doing <code>m4 /etc/mail/sendmail.mc &gt; /etc/mail/sendmail.cf</code></li>
	<li>Open up <code>mailertable</code> typically located in <code>/etc/mail</code> and add <code>.[TAB]aws-email:%0</code>. Replace <code>[TAB]</code> with a real TAB character</li>
	<li>Build the <code>mailertable</code> database by doing <code>makemap hash /etc/mail/mailertable &lt; /etc/mail/mailertable</code></li>
	<li>Test the configuration by doing <code>sendmail -bv test-email@domain.com</code></li>
	<li>If all goes well, restart sendmail by doing <code>/etc/init.d/sendmail restart</code></li>
</ol>