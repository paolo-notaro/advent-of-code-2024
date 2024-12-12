from part1 import load_input_map, compute_antinodes

if __name__ == "__main__":
    antenna_map = load_input_map("input.txt")

    antinodes_map = compute_antinodes(antenna_map, any_distance=True)

    antinode_count = 0
    for row in antinodes_map:
        for cell in row:
            print(cell, end="")
            if cell == "#":
                antinode_count += 1
        print()

    print(f"\nAntinode count: {antinode_count}")
