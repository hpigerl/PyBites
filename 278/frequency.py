from typing import List
from collections import Counter


def major_n_minor(numbers: List[int]):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counts = Counter(numbers)
    return (max(counts, key=counts.get), min(counts, key=counts.get))
