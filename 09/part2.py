from part1 import load_dense_disk, generate_disk, compute_checksum


def declutter_disk2(disk: list[int]):

    # get indices of movable blocks
    empty_blocks = []
    full_blocks = dict()
    i = 0
    while i < len(disk):

        if disk[i] is not None:
            full_start = i
            full_end = i
            full_value = disk[i]
            while full_end < len(disk) and disk[full_end] == full_value:
                full_end += 1
            full_blocks[full_value] = (full_start, full_end)
            i = full_end

        else:
            empty_start = i
            empty_end = i
            while empty_end < len(disk) and disk[empty_end] is None:
                empty_end += 1

            empty_blocks.append((empty_start, empty_end))
            i = empty_end

    empty_blocks = empty_blocks
    full_blocks = [
        x[1] for x in sorted(full_blocks.items(), key=lambda x: x[0], reverse=True)
    ]

    print(empty_blocks)
    print(full_blocks)

    for full_block in full_blocks:

        full_block_size = full_block[1] - full_block[0]
        for empty_block in empty_blocks:
            empty_block_size = empty_block[1] - empty_block[0]
            if empty_block_size >= full_block_size and empty_block[0] < full_block[0]:
                disk[empty_block[0] : empty_block[0] + full_block_size] = disk[
                    full_block[0] : full_block[1]
                ]
                disk[full_block[0] : full_block[1]] = [None] * full_block_size
                empty_blocks[empty_blocks.index(empty_block)] = (
                    empty_block[0] + full_block_size,
                    empty_block[1],
                )
                break

        # print(disk)

    return disk


if __name__ == "__main__":
    dense_disk = load_dense_disk("input.txt")
    print(dense_disk)

    disk = generate_disk(dense_disk)
    print(disk)

    disk = declutter_disk2(disk)
    print(disk)

    checksum = compute_checksum(disk)
    print("Checksum:", checksum)
