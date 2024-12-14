# problem 1

import re

def print_debug(positions, x_len, y_len):
    for y in range(y_len):
        for x in range(x_len):
            if (x, y) in positions:
                print("#", end='')
            else:
                print('.', end='')
        print()

def is_xmas_tree(positions, x_len, y_len):
    SIDE_LEN = 4
    for pos in positions:
        x, y = pos
        diag = []
        for i in range(SIDE_LEN):
            diag.append((x + i, y + i))
        if all([d in positions for d in diag]):
            for x_r in range(SIDE_LEN, x + 1):
                r_diag = []
                for i in range(SIDE_LEN):
                    r_diag.append((x_r - i, y + i))
                if all([d in positions for d in r_diag]):
                    print("pos", pos)
                    print_debug(positions, x_len, y_len)
                    return True
    return False

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

    robot_positions = []
    robot_velocities = []
    pattern = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        p_x, p_y, v_x, v_y = re.match(pattern, line).groups()
        robot_positions.append(((int(p_x), int(p_y))))
        robot_velocities.append((int(v_x), int(v_y)))

    seconds = 0
    while seconds < 10000:
        if is_xmas_tree(robot_positions, X_LEN, Y_LEN):
            print("second", seconds)
            # break
        for i in range(len(robot_positions)):
            p = robot_positions[i]
            v = robot_velocities[i]
            new_p_x = (p[0] + v[0]) % X_LEN
            new_p_y = (p[1] + v[1]) % Y_LEN
            robot_positions[i] = ((new_p_x, new_p_y))
        seconds += 1

    # print(safety_factor)

if __name__ == '__main__':
    main()