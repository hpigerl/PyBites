def wc(file_: str):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""
    text = open(file_, "r").read()
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    return f"{lines}   {words}   {chars}   {file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
