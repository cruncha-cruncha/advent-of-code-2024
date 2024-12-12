# problem 2 part 2

import pickle

def sum_single(num, depth, depth_limit, sums_n, total):
    if depth >= depth_limit:
        return 1
    if not num in sums_n:
        raise Exception('Num not in sums_n', num)

    for k, v in sums_n[num].items():
        total += v * sum_single(k, depth + 1, depth_limit, sums_n, 0)

    return total

def main():
    sums_n = {}
    with open('dict.pickle', 'rb') as handle:
        sums_n = pickle.load(handle)

    print("loaded")

    original_nums = []
    with open('input.txt') as f:
        text = f.read().strip()
        original_nums = [int(c) for c in text.split()]

    JUMP = 25
    DEPTH = 3

    print(original_nums)

    total = 0
    for num in original_nums:
        print("summing", num)
        total = sum_single(num, 0, DEPTH, sums_n, total)
        print(total)

    print(total)

if __name__ == '__main__':
    main()