def is_armstrong(n: int) -> bool:
    digits = [int(c) for c in str(n)]
    sum_ = sum([digit ** len(digits) for digit in digits])
    return sum_ == n
