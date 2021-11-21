def tail(filepath: str, n: int):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines"""
    text = open(filepath, "r").read()
    tail = text.splitlines()[-n:]
    return tail
