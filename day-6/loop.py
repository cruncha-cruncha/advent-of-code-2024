# problem 2

#  - y
# |
# x
#

# verify that no obstactles exist along the lines of a rectangle between the points
# first validates that these points form a rectangle
# then orders them top left, top right, bottom right, bottom left
def verify_rectangle(room, d1, d2, d3, d4):
    # lowest x = p1
    # highest y = p2
    # highest x = p3
    # lowest y = p4

    points = [d1, d2, d3, d4]
    points.sort(key=lambda tup: tup[0])
    p1 = points[0]
    p3 = points[3]
    points.sort(key=lambda tup: tup[1])
    p2 = points[3]
    p4 = points[0]

    if p1[0] + 1 != p2[0] or p2[1] != p3[1] + 1 or p3[0] != p4[0] + 1 or p4[1] + 1 != p1[1]:
        print("not a rectangle")
        return False

    for j in range(p1[1], p2[1]):
        if room[p1[0] + 1][j] == 1:
            return False
    for i in range(p2[0], p3[0]):
        if room[i][p2[1] - 1] == 1:
            return False
    for j in range(p3[1], p4[1]):
        if room[p3[0] - 1][j] == 1:
            return False
    for i in range(p4[0], p1[0]):
        if room[i][p4[1] + 1] == 1:
            return False
    return True

def walk(room, guard_index, direction):
    x, y = guard_index
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

    count = 0
    direction = 'up'
    while True:
        room, new_guard_index, new_direction, end = walk(room, guard_index, direction)
        if end:
            break

        debug = False
        found = False
        if direction == new_direction:
            dx = 1
            dy = 1

            if new_guard_index == (8,3):
                debug = True

            if debug:
                print("debug guard_index", guard_index)
                print("debug new_guard_index", new_guard_index)

            if direction == 'up':
                # top left corner = new_guard_index

                # find top right corner
                while guard_index[1] + dy < len(room[guard_index[0]]):
                    if room[guard_index[0]][guard_index[1] + dy] == 1:
                        found = True
                        break
                    dy += 1

                # find bottom left corner
                if guard_index[1] <= 0:
                    found = False
                if found:
                    found = False
                    while guard_index[0] + dx < len(room):
                        if room[guard_index[0] + dx][guard_index[1] - 1] == 1:
                            found = True
                            break
                        dx += 1

                # find bottom right corner
                if guard_index[0] + dx + 1 >= len(room):
                    found = False
                if found:
                    found = room[guard_index[0] + dx + 1][guard_index[1] + dy - 1] == 1

                # verify no obstacles exist on the path formed by these four points
                if found:
                    found = verify_rectangle(room, new_guard_index, (guard_index[0], guard_index[1] + dy), (guard_index[0] + dx + 1, guard_index[1] + dy - 1), (guard_index[0] + dx, guard_index[1] - 1))
            elif direction == 'right':
                # top right corner = new_guard_index

                # find bottom right corner
                while guard_index[0] + dx < len(room):
                    if room[guard_index[0] + dx][guard_index[1]] == 1:
                        found = True
                        break
                    dx += 1

                # find top left corner
                if guard_index[0] <= 0 or guard_index[1] <= 0:
                    found = False
                if found:
                    found = False
                    while guard_index[1] - dy >= 0:
                        if room[guard_index[0] - 1][guard_index[1] - dy] == 1:
                            found = True
                            break
                        dy += 1

                # find bottom left corner
                if guard_index[1] - dy - 1 < 0:
                    found = False
                if found:
                    found = room[guard_index[0] + dx - 1][guard_index[1] - dy - 1] == 1

                # verify no obstacles exist on the path formed by these four points
                if found:
                    found = verify_rectangle(room, (guard_index[0] - 1, guard_index[1] - dy), new_guard_index, (guard_index[0] + dx, guard_index[1]), (guard_index[0] + dx - 1, guard_index[1] - dy - 1))
            elif direction == 'down':
                # bottom right corner = new_guard_index

                # find bottom left corner
                while guard_index[1] - dy >= 0:
                    if room[guard_index[0]][guard_index[1] - dy] == 1:
                        found = True
                        break
                    dy += 1

                # find top right corner
                if guard_index[0] <= 0:
                    found = False
                if found:
                    found = False
                    while guard_index[0] - dx >= 0:
                        if len(room[guard_index[0] - dx]) < guard_index[1] + 1:
                            break
                        if room[guard_index[0] - dx][new_guard_index[1] + 1] == 1:
                            found = True
                            break
                        dx += 1

                # find top left corner
                if guard_index[0] - dx - 1 < 0:
                    found = False
                if found:
                    found = room[guard_index[0] - dx - 1][guard_index[1] - dy + 1] == 1

                # verify no obstacles exist on the path formed by these four points
                if found:
                    found = verify_rectangle(room, (guard_index[0] - dx - 1, guard_index[1] - dy + 1), (guard_index[0] - dx, guard_index[1] + 1), new_guard_index, (guard_index[0], guard_index[1] - dy))
            elif direction == 'left':
                # bottom left corner = new_guard_index

                # find top left corner
                while guard_index[0] - dx >= 0:
                    if room[guard_index[0] - dx][guard_index[1]] == 1:
                        found = True
                        break
                    dx += 1

                # find bottom right corner
                if guard_index[0] + 1 >= len(room):
                    found = False
                if found:
                    found = False
                    while guard_index[1] + dy < len(room[guard_index[0] + 1]):
                        if room[guard_index[0] + 1][guard_index[1] + dy] == 1:
                            found = True
                            break
                        dy += 1

                # find top right corner
                if guard_index[1] + dy + 1 >= len(room[guard_index[0] - dx + 1]):
                    found = False
                if found:
                    found = room[guard_index[0] - dx + 1][guard_index[1] + dy + 1] == 1

                # verify no obstacles exist on the path formed by these four points
                if found:
                    found = verify_rectangle(room, (guard_index[0] - dx, guard_index[1]), (guard_index[0] - dx + 1, guard_index[1] + dy + 1), (guard_index[0] + 1, guard_index[1] + dy), new_guard_index)
        if found:
            print(direction, new_guard_index)
            count += 1
        guard_index = new_guard_index
        direction = new_direction

        # 177 is too low?

    print(count)

# 6,3
# 7,6
# 7,7
# 8,1
# 8,3
# 9,7
#
  
if __name__ == '__main__':
    main()