# -*- coding:utf8 -*-

import musixmatch_fetcher, lyricwiki_fetcher, nashe_fetcher, lyrics78_fetcher
import textypesen_fetcher, waptorrent_fetcher

from BaseFetcher import BaseFetcher,NotFetched
fetchers_chain = waptorrent_fetcher.Fetcher(None)
fetchers_chain = musixmatch_fetcher.Fetcher(fetchers_chain)
fetchers_chain = lyrics78_fetcher.Fetcher(fetchers_chain)
fetchers_chain = textypesen_fetcher.Fetcher(fetchers_chain)
fetchers_chain = nashe_fetcher.Fetcher(fetchers_chain)
fetchers_chain = lyricwiki_fetcher.Fetcher(fetchers_chain)

def get_lyrics(title, artist):
    #TODO: сортировать по-разному фетчеры при разных входных данных
    BaseFetcher.passed = 0
    return fetchers_chain.fetch(title, artist)

def get_passed_fetchers_count():
    return BaseFetcher.passed
