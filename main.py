from computesquare import square

def cube(x):
    """Returns the cube of x."""
    return x * x * x

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate square")
        print("2. Calculate cube")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, 3): ").strip()
        if choice == "1":
            number = get_number()
            print(f"The square of {number} is {square(number)}.")
        elif choice == "2":
            number = get_number()
            print(f"The cube of {number} is {cube(number)}.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_number():
    """Get a valid number from the user."""
    while True:
        try:
            return float(input("Enter a number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
