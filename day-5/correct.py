# problem 1

def valid_update(rules, update):
    for i, num1 in enumerate(update):
        for num2 in update[i + 1:]:
            if f"{num2}|{num1}" in rules:
                return False
    return True

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    split_at = lines.index("")
    rules = set(lines[:split_at])
    updates = [line.split(",") for line in lines[split_at + 1:]]

    center_count = 0
    for update in updates:
        if valid_update(rules, update):
            center = len(update) // 2
            center_count += int(update[center])

    print(center_count)
  
if __name__ == '__main__':
    main()