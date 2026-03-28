from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


def build_url(wiki: str, query: str, fulltext: bool) -> str:
    domain = "www.poewiki.net" if wiki == "poewiki" else "www.poe2wiki.net"

    params = {
        "search": query,
        "title": "Special:Search",
        "profile": "default",
        "fulltext": "1" if fulltext else "0",
    }

    return f"https://{domain}/index.php?{urlencode(params)}"


def search_wiki(wiki: str, query: str, fulltext: bool = False) -> dict:
    url = build_url(wiki, query, fulltext)

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Target main content area
    content = soup.select_one(".mw-parser-output")

    if not content:
        return _no_result(response.url)

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    paragraph = None
    for tag in content.select(".hoverbox"):
        tag.replaceWith(tag.select_one("a"))
    
    for p in content.find_all("p"):
        text = p.get_text(strip=True, separator=' ')
        if text:  # skip empty paragraphs
            paragraph = text
            break

    if title and paragraph:
        return {
            "status": {
                "code": 200,
                "status": "result_found",
            },
            "title": title,
            "summary": paragraph,
            "tooltip": None,
            "url": response.url,
            "results": [],
        }

    return _no_result(response.url)


def _no_result(url: str) -> dict:
    return {
        "status": {
            "code": 404,
            "status": "no_result",
        },
        "title": None,
        "summary": None,
        "tooltip": None,
        "url": url,
        "results": [],
    }