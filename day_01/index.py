import re, os

def load(file_name): 
     # Initialize an empty array/list
    left_locations = []
    right_locations = []

    with open(file_name, "r") as file:
        for line in file:
            # Split line into two numbers using regex
            numbers = re.findall(r'\d+', line)
            if len(numbers) >= 2:
                left_locations.append(int(numbers[0]))
                right_locations.append(int(numbers[1]))

    return left_locations, right_locations

def part_1(left_locations, right_locations):
    print("Day 1, Part 1")

     # Sort both arrays from lowest to highest
    left_locations.sort()
    right_locations.sort()

    # Subtract corresponding right values from left values
    differences = []
    for i in range(len(left_locations)):
        right = right_locations[i]
        left = left_locations[i]
        difference = right -left

        # Utilize the absolute difference between the two values
        if difference < 0:
            difference = abs(difference)
        differences.append(difference)

    # Calculate total difference
    total_difference = sum(differences)
    print(f"\nTotal difference between locations: {total_difference}")

def part_2(left_locations, right_locations):
    print("Day 1, Part 2")

    # Create a dictionary to count occurrences in right_locations
    right_counts = {}
    for num in right_locations:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate similarity score by multiplying each left number by its count in right
    total_similarity = 0
    for left_num in left_locations:
        count = right_counts.get(left_num, 0)  # Get count from right list (0 if not found)
        total_similarity += left_num * count

    print(f"\nTotal similarity score: {total_similarity}")


def main(file_name): 
    left_locations, right_locations = load(file_name)
    part_1(left_locations, right_locations)
    print("--------------------------------")
    part_2(left_locations, right_locations)
    


if __name__ == "__main__":
    
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
