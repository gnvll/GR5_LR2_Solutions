def navigate_file_lines():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Read the lines of text from the file into a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Enter a loop to navigate the lines
        while True:
            # Print the number of lines in the file
            num_lines = len(lines)
            print(f"The file has {num_lines} lines.")

            # Prompt the user for a starting line number
            start_line = int(input("Enter the starting line number (0 to quit): "))

            # If the input is 0, quit the program
            if start_line == 0:
                print("Exiting the program.")
                break

            # Prompt the user for an ending line number
            end_line = int(input("Enter the ending line number: "))

            # Validate the line numbers
            if 1 <= start_line <= num_lines and 1 <= end_line <= num_lines and start_line <= end_line:
                # Print the specified range of lines
                for i in range(start_line - 1, end_line):
                    print(lines[i].strip())
            else:
                print("Invalid line numbers. Please try again.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Call the function to run the program
navigate_file_lines()
