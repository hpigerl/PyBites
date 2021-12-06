from itertools import combinations


def find_number_pairs(numbers, N=10):
    return list(gen_valid_combinations(numbers, N))


def gen_valid_combinations(numbers, N):
    for combo in combinations(numbers, 2):
        if sum(list(combo)) == N:
            yield combo
