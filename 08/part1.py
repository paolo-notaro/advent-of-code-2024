from collections import defaultdict
from itertools import combinations


def load_input_map(filename: str) -> list[list[str]]:
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def compute_antinodes(
    antenna_map: list[list[str]], any_distance: bool = False
) -> list[list[str]]:

    # identify antennas by frequency
    antennas = defaultdict(list)
    for i, row in enumerate(antenna_map):
        for j, antenna in enumerate(row):
            if antenna != ".":
                antennas[antenna] += [(i, j)]

    antinodes_map = [
        ["." for _ in range(len(antenna_map[0]))] for _ in range(len(antenna_map))
    ]
    for antenna_id, antenna_group in antennas.items():
        print(antenna_group)
        for antenna_a, antenna_b in combinations(antenna_group, r=2):
            print("antenna_a: ", antenna_a, "antenna_b: ", antenna_b)

            # compute the line between the two antennas
            x1, y1 = antenna_a
            x2, y2 = antenna_b
            dx = x2 - x1
            dy = y2 - y1
            print(f"dx: {dx}, dy: {dy}")

            # compute antinodes by adding and subtracting dx and dy
            distances = (
                range(max(len(antenna_map) // dx, len(antenna_map[0]) // dy))
                if any_distance
                else [1]
            )
            for k in distances:
                antinode_1 = (x1 - k * dx, y1 - k * dy)
                antinote_2 = (x2 + k * dx, y2 + k * dy)
                print(f"k={k}, antinode_1: {antinode_1}, antinode_2: {antinote_2}")

                # mark antinodes on the map
                if 0 <= antinode_1[0] < len(antenna_map) and 0 <= antinode_1[1] < len(
                    antenna_map[0]
                ):
                    antinodes_map[antinode_1[0]][antinode_1[1]] = "#"

                if 0 <= antinote_2[0] < len(antenna_map) and 0 <= antinote_2[1] < len(
                    antenna_map[0]
                ):
                    antinodes_map[antinote_2[0]][antinote_2[1]] = "#"

    return antinodes_map


if __name__ == "__main__":
    antenna_map = load_input_map("input.txt")

    antinodes_map = compute_antinodes(antenna_map, any_distance=False)

    antinode_count = 0
    for row in antinodes_map:
        for cell in row:
            print(cell, end="")
            if cell == "#":
                antinode_count += 1
        print()

    print(f"\nAntinode count: {antinode_count}")
