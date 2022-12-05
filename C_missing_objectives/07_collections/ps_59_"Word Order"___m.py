"""
You are given n words. Some words may repeat. 
"""


def find_unique_words(words):
    """
    :param words: a list of words
    :return: a list of unique words
    """
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def test_find_unique_words():
    words = ["python", "python", "python", "ruby"]
    assert ["python", "ruby"] == find_unique_words(words)


if __name__ == '__main__':
    test_find_unique_words()