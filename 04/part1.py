import numpy as np 


def load_input(filename: str) -> list:
    with open(filename, "r") as f:
        # convert each line to an ndarray of chars, then stack them
        grid = np.stack([list(line.strip()) for line in f.readlines()])
        return grid

def count_string(grid: np.ndarray, string: str) -> int:
    count = 0

    # search horizontally
    for row in grid:
        # convert row to string, then count occurrences of string
        row_str = "".join(row)
        count += row_str.count(string)
        
        # reverse
        count += row_str.count(string[::-1])

    # search vertically
    for col in grid.T:
        # convert col to string, then count occurrences of string
        col_str = "".join(col)
        count += col_str.count(string)

        # reverse
        count += col_str.count(string[::-1])

    # search diagonally
    for i in range(-len(grid), len(grid)):
        # search from top-left to bottom-right
        diag = "".join(np.diagonal(grid, i))
        count += diag.count(string)
        count += diag.count(string[::-1])

        # search from top-right to bottom-left
        diag = "".join(np.diagonal(np.fliplr(grid), i))
        count += diag.count(string)
        count += diag.count(string[::-1])

    return count


if __name__ == "__main__":
    grid = load_input("input.txt")
    print(count_string(grid, "XMAS"))