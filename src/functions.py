import json
from urllib.request import urlopen
from urllib.parse import urlencode


SEARCH_URL = "https://duckduckgo.com/?"
SUGGESTION_URL = "https://duckduckgo.com/ac/?"


def generate_url(search):
    """
    >>> generate_url("hallo")
    'https://duckduckgo.com/?q=hallo'
    """
    return SEARCH_URL + urlencode({"q": search})


def generate_suggestions(search):
    """
    >>> generate_suggestions("hello")
    ['hello', 'hello fresh', 'hello neighbor', 'hello kitty', 'hellosign', 'hello magazine', 'hello fresh meals', 'hellofax']
    """
    suggestions = []
    with urlopen(SUGGESTION_URL + urlencode({"q": search})) as url:
        suggestions = json.loads(url.read().decode()) or []

    return [s["phrase"] for s in suggestions if s.get("phrase")]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
