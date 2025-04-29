import re
import string
from collections import Counter
from typing import List

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def get_longest_diverse_words(file_path: str) -> List[str]:
    text = read_file(file_path)
    words = set(word.lower() for word in re.findall(r'\b\w+\b', text))
    return sorted(words, key=lambda w: (-len(set(w)), -len(w), w))[:10]

def get_rarest_char(file_path: str) -> str:
    text = read_file(file_path)
    if not text:
        return ""
    counts = Counter(text)
    return min(counts.items(), key=lambda x: (x[1], ord(x[0])))[0]

def count_chars(file_path: str, char_set: str) -> int:
    text = read_file(file_path)
    return sum(1 for ch in text if ch in char_set)

def get_most_common_non_ascii_char(file_path: str) -> str:
    text = read_file(file_path)
    non_ascii = [ch for ch in text if ord(ch) > 127]
    if not non_ascii:
        return ""
    counts = Counter(non_ascii)
    return max(counts.items(), key=lambda x: (x[1], -ord(x[0])))[0]

if __name__ == "__main__":
    file_path = "C:\\1\\data.txt"  

    print("10 longest diverse words:")
    print(get_longest_diverse_words(file_path))

    print("\nRarest character:", repr(get_rarest_char(file_path)))

    print("\nNumber of punctuation characters:", count_chars(file_path, string.punctuation))

    print("\nNumber of non-ASCII characters:", count_chars(file_path, filter(lambda x: ord(x) > 127, string.printable)))

    print("\nMost common non-ASCII character:", repr(get_most_common_non_ascii_char(file_path)))