# -*- coding:utf8 -*-

MM_API_KEY = 'a453f8a71d8e47edf061cc7d53b375d6'

import os
os.environ['MUSIXMATCH_API_KEY'] = MM_API_KEY

from musixmatch.track import search as mm_search
from BaseFetcher import BaseFetcher

class Fetcher(BaseFetcher):
    def _do_fetch(self, title, artist):
        sr = mm_search(q_track=title, q_artist=artist)
        sr = filter(lambda x: x.lyrics_id != 0, sr)
        sr = map(lambda x: x.lyrics(), sr[:3])
        sr = map(lambda x: u"%s \n%s (c)\nSource: MusiXmatch.com" % (x['lyrics_body'],x['lyrics_copyright']), sr)
        return sr
