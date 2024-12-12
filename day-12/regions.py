# problem 1

def find_valid_neighbours(loc, lines):
    x, y = loc
    marker = lines[x][y]
    neighbours = []
    if x > 0 and lines[x-1][y] == marker:
        neighbours.append((x-1, y))
    if x < len(lines) - 1 and lines[x+1][y] == marker:
        neighbours.append((x+1, y))
    if y > 0 and lines[x][y-1] == marker:
        neighbours.append((x, y-1))
    if y < len(lines[0]) - 1 and lines[x][y+1] == marker:
        neighbours.append((x, y+1))
    return neighbours

def build_region(loc, lines):
    x, y = loc
    marker = lines[x][y]
    perimeter_length = 0
    region = set()
    boundary = {loc}
    next_boundary = set()
    while len(boundary) > 0:
        for pos in boundary:
            if pos in region:
                continue
            region.add(pos)
            neighbours = find_valid_neighbours(pos, lines)
            next_boundary.update(neighbours)
            perimeter_length += 4 - len(neighbours)
        boundary = next_boundary
        next_boundary = set()
    return region, perimeter_length

def explore_lines(lines):
    regions = []
    already_found = set()

    for i, v in enumerate(lines):
        for j in range(len(v)):
            if (i, j) in already_found:
                continue
            new_region, perimeter = build_region((i, j), lines)
            regions.append({ "points": new_region, "perimeter": perimeter })
            already_found.update(new_region)
    return regions

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    regions = explore_lines(lines)

    total_price = 0
    for r in regions:
        total_price += len(r["points"]) * r["perimeter"]
        
    print(total_price)

if __name__ == '__main__':
    main()