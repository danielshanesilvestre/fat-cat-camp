# lib/helpers.py
from models.owner import Owner;
from models.cat import Cat;

def owners_menu():
    exit = False

    while not exit:
        print("Viewing owners:")
        for owner in Owner.get_all():
            print(f"- {owner.name}, {owner.phone_number}")
            pass
        print("Please select an option:")
        print("b - Go back to previous menu")
        print("c - Register an owner")
        print("d - Delete an owner")
        choice = input("> ")
        if choice == "b":
            exit = True
        elif choice == "c":
            create_owner()
        elif choice == "d":
            delete_owner()
        else:
            print("Invalid choice")

def create_owner():

    print("Please enter the new owner's name:")
    name = input("> ")
    print("Enter the new owner's phone number:")
    phone_number = input("> ")
    owner = Owner.create(name, phone_number)
    print(f"Registered: {owner.name}, {owner.phone_number}")

    pass


def cats_menu():
    print("Viewing cats:")
    for cat in Cat.get_all():
        owner = Owner.find_by_id(cat.owner_id)


        print(f"- {cat.name}, {cat.weight}, owned by {owner.name}")
        pass

def exit_program():
    print("Goodbye!")
    exit()
