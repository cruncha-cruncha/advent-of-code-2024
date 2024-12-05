# problem 2

def valid_update(rules, update):
    for i, num1 in enumerate(update):
        for num2 in update[i + 1:]:
            if f"{num2}|{num1}" in rules:
                return False
    return True

def correct_update(rules, update):
    out = [update[0]]

    for num in update[1:]:
        inserted = False
        for i, o in enumerate(out):
            if f"{num}|{o}" in rules:
                out.insert(i, num)
                inserted = True
                break
        if not inserted:
            out.append(num)
    
    return out
        

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    split_at = lines.index("")
    rules = set(lines[:split_at])
    updates = [line.split(",") for line in lines[split_at + 1:]]

    invalid = []
    for update in updates:
        if not valid_update(rules, update):
            invalid.append(update)

    invalid = [correct_update(rules, update) for update in invalid]

    center_count = 0
    for update in invalid:
        center = len(update) // 2
        center_count += int(update[center])

    print(center_count)

if __name__ == '__main__':
    main()