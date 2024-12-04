# problem 1

def check_up(lines, x, y):
    if y - 3 < 0:
        return False
    return lines[y - 1][x] == 'M' and lines[y - 2][x] == 'A' and lines[y - 3][x] == 'S'

def check_up_right(lines, x, y):
    if y - 3 < 0 or len(lines[y]) <= x + 3:
        return False
    return lines[y - 1][x + 1] == 'M' and lines[y - 2][x + 2] == 'A' and lines[y - 3][x + 3] == 'S'

def check_right(lines, x, y):
    if len(lines[y]) <= x + 3:
       return False
    return lines[y][x + 1] == 'M' and lines[y][x + 2] == 'A' and lines[y][x + 3] == 'S'

def check_down_right(lines, x, y):
    if len(lines) <= y + 3 or len(lines[y]) <= x + 3:
        return False
    return lines[y + 1][x + 1] == 'M' and lines[y + 2][x + 2] == 'A' and lines[y + 3][x + 3] == 'S'

def check_down(lines, x, y):
    if len(lines) <= y + 3:
        return False
    return lines[y + 1][x] == 'M' and lines[y + 2][x] == 'A' and lines[y + 3][x] == 'S'

def check_down_left(lines, x, y):
    if len(lines) <= y + 3 or x - 3 < 0:
        return False
    return lines[y + 1][x - 1] == 'M' and lines[y + 2][x - 2] == 'A' and lines[y + 3][x - 3] == 'S'

def check_left(lines, x, y):
    if x - 3 < 0:
        return False
    return lines[y][x - 1] == 'M' and lines[y][x - 2] == 'A' and lines[y][x - 3] == 'S'

def check_up_left(lines, x, y):
    if y - 3 < 0 or x - 3 < 0:
        return False
    return lines[y - 1][x - 1] == 'M' and lines[y - 2][x - 2] == 'A' and lines[y - 3][x - 3] == 'S'

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    count = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'X':
                if check_up(lines, j, i):
                    count += 1
                if check_up_right(lines, j, i):
                    count += 1
                if check_right(lines, j, i):
                    count += 1
                if check_down_right(lines, j, i):
                    count += 1
                if check_down(lines, j, i):
                    count += 1
                if check_down_left(lines, j, i):
                    count += 1
                if check_left(lines, j, i):
                    count += 1
                if check_up_left(lines, j, i):
                    count += 1
                
    print(count)

if __name__ == '__main__':
    main()