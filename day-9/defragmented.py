# problem 2

def main():
    chars = []
    with open('input.txt') as f:
        chars = f.read()
        chars = [*chars.strip()]

    index = 0
    # disk = []
    gaps = []
    files = []
    for i, c in enumerate(chars):
        if i % 2 == 0:
            # disk.extend([str(i // 2)] * int(c))
            files.append((index, int(c), i // 2))
            index += int(c)
        else:
            # disk.extend(['.'] * int(c))
            gaps.append((index, int(c)))
            index += int(c)

    placed_files = [files[0]]
    for i in range(len(files)):
        chunk_start, chunk_size, file_id = files[len(files) - 1 - i]
        found = False
        for gi, g in enumerate(gaps):
            gap_start, gap_size = g
            if gap_start >= chunk_start:
                break
            if gap_size >= chunk_size:
                # disk[gap_index:gap_index+chunk_size] = [str(value)] * chunk_size
                # disk[val_index:val_index+chunk_size] = ['.'] * chunk_size
                if gap_size == chunk_size:
                    gaps.pop(gi)
                else:
                    gaps[gi] = (gap_start + chunk_size, gap_size - chunk_size)
                placed_files.append((gap_start, chunk_size, file_id))
                found = True
                break
        if not found:
            placed_files.append((chunk_start, chunk_size, file_id))

    checksum = 0
    for file in placed_files:
        chunk_start, chunk_size, file_id = file
        for i in range(chunk_size):
            checksum += (chunk_start + i) * int(file_id)

    # 8354941967530 is too high
    # 43725457936257 is too high

    # print(''.join(disk))
    print(checksum)

if __name__ == '__main__':
    main()