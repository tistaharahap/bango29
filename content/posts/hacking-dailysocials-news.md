+++
author = "Batista Harahap"
categories = ["hack", "machine learning", "naive bayes classifier", "nltk", "textblob", "dailysocial"]
date = 2014-03-20T13:31:09Z
description = ""
draft = false
slug = "hacking-dailysocials-news"
tags = ["hack", "machine learning", "naive bayes classifier", "nltk", "textblob", "dailysocial"]
title = "Hacking DailySocial's News"

+++


[DailySocial.net](http://dailysocial.net) is a tech blog founded by [Rama Mamuaya](https://twitter.com/rampok).  I enjoy visiting DailySocial and reading about the Indonesian tech scene. But yet I've grown weary of filtering news to read. So why not hack a news classifier I thought.

## Core Computing

It took 10 minutes to hack something up in Python. Why so fast you ask? Because text processing is second nature in Python. [NLTK](http://nltk.org/) is good but [TextBlob](https://textblob.readthedocs.org/) is great. I used a Naive Bayes Classifier algorithm provided by TextBlob. All I coded was a feature extractor catered to my likings.

Here's the feature extractor.

```
from textblob import TextBlob
 
 
def feature_extractor(text):
    if not isinstance(text, TextBlob):
        text = TextBlob(text.lower())
 
    feats = {
        'has_rumor': 'rumor' in text.words,
        'has_gosip': 'gosip' in text.words,
        'has_pemasaran': 'pemasaran' in text.words,
        'has_saham': 'saham' in text.words,
        'has_hackathon': 'hackathon' in text.words,
        'has_ipo': 'ipo' in text.words,
        'has_akuisisi': 'akuisisi' in text.words,
        'has_startup': 'startup' in text.words,
        'has_android': 'android' in text.words,
        'has_aplikasi': 'aplikasi' in text.words,
        'has_payment': 'payment' in text.words,
        'has_pembayaran': 'pembayaran' in text.words,
        'has_api': 'api' in text.words,
        'has_kompetisi': 'kompetisi' in text.words,
        'has_ide': 'ide' in text.words,
        'has_permainan': 'permainan' in text.words,
        'has_game': 'game' in text.words,
        'has_fundraising': 'fundraising' in text.words,
        'has_askds': '[Ask@DailySocial]' in text.words,
        'has_investasi': 'investasi' in text.words,
        'has_akuisisi': 'akuisisi' in text.words,
        'has_musik': 'musik' in text.words,
        'has_bhinneka': 'bhinneka' in text.words,
        'has_marketplace': 'marketplace' in text.words,
        'has_mobile': 'mobile' in text.words
    }
    return feats
```

[Github Gist](https://gist.github.com/tistaharahap/9167752)

Quite simple isn't it? That's why I'm having a hard time filtering the news. Too much noise for my own interest.

Now I need a train set so that the algorithm can be smart enough to figure out which story is interesting to me. There were discussions in my head whether to only parse only the article title or including the whole body. Long story short, I only settled for only the article title. If the title isn't concise enough then it's not interesting enough.

```
# -*- coding: utf-8 -*-
from text.classifiers import NaiveBayesClassifier
from textblob import TextBlob
 
 
def feature_extractor(text):
    if not isinstance(text, TextBlob):
        text = TextBlob(text.lower())
 
    feats = {
        'has_rumor': 'rumor' in text.words,
        'has_gosip': 'gosip' in text.words,
        'has_pemasaran': 'pemasaran' in text.words,
        'has_saham': 'saham' in text.words,
        'has_hackathon': 'hackathon' in text.words,
        'has_ipo': 'ipo' in text.words,
        'has_akuisisi': 'akuisisi' in text.words,
        'has_startup': 'startup' in text.words,
        'has_android': 'android' in text.words,
        'has_aplikasi': 'aplikasi' in text.words,
        'has_payment': 'payment' in text.words,
        'has_pembayaran': 'pembayaran' in text.words,
        'has_api': 'api' in text.words,
        'has_kompetisi': 'kompetisi' in text.words,
        'has_ide': 'ide' in text.words,
        'has_permainan': 'permainan' in text.words,
        'has_game': 'game' in text.words,
        'has_fundraising': 'fundraising' in text.words,
        'has_askds': '[Ask@DailySocial]' in text.words,
        'has_investasi': 'investasi' in text.words,
        'has_akuisisi': 'akuisisi' in text.words,
        'has_musik': 'musik' in text.words,
        'has_bhinneka': 'bhinneka' in text.words,
        'has_marketplace': 'marketplace' in text.words,
        'has_mobile': 'mobile' in text.words
    }
    return feats
 
train_set = [
    ('Berbarengan dengan Launch Festival, Ice House Buka Kompetisi Wujudkan Ide-Ide Aplikasi Mobile.', 'ok'),
    ('Ulang Tahun Ke-21, Layanan E-Commerce Bhinneka Segera Perbarui Platform E-Commerce dan Luncurkan Marketplace Terkurasi.', 'ko'),
    ('Aplikasi Pencatat Blastnote Hadir di Android.', 'ok'),
    ('Portal Hiburan Digital UZone Kini Hadir Dalam Versi Aplikasi Mobile.', 'ok'),
    ('CTI IT Infrastructure Summit 2014 Bahas Big Data Sebagai Tren Teknologi', 'ko'),
    ('Dua Berita Buruk Besar Bagi Blackberry', 'ok'),
    ('Tanggapan Pelaku Industri Digital di Indonesia tentang Fenomena Permainan Mobile Flappy Bird', 'ok'),
    ('[Ask@DailySocial] Proses Fundraising Untuk Startup', 'ok'),
    ('Investasi $1 Miliar, Foxconn Pastikan Bangun Pabriknya di DKI Jakarta', 'ok'),
    ('Raksasa Digital Cina Tencent Dikabarkan Akuisisi Portal Berita Okezone', 'ko'),
    ('Wego Tawarkan Akses Reservasi Tiket dan Hotel Lebih Mudah Melalui Aplikasi Mobile', 'ok'),
    ('Telkom Hadirkan Agen Wisata Online Hi Indonesia', 'ko'),
    ('Meski Didera Isu Fake Likes, Facebook Tetap Jadi Pilihan Utama Untuk Pemasaran Digital', 'ok'),
    ('Dave Morin Pastikan Saham Bakrie Global Group di Path Kurang dari 1%', 'ok'),
    ('Kecil Kemungkinan Pemerintah Tutup Telkomsel dan Indosat Terkait Dugaan Penyadapan oleh Australia', 'ok'),
    ('Kakao Dikabarkan Gelar Penawaran Saham Perdana Tahun Depan', 'ok'),
    ('Ericsson Akan Hadirkan Layanan Streaming TV', 'ok'),
    ('Ryu Kawano: Ingin Startup Anda Go Global? Tunggu Dulu!', 'ok'),
    ('Kerja Sama dengan GHL Systems Malaysia, Peruri Digital Security Kembangkan Sistem Pembayaran Online', 'ok'),
    ('Aplikasi Logbook Travel Kini Telah Hadir di Android', 'ok'),
    ('Musikator Hadirkan Layanan Agregator Lagu Untuk Distribusi Digital', 'ok'),
    ('[Manic Monday] Strategi Produksi Konten Di Era Multilayar', 'ok'),
    ('Bakrie Telecom Jajaki Kemungkinan Carrier Billing untuk Path', 'ok'),
    ('Viber Secara Resmi Telah Diakuisisi Oleh Rakuten Sebesar US$ 900 Juta', 'ok'),
    ('Situs Panduan Angkutan Umum Kiri.travel Buka API, Tantang Pengembang Buat Aplikasi Windows Phone', 'ok'),
    ('Wego Luncurkan Jaringan Afiliasi WAN.Travel', 'ko'),
    ('Business Insider Masuki Pasar Indonesia Bekerja Sama dengan REV Asia', 'ko'),
    ('Waze Memiliki 750.000 Pengguna di Indonesia', 'ok'),
    ('Survei Nielsen: Masyarakat Asia Tenggara Lebih Suka Gunakan Uang Tunai untuk Belanja Online', 'ok'),
    ('CTI IT Infrastructure Summit 2014 Bahas Big Data Sebagai Tren Teknologi', 'ko'),
    ('Pacu Bisnis di Asia Tenggara, Game Online Asing Kini Lebih Lokal', 'ko'),
    ('Enam Pilihan Layanan Streaming Musik Yang Dapat Dinikmati di Indonesia', 'ok'),
    ('Country Manager Yahoo Indonesia Roy Simangunsong Mengundurkan Diri', 'ko'),
    ('Investasi $1 Miliar, Foxconn Pastikan Bangun Pabriknya di DKI Jakarta', 'ok'),
    ('Jomblo.com Tawarkan Media Sosial Untuk Mencari Jodoh', 'ko'),
    ('Mitra Adiperkasa dan Groupon Pilih aCommerce Indonesia untuk Pusat Logistik dan Pengiriman Layanan E-Commerce', 'ko'),
    ('Transformasi Portal Informasi Kecantikan Female Daily Disambut Positif, Beberkan Rencana-Rencana 2014', 'ko'),
    ('Visa Gelar Promosi Diskon Setiap Jumat Bekerja Sama dengan Enam Layanan E-Commerce Lokal', 'ko'),
    ('Kerjasama Strategis, Blue Bird Group Benamkan Teknologi Interkoneksi Microsoft Ke Armada Premium Big Bird', 'ko'),
    ('Ramaikan Industri Fashion E-Commerce Indonesia, VIP Plaza Hadir Tawarkan Promo Flash Sale', 'ko'),
    ('Bidik Citizen Journalism, Detik Hadirkan Media Warga PasangMata', 'ko'),
    ('Asia Pasifik Jadi Kawasan E-Commerce B2C Terbesar di Dunia Tahun 2014', 'ko')
]
cl = NaiveBayesClassifier(train_set=train_set, feature_extractor=feature_extractor)
print cl.classify('Asia Pasifik Jadi Kawasan E-Commerce B2C Terbesar di Dunia Tahun 2014'.lower())
```

Have a look again at the `feature_extractor.py` snippet. The code is clear enough to show that I'm only extracting keywords. You can do a lot smarter by say including the length of the trained text. I'll leave that to the reader's imagination.

## Integrating With DailySocial's Feed

Machine Learning is an art. There's no one size fits all solution. But nothing is impossible.

The RSS feed for DailySocial is available [here](http://feeds.feedburner.com/dsnet?format=xml). I'm gonna use that to get data in and measure how "OK" the data is for my own liking.

```
# -*- coding: utf-8 -*-
from text.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import feedparser
import time
import redis
import hashlib
import json


TIMEOUT = 60*60

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


def feature_extractor(text):
    if not isinstance(text, TextBlob):
        text = TextBlob(text.lower())

    return {
        'has_rumor': 'rumor' in text.words,
        'has_gosip': 'gosip' in text.words,
        'has_urbanesia': 'urbanesia' in text.words,
        'has_batista': 'batista' in text.words,
        'has_harahap': 'harahap' in text.words,
        'has_pemasaran': 'pemasaran' in text.words,
        'has_saham': 'saham' in text.words,
        'has_hackathon': 'hackathon' in text.words,
        'has_ipo': 'ipo' in text.words,
        'has_akuisisi': 'akuisisi' in text.words,
        'has_startup': 'startup' in text.words,
        'has_android': 'android' in text.words,
        'has_aplikasi': 'aplikasi' in text.words,
        'has_payment': 'payment' in text.words,
        'has_pembayaran': 'pembayaran' in text.words,
        'has_api': 'api' in text.words,
        'has_kompetisi': 'kompetisi' in text.words,
        'has_ide': 'ide' in text.words,
        'has_permainan': 'permainan' in text.words,
        'has_game': 'game' in text.words,
        'has_fundraising': 'fundraising' in text.words,
        'has_askds': '[Ask@DailySocial]' in text.words,
        'has_investasi': 'investasi' in text.words,
        'has_musik': 'musik' in text.words,
        'has_lagu': 'lagu' in text.words,
        'has_bhinneka': 'bhinneka' in text.words,
        'has_marketplace': 'marketplace' in text.words,
        'has_mobile': 'mobile' in text.words,
        'has_cto': 'cto' in text.words,
        'has_traffic': 'traffic' in text.words,
        'starts_with_[': text[0] == '['
    }

train_set = [
    ('Berbarengan dengan Launch Festival, Ice House Buka Kompetisi Wujudkan Ide-Ide Aplikasi Mobile.', 'ok'),
    ('Ulang Tahun Ke-21, Layanan E-Commerce Bhinneka Segera Perbarui Platform E-Commerce dan Luncurkan Marketplace Terkurasi.', 'ko'),
    ('Aplikasi Pencatat Blastnote Hadir di Android.', 'ok'),
    ('Portal Hiburan Digital UZone Kini Hadir Dalam Versi Aplikasi Mobile.', 'ok'),
    ('CTI IT Infrastructure Summit 2014 Bahas Big Data Sebagai Tren Teknologi', 'ko'),
    ('Dua Berita Buruk Besar Bagi Blackberry', 'ok'),
    ('Tanggapan Pelaku Industri Digital di Indonesia tentang Fenomena Permainan Mobile Flappy Bird', 'ok'),
    ('[Ask@DailySocial] Proses Fundraising Untuk Startup', 'ok'),
    ('Investasi $1 Miliar, Foxconn Pastikan Bangun Pabriknya di DKI Jakarta', 'ok'),
    ('Raksasa Digital Cina Tencent Dikabarkan Akuisisi Portal Berita Okezone', 'ko'),
    ('Wego Tawarkan Akses Reservasi Tiket dan Hotel Lebih Mudah Melalui Aplikasi Mobile', 'ok'),
    ('Telkom Hadirkan Agen Wisata Online Hi Indonesia', 'ko'),
    ('Meski Didera Isu Fake Likes, Facebook Tetap Jadi Pilihan Utama Untuk Pemasaran Digital', 'ok'),
    ('Dave Morin Pastikan Saham Bakrie Global Group di Path Kurang dari 1%', 'ok'),
    ('Kecil Kemungkinan Pemerintah Tutup Telkomsel dan Indosat Terkait Dugaan Penyadapan oleh Australia', 'ok'),
    ('Kakao Dikabarkan Gelar Penawaran Saham Perdana Tahun Depan', 'ok'),
    ('Ericsson Akan Hadirkan Layanan Streaming TV', 'ok'),
    ('Ryu Kawano: Ingin Startup Anda Go Global? Tunggu Dulu!', 'ok'),
    ('Kerja Sama dengan GHL Systems Malaysia, Peruri Digital Security Kembangkan Sistem Pembayaran Online', 'ok'),
    ('Aplikasi Logbook Travel Kini Telah Hadir di Android', 'ok'),
    ('Musikator Hadirkan Layanan Agregator Lagu Untuk Distribusi Digital', 'ok'),
    ('[Manic Monday] Strategi Produksi Konten Di Era Multilayar', 'ok'),
    ('Bakrie Telecom Jajaki Kemungkinan Carrier Billing untuk Path', 'ok'),
    ('Viber Secara Resmi Telah Diakuisisi Oleh Rakuten Sebesar US$ 900 Juta', 'ok'),
    ('Situs Panduan Angkutan Umum Kiri.travel Buka API, Tantang Pengembang Buat Aplikasi Windows Phone', 'ok'),
    ('Wego Luncurkan Jaringan Afiliasi WAN.Travel', 'ko'),
    ('Business Insider Masuki Pasar Indonesia Bekerja Sama dengan REV Asia', 'ko'),
    ('Waze Memiliki 750.000 Pengguna di Indonesia', 'ok'),
    ('Survei Nielsen: Masyarakat Asia Tenggara Lebih Suka Gunakan Uang Tunai untuk Belanja Online', 'ok'),
    ('CTI IT Infrastructure Summit 2014 Bahas Big Data Sebagai Tren Teknologi', 'ko'),
    ('Pacu Bisnis di Asia Tenggara, Game Online Asing Kini Lebih Lokal', 'ko'),
    ('Enam Pilihan Layanan Streaming Musik Yang Dapat Dinikmati di Indonesia', 'ok'),
    ('Country Manager Yahoo Indonesia Roy Simangunsong Mengundurkan Diri', 'ko'),
    ('Investasi $1 Miliar, Foxconn Pastikan Bangun Pabriknya di DKI Jakarta', 'ok'),
    ('Jomblo.com Tawarkan Media Sosial Untuk Mencari Jodoh', 'ko'),
    ('Mitra Adiperkasa dan Groupon Pilih aCommerce Indonesia untuk Pusat Logistik dan Pengiriman Layanan E-Commerce', 'ko'),
    ('Transformasi Portal Informasi Kecantikan Female Daily Disambut Positif, Beberkan Rencana-Rencana 2014', 'ko'),
    ('Visa Gelar Promosi Diskon Setiap Jumat Bekerja Sama dengan Enam Layanan E-Commerce Lokal', 'ko'),
    ('Kerjasama Strategis, Blue Bird Group Benamkan Teknologi Interkoneksi Microsoft Ke Armada Premium Big Bird', 'ko'),
    ('Ramaikan Industri Fashion E-Commerce Indonesia, VIP Plaza Hadir Tawarkan Promo Flash Sale', 'ko'),
    ('Bidik Citizen Journalism, Detik Hadirkan Media Warga PasangMata', 'ko'),
    ('Asia Pasifik Jadi Kawasan E-Commerce B2C Terbesar di Dunia Tahun 2014', 'ko'),
    ('CTO Urbanesia Batista Harahap Mengundurkan Diri', 'ok'),
    ('Tees Indonesia Alami Peningkatan Traffic Hingga 7x, Namun Tidak Seperti Yang Anda Kira', 'ok')
]

cl = NaiveBayesClassifier(train_set=train_set, 
                          feature_extractor=feature_extractor)

redis_conn = redis.StrictRedis(host=REDIS_HOST, 
                               port=REDIS_PORT)


def get_feed():
    feed_url = 'http://feeds.feedburner.com/dsnet?format=xml'
    feeds = feedparser.parse(feed_url).get('entries')

    if feeds is None:
        return

    def process_entry(entry):
        def process_tags(tags):
            return [tag.get('term') for tag in tags]

        cls = cl.classify(text=entry.get('title'))

        data = {
            'author': entry.get('author'),
            'title': entry.get('title'),
            'link': entry.get('link'),
            'published': int(time.mktime(entry.get('published_parsed'))),
            'summary': entry.get('summary'),
            'tags': process_tags(entry.get('tags')),
            'class': cls
        }

        return data if cls == 'ok' else None

    feeds = [process_entry(entry) for entry in feeds]

    return [entry for entry in feeds if entry is not None]

def md5(text):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

def cycle():
    try:
        posts = get_feed()
    except KeyError:
        print 'Unreadable RSS feed, bailing..'
        return

    if not posts:
        print 'Got nothing, bailing..'
        return

    def redis_insert(post):
        print 'Adding: %s..' % post.get('title')
        
        name = 'ds-articles-ok'

        redis_conn.zadd(name, post.get('published'), json.dumps(post))

    [redis_insert(post=post) for post in posts]

    print 'Got %d posts this time.' % len(posts)


if __name__ == '__main__':
    print 'Starting up..'
    while True:
        cycle()
        print 'Sleeping for %s seconds.' % TIMEOUT
        time.sleep(TIMEOUT)
```

[Github Gist](https://gist.github.com/tistaharahap/9670285)

Notice that I'm using a Redis sorted set. Why? Because with it I can score each entry according to a unique timestamp from when they are published. The more recent the news, the higher the score.

Even though there will be repetition when examining each post, the sorted set will only be adding new posts. It's a set so what's in it is basically unique. More reading is [here](http://redis.io/topics/data-types).

## Hacking Up a Frontend

I want the frontend to be responsive and light. That canceled out [Bootstrap](#) and [Foundation](#) as options. I opted for [Micro RWD Grid](http://roybarber.github.io/micro-rwd-grid/) by [Row Barber](http://roybarber.com/). It's 32 lines of CSS.

But then I'm not a web designer, you are welcomed to design one.

Here is the frontend: [DailySocial For ME!](http://ds-for-me.bango29.com).

## Source Code

Source code is available at [https://github.com/tistaharahap/ds-for-me](https://github.com/tistaharahap/ds-for-me).

Hack! \m/