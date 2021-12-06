from collections import Counter


def freq_digit(num: int) -> int:
    freqs = Counter(str(num))
    return int(freqs.most_common(1)[0][0])
