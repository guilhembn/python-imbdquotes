import urllib.request
import urllib.parse

movie_ids = {"The Matrix": "tt0133093",
             "Rick and Morty": "tt2861424"}


IMBD_URL_QUOTE = 'https://www.imdb.com/title/{movie_id}/quotes'
DEFAULT_MAX_QUOTES = 100


def html_from_url(url, params=None):
    if params:
        url += urllib.parse.quote(params)
    res = urllib.request.urlopen(url)
    body = res.read().decode()
    return body
