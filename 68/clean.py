def remove_punctuation(input_string: str):
    """Return a str with punctuation chars stripped out"""
    punctuation = [
        "!",
        "#",
        "$",
        "%",
        "&",
        "[\]",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "\\",
        "^",
        "_",
        "`",
        "'",
        "{",
        "|",
        "}",
        "~",
    ]
    cleaned_string = "".join([char if char not in punctuation else "" for char in input_string])

    return cleaned_string
