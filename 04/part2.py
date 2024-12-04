from part1 import load_input
import numpy as np
import re

def count_xmas_pattern(grid: np.ndarray) -> int:
    count = 0

    
    for i in range(len(grid) - 2):
        for j in range(len(grid) - 2):
            # M M     M S
            #  A       A
            # S S and M S
            if grid[i][j] == "M" and grid[i+1][j+1] == "A" and grid[i+2][j+2] == "S":
                # search second MAS pattern diagonally
                if grid[i][j+2] == "M" and grid[i+2][j] == "S":
                    count += 1

                elif grid[i][j+2] == "S" and grid[i+2][j] == "M":
                    count += 1

            # S S     S M
            #  A       A
            # M M and S M
            if grid[i][j] == "S" and grid[i+1][j+1] == "A" and grid[i+2][j+2] == "M":
                if grid[i][j+2] == "S" and grid[i+2][j] == "M":
                    count += 1
                elif grid[i][j+2] == "M" and grid[i+2][j] == "S":
                    count += 1

            
        
    return count

if __name__ == '__main__':
    grid = load_input("input.txt")
    print(count_xmas_pattern(grid))