# -*- coding:utf8 -*-

import amalgamalab_fetcher, lyrsense_fetcher

from BaseFetcher import NotFetched

fetchers = [lyrsense_fetcher.Fetcher(None), amalgamalab_fetcher.Fetcher(None)]

def get_translations(title, artist):
    res = []
    for f in fetchers:
        res = res + f.fetch(title, artist)
    return res
