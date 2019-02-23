import re
from urllib import request

from bs4 import BeautifulSoup

from crawler import daum
from crawler.daum import parser
from utils.normalize import normalize_string


class DaumNews(object):

    def __init__(self):
        self._titles: list = []
        self._links: list = []
        self.site = BeautifulSoup(
            request.urlopen("https://media.daum.net/").read(),
            "lxml",
            from_encoding="UTF-8"
        )

        self._parse_page()

        self._links = list(set(self._links))

    def _parse_page(self):
        for item in self.site.find_all('a', {"href": re.compile(r'https?://v\.media\.daum\.net/v')}):
            title = normalize_string(item.text)
            if title:
                self._titles.append(title)
            self._links.append(item["href"])

        for item in self.site.find_all("strong", {"class": re.compile("tit_\w+")}):
            title = normalize_string(item.text)
            if title:
                self._titles.append(title)

    def get_article_body(self) -> str:
        for link in self._links:
            yield daum.parser.parse_body(link)

    @property
    def titles(self) -> tuple:
        return tuple(set(self._titles))
