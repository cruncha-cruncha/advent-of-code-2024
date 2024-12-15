# moving up
# for yr in range(y - 1, 0, -1):
#   if (x, yr) is a wall, move fails
#   if (x, yr) is empty, save yr, then break (can move)
# if can move, delete the box at (x, y - 1) and add a box at (x, yr)
# move robot to (x, y - 1)

# three key position variables: robot location tuple, set of boxes, and set of walls
# after every 100 moves, for every box stuck in a corner, add a wall there (so the robot will treat the box as if it was a wall)

def print_debug(robot, boxes, walls, x_max, y_max):
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) in walls:
                print('#', end='')
            elif (x, y) in boxes:
                print('O', end='')
            elif (x, y) == robot:
                print('@', end='')
            else:
                print('.', end='')
        print()

def move(cmd, robot, boxes, walls, x_max, y_max):
    x, y = robot
    if cmd == '^':
        for yr in range(y - 1, 0, -1):
            if (x, yr) in walls:
                return robot
            elif (x, yr) not in boxes:
                if yr < y-1:
                    boxes.remove((x, y - 1))
                    boxes.add((x, yr))
                return (x, y - 1)
    elif cmd == '>':
        for xr in range(x + 1, x_max):
            if (xr, y) in walls:
                return robot
            elif (xr, y) not in boxes:
                if xr > x + 1:
                    boxes.remove((x + 1, y))
                    boxes.add((xr, y))
                return (x + 1, y)
    elif cmd == 'v':
        for yr in range(y + 1, y_max):
            if (x, yr) in walls:
                return robot
            elif (x, yr) not in boxes:
                if yr > y + 1:
                    boxes.remove((x, y + 1))
                    boxes.add((x, yr))
                return (x, y + 1)
    else:
        for xr in range(x - 1, 0, -1):
            if (xr, y) in walls:
                return robot
            elif (xr, y) not in boxes:
                if xr < x - 1:
                    boxes.remove((x - 1, y))
                    boxes.add((xr, y))
                return (x - 1, y)
    return robot
        

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]


    walls = set()
    boxes = set()
    robot = (0, 0)
    x_max = len(lines[0])
    y_max = 0
    for y, line in enumerate(lines):
        for x, c in enumerate([*line]):
            if c == '#':
                walls.add((x, y))
            elif c == 'O':
                boxes.add((x, y))
            elif c == '@':
                robot = (x, y)
        if y > 0 and line == lines[0]:
            y_max = y + 1
            break

    commands = ""
    for line in lines[y_max + 1:]:
        commands += line

    for cmd in [*commands]:
        robot = move(cmd, robot, boxes, walls, x_max, y_max)

    total_gps = 0
    for box in boxes:
        x, y = box
        total_gps += x + 100 * y

    print_debug(robot, boxes, walls, x_max, y_max)
    print(total_gps)

if __name__ == '__main__':
    main()