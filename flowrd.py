import time
from multiprocessing import Process

from crawler.daum import daum
from crawler.naver import naver

TEST_URL: str = "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=018&aid=0004314611"


def main():
    start_time = time.time()
    process_naver = Process(target=naver.get_word_frequency)
    process_daum = Process(target=daum.get_word_frequency)

    process_naver.start()
    process_daum.start()

    process_naver.join()
    process_daum.join()

    print(time.time() - start_time)


if __name__ == '__main__':
    main()
