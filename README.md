# Arakaali

**Arakaali** is a Python project made of two apps:

* **crawler**: a wiki crawler/search service for Path of Exile wikis
* **doe**: a Discord interface that queries the crawler and formats results

## Example usecase

### Exact match

```text
/doe2 armor
→ page found
→ return summary + tooltip + link + more results
```

### No result

```text
/doe1 asdfghjkl
→ no page and no related result
→ "No result found. Please try another query."
```

### Related results

```text
/doe1 aura
→ no direct page
→ return top 5 matching pages
```

The Discord bot should not parse wiki HTML directly. Keep parsing inside `crawler` so `doe` stays simple.

## Project structure

```text
/arakaali
  /crawler          # wiki crawler app
  /doe              # discord interface
```

## Apps

### 1) crawler — wiki crawler

The crawler searches:

* `https://www.poewiki.net`
* `https://www.poe2wiki.net`

Search endpoint example:

```text
https://www.poe2wiki.net/index.php?search=armor&title=Special%3ASearch&profile=default&fulltext=1
```

Parameters:

* `search`: the user query
* `fulltext=1`: show full search results
* without `fulltext=1`: redirect to the first valid result when possible

The crawler should return one of these outcomes:

1. **Exact page found**

   * page title
   * first paragraph
   * tooltip if available
   * page link
   * extra results if relevant

2. **No page found**

   * `No result found. Please try another query.`

3. **No exact page, but related results found**

   * top 5 results

## Minimal API contract suggestion

The crawler can expose a simple function or API like this:

```python
def search_wiki(wiki: str, query: str, fulltext: bool = False) -> dict:
    ...
```

Possible response shape:

```python
{
    "status": "page_found" | "no_result" | "results_found",
    "title": "Armor",
    "summary": "First paragraph...",
    "tooltip": "Optional tooltip",
    "url": "https://...",
    "results": [
        {"title": "...", "url": "..."}
    ]
}
```
### 2) doe — Discord interface

Slash commands:

* `/doe1 [query]` → search **poewiki.net**
* `/doe2 [query]` → search **poe2wiki.net**

Bot behavior:

* If a page is found, show:

  * first paragraph
  * tooltip if available
  * page link
  * button or action to show more results

* If nothing is found, show:

  * `No result found. Please try another query.`

* If no exact page is found but search results exist, show:

  * top 5 results




## Development notes

* Normalize queries before searching
* Handle redirects cleanly
* Limit fallback results to 5
* Keep Discord responses short and readable
* Cache frequent requests to reduce wiki load
* Add rate limiting to avoid abuse

## Requirements

* **Python 3.11+**
* **Scrapy** for crawling and parsing
* **discord.py** for the bot

## Installation

### For Windows
```bash
python -m venv .venv
.venv\Scripts\activate.bat

```

## Run

### Start crawler

```bash
python -m crawler.app
```

### Start Discord bot

```bash
python -m doe.app
```

## Roadmap

To Be Determined