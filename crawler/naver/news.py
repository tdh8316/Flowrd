import re
from urllib import request

from bs4 import BeautifulSoup

from crawler import naver
from crawler.naver import parser
from utils.normalize import normalize_string


class NaverNews(object):

    def __init__(self):
        self._titles: list = []
        self._links: list = []
        self.site = BeautifulSoup(
            request.urlopen("https://news.naver.com/main/home.nhn").read(),
            "lxml",
            from_encoding="UTF-8"
        )

        self._parse_page()

        self._links = list(set(self._links))

    def _parse_page(self):
        for item in self.site.find_all("div", {"class": "newsnow_tx_inner"}):
            self._titles.append(normalize_string(item.text))
            self._links.append(item.find('a')["href"])

        for item in self.site.select("div.mtype_list_wide"):
            for arts in item.find_all("li"):
                self._titles.append(normalize_string(arts.text))
                self._links.append(item.find('a')["href"])

        for item in self.site.select("div.com_list"):
            for arts in (item.find_all("li")):
                self._titles.append(normalize_string(arts.text))
                self._links.append(item.find('a')["href"])

        for item in self.site.find_all("a", {"href": re.compile(r'/main/ranking/read\.nhn\?.+')}):
            self._titles.append(normalize_string(item.text))
            self._links.append(item["href"])

        for i in range(len(self._links)):
            if not self._links[i].startswith("https://"):
                self._links[i] = "https://news.naver.com/" + self._links[i]

    def get_article_body(self) -> str:
        for link in self._links:
            yield naver.parser.parse_body(link)

    @property
    def titles(self) -> tuple:
        return tuple(set(self._titles))
