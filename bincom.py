import psycopg2
from collections import Counter

# Data extracted from the HTML table
data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Database connection details
db_config = {
    'dbname': 'bincom',
    'user': 'bolu',
    'password': 'ajijola',
    'host': 'localhost', 
    'port': '5432'       
}

# Connect to PostgreSQL database and create table
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50),
        frequency INT
    );
    """)
    conn.commit()

    # Insert color frequencies into the database
    for color, frequency in all_colors.items():
        cursor.execute("""
        INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)
        ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency;
        """, (color, frequency))
    
    conn.commit()

    print("Color frequencies successfully saved to the database.")
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cursor.close()
    conn.close()


# Count colors for each day
color_counts = {}

for day, colors in data.items():
    # Split the color string and count occurrences
    color_list = [color.strip() for color in colors.split(",")]
    color_counts[day] = Counter(color_list)

# Display color counts
for day, counts in color_counts.items():
    print(f"Color counts for {day}:")
    for color, count in counts.items():
        print(f"  {color}: {count}")
    print()  # Blank line for better readability

# Determine the most common color for T-shirts
all_colors = Counter()

for counts in color_counts.values():
    all_colors.update(counts)

# Calculate the average frequency
total_colours = sum(all_colors.values())
colours = len(all_colors)

mean_frequency = total_colours / colours

print(f"Mean frequency: {mean_frequency:.2f}")
print("Colors closest to the mean frequency:")

# Find the most common color
most_common_color = all_colors.most_common(1)[0]
print(f"The most common color for T-shirts is {most_common_color[0]} with {most_common_color[1]} occurrences.")

#Variance of the colors
variance = sum((count - mean_frequency) ** 2 for count in all_colors.values()) / colours
print(f"Variance of color frequencies: {variance:.2f}")

# Calculate total occurrences and occurrences of red
total_occurrences = sum(all_colors.values())
red_occurrences = all_colors.get('RED', 0)

# Calculate probability of choosing red
probability_red = red_occurrences / total_occurrences

# Display results
print(f"Total occurrences: {total_occurrences}")
print(f"Occurrences of RED: {red_occurrences}")
print(f"Probability of choosing RED: {probability_red:.4f}")


#write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def recursive_linear_search(arr, target, index=0):
    # Base case: if the index exceeds the length of the list, the target is not found
    if index >= len(arr):
        return -1  # Target not found
    # If the target is found, return the index
    if arr[index] == target:
        return index
    # Recur for the next index
    return recursive_linear_search(arr, target, index + 1)

# Example usage
numbers = [3, 5, 2, 8, 1, 4]
user_input = int(input("Enter a number to search for: "))
result = recursive_linear_search(numbers, user_input)

if result != -1:
    print(f"Number {user_input} found at index {result}.")
else:
    print(f"Number {user_input} not found in the list.")
    
#Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.5  
    
import random

def generate_random_binary():
    # Generate a random 4-digit binary number as a string
    binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
    return binary_number

def binary_to_decimal(binary_str):
    # Convert binary string to decimal
    return int(binary_str, 2)

# Main program
if __name__ == "__main__":
    random_binary = generate_random_binary()
    decimal_value = binary_to_decimal(random_binary)
    
    print(f"Generated 4-digit binary number: {random_binary}")
    print(f"Converted to decimal (base 10): {decimal_value}")

##Write a program to sum the first 50 fibonacci sequence.

def fibonacci_sum(n):
    a, b = 0, 1  # Starting values for the Fibonacci sequence
    total_sum = 0

    for _ in range(n):
        total_sum += a  # Add the current Fibonacci number to the total
        a, b = b, a + b  # Update to the next Fibonacci number

    return total_sum

# Main program
if __name__ == "__main__":
    n = 50  # Number of Fibonacci numbers to sum
    result = fibonacci_sum(n)
    print(f"The sum of the first {n} Fibonacci numbers is: {result}")
