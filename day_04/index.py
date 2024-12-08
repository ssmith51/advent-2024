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


def part_1(file):
    print("Day 2, Part 1")

    # Initialize count of XMAS occurrences
    xmas_count = 0
    rows = len(file)
    cols = len(file[0])
    
    # Define all 8 possible directions to search
    directions = [
        (-1,-1), (-1,0), (-1,1),  # Up-left, Up, Up-right
        (0,-1),          (0,1),   # Left, Right
        (1,-1),  (1,0),  (1,1)    # Down-left, Down, Down-right
    ]
    
    # For each starting position in grid
    for row in range(rows):
        for col in range(cols):
            # Try each direction from this position
            for d_row, d_col in directions:
                # Check if XMAS can fit in this direction from here
                if (0 <= row + 3*d_row < rows and 
                    0 <= col + 3*d_col < cols):
                    
                    # Get the 4 characters in this direction
                    chars = [
                        file[row + i*d_row][col + i*d_col] 
                        for i in range(4)
                    ]
                    
                    # Check if they spell XMAS
                    if chars == ['X','M','A','S']:
                        xmas_count += 1
                        
    print(f"\n Instances of XMAS found: {xmas_count} ")

   

def part_2(file):
    print("Day 2, Part 2")

    # Initialize count of X-shaped MAS occurrences
    mas_x_count = 0
  
                        
    print(f"\n X-shaped MAS patterns found: {mas_x_count}")


def main(file_name):
    print("Day 2")
    grid = load(file_name)
    part_1(grid)
    part_2(grid)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "test.txt"))
    
