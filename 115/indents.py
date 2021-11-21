def count_indents(text: str):
    """Takes a string and counts leading white spaces, return int count"""
    # indent_level = sum([1 if char==' ' else 0 for char in text])
    i = 0
    indent_level = 0
    while text[i] == " ":
        indent_level += 1
        i += 1
    return indent_level
