# lib/cli.py

from helpers import (
    exit_program,
    cats_menu,
    owners_menu
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "o":
            owners_menu()
        elif choice == "c":
            cats_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("e - Exit the program")
    print("o - View owners")
    print("c - View cats")


if __name__ == "__main__":
    main()
