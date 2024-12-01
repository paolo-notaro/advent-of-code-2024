from part1 import read_file

list_a, list_b = read_file()

if __name__ == "__main__":
    list_a.sort()
    dist = 0
    for item in list_a:
        count_item = list_b.count(item)
        dist += item*count_item

    print("Distance:", dist)