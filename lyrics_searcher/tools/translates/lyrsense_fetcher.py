# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
from grab import Grab
import html2text
import urllib

class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        g = Grab()
        search_response = g.go("http://www.google.com/search?q=%s" % urllib.quote('site:en.lyrsense.com "%s" "%s"' % (artist, title))).body
        if search_response.find("yellow_warning.gif") != -1:
            return []
        x1 = search_response.find("http://en.lyrsense.com/")
        if x1 == -1:
            return []
        x2 = search_response.find(r'"',x1)
        link = search_response[x1:x2].replace("&amp;","&")
#        text = g.go(link).body
#        x1 = text.find("Все переводы автора")
#        x1 = text.find('class="text"', x1)+13
        return [ (link, "lyrsense.com") ]
