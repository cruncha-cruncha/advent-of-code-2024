# problem 1

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [x.split() for x in lines]
        lines = [(int(x[0].strip()), int(x[1].strip())) for x in lines]
    left, right = zip(*lines)
    left, right = list(left), list(right)

    left.sort()
    right.sort()
    difference = [abs(x[0] - x[1]) for x in zip(left, right)]
    print(sum(difference))

if __name__ == '__main__':
    main()