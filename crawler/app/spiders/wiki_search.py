from urllib.parse import urlencode

import scrapy


class WikiSearchSpider(scrapy.Spider):
    name = "wiki_search"
    allowed_domains = ["poewiki.net", "poe2wiki.net"]

    custom_settings = {
        "LOG_LEVEL": "INFO",
    }

    def start_requests(self):
        wiki = getattr(self, "wiki", "poewiki").strip().lower()
        query = getattr(self, "query", "").strip()
        fulltext = str(getattr(self, "fulltext", "1")).strip()

        if wiki not in {"poewiki", "poe2wiki"}:
            raise ValueError("wiki must be 'poewiki' or 'poe2wiki'")

        if not query:
            raise ValueError("query argument is required")

        domain = "www.poewiki.net" if wiki == "poewiki" else "www.poe2wiki.net"
        params = {
            "search": query,
            "title": "Special:Search",
            "profile": "default",
            "fulltext": fulltext,
        }
        url = f"https://{domain}/index.php?{urlencode(params)}"
        yield scrapy.Request(url=url, callback=self.parse_search)

    def parse_search(self, response):
        yield {
            "status": "initialized",
            "query": getattr(self, "query", ""),
            "wiki": getattr(self, "wiki", "poewiki"),
            "url": response.url,
        }
