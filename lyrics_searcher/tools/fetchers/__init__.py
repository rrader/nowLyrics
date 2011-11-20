# -*- coding:utf8 -*-

import musixmatch_fetcher, lyricwiki_fetcher, nashe_fetcher

from BaseFetcher import NotFetched

def get_lyrics(title, artist):
    #TODO: сортировать по-разному фетчеры при разных входных данных
    fetchers_chain = musixmatch_fetcher.Fetcher(None)
    fetchers_chain = nashe_fetcher.Fetcher(fetchers_chain)
    fetchers_chain = lyricwiki_fetcher.Fetcher(fetchers_chain)
    return fetchers_chain.fetch(title.encode('utf-8'), artist.encode('utf-8'))
