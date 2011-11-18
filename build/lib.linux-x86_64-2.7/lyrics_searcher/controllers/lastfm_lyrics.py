# -*- coding:utf8 -*-

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lyrics_searcher.lib.base import BaseController, render
import pylast
import musixmatch
log = logging.getLogger(__name__)

LF_API_KEY = '021d3c78eac4df04c8719ad9c880d954'
LF_API_SEC = '84c1f32b5b4e004d7146cb01292a604a'
MM_API_KEY = 'a453f8a71d8e47edf061cc7d53b375d6'

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
       np = make_track_text(luser.get_now_playing())
       if np is None:
           last_played = make_track_text(luser.get_recent_tracks()[0].track) # проверить на [] или вообще есть
           np = "no now_playing, but last played: %s" % (last_played)
       c.nowplaying = np
       return render('/info.mako')
