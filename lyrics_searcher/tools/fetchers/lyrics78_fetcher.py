# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
from grab import Grab
import html2text
import urllib
# за доп.плату - фетчер с изменениями. (live) убирать
class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        g = Grab()
        search_response = g.go("http://www.google.com/search?q=%s" % urllib.quote("site:www.lyrics78.com %s %s" % (artist, title))).body
        x1 = search_response.find("http://www.lyrics78.com/")
        if x1 == -1:
            return []
        x2 = search_response.find(r'"',x1)
        link = search_response[x1:x2].replace("&amp;","&")
        response = g.go(link).body
        x1 = response.find("</h2>")+5
        x2 = response.find("<h2>",x1)
        lyrics = html2text.html2text(response[x1:x2].decode("utf8")).replace("\n\n",'\n')
        sr = [ lyrics ]
        sr = map(lambda x: u"%s \nSource: www.lyrics78.com" % x, sr)
        return sr
