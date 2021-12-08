from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    return [convert_num(num, n) for num in numbers]


def convert_num(num, n):
    prefix = ""
    num_str_clean = str(num).replace(".", "")
    if num_str_clean[0] == "-":
        prefix = "-"
        num_str_clean = num_str_clean[1:]
    if len(num_str_clean) >= n:
        num_str_converted = num_str_clean[:n]
    else:
        num_zeros = n - len(num_str_clean)
        zeros = ["0" for i in range(num_zeros)]
        num_str_converted = num_str_clean + "".join(zeros)
    return int(prefix + num_str_converted)
