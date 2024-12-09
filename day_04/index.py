import os, re

def load(file_name):
    print("Loading file...")
    # Initialize empty grid to store characters
    grid = []
    
    # Read file line by line
    with open(file_name, "r") as file:
        for line in file:
            # Strip any whitespace/newlines and convert line to list of chars
            char_row = list(line.strip())
            grid.append(char_row)
            
    return grid


def check_xmas_at_position(file, row, col, d_row, d_col, rows, cols):
    if not (0 <= row + 3*d_row < rows and 0 <= col + 3*d_col < cols):
        return False
    
    chars = [file[row + i*d_row][col + i*d_col] for i in range(4)]
    return chars == ['X','M','A','S']

def part_1(file):
    print("Day 2, Part 1")
    xmas_count = 0
    rows, cols = len(file), len(file[0])
    
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    
    for row in range(rows):
        for col in range(cols):
            xmas_count += sum(
                check_xmas_at_position(file, row, col, d_row, d_col, rows, cols)
                for d_row, d_col in directions
            )
                        
    print(f"\n Instances of XMAS found: {xmas_count} ")

def check_x_pattern(file, row, col, rows, cols):
    if file[row][col] != 'A':
        return False
        
    diagonals = [(-1,-1), (-1,1), (1,-1), (1,1)]
    
    # Check bounds
    for d_row, d_col in diagonals:
        if not (0 <= row + d_row < rows and 0 <= col + d_col < cols):
            return False
            
    # Get characters in both diagonals
    diag1 = [file[row + diagonals[0][0]][col + diagonals[0][1]],
             file[row + diagonals[3][0]][col + diagonals[3][1]]]
    diag2 = [file[row + diagonals[1][0]][col + diagonals[1][1]],
             file[row + diagonals[2][0]][col + diagonals[2][1]]]
             
    return ('M' in diag1 and 'S' in diag1 and 
            'M' in diag2 and 'S' in diag2)

def part_2(file):
    print("Day 2, Part 2")
    rows, cols = len(file), len(file[0])
    x_mas_count = sum(
        check_x_pattern(file, row, col, rows, cols)
        for row in range(rows)
        for col in range(cols)
    )
    print(f"\n X-shaped MAS patterns found: {x_mas_count}")


def main(file_name):
    print("Day 2")
    grid = load(file_name)
    part_1(grid)
    part_2(grid)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
