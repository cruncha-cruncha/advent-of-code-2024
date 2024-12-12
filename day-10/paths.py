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

def find_paths(loc, nums, peaks, already_visited):
    # loc is a tuple of (i, j)
    # nums is a list of lists of numbers representing altitudes
    # peaks is a set of tuples which are peaks accessible from this trailhead
    # already_visited is a set of tuples which are locations we've already visited
    for dir in DIRECTIONS:
        new_loc, success = go_dir(loc, nums, dir)
        if new_loc in already_visited:
            continue
        else:
            already_visited.add(new_loc)

        if success:
            x, y = new_loc
            altitude = nums[x][y]
            if altitude == 9:
                peaks.add(new_loc)
            else: 
                find_paths(new_loc, nums, peaks, already_visited)

    # four directions: up, down, left, right
    pass

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
    for trailhead in trailheads:
        found_peaks = set()
        find_paths(trailhead, nums, found_peaks, set(trailhead))
        trails[trailhead] = found_peaks

    # this only made sense if trails could also be descending
    # peak_to_peak = {}
    # for peak in peaks:
    #     found_peaks = set()
    #     find_paths(peak, nums, found_peaks, set(peak))
    #     peak_to_peak[peak] = found_peaks

    # for trailhead, accessible_peaks in trails.items():
    #     all_accessible = set()
    #     to_investigate = accessible_peaks.copy()
    #     while len(to_investigate) > 0:
    #         peak = to_investigate.pop()

    #         if peak in all_accessible:
    #             continue
    #         else:
    #             all_accessible.add(peak)

    #         if peak in peak_to_peak:
    #             to_investigate.update(peak_to_peak[peak])

    total = 0
    for trailhead, peaks in trails.items():
        total += len(peaks)

    print(total)

if __name__ == '__main__':
    main()