# -*- coding:utf8 -*-

from BaseFetcher import BaseFetcher
import lyricwiki
# за доп.плату - фетчер с изменениями (live) убирать
class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        sr = lyricwiki.get_lyrics(artist, title)
        if sr is None:
            sr = []
        else:
            sr = [sr]
        sr = map(lambda x: u"%s \nSource: lyrics.wikia.com" % x, sr)
        return sr
