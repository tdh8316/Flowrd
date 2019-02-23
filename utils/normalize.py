import re


def normalize_string(text: str) -> str:
    text = re.sub(r'function .+|//.*\n', '', text)
    text = re.sub(r' *.+\n *.+\n| *\n *| {2,}', '', text)
    text = ' '.join(text.split())
    return text


dummy_words = (
    "기자",
    "뉴스",
    "구독",
    "대해",
    "때문",
    "특별",
    "대한",
    "한국",
    "경우",
    "이번"
)
