# problem 2 part 1

# this is not a good solution, would be better to:
# a. memoize/cache based on a tuple: (number on stone, depth) (https://github.com/sanvirk99/adventcode/blob/fa8d4d3649da13187d7e9a66f5b98c54c944d558/day11.py#L49) or
# b. use two maps: current and next, where key = number on the stone and value = count of stones with that number (https://github.com/bozdoz/advent-of-code-2024/blob/main/day-11/src/main.rs)

from collections import Counter
import pickle

def iterate_rocks(nums, count):
    for blink in range(count):
        end = len(nums)
        for i in range(end):
            if nums[i] == 0:
                nums[i] = 1
            elif len(str(nums[i])) % 2 == 0:
                num = str(nums[i])
                half = len(num) // 2
                nums[i] = int(num[:half])
                nums.append(int(num[half:]))
            else:
                nums[i] *= 2024
    return dict(Counter(nums))

def iterate_options(nums, already_computed, jump):
    sums_n = {}
    todo = set()
    for num in nums:
        if num in already_computed:
            continue
        else:
            already_computed.add(num)
        sums_n[num] = iterate_rocks([num], jump)
        todo.update(sums_n[num].keys())
    return sums_n, already_computed, todo - set(nums)

def main():
    nums = []
    with open('input.txt') as f:
        text = f.read().strip()
        nums = [int(c) for c in text.split()]

    original_nums = nums.copy()

    JUMP = 25
    DEPTH = 3

    print(original_nums)

    list_of_sums = []
    already_computed = set()
    for i in range(DEPTH):
        sums_n, already_computed, todo = iterate_options(nums, already_computed, JUMP)
        list_of_sums.append(sums_n)
        nums = list(todo)
        print("checkpoint", i)

    print(JUMP, DEPTH)

    sums_n = {}
    for sub_sum in list_of_sums:
        sums_n.update(sub_sum)

    with open('dict.pickle', 'wb') as handle:
        pickle.dump(sums_n, handle)

    print("saved")

if __name__ == '__main__':
    main()