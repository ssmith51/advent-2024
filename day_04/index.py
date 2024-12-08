import os, re

def load(file_name):
    print("Loading file...")
    # Initialize array to store matches
    file_instructions = ""
    with open(file_name, "r") as file:
        for line in file:
            print(line)

            
    return file_instructions


def part_1(instructions):
    print("Day 2, Part 1")
   

def part_2(instructions):
    print("Day 2, Part 2")


def main(file_name):
    print("Day 2")
    instructions = load(file_name)
    part_1(instructions)
    part_2(instructions)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
