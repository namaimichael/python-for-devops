from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""

    search_results = search_wiki(value)
    return {"search_results": search_results}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve Wikipedia page"""

    wiki_results = wikilogic(name)
    return {"wiki_results": wiki_results}


@app.get("/phrase/{value}")
async def phrase(value: str):
    """Page to search in Wikipedia and phrases"""

    phrase_results = wikiphrases(value)
    return {"phrase_results": phrase_results}


if __name__ == "__main__":
    uvicorn.run(app, port=8282, host="0.0.0.0")
