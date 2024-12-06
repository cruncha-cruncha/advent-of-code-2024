# problem 2

#  - y
# |
# x
#

def walk(room, guard_index, direction):
    x, y = guard_index
    end = False

    if direction == 'up':
        if x - 1 < 0:
            return (room, guard_index, direction, True) 
        elif room[x - 1][y] == 1:
            return (room, guard_index, "right", False) 
        else:
            return (room, (x - 1, y), direction, False)
    elif direction == 'right':
        if y + 1 >= len(room[x]):
            return (room, guard_index, direction, True) 
        elif room[x][y + 1] == 1:
            return (room, guard_index, "down", False) 
        else:
            return (room, (x, y + 1), direction, False)
    elif direction == 'down':
        if x + 1 >= len(room):
            return (room, guard_index, direction, True) 
        elif room[x + 1][y] == 1:
            return (room, guard_index, "left", False) 
        else:
            return (room, (x + 1, y), direction, False)
    elif direction == 'left':
        if y - 1 < 0:
            return (room, guard_index, direction, True)
        elif room[x][y - 1] == 1:
            return (room, guard_index, "up", False)
        else:
            return (room, (x, y - 1), direction, False)

def is_loop(room, guard_index, direction):
    count = 0
    velocity = set()
    velocity.add((guard_index, direction))
    while count < 100000:
        room, new_guard_index, new_direction, end = walk(room, guard_index, direction)
        if end:
            return False
        elif (new_guard_index, new_direction) in velocity:
            return True   
        else:
            velocity.add((new_guard_index, new_direction))
        count += 1
        guard_index = new_guard_index
        direction = new_direction
    print("ERROR: loop count too high")

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
    unique_positions = set()
    path_locations = {guard_index}
    while True:
        room, new_guard_index, new_direction, end = walk(room, guard_index, direction)
        print('.', end='', flush=True)
        if end:
            break

        if direction == new_direction and not new_guard_index in path_locations:
            room[new_guard_index[0]][new_guard_index[1]] = 1
            if is_loop(room, guard_index, direction):
                unique_positions.add(new_guard_index)
            room[new_guard_index[0]][new_guard_index[1]] = 0

        path_locations.add(new_guard_index)
        guard_index = new_guard_index
        direction = new_direction

    print("")
    print(len(unique_positions))
  
if __name__ == '__main__':
   main()