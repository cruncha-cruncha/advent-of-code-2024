# problem 2

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [x.split() for x in lines]
        lines = [(int(x[0].strip()), int(x[1].strip())) for x in lines]
    left, right = zip(*lines)
    left, right = list(left), list(right)

    left_set, right_set = set(left), set(right)
    left_count = {x: left.count(x) for x in left_set}
    right_count = {x: right.count(x) for x in right_set}
    total = 0
    for k, v in left_count.items():
        if k in right_count:
            total += k * right_count[k]
    print(total)

if __name__ == '__main__':
    main()