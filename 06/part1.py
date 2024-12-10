def load_map(input_file: str) -> list[list[str]]:
    with open(input_file, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def detect_cycle(sequence: list[tuple[int, int, str]]) -> bool:
    seen_corners = {sequence[0]}
    prev = sequence[0]
    for i, item in enumerate(sequence[1:], 1):
        if item in seen_corners:
            return True

        seen_corners.add(prev)

        prev = item

    return False


def print_map(guard_map):
    for row in guard_map:
        print("".join(row))
    print()


def estimate_guard_path(guard_map: list[list[str]]) -> list[list[str]]:

    history_positions = list()

    # get initial guard position
    guard_position = None
    for i, row in enumerate(guard_map):
        for dir in directions:
            if dir in row:
                j = row.index(dir)
                guard_position = (i, j)
                guard_direction = row[j]
                break

    # print_map(guard_map)

    history_positions.append((*guard_position, guard_direction))

    while guard_position is not None:

        guard_map[guard_position[0]][guard_position[1]] = "X"

        guard_direction_vector = directions[guard_direction]
        guard_next_position = (
            guard_position[0] + guard_direction_vector[0],
            guard_position[1] + guard_direction_vector[1],
        )

        # out of bounds detection
        if (
            guard_next_position[0] < 0
            or guard_next_position[0] >= len(guard_map)
            or guard_next_position[1] < 0
            or guard_next_position[1] >= len(guard_map[0])
        ):
            return guard_map

        # obstacle detection
        elif guard_map[guard_next_position[0]][guard_next_position[1]] in ("#", "O"):

            # change direction
            guard_direction = list(directions.keys())[
                (list(directions.keys()).index(guard_direction) + 1) % 4
            ]
            history_positions.append((*guard_position, guard_direction))

            guard_direction_vector = directions[guard_direction]
            guard_next_position = (
                guard_position[0] + guard_direction_vector[0],
                guard_position[1] + guard_direction_vector[1],
            )

        # new position
        guard_position = guard_next_position
        guard_map[guard_position[0]][guard_position[1]] = guard_direction

        # print_map(guard_map)

        # cycle detection
        if detect_cycle(history_positions):
            print(guard_map)
            print(history_positions)
            raise RecursionError("Cycle detected")

    return guard_map


if __name__ == "__main__":
    guard_map = load_map("input.txt")

    guard_map = estimate_guard_path(guard_map)

    guard_position_count = 0
    for row in guard_map:
        for pos in row:
            if pos == "X":
                guard_position_count += 1

    print("Total guard positions:", guard_position_count)
