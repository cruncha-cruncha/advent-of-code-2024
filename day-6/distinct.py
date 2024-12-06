# problem 1

#  - y
# |
# x
#

def walk(room, guard_index, direction):
    x, y = guard_index
    room[x][y] = 2
    end = False

    if direction == 'up':
        if x - 1 < 0:
            return (room, guard_index, direction, True) 
        elif room[x - 1][y] == 1:
            return (room, guard_index, "right", False) 
        else:
            return (room, (guard_index[0] - 1, guard_index[1]), direction, False)
    elif direction == 'right':
        if y + 1 >= len(room[x]):
            return (room, guard_index, direction, True) 
        elif room[x][y + 1] == 1:
            return (room, guard_index, "down", False) 
        else:
            return (room, (guard_index[0], guard_index[1] + 1), direction, False)
    elif direction == 'down':
        if x + 1 >= len(room):
            return (room, guard_index, direction, True) 
        elif room[x + 1][y] == 1:
            return (room, guard_index, "left", False) 
        else:
            return (room, (guard_index[0] + 1, guard_index[1]), direction, False)
    elif direction == 'left':
        if y - 1 < 0:
            return (room, guard_index, direction, True)
        elif room[x][y - 1] == 1:
            return (room, guard_index, "up", False)
        else:
            return (room, (guard_index[0], guard_index[1] - 1), direction, False)

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    room = [[1 if x == '#' else 0 for x in line] for line in lines]
    guard_index = (0, 0)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '^':
                guard_index = (i, j)
                break

    direction = 'up'
    end = False
    while not end:
        room, guard_index, direction, end = walk(room, guard_index, direction)

    count = 0
    for line in room:
        for c in line:
            if c == 2:
                count += 1

    print(count)
  
if __name__ == '__main__':
    main()