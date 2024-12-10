# problem 1

def main():
    chars = []
    with open('input.txt') as f:
        chars = f.read()
        chars = [*chars.strip()]

    right = len(chars) - 1
    checksum = 0
    index = 0

    for left, c in enumerate(chars):
        if left % 2 == 1:
            continue

        for x in range(0, int(c)):
            checksum += index * (left // 2)
            index += 1

        if left >= right:
            break

        gap = int(chars[left+1])
        while True:
            right_num = int(chars[right])
            for x in range(0, min(right_num, gap)):
                checksum += index * (right // 2)
                index += 1

            if right_num > gap:
                chars[right] = str(right_num - gap)
                gap = 0
            else:
                gap -= right_num
                right -= 2

            if gap <= 0 or left >= right:
                break
            
        if left >= right:
            break

    print(checksum)


if __name__ == '__main__':
    main()