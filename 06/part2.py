from part1 import load_map, estimate_guard_path, directions
from copy import deepcopy

if __name__ == "__main__":
    guard_map = load_map("input2.txt")

    # get positions where the guard would normally be
    guard_map_x = estimate_guard_path(deepcopy(guard_map))
    guard_positions = []
    for i, row in enumerate(guard_map_x):
        for j, pos in enumerate(row):
            if pos == "X":
                guard_positions.append((i, j))
    print(guard_positions)

    cycle_count = 0
    for i, j in guard_positions:
        if guard_map[i][j] == ".":
            print("\nTesting", i, j)
            try:
                guard_map_copy = deepcopy(guard_map)
                guard_map_copy[i][j] = "O"
                assert all("X" not in row for row in guard_map_copy)
                estimate_guard_path(guard_map_copy)
            except RecursionError:
                cycle_count += 1
                print("Cycle detected at", i, j)

    print("Possible cycle positions:", cycle_count)
