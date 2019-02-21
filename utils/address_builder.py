import urllib.parse


_BASE_URL = "https://search.naver.com/search.naver?"


def build_address(keyword: str, site: str = _BASE_URL):
    return f"{site}&query={urllib.parse.quote_plus(keyword)}"
