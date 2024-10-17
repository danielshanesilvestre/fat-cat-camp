# lib/helpers.py
from models.owner import Owner;
from models.cat import Cat;

def owners_menu():
    exit = False

    while not exit:
        print("Viewing owners:")
        print("--------------------")
        owners = Owner.get_all()
        for i, owner in enumerate(owners, start = 1):
            print(f"{i}. {owner.name}")
            pass
        print("--------------------")
        print("Please select an option:")
        print("  b - Go back to previous menu")
        print("  (number) - View owner details")
        print("  c - Register an owner")
        print("  d - Delete an owner")
        
        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if type(choice) == int:
            view_owner(owners[choice - 1])
        elif choice == "b":
            exit = True
        elif choice == "c":
            create_owner()
        elif choice == "d":
            delete_owner()
        else:
            print("Invalid choice")

def view_owner(owner):
    exit = False

    while not exit:
        print(f"Viewing details of {owner.name}:")
        print("--------------------")
        print(f"Name: {owner.name}")
        print(f"Phone number: {owner.phone_number}")
        print("Cats:")
        cats = [cat for cat in Cat.get_all() if cat.owner_id == owner.id]
        for i, cat in enumerate(cats, start = 1):
            print(f"  {i}. {cat.name}")
        print("--------------------")

        print("Please select an option:")
        print("  b - Go back to previous menu")
        print("  (number) - View cat details")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if type(choice) == int:
            if 0 <= choice - 1 < len(cats):
                view_cat(cats[choice - 1])
            else:
                print("Invalid choice")
        elif choice == "b":
            exit = True

def view_cat(cat):
    exit = False

    while not exit:
        print(f"Viewing details of {cat.name}")
        print("--------------------")
        print(f"Name: {cat.name}")
        print(f"Weight: {cat.weight} lbs")
        owner = Owner.find_by_id(cat.owner_id)
        print(f"Owner: {owner.name}")
        print("--------------------")

        print("Please select an option:")
        print("  b - Go back to previous menu")
        print("  o - View owner details")

        choice = input("> ")
        print("")

        if choice == "b":
            exit = True
        elif choice == "o":
            view_owner(owner)

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
