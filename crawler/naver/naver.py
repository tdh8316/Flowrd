from collections import Counter

from konlpy.tag import Okt

from crawler.naver.news import list_naver_news, NaverNews

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

    count = Counter(nouns)

    for k, v in count.most_common(100):
        print(k, v)
