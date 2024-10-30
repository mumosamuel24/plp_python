# file_handling.py

def create_file():
    """Creates a new text file and writes some lines to it."""
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is a number: 42\n")
            file.write("Last line of initial content.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    """Reads the contents of the text file and displays them."""
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("Error: my_file.txt does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    """Appends additional lines to the existing text file."""
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Another line with a number: 100\n")
            file.write("Final appended line.\n")
        print("Additional content appended successfully.")
    except FileNotFoundError:
        print("Error: my_file.txt does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to display all contents

if __name__ == "__main__":
    main()
