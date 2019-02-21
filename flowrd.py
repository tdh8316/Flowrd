from crawler import naver

from crawler.naver.naver import list_naver_news

TEST_URL: str = "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=018&aid=0004314611"


def main():
    naver.naver.get_word_frequency()


if __name__ == '__main__':
    main()
