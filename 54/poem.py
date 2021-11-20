INDENTS = 4

import re


def print_hanging_indents(poem: str):
    poem_lines = poem.splitlines()
    i = 0
    del_lines = [False for line in poem_lines]
    poem_lines_formatted = poem_lines.copy()
    for line in poem_lines:
        if line == "":
            del_lines[i] = True
        else:
            poem_lines_formatted[i] = "".join(" " for i in range(INDENTS)) + line
        i += 1
    poem_formatted = "".join(
        [
            line + "\n" if not del_line else ""
            for (line, del_line) in zip(poem_lines_formatted, del_lines)
        ]
    )
    print(poem_formatted)
