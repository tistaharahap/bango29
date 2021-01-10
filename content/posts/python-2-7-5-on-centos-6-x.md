+++
author = "Batista Harahap"
categories = ["2.7", "centos", "python", "update", "upgrade"]
date = 2013-07-17T18:14:28Z
description = ""
draft = false
slug = "python-2-7-5-on-centos-6-x"
tags = ["2.7", "centos", "python", "update", "upgrade"]
title = "Python 2.7.5 on CentOS 6.x"

+++


For the last few months, I've been coding in Python relentlessly. It's new to me and it just makes sense. The one thing I really like is keeping codes and logic simple. You can comment Python's OOP implementation but then again, everyone got a favourite right?

Most of the servers I handle everyday are CentOS 6.x distros with Python 2.6.x preinstalled by the system. You <strong>DON'T</strong> wanna upgrade it through <code>yum</code> or any other method, you will break the whole system. So here's to how get Python 2.7.5 working.

<pre lang="bash">
$ wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2
$ tar xf Python-2.7.5.tar.bz2
$ cd Python-2.7.5
$ ./configure --prefix=/usr/local
$ make -j4
$ make <strong>altinstall</strong> # DON'T use make install!
</pre>

Pretty easy right? Python 2.7.5 is now installed at <code>/usr/local/bin</code> and next is to get <code>distribute</code> and <code>pip</code> working with it.

<pre lang="bash">
$ wget http://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz
$ tar xfz distribute-0.6.35.tar.gz
$ cd distribute-0.6.35
$ python2.7 setup.py install
$ easy_install-2.7 pip
$ pip-2.7 install --upgrade pip
</pre>

Now to make Python 2.7.5 available as your Python environment, <code>virtualenv</code> is what you need. Let's get it on our system.

<pre lang="bash">
$ pip-2.7 install virtualenv
$ virtualenv-2.7 /usr/local/python-env --distribute
</pre>

As it stands, you now have a Python 2.7.5 environment available at <code>/usr/local/python-env</code> instead of the default Python 2.6.x on your system. To activate, do the following.

<pre lang="bash">
$ source /usr/local/python-env/bin/activate
</pre>

Your shell prompt will be prefixed with <code>(python-env)</code> signifying that you are using that particular Python environment. Check your Python version now by doing:

<pre lang="bash">
$ which python
/usr/local/python-env/bin/python
$ python --version
Python 2.7.5
</pre>

If you're like me who dwells in running a website, you might wanna install <a href="http://gunicorn.org/" title="Gunicorn" target="_blank"><code>gunicorn</code></a> and <a href="http://supervisord.org/" title="Supervisord" target="_blank"><code>supervisor</code></a>. Try <a href="http://flask.pocoo.org/" title="Flask" target="_blank"><code>flask</code></a> while you're at it.

<pre lang="bash">
$ pip install gunicorn supervisor flask
</pre>

Next post will be about the last 3 Python packages we installed.