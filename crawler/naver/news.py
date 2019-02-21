import re
import urllib.request as request

from bs4 import BeautifulSoup, Tag

from utils.normalize import normalize_string


class NaverNews(object):

    def __init__(self, url: str):
        self.response = request.urlopen(url)
        self.soup = None
        if self.response.status == 200:
            self.soup = BeautifulSoup(self.response.read(), "lxml", from_encoding="UTF-8")

    def get_body(self) -> str:
        article: str = ''
        for body in self.soup.find_all("div", {"id": "articleBodyContents"}):
            article = ''.join(body.find_all(text=True))

        return normalize_string(article)


def list_naver_news() -> tuple:
    """
    [0] = titles: str, [1] = links: str
    :return:
    """
    article_list = []
    address_list = []

    bs = BeautifulSoup(
        request.urlopen("https://news.naver.com/main/home.nhn").read(),
        "lxml",
        from_encoding="UTF-8")

    for item in bs.find_all("div", {"class": "newsnow_tx_inner"}):
        article_list.append(normalize_string(item.text))
        item: Tag
        address_list.append(item.find('a')["href"])

    for item in bs.select("div.mtype_list_wide"):
        for arts in item.find_all("li"):
            article_list.append(normalize_string(arts.text))
            address_list.append(item.find('a')["href"])

    for item in bs.select("div.com_list"):
        for arts in (item.find_all("li")):
            article_list.append(normalize_string(arts.text))
            address_list.append(item.find('a')["href"])

    for item in bs.find_all("a", {"href": re.compile(r'/main/ranking/read\.nhn\?.+')}):
        article_list.append(normalize_string(item.text))
        address_list.append(item["href"])

    for i in range(len(address_list)):
        if not address_list[i].startswith("https://"):
            address_list[i] = "https://news.naver.com/" + address_list[i]

    return (
        tuple(set(article_list)),
        tuple(set(address_list))
    )
