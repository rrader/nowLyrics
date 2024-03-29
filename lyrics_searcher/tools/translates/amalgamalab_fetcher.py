# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
from grab import Grab
import html2text
import urllib

class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        g = Grab()
        request = "http://www.google.com/search?q=%s" % urllib.quote('site:amalgama-lab.com "%s" "%s"' % (artist, title))
        search_response = g.go(request).body
        if search_response.find("yellow_warning.gif") != -1:
            return []
        x1 = search_response.find("http://www.amalgama-lab.com/songs/")
        if x1 == -1:
            return []
        x2 = search_response.find(r'"',x1)
        link = search_response[x1:x2].replace("&amp;","&")
        return [ (link, "amalgama-lab.com") ]
