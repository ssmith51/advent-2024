# Day 4: X-MAS Word Search Solver

A solution for finding XMAS patterns in a grid-based word search puzzle.

## Functions

### `load(file_name)`
- Reads input file and converts it into a 2D grid of characters
- Returns the grid as a list of lists

### `check_xmas_at_position(file, row, col, d_row, d_col, rows, cols)`
- Checks if "XMAS" exists starting from a given position in a specified direction
- Returns boolean indicating if pattern was found

### `part_1(file)`
- Finds all instances of "XMAS" in any direction (horizontal, vertical, diagonal)
- Counts overlapping instances
- Prints total count of "XMAS" patterns found

### `check_x_pattern(file, row, col, rows, cols)`
- Checks if an X-shaped pattern exists with 'A' at center
- Pattern must have 'M' and 'S' in both diagonals
- Returns boolean indicating if pattern was found

### `part_2(file)`
- Finds all X-shaped patterns where:
  - 'A' is at the center
  - Each diagonal contains both 'M' and 'S'
- Prints total count of valid X patterns found

### `main(file_name)`
- Orchestrates the solution by running both parts
- Takes input file path as parameter