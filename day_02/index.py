import os

def load(file_name):
    print("Loading file...")

    # Initialize array to store all sequences
    sequences = []

    with open(file_name, "r") as file:
        for line in file:
            
            
            # Split line into numbers and convert to integers
            numbers = [int(num) for num in line.strip().split()]
            
            # Add sequence to main array if not empty
            if numbers:
                sequences.append(numbers)
                
    return sequences

def part_1(sequences):
    print("Day 2, Part 1")
    # Counter for valid sequences
    valid_sequences = 0

    # Check each sequence
    for sequence in sequences:
        # Check if sequence is monotonic (all increasing or all decreasing)
        is_increasing = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
        is_decreasing = all(sequence[i] >= sequence[i+1] for i in range(len(sequence)-1))
        
        # Check adjacent number differences
        valid_differences = True
        for i in range(len(sequence)-1):
            diff = abs(sequence[i] - sequence[i+1])
            if diff < 1 or diff > 3:
                valid_differences = False
                break
                
        # Increment counter if all conditions are met
        if (is_increasing or is_decreasing) and valid_differences:
            valid_sequences += 1
            
    print(f"\nNumber of valid sequences: {valid_sequences}")

def part_2(sequences):
    print("Day 2, Part 2")

    # Counter for safe sequences
    safe_sequences = 0

    # Check each sequence
    for sequence in sequences:
        # First check if sequence is already safe
        is_increasing = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
        is_decreasing = all(sequence[i] >= sequence[i+1] for i in range(len(sequence)-1))
        
        valid_differences = True
        for i in range(len(sequence)-1):
            diff = abs(sequence[i] - sequence[i+1])
            if diff < 1 or diff > 3:
                valid_differences = False
                break
                
        if (is_increasing or is_decreasing) and valid_differences:
            safe_sequences += 1
            continue
            
        # If not safe, try removing one number at a time
        sequence_length = len(sequence)
        for skip_index in range(sequence_length):
            # Create new sequence without number at skip_index
            test_sequence = sequence[:skip_index] + sequence[skip_index+1:]
            
            # Check if modified sequence is safe
            is_increasing = all(test_sequence[i] <= test_sequence[i+1] for i in range(len(test_sequence)-1))
            is_decreasing = all(test_sequence[i] >= test_sequence[i+1] for i in range(len(test_sequence)-1))
            
            valid_differences = True
            for i in range(len(test_sequence)-1):
                diff = abs(test_sequence[i] - test_sequence[i+1])
                if diff < 1 or diff > 3:
                    valid_differences = False
                    break
                    
            if (is_increasing or is_decreasing) and valid_differences:
                safe_sequences += 1
                break
                
    print(f"\nNumber of safe sequences: {safe_sequences}")

def main(file_name):
    print("Day 2")
    sequences = load(file_name)
    part_1(sequences)
    part_2(sequences)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
