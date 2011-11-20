# -*- coding:utf8 -*-

class NotFetched(Exception):
    pass

#class TranslationURL(unicode):
#    pass

class BaseFetcher(object):
    def __init__(self, next):
        self.next = next
    
    def _do_fetch(self, title, artist):
        pass
    
    def fetch(self, title, artist):
        #print type(self)
        translates = self._do_fetch(title, artist)
        if (translates is None) or (len(translates) == 0):
            if self.next is not None:
                return self.next.fetch(title, artist)
            else:
                raise NotFetched("can't found translations for %s by %s" % (title, artist))
        return translates
