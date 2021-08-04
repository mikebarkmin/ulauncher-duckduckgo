import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode


SEARCH_URL = "https://duckduckgo.com/?"
SUGGESTION_URL = "https://duckduckgo.com/ac/?"
API_URL = "https://api.duckduckgo.com/?"

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


def generate_instant_answer(search, lang="en-US"):
    """
    >>> generate_instant_answer("duckduckgo")
    ('DuckDuckGo', "DuckDuckGo is an internet search engine that emphasizes protecting searchers' privacy and avoiding
     the filter bubble of personalized search results. DuckDuckGo distinguishes itself from other search engines by not
     profiling its users and by showing all users the same search results for a given search term. The company is based
     in Paoli, Pennsylvania, in Greater Philadelphia and has 130 employees as of July 2021. The company name is a
     reference to the children's game duck, duck, goose.", 'https://en.wikipedia.org/wiki/DuckDuckGo')
    """
    url = API_URL + urlencode(
        {
            "q": search,
             "format": "json",
             "no_redirect": 1,
             "no_html": 1,
             "skip_disambig": 1,
        }
    )
    headers = {'Accept-Language': lang + ",en-US;q=0.7"}
    req = Request(url, headers=headers)
    with urlopen(req) as url:
        response = json.loads(url.read().decode()) or {}
    instant_item = response.get("Heading", "")
    instant_answer = response.get("AbstractText", "")
    instant_url = response.get("AbstractURL", "")

    return instant_item, instant_answer, instant_url


if __name__ == "__main__":
    import doctest

    doctest.testmod()
