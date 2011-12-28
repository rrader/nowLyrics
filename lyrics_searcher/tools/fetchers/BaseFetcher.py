# -*- coding:utf8 -*-

class NotFetched(Exception):
    pass

class BaseFetcher(object):
    def __init__(self, next):
        self.next = next
    
    def _do_fetch(self, title, artist):
        pass
    
    def fetch(self, title, artist):
        #print type(self)
        BaseFetcher.passed += 1
        lyrics = self._do_fetch(title, artist)
        if (lyrics is None) or (len(lyrics) == 0):
            if self.next is not None:
                return self.next.fetch(title, artist)
            else:
                raise NotFetched("can't found lyrics for %s by %s" % (title, artist))
        return lyrics
