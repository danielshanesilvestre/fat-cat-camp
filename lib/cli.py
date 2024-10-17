# lib/cli.py

from helpers import (
    exit_program,
    cats_menu,
    owners_menu
)


def main():
    print("Welcome to the Fat Cat Camp manager utility program!")
    while True:
        
        print("Please select an option:")
        print("  e - Exit the program")
        print("  o - View owners")
        print("  c - View cats")

        choice = input("> ")
        print("")
        
        if choice == "e":
            exit_program()
        elif choice == "o":
            owners_menu()
        elif choice == "c":
            cats_menu()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
