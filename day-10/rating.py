# problem 1

DIRECTIONS = ["up", "down", "left", "right"]

def go_dir(loc, nums, dir):
    x, y = loc
    altitude = nums[x][y]
    if dir == "up":
        if x == 0:
            return loc, False
        elif not nums[x - 1][y] - altitude == 1:
            return loc, False
        return (x - 1, y), True
    elif dir == "down":
        if x == len(nums) - 1:
            return loc, False
        elif not nums[x + 1][y] - altitude == 1:
            return loc, False
        return (x + 1, y), True
    elif dir == "left":
        if y == 0:
            return loc, False
        elif not nums[x][y - 1] - altitude == 1:
            return loc, False
        return (x, y - 1), True
    elif dir == "right":
        if y == len(nums[0]) - 1:
            return loc, False
        elif not nums[x][y + 1] - altitude == 1:
            return loc, False
        return (x, y + 1), True

def find_paths(loc, nums, found_count):
    # loc is a tuple of (i, j)
    # nums is a list of lists of numbers representing altitudes
    # found_count is the number of peaks found so far
    for dir in DIRECTIONS:
        new_loc, success = go_dir(loc, nums, dir)

        if success:
            x, y = new_loc
            altitude = nums[x][y]
            if altitude == 9:
                found_count += 1
            else: 
                found_count = find_paths(new_loc, nums, found_count)
    
    return found_count

def main():
    nums = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        nums = [[int(c) for c in line] for line in lines]

    peaks = []
    trailheads = []
    for i, line in enumerate(nums):
        for j, num in enumerate(line):
            if num == 0:
                trailheads.append((i, j))
            elif num == 9:
                peaks.append((i, j))

    trails = {}
    total_paths = 0
    for trailhead in trailheads:
        total_paths += find_paths(trailhead, nums, 0)

    print(total_paths)

if __name__ == '__main__':
    main()