# -*- coding:utf8 -*-

import amalgamalab_fetcher, lyrsense_fetcher

from BaseFetcher import NotFetched

def get_translations(title, artist):
    fetchers_chain = lyrsense_fetcher.Fetcher(None)
    fetchers_chain = amalgamalab_fetcher.Fetcher(fetchers_chain)
    return fetchers_chain.fetch(title, artist)
