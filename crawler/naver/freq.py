import json
from collections import Counter

from konlpy.tag import Okt, Hannanum

from crawler.naver.news import NaverNews
from utils.normalize import dummy_words

kt = Hannanum()


def get_word_frequency():
    naver_news = NaverNews()
    nouns = []

    titles = naver_news.titles

    for title in titles:
        for noun in kt.nouns(title):
            if len(noun) > 1 and noun not in dummy_words:
                nouns.append(noun)

    for body in naver_news.get_article_body():
        for noun in kt.nouns(body):
            if len(noun) > 1 and noun not in dummy_words:
                nouns.append(noun)

    with open("model/naver.json", 'w', encoding="UTF-8") as data:
        _data: dict = {}
        for k, v in Counter(nouns).most_common(100):
            _data[k] = v
        data.write(json.dumps(_data, ensure_ascii=False))
