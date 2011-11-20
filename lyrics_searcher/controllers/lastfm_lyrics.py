# -*- coding:utf8 -*-

LF_API_KEY = '021d3c78eac4df04c8719ad9c880d954'
LF_API_SEC = '84c1f32b5b4e004d7146cb01292a604a'

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lyrics_searcher.lib.base import BaseController, render
import pylast
from pylast import WSError
from lyrics_searcher.tools.fetchers import get_lyrics, NotFetched as LyricsNotFetched
from lyrics_searcher.tools.translates import get_translations, NotFetched as TranslationsNotFetched

log = logging.getLogger(__name__)

def make_track_text(track):
    if track is None:
        return u"No track"
    else:
        return u'"%s" BY %s' % (track.title, track.artist.name)

class LastfmLyricsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/lastfm_lyrics.mako')
        # or, return a string
        return render('/input.mako')
    
    def username(self):
       user = request.params['user']
       session['username'] = user
       session.save()
       api = pylast.LastFMNetwork(api_key = LF_API_KEY, api_secret = LF_API_SEC)
       luser = api.get_user(user)
       c.luser = user
       track = None
       try:
           track = luser.get_now_playing()
       except WSError:
           return render('/error.mako')
       np = make_track_text(track)
       if track is None:
           track = luser.get_recent_tracks()[0].track
           last_played = make_track_text(track) # проверить на [] или вообще есть
           np = "no now_playing, but last played: %s" % (last_played)
       c.nowplaying = np
       if track is not None:
           sr = []
           title = track.title.encode('utf-8')
           artist = track.artist.name.encode('utf-8')
           try:
               sr = get_lyrics(title, artist)
           except LyricsNotFetched:
               pass
           tr = []
           try:
               tr = get_translations(title, artist)
           except TranslationsNotFetched:
               pass
           c.found_count = len(sr)
           c.lyricses = sr
           c.trans_count = len(tr)
           c.trans = tr
       else:
           c.found_count = 0
           c.trans_count = 0
       return render('/info.mako')
