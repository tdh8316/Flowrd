import json
import os
import time
from multiprocessing import Process

import matplotlib.pyplot as plt

from crawler import naver, daum


def main():
    start_time = time.time()
    process_naver = Process(target=naver.get_word_frequency)
    process_daum = Process(target=daum.get_word_frequency)

    process_naver.start()
    process_daum.start()

    process_naver.join()
    process_daum.join()

    import wordcloud

    naver_img = wordcloud.WordCloud(
        font_path="bin/nanumbarunpen.ttf",
        width=1200,
        height=800,
        background_color="white"
    ).generate_from_frequencies(json.loads(open("model/naver.json", 'r', encoding="UTF-8").read()))

    plt.figure(figsize=(16, 8))
    plt.axis("off")
    plt.imshow(naver_img)
    plt.savefig("naver.png")

    naver_img = wordcloud.WordCloud(
        font_path="bin/nanumbarunpen.ttf",
        width=1200,
        height=800,
        background_color="white"
    ).generate_from_frequencies(json.loads(open("model/daum.json", 'r', encoding="UTF-8").read()))

    plt.figure(figsize=(16, 8))
    plt.axis("off")
    plt.imshow(naver_img)
    plt.savefig("daum.png")

    print(time.time() - start_time)


if __name__ == '__main__':
    if not os.path.isdir("./model/"):
        os.mkdir(path="model", mode=0o777)

    main()
