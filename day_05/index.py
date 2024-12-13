import os, re
from collections import defaultdict

def load(file_name):
    print("Loading file...")
    rules = []
    updates = []
    
    with open(file_name, 'r') as file:
        # Read all lines and split into rules and updates sections
        sections = file.read().strip().split('\n\n')
        
        # Parse rules
        for line in sections[0].split('\n'):
            before, after = line.split('|')
            rules.append((int(before), int(after)))
            
        # Parse updates
        for line in sections[1].split('\n'):
            update = [int(x) for x in line.strip().split(',')]
            updates.append(update)
    
    return rules, updates

def is_valid_order(update, rules):
    # Create a set of rules that apply to this update
    relevant_rules = []
    update_pages = set(update)
    
    # Only consider rules where both pages are in the update
    for before, after in rules:
        if before in update_pages and after in update_pages:
            relevant_rules.append((before, after))
    
    # Check each relevant rule
    for before, after in relevant_rules:
        # Find positions of both pages
        before_pos = update.index(before)
        after_pos = update.index(after)
        
        # If 'after' page comes before 'before' page, order is invalid
        if after_pos < before_pos:
            return False
            
    return True

def part_1(rules, updates):
    print("Day 5, Part 1")
    
    # Find valid updates and their middle numbers
    valid_middle_sum = 0
    
    for update in updates:
        if is_valid_order(update, rules):
            # Get middle number
            middle_idx = len(update) // 2
            middle_number = update[middle_idx]
            valid_middle_sum += middle_number
    
    print(f"Sum of middle numbers from valid updates: {valid_middle_sum}")
    return valid_middle_sum

def find_correct_order(update, rules):
    # Convert update to list to allow modifications
    pages = list(update)
    n = len(pages)
    
    # Bubble sort with rules
    changed = True
    while changed:
        changed = False
        for i in range(n-1):
            for before, after in rules:
                # If we find a pair that matches a rule and is in wrong order
                if pages[i] == after and pages[i+1] == before:
                    # Swap them
                    pages[i], pages[i+1] = pages[i+1], pages[i]
                    changed = True
    
    return pages

def part_2(rules, updates):
    print("Day 5, Part 2")
    
    middle_sum = 0
    
    # Process only invalid updates
    for update in updates:
        if not is_valid_order(update, rules):
            # Get correct order
            correct_order = find_correct_order(update, rules)
            
            # Get middle number
            middle_idx = len(correct_order) // 2
            middle_number = correct_order[middle_idx]
            middle_sum += middle_number
    
    print(f"Sum of middle numbers from corrected invalid updates: {middle_sum}")
    return middle_sum

def main(file_name):
    print("Day 5")
    rules, updates = load(file_name)
    part_1(rules, updates)
    part_2(rules, updates)

if __name__ == "__main__":
    main(os.path.join(os.path.dirname(__file__), "input.txt"))
    
