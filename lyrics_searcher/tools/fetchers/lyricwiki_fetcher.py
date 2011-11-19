# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
import lyricwiki
from lyrics_searcher.tools.LyricWiki import LyricWiki_services
# за доп.плату - фетчер с изменениями (live) убирать
class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        try:
            soap = LyricWiki_services.LyricWikiBindingSOAP("http://lyrics.wikia.com/server.php")
            song = LyricWiki_services.getSongRequest()
            song.Artist = unicode(artist).strip()
            song.Song = unicode(title).strip()
            result = soap.getSong(song)
            sr = [ result.Return.Lyrics ]
            if result.Return.Lyrics.strip() == u"Not found":
                sr = []
        except:
            sr = []
        sr = map(lambda x: u"%s \nSource: lyrics.wikia.com" % x, sr)
        return sr
