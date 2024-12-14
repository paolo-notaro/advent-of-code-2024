def load_dense_disk(filename: str):
    with open(filename, "r") as file:
        # single line file
        return [int(x) for x in file.read().strip()]


def generate_disk(dense_disk: list[int]):
    disk = []
    file_id = 0
    for i, n_blocks in enumerate(dense_disk):
        if i % 2 == 0:
            disk += [file_id] * n_blocks
            file_id += 1
        else:
            disk += [None] * n_blocks
    return disk


def declutter_disk(disk: list[int]):
    i, j = 0, len(disk) - 1
    while j > i:
        while disk[i] is not None and i < j:
            i += 1
        while disk[j] is None and i < j:
            j -= 1
        disk[i], disk[j] = disk[j], None
        # print(i, j, disk)

    return disk


def compute_checksum(disk: list[int]):
    checksum = 0
    for i, file_id in enumerate(disk):
        if file_id is not None:
            checksum += i * file_id
    return checksum


if __name__ == "__main__":
    dense_disk = load_dense_disk("input.txt")
    # print(dense_disk)

    disk = generate_disk(dense_disk)
    # print(disk)

    disk = declutter_disk(disk)
    # print(disk)

    checksum = compute_checksum(disk)
    print("Checksum:", checksum)
