import re
from urllib import request

from bs4 import BeautifulSoup

from utils.normalize import normalize_string


class DaumNews(object):

    def __init__(self, url: str):
        self.response = request.urlopen(url)
        self.soup = None
        if self.response.status == 200:
            self.soup = BeautifulSoup(self.response.read(), "lxml", from_encoding="UTF-8")

    def get_body(self) -> str:
        article: str = ''
        for body in self.soup.find_all('p', {"dmcf-ptype": "general"}):
            article += ' ' + body.text

        return normalize_string(article)


def list_daum_news() -> tuple:
    """
    [0] = titles: str, [1] = links: str
    :return:
    """
    article_list = []
    address_list = []

    bs = BeautifulSoup(
        request.urlopen("https://media.daum.net/").read(),
        "lxml",
        from_encoding="UTF-8")
    for item in bs.find_all('a', {"href": re.compile(r'.+v\.media\.daum')}):
        title = normalize_string(item.text)
        if title:
            article_list.append(title)
        address_list.append(item["href"])

    for item in bs.find_all("strong", {"class": "tit_thumb"}):
        title = normalize_string(item.text)
        if title:
            article_list.append(title)

    return (
        tuple(set(article_list)),
        tuple(set(address_list))
    )
