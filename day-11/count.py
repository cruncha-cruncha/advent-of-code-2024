# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

# problem 1

def main():
    nums = []
    with open('input.txt') as f:
        text = f.read().strip()
        nums = [int(c) for c in text.split()]

    # print(nums)

    for blink in range(25):
        end = len(nums)
        for i in range(end):
            if nums[i] == 0:
                nums[i] = 1
            elif len(str(nums[i])) % 2 == 0:
                num = str(nums[i])
                half = len(num) // 2
                left = int(num[:half])
                right = int(num[half:])
                nums[i] = left
                # nums.insert(i + 1, right)
                nums.append(right)
            else:
                nums[i] *= 2024

    print(len(nums))

if __name__ == '__main__':
    main()