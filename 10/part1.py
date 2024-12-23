TopographicMap = list[list[int]]
Coordinate = tuple[int, int]
Trail = list[Coordinate]


def load_topographic_map(filename: str):
    with open(filename, "r") as f:
        return [[int(x) if x.isdigit() else None for x in line.strip()] for line in f]


def get_trails(
    start_point: Coordinate, tmap: TopographicMap, prefix_trail: Trail = None
) -> list[Trail]:

    if prefix_trail is None:
        prefix_trail = []

    if tmap[start_point[0]][start_point[1]] == 9:
        print("Found a trail: ", prefix_trail)
        return [prefix_trail + [start_point]]

    trails = []
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_point = (start_point[0] + dir[0], start_point[1] + dir[1])
        if (
            next_point[0] >= 0
            and next_point[0] < len(tmap)
            and next_point[1] >= 0
            and next_point[1] < len(tmap[0])
        ) and tmap[next_point[0]][next_point[1]] == tmap[start_point[0]][
            start_point[1]
        ] + 1:
            print(
                "Currently at {}, exploring {} with value {}".format(
                    start_point, next_point, tmap[next_point[0]][next_point[1]]
                )
            )
            if new_trails := get_trails(next_point, tmap, prefix_trail + [start_point]):
                trails.extend(new_trails)

    return trails


def compute_trailhead_score(
    trailhead: Coordinate, tmap: TopographicMap, routes: list[Trail] = None
):

    if routes is None:
        routes = []

    trails = get_trails(trailhead, tmap)
    print("Total trails: ", len(trails))

    distinct_trailheads = {trail[-1] for trail in trails}
    print("Distinct trailheads: ", len(distinct_trailheads))

    return len(distinct_trailheads), len(trails)


if __name__ == "__main__":
    tmap = load_topographic_map("input.txt")

    # get indices of trailheads
    trailheads = []
    for i in range(len(tmap)):
        for j in range(len(tmap[i])):
            if tmap[i][j] == 0:
                trailheads.append((i, j))

    # get score of each trailhead
    total_score = 0
    total_rating = 0
    for trailhead in trailheads:
        print("Examining trails for trailhead: ", trailhead)
        t_head_score, t_head_rating = compute_trailhead_score(trailhead, tmap)
        total_score += t_head_score
        total_rating += t_head_rating

    print("Total score: ", total_score)
    print("Total rating: ", total_rating)
