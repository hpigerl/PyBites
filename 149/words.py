from typing import List


def sort_words_case_insensitively(words: List[str]):
    """Sort the provided word list ignoring case, and numbers last
    (1995, 19ab = numbers / Happy, happy4you = strings, hence for
     numbers you only need to check the first char of the word)
    """
    # words = [word.lower() for word in words]
    numbers = [word for word in words if word[0].isnumeric()]
    words_no_numbers = [word for word in words if word not in numbers]
    return sorted(words_no_numbers, key=str.lower) + sorted(numbers, key=str.lower)
