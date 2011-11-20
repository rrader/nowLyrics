# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
import lyricwiki
from lyrics_searcher.tools.LyricWiki import LyricWiki_services
from grab import Grab
import html2text
import urllib
# за доп.плату - фетчер с изменениями. (live) убирать
class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        g = Grab()
        response = g.go("http://lyrics.wikia.com/%s:%s" % (urllib.quote(artist), urllib.quote(title))).body
        lyricbox = response.find("class='lyricbox")
        if lyricbox == -1:
            return []
        a = response.find("</div>", lyricbox)
        b = response.find("<!--", lyricbox)
        lyrics = html2text.html2text(response[a+6:b]).replace("\n\n",'\n')
        sr = [ lyrics ]
        sr = map(lambda x: u"%s \nSource: lyrics.wikia.com" % x, sr)
        return sr
