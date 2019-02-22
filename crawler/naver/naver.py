from collections import Counter

from konlpy.tag import Okt

from crawler.naver.news import list_naver_news, NaverNews
from utils.normalize import dummy_words

LP = Okt()


def get_word_frequency():
    nouns = []
    naver_news = list_naver_news()

    # Analyze the titles of the news
    for title in naver_news[0]:
        for n in LP.nouns(title):
            if len(n) > 1:
                nouns.append(n)

    for link in naver_news[1]:
        for n in LP.nouns(
                NaverNews(link).get_body()
        ):
            if len(n) > 1:
                nouns.append(n)

    nouns = [noun for noun in nouns if noun not in dummy_words]

    count = Counter(nouns)

    with open("naver.txt", 'w', encoding="utf8") as res:
        for k, v in count.most_common(10):
            res.write(f"{k}: {v}\n")
