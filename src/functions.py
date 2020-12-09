import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode


SEARCH_URL = "https://duckduckgo.com/?"
SUGGESTION_URL = "https://duckduckgo.com/ac/?"

url = "https://docs.python.org/3.4/howto/urllib2.html"


def generate_url(search):
    """
    >>> generate_url("hallo")
    'https://duckduckgo.com/?q=hallo'
    """
    return SEARCH_URL + urlencode({"q": search})


def generate_suggestions(search, lang="en-US"):
    """
    >>> generate_suggestions("hello")
    ['hello', 'hello fresh', 'hello neighbor', 'hello kitty', 'hellosign', 'hello magazine', 'hellofax', 'hello world']

    >>> generate_suggestions("hallo", "de-DE")
    ['hallo', 'halloween', 'hallo zusammen', 'hallo meinung', 'hallo hessen', 'halloleinwand', 'halloween 2020', 'halloween rezepte']

    """
    url = SUGGESTION_URL + urlencode({"q": search})
    headers = {'Accept-Language': lang + ",en-US;q=0.7"}
    req = Request(url, headers=headers)
    suggestions = []
    with urlopen(req) as url:
        suggestions = json.loads(url.read().decode()) or []

    return [s["phrase"] for s in suggestions if s.get("phrase")]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
