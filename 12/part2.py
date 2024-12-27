from part1 import (
    load_garden_map,
    determine_regions,
    Coordinate,
    Map,
    Region,
    Directions,
)
from collections import defaultdict


def count_contiguous(items: set[int]) -> int:

    group_start = False
    groups = 0
    for i in range(max(items) + 1):
        if i in items:
            if not group_start:
                group_start = i
        elif group_start is not False:
            groups += 1
            group_start = False

    if group_start is not False:
        groups += 1

    return groups


def determine_area_and_sides(region: Region) -> tuple[int, int]:

    # determine area
    area = len(region)

    # determine sides
    external_sides = defaultdict(set)

    # determine sides of all external sides
    for plot in region:
        for direction in Directions:
            next_position = (plot[0] + direction.value[0], plot[1] + direction.value[1])
            # print(plot, next_position, direction)
            if next_position not in region:
                external_sides[direction].add(plot)

    sides = 0
    for direction, direction_sides in external_sides.items():
        if direction in (Directions.UP, Directions.DOWN):
            distinct_rows = set([side[0] for side in direction_sides])
            for row in distinct_rows:
                # same row
                relevant_sides = [side for side in direction_sides if side[0] == row]
                # print(direction, row, relevant_sides)
                direction_row_sides = count_contiguous(
                    set([side[1] for side in relevant_sides])
                )
                # print(direction_row_sides)
                sides += direction_row_sides
        else:
            distinct_cols = set([side[1] for side in direction_sides])
            for col in distinct_cols:
                # same col
                relevant_sides = [side for side in direction_sides if side[1] == col]
                # print(direction, row, relevant_sides)
                direction_col_sides = count_contiguous(
                    set([side[0] for side in relevant_sides])
                )
                # print(direction_col_sides)
                sides += direction_col_sides

    return area, sides


if __name__ == "__main__":
    garden_map = load_garden_map("input.txt")
    print(garden_map)

    regions = determine_regions(garden_map)
    print(regions)

    total_cost = 0
    for region in regions:
        area, sides = determine_area_and_sides(region)
        print(f"Area: {area}, Sides: {sides}")
        total_cost += area * sides

    print(f"Total cost: {total_cost}")
