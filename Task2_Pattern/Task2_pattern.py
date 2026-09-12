# Task 2: Generate and print simple number patterns
# Objective: Utilize loops to control the structure of number patterns.

def print_right_angled_pyramid(rows):
    """Generates a right-angled number pyramid based on user input."""
    print(f"\n--- Generating Pyramid with {rows} rows ---")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")


def print_reverse_pyramid(rows):
    """Generates a reverse number pyramid based on user input."""
    print(f"\n--- Generating Reverse Pyramid with {rows} rows ---")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")



if __name__ == "__main__":
    print("Welcome to the Pattern Generator!")
    try:

        user_input = int(input("Enter the number of rows you want for your pattern: "))

        if user_input <= 0:
            print("Please enter a positive number greater than 0.")
        else:
            print_right_angled_pyramid(user_input)
            print_reverse_pyramid(user_input)

    except ValueError:

        print("Invalid input! Please enter a valid integer.")