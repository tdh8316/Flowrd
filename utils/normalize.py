import re


def normalize_string(text: str) -> str:
    text = re.sub(r'function .+|//.*\n', '', text)
    text = re.sub(r' *.+\n *.+\n| *\n *', '', text)
    return text
