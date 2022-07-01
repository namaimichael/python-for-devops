import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    my_search = wikipedia.search(name)
    return my_search


def phrase(name):
    """Returns phrases from Wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
