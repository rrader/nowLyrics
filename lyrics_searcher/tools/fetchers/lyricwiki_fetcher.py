# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
from grab import Grab
import html2text
import urllib
# за доп.плату - фетчер с изменениями. (live) убирать
class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        g = Grab()
        search_response = g.go("http://www.google.com/search?q=%s" % urllib.quote("site:lyrics.wikia.com %s %s" % (artist, title))).body
        x1 = search_response.find("http://lyrics.wikia.com/")
        if x1 == -1:
            return []
        x2 = search_response.find(r'"',x1)
        link = search_response[x1:x2].replace("&amp;","&")
        response = g.go(link).body
        lyricbox = response.find("class='lyricbox")
        if lyricbox == -1:
            return []
        a = response.find("</div>", lyricbox)
        b = response.find("<!--", lyricbox)
        lyrics = html2text.html2text(response[a+6:b]).replace("\n\n",'\n')
        sr = [ lyrics ]
        sr = map(lambda x: u"%s \nSource: lyrics.wikia.com" % x, sr)
        return sr
