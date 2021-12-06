from collections import Counter


def freq_digit(num: int) -> int:
    freqs = Counter([int(c) for c in str(num)])
    return freqs.most_common(2)[0][0]
