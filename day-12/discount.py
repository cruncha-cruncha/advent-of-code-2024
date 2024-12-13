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
    region = set()
    boundary = {loc}
    next_boundary = set()
    while len(boundary) > 0:
        for pos in boundary:
            if pos in region:
                continue
            region.add(pos)
            next_boundary.update(find_valid_neighbours(pos, lines))
        boundary = next_boundary
        next_boundary = set()
    return region

def explore_lines(lines):
    regions = []
    already_found = set()

    for i, v in enumerate(lines):
        for j in range(len(v)):
            if (i, j) in already_found:
                continue
            new_region = build_region((i, j), lines)
            regions.append(new_region)
            already_found.update(new_region)
    return regions

# only count perimeter if not striaght line to the right of an open face
def calculate_perimeter(region):
    perimeter = 0
    for loc in region:
        x, y = loc
        top = (x-1, y)
        top_left = (x-1, y-1)
        left = (x, y-1)
        bottom_left = (x+1, y-1)
        bottom = (x+1, y)
        bottom_right = (x+1, y+1)
        right = (x, y+1)
        top_right = (x-1, y+1)

        if top not in region:
            if right not in region or top_right in region:
                perimeter += 1
        if right not in region:
            if bottom not in region or bottom_right in region:
                perimeter += 1
        if bottom not in region:
            if left not in region or bottom_left in region:
                perimeter += 1
        if left not in region:
            if top not in region or top_left in region:
                perimeter += 1
    return perimeter

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [[*line.strip()] for line in lines]

    regions = explore_lines(lines)

    total_price = 0
    for region in regions:
        perimeter = calculate_perimeter(region)
        total_price += len(region) * perimeter
        
    print(total_price)

if __name__ == '__main__':
    main()