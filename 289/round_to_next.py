from math import ceil


def round_to_next(number: int, multiple: int):
    fraction_of_multiple = number / multiple
    next_multiple = multiple * ceil(fraction_of_multiple)
    return next_multiple
