#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from search import search
from bs4 import BeautifulSoup
import urllib, os, re
from urllib.request import Request, urlopen
import config

artists = config.artists
outputfilename = "lyrics.csv"
client_access_token = 'btFfEb8mMiv7pdXMBz2PVYmAsVPW3czBjFUwmmKC8IP4yDpaR_2HBlATdwpiP1GA'

def get_lyrics(url):
    request = Request(url)
    request.add_header("Authorization", "Bearer " + client_access_token)
    request.add_header("User-Agent",
                       "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")  # Must include user agent of some sort, otherwise 403 returned

    page = urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_= "lyrics")
    return lyrics.text

f2 = open('urls', 'wb')

for artist in artists:
    urls = search(artist, outputfilename, client_access_token)
    #print(a)
    #urls = map(lambda t: t[3], a)
    print(artist, len(urls))

    f = open('lyrics/' + artist, 'wb')
    f2.write(artist.encode())
    for url in urls:
        lyrics = get_lyrics(url)
        f2.write(url.encode())
        print(url)
        f.write(lyrics.encode("utf8"))

    f.close()
f2.close()
