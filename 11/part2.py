from part1 import read_file, stone_iteration, map_stone
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def multi_stone_iteration(stone: int, iters: int) -> int:

    new_stones = map_stone(stone)
    if iters == 1:
        return len(new_stones)

    return sum(multi_stone_iteration(s, iters=iters - 1) for s in new_stones)


if __name__ == "__main__":
    initial_stones = read_file("input.txt")
    n_iters = 75

    print("Initial arrangement:")
    print(initial_stones)

    total_stones = 0
    for k, initial_stone in enumerate(initial_stones):
        print(f"Initial stone ({k}): {initial_stone}")

        stones = [initial_stone]
        stone_count = multi_stone_iteration(initial_stone, iters=n_iters)
        print(
            f"Total count of stones generated by stone {k}: {stone_count}\n",
        )
        total_stones += stone_count

    print("Final number of stones:", total_stones)
