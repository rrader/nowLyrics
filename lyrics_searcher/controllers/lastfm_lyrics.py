# -*- coding:utf8 -*-

import os
LF_API_KEY = '021d3c78eac4df04c8719ad9c880d954'
LF_API_SEC = '84c1f32b5b4e004d7146cb01292a604a'
MM_API_KEY = 'a453f8a71d8e47edf061cc7d53b375d6'

os.environ['MUSIXMATCH_API_KEY'] = MM_API_KEY

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lyrics_searcher.lib.base import BaseController, render
import pylast
import musixmatch
from musixmatch.track import search as mm_search

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
           sr = mm_search(q_track=unicode(track.title), q_artist=unicode(track.artist.name))
           sr = filter(lambda x: x.lyrics_id != 0, sr)
           c.found_count = len(sr)
           print c.found_count
           if c.found_count>0:
               lyricses = map(lambda x: x.lyrics(), sr[:2])
               lyricses = map(lambda x: u"%s \n%s (c)\nSource: MusiXmatch.com" % (x['lyrics_body'],x['lyrics_copyright']), lyricses)
               c.lyricses = lyricses
       else:
           c.found_count = 0
       return render('/info.mako')
