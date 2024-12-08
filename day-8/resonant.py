# problem 2

def debug_print(lines, antinodes):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if (i, j) in antinodes:
                print('#', end='')
            else:
                print(c, end='')
        print()

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    i_min = 0
    i_max = len(lines)
    j_min = 0
    j_max = len(lines[0])

    frequencies = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue
            if not c in frequencies:
                frequencies[c] = []
            frequencies[c].append((i, j))
    
    antinodes = set()
    for freq in frequencies.values():
        for s in range(len(freq)):
            selected = freq[s]
            others = freq[:s] + freq[s+1:]
            antinodes.add(selected)
            for other in others:
                i_diff = other[0] - selected[0]
                j_diff = other[1] - selected[1]
                antinode = (other[0] + i_diff, other[1] + j_diff)
                while antinode[0] >= i_min and antinode[0] < i_max and antinode[1] >= j_min and antinode[1] < j_max:
                    antinodes.add(antinode)
                    antinode = (antinode[0] + i_diff, antinode[1] + j_diff)

    print(len(antinodes))
  
if __name__ == '__main__':
    main()