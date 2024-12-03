# problem 1
import re

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    good_commands = 0
    for line in lines:
        matches = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line)
        good_commands += sum([int(x) * int(y) for x, y in matches])
    print(good_commands)

if __name__ == '__main__':
    main()