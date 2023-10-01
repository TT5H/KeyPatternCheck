import random

def detect_pattern(serial_key):
    # Define the mapping of letters to numbers
    letter_to_number = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
        # Add more mappings as needed
    }
    
    # Define the mapping of numbers to odd/even
    number_to_odd_even = {
        1: 'odd',
        2: 'even',
        3: 'odd',
        4: 'even',
        5: 'odd',
        6: 'even',
        7: 'odd',
        8: 'even',
        9: 'odd',
        0: 'even',  # Add 0 as even
        # Add more mappings as needed
    }
    
    # Convert the serial key to a list of numbers and characters
    numbers = []
    characters = []
    for char in serial_key:
        if char.isalpha():
            try:
                number = letter_to_number[char]
                numbers.append(number)
            except KeyError:
                # Handle the case where the letter is not in the mapping
                print(f"Invalid letter '{char}' in serial key")
                return
        elif char.isdigit():
            numbers.append(int(char))
        else:
            characters.append(char)
    
    # Determine the pattern of odd/even for numbers and alphabets
    pattern = []
    for number in numbers:
        odd_even = number_to_odd_even[number]
        pattern.append(odd_even)
    for char in characters:
        if char.isalpha():
            pattern.append(random.choice(['odd', 'even']))
        else:
            pattern.append(number_to_odd_even[int(char)])
    
    # Combine the pattern and characters
    combined_pattern = []
    for char in serial_key:
        if char.isalpha():
            combined_pattern.append(pattern.pop(0))
        else:
            combined_pattern.append(number_to_odd_even[int(char)])
    
    # Print the combined pattern with dashes between each character
    pattern_string = '-'.join(map(str, combined_pattern))
    print(f"Pattern: {pattern_string}")
    
    # Generate more serial keys based on the pattern
    generate_more = input("Do you want to generate more serial keys based on the pattern? (y/n): ")
    if generate_more.lower() == 'y':
        num_keys = int(input("How many serial keys do you want to generate? "))
        generated_keys = []
        for i in range(num_keys):
            generated_key = ''
            for p in combined_pattern:
                if p == 'odd':
                    if random.choice([True, False]):
                        generated_key += str(random.choice([1, 3, 5, 7, 9]))
                    else:
                        generated_key += chr(random.choice(range(65, 91)))
                elif p == 'even':
                    if random.choice([True, False]):
                        generated_key += str(random.choice([0, 2, 4, 6, 8]))
                    else:
                        generated_key += chr(random.choice(range(65, 91)))
                else:
                    if p.isalpha():
                        if random.choice([True, False]):
                            generated_key += 'odd' if p == 'O' else 'even'
                        else:
                            generated_key += p
                    else:
                        generated_key += p  # Keep non-numeric characters as they are
            generated_keys.append(generated_key)
        print(f"Generated keys: {generated_keys}")
        
        # Save generated keys to a text file
        save_to_file = input("Do you want to save the generated keys to a text file? (y/n): ")
        if save_to_file.lower() == 'y':
            filename = input("Enter the filename: ")
            with open(filename, 'w') as f:
                for key in generated_keys:
                    f.write(key + '\n')

# User input for the serial key
serial_key = input("Enter the serial key: ")
detect_pattern(serial_key)
