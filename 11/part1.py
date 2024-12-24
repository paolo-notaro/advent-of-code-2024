import time
from multiprocessing import Pool
from functools import lru_cache


def read_file(file_path: str) -> list:
    # read a single line of ints separated by spaces
    with open(file_path, "r") as file:
        return [int(x) for x in file.readline().split(" ")]


def get_digits(number: int) -> list[str]:
    assert number >= 0, "Number must be non-negative"
    digits = list(str(number))
    return digits


@lru_cache(maxsize=None)
def map_stone(old_stone: int) -> tuple[int]:
    if old_stone == 0:
        return (1,)
    elif len(digits := get_digits(old_stone)) % 2 == 0:
        stone1 = int("".join(digits[: len(digits) // 2]))
        stone2 = int("".join(digits[len(digits) // 2 :]))
        return (stone1, stone2)
    else:
        return (old_stone * 2024,)


def stone_iteration(old_stones: list[int]) -> list[int]:

    new_stones = [
        new_stone for old_stone in old_stones for new_stone in map_stone(old_stone)
    ]

    return new_stones


if __name__ == "__main__":
    stones = read_file("input.txt")
    n_iters = 25

    print("Initial arrangement:")
    print(stones)

    for i in range(n_iters):
        t_start = time.time()
        stones = stone_iteration(stones)
        iter_time = time.time() - t_start
        print(
            f"After {i+1} blink{'s' if i != 1 else ''}: {len(stones)} stones ({iter_time:5.2f}s)"
        )
        # print(stones)
        # print()

    print("Final number of stones:", len(stones))
