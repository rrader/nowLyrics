from lyrics_searcher.tests import *

class TestLastfmLyricsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='lastfm_lyrics', action='index'))
        # Test response...
