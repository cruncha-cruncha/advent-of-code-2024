# problem 1

def bad_indices(lines, x, y):
    return y - 1 < 0 or len(lines) <= y + 1 or x - 1 < 0 or len(lines[y]) <= x + 1

# . . X
# . X .
# X . .
def check_one(lines, x, y):
    return (lines[y - 1][x + 1] == 'M' and lines[y + 1][x - 1] == 'S') or (lines[y - 1][x + 1] == 'S' and lines[y + 1][x - 1] == 'M')

# X . .
# . X .
# . . X
def check_two(lines, x, y):
    return (lines[y - 1][x - 1] == 'M' and lines[y + 1][x + 1] == 'S') or (lines[y - 1][x - 1] == 'S' and lines[y + 1][x + 1] == 'M')

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    count = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'A' and not bad_indices(lines, j, i):
                if check_one(lines, j, i) and check_two(lines, j, i):
                    count += 1
                      
    print(count)

if __name__ == '__main__':
    main()