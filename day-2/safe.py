# problem 1

def safe_sequence(sequence):
    if len(sequence) <= 1:
        return True

    ascending = True
    if sequence[0] > sequence[1]:
        ascending = False

    for i in range(0, len(sequence)-1):
        if ascending and sequence[i] >= sequence[i + 1]:
            return False
        elif not ascending and sequence[i] <= sequence[i + 1]:
            return False
        elif abs(sequence[i] - sequence[i + 1]) > 3:
            return False

    return True

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        lines = [[int(num.strip()) for num in line] for line in lines]

    count_safe = sum(1 for line in lines if safe_sequence(line))
    print(count_safe)

if __name__ == '__main__':
    main()