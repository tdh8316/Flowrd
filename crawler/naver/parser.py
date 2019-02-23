from urllib import request

from bs4 import BeautifulSoup

from utils.normalize import normalize_string


def parse_body(url: str) -> str:
    article_body: str = ''
    for body in BeautifulSoup(
            request.urlopen(url),
            "lxml",
            from_encoding="UTF-8"
    ).find_all("div", {"id": "articleBodyContents"}):
        article_body = ''.join(body.find_all(text=True))

    return normalize_string(article_body)
