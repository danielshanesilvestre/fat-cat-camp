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
        
        cats = [cat for cat in Cat.get_all() if cat.owner_id == owner.id]
        if len(cats) == 0:
            print("Cats: None")
        else:
            print("Cats:")
            for i, cat in enumerate(cats, start = 1):
                print(f"  {i}. {cat.name}")
        print("--------------------")

        print("Please select an option:")
        print("  b - Go back to previous menu")
        if len(cats) != 0:
            print("  (number) - View cat details")
        if len(cats) == 0:
            print(f"  d - Delete {owner.name}")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if type(choice) == int and 0 <= choice - 1 < len(cats):
            view_cat(cats[choice - 1])
        elif choice == "b":
            exit = True
        elif choice == "d" and len(cats) == 0:
            delete_owner(owner)
            exit = True
        else:
            print("Invalid choice")

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
        else:
            print("Invalid choice")

def create_owner():
    print("Enter the new owner's name:")
    name = input("> ")
    print("Enter the new owner's phone number:")
    phone_number = input("> ")
    owner = Owner.create(name, phone_number)
    print(f"{owner.name} has been successfully registered.")
    view_owner(owner)
    pass

def delete_owner(owner = None):
    while owner == None:
        print("Select an owner to delete, or enter c to cancel:")
        print("--------------------")
        owners = Owner.get_all()
        for i, owner in enumerate(owners, start = 1):
            print(f"  {i}. {owner.name}")
        print("--------------------")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if choice == "c":
            print("Cancelling operation.")
            return
        elif type(choice) == int and 1 <= choice <= len(owners):
            owner = owners[choice - 1]
        else:
            print("Invalid choice")
    
    cats = [cat for cat in Cat.get_all() if cat.owner_id == owner.id]

    if len(cats) > 0:
        print("Owner must have no cats to be deleted.")
        return

    name = owner.name
    owner.delete()
    print(f"{name} has been successfully deleted.")
    pass

def cats_menu():
    exit = False

    while not exit:
        print("Viewing cats:")
        print("--------------------")
        cats = Cat.get_all()
        for i, cat in enumerate(cats, start = 1):
            print(f"{i}. {cat.name}")
        print("--------------------")
        
        print("Please select an option:")
        print("  b - Go back to previous menu")
        print("  (number) - View cat details")
        print("  c - Register a cat")
        print("  d - Delete a cat")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if type(choice) == int and 0 <= choice - 1 < len(cats):
            view_cat(cats[choice - 1])
        elif choice == "b":
            exit = True
        elif choice == "d":
            delete_cat()
        else:
            print("Invalid choice")


def delete_cat(cat = None):
    while cat == None:
        print("Select a cat to delete, or enter c to cancel:")
        print("--------------------")
        cats = Cat.get_all()
        for i, cat in enumerate(cats, start = 1):
            print(f"  {i}. {cat.name}")
        print("--------------------")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if choice == "c":
            print("Cancelling operation.")
            return
        elif type(choice) == int and 1 <= choice <= len(cats):
            cat = cats[choice - 1]
        else:
            print("Invalid choice")
    
    name = cat.name
    cat.delete()
    print(f"{name} has been successfully deleted.")


def exit_program():
    print("Goodbye!")
    exit()
