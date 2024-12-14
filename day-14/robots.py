# problem 1

import re

def print_debug(robots, x_len, y_len):
    positions = [p for p, v in robots]
    count = {}
    for pos in positions:
        count[pos] = count.get(pos, 0) + 1
    for y in range(y_len):
        for x in range(x_len):
            if (x, y) in count:
                print(count[(x, y)], end='')
            else:
                print('.', end='')
        print()

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    # X_LEN = 11
    # Y_LEN = 7
    X_LEN = 101
    Y_LEN = 103
    SECONDS = 100

    robots = []
    pattern = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        p_x, p_y, v_x, v_y = re.match(pattern, line).groups()
        robots.append(((int(p_x), int(p_y)), (int(v_x), int(v_y))))

    for i in range(len(robots)):
        p, v = robots[i]
        new_p_x = (p[0] + SECONDS * v[0]) % X_LEN
        new_p_y = (p[1] + SECONDS * v[1]) % Y_LEN
        robots[i] = ((new_p_x, new_p_y), v)

    count = {}
    for pos, vel in robots:
        count[pos] = count.get(pos, 0) + 1

    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    for x in range(X_LEN // 2):
        for y in range(Y_LEN // 2):
            if (x, y) in count:
                top_left += count[(x, y)]
        for y in range(Y_LEN // 2 + 1, Y_LEN):
            if (x, y) in count:
                bottom_left += count[(x, y)]
    for x in range(X_LEN // 2 + 1, X_LEN):
        for y in range(Y_LEN // 2):
            if (x, y) in count:
                top_right += count[(x, y)]
        for y in range(Y_LEN // 2 + 1, Y_LEN):
            if (x, y) in count:
                bottom_right += count[(x, y)]
    
    safety_factor = top_left * top_right * bottom_left * bottom_right

    print_debug(robots, X_LEN, Y_LEN)
    # print(safety_factor)

if __name__ == '__main__':
    main()