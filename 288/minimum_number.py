from typing import List


def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0:
        min_num = 0
    else:
        digits = sorted(list(set([str(digit) for digit in digits])))
        min_num = int("".join(digits))
    return min_num
