# -*- coding:utf8 -*-

LF_API_KEY = '021d3c78eac4df04c8719ad9c880d954'
LF_API_SEC = '84c1f32b5b4e004d7146cb01292a604a'

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lyrics_searcher.lib.base import BaseController, render
import pylast
from lyrics_searcher.tools.fetchers import get_lyrics, NotFetched

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
       track = luser.get_now_playing()
       np = make_track_text(track)
       if np is None:
           track = luser.get_recent_tracks()[0].track
           last_played = make_track_text(track) # проверить на [] или вообще есть
           np = "no now_playing, but last played: %s" % (last_played)
       c.nowplaying = np
       if track is not None:
           sr = []
           try:
               title = track.title
               artist = track.artist.name
               sr = get_lyrics(title, artist)
           except NotFetched:
               pass
           c.found_count = len(sr)
           c.lyricses = sr
       else:
           c.found_count = 0
       return render('/info.mako')
