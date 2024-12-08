# problem 1

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

    # for each antenna, get all others in the frequency
    # calculate the antinode (start by calculating the difference)
    antinodes = set()
    for freq in frequencies.values():
        for s in range(len(freq)):
            selected = freq[s]
            others = freq[:s] + freq[s+1:]
            for other in others:
                i_diff = other[0] - selected[0]
                j_diff = other[1] - selected[1]
                antinode = (other[0] + i_diff, other[1] + j_diff)
                if antinode[0] >= i_min and antinode[0] < i_max and antinode[1] >= j_min and antinode[1] < j_max:
                    antinodes.add(antinode)

    print(len(antinodes))
  
if __name__ == '__main__':
    main()