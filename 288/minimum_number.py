from typing import List
from functools import reduce


def minimum_number(digits: List[int]) -> int:
    digits = sorted(set(digits))
    min_num = reduce(lambda x, y: 10 * x + y, digits, 0)
    return min_num
