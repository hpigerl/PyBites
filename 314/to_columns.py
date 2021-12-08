from typing import List  # not needed when we upgrade to 3.9
from math import ceil


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    rows = ceil(len(names) / cols)
    for i in range(rows):
        row_names = [
            name + "".join([" " for _ in range(10 - len(name))])
            for name in names[i * cols : (i + 1) * cols]
        ]
        row_str = "| " + "| ".join(row_names)
        print(row_str)
