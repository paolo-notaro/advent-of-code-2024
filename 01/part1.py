# read file
def read_file():
    list_a, list_b = [], []
    with open("input.txt") as f:
        rows = f.read().splitlines()
        for row in rows:
            splits = row.split()
            list_a.append(int(splits[0]))
            list_b.append(int(splits[1]))
    return list_a, list_b


if __name__ == "__main__":
    list_a, list_b = read_file()

    # sort the two lists
    list_a.sort()
    list_b.sort()

    # compute the distance
    dist = 0
    for a, b in zip(list_a, list_b):
        dist += abs(int(a) - int(b))

    print("Distance:", dist)