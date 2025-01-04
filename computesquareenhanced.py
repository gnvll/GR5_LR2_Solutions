"""
File: computesquare.py
Illustrates the definition of a main function with error handling.
"""

def main():
    """The main function for this script."""
    while True:
        try:
            number = float(input("Enter a number: ").strip())
            result = square(number)
            print("The square of", number, "is", result)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def square(x):
    """Returns the square of x."""
    return x * x

# The entry point for program execution
if __name__ == "__main__":
    main()
