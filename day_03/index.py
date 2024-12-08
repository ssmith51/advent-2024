import os, re

def load(file_name):
    print("Loading file...")
    # Initialize array to store matches
    file_instructions = ""
    with open(file_name, "r") as file:
        for line in file:
            file_instructions += line
            # Use regex to find all mul(number,number) patterns
            pattern = r"mul\((\d+),(\d+)\)"
            
            # Find all matches in the line
            for match in re.finditer(pattern, line):
                num1 = int(match.group(1))
                num2 = int(match.group(2))
    
    return file_instructions


def part_1(instructions):
    print("Day 2, Part 1")

    matches = []
    # Use regex to find all mul(number,number) patterns
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the line
    for match in re.finditer(pattern, instructions):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        matches.append((num1, num2))

    total = calc_instructions(matches)
        
    print(f"\nSum of all instructions: {total}")
   

def part_2(instructions):
    print("Day 2, Part 2")

    matches = []
    # Use regex to find all mul(number,number) patterns
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find positions of do() and don't() patterns
    do_matches = [m.start() for m in re.finditer(r"do\(\)", instructions)]
    dont_matches = [m.start() for m in re.finditer(r"don't\(\)", instructions)]
    
    # Find all mul() matches
    for match in re.finditer(pattern, instructions):
        match_pos = match.start()
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        
        # Check if match is valid based on do() and don't() positions
        valid = True
        
        # If there are any don't() matches before this mul()
        preceding_donts = [pos for pos in dont_matches if pos < match_pos]
        if preceding_donts:
            # Check if there's a do() between the last don't() and current mul()
            last_dont = max(preceding_donts)
            valid_dos = [pos for pos in do_matches if last_dont < pos < match_pos]
            if not valid_dos:
                valid = False
                
        if valid:
            matches.append((num1, num2))
            
    total = calc_instructions(matches)
    print(f"\nSum of all valid instructions: {total}")

def calc_instructions(matches):
      # Initialize sum of multiplications
    total = 0
    
    # Iterate through each instruction tuple
    for num1, num2 in matches:
        # Multiply the two numbers together
        result = num1 * num2
        total += result

    return total

def main(file_name):
    print("Day 2")
    instructions = load(file_name)
    part_1(instructions)
    part_2(instructions)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
