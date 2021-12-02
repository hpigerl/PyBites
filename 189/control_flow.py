from typing import List


IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: List[str]):
    names_filtered = []
    for name in names:
        if name[0] == QUIT_CHAR:
            break
        elif name[0] == IGNORE_CHAR or any([char.isnumeric() for char in name]):
            continue
        names_filtered.append(name)
        if len(names_filtered) == MAX_NAMES:
            break
    return names_filtered
