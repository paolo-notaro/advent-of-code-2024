from collections import defaultdict
from enum import Enum

Coordinate = tuple[int, int]
Map = list[list[str]]
Region = list[Coordinate]


class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)


def load_garden_map(filename: str) -> list[list[str]]:
    garden_map = []
    with open(filename, "r") as file:
        for line in file:
            garden_map.append(list(line.strip()))
    return garden_map


def explore_region(
    garden_map: Map,
    row: int,
    col: int,
    mapped: dict[Coordinate, bool],
    regions: list[Region],
) -> list[Region]:

    if (row, col) not in mapped:
        mapped[(row, col)] = True

    for direction in Directions:
        if 0 <= row + direction.value[0] < len(
            garden_map
        ) and 0 <= col + direction.value[1] < len(garden_map[row]):
            next_position = (row + direction.value[0], col + direction.value[1])
            if (
                garden_map[row][col] == garden_map[next_position[0]][next_position[1]]
                and next_position not in mapped
            ):
                regions[-1].append(next_position)
                explore_region(
                    garden_map, next_position[0], next_position[1], mapped, regions
                )

    return regions


def determine_regions(garden_map: Map) -> list[Region]:

    regions: list[Region] = []
    mapped: dict[Coordinate, bool] = {}
    for row in range(len(garden_map)):
        for col in range(len(garden_map[row])):
            if (row, col) not in mapped:
                regions.append([(row, col)])
                regions = explore_region(garden_map, row, col, mapped, regions)

    return regions


def determine_area_and_perimeter(region: Region) -> tuple[int, int]:

    # determine area
    area = len(region)

    # determine perimeter
    perimeter = 0

    # determine sides of all plots that are not contiguous
    for plot in region:
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_position = (plot[0] + direction[0], plot[1] + direction[1])
            if next_position not in region:
                perimeter += 1

    return area, perimeter

    return area, perimeter


if __name__ == "__main__":
    garden_map = load_garden_map("input.txt")
    print(garden_map)

    regions = determine_regions(garden_map)
    print(regions)

    total_cost = 0
    for region in regions:
        area, perimeter = determine_area_and_perimeter(region)
        print(f"Area: {area}, Perimeter: {perimeter}")
        total_cost += area * perimeter

    print(f"Total cost: {total_cost}")
