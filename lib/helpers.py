# lib/helpers.py
from models.owner import Owner;
from models.cat import Cat;

def owners_menu():
    exit = False

    while not exit:
        print("Viewing owners:")
        owners = Owner.get_all()
        if len(owners) == 0:
            print("No owners registered.")
        else:
            print("--------------------")
            for i, owner in enumerate(owners, start = 1):
                print(f"{i}. {owner.name}")
            print("--------------------")
        print("Please select an option:")
        print("  b - Go back to previous menu")
        print("  c - Register an owner")
        if len(owners) > 0:
            print("  (number) - View an owner's details")
            print("  u - Update an owner")
            print("  d - Delete an owner")
            print("  f - Search for an owner by phone number")
        
        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if choice == "b":
            exit = True
        elif choice == "c":
            create_owner()
        elif type(choice) == int and 1 <= choice <= len(owners):
            view_owner(owners[choice - 1])
        elif choice == "u" and len(owners) > 0:
            update_owner()
        elif choice == "d" and len(owners) > 0:
            delete_owner()
        elif choice == "f" and len(owners) > 0:
            find_owner_by_phone_number()
        else:
            print("Invalid choice")

def create_owner():
    print("Enter the new owner's name:")

    choice = None
    while type(choice) != Owner:
        print("Enter the new owner's name:")
        choice = select_owner(owner)
        if choice == False:
            return
    cat.owner_id = choice.id


    name = input("> ")
    print("Enter the new owner's phone number:")
    phone_number = input("> ")
    owner = Owner.create(name, phone_number)
    print(f"{owner.name} has been successfully registered.")
    view_owner(owner)
    pass

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
        print(f"  u - Update {owner.name}")
        print(f"  c - Register a cat under {owner.name}")
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

        if choice == "b":
            exit = True
        elif choice == "u":
            update_owner(owner)    
        elif type(choice) == int and 0 <= choice - 1 < len(cats):
            view_cat(cats[choice - 1])
        elif choice == "d" and len(cats) == 0:
            delete_owner(owner)
            exit = True
        elif choice == "c":
            create_cat(owner = owner)
        else:
            print("Invalid choice")
        
        if owner.id == None:
            exit = True

def select_owner(default = None):
    print("--------------------")
    owners = Owner.get_all()
    for i, owner in enumerate(owners, start = 1):
        print(f"  {i}. {owner.name}")
    print("--------------------")

    choice = input("> ")
    print("")

    if default != None and choice == "":
        return default

    try:
        choice = int(choice)
    except ValueError:
        pass

    if choice == "c":
        print("Cancelling operation.")
        return False
    elif type(choice) == int and 1 <= choice <= len(owners):
        return owners[choice - 1]
    else:
        print("Invalid choice")

def update_owner(owner = None):
    while owner == None:
        print("Select an owner to update, or enter c to cancel:")
        owner = select_owner()
        if owner == False:
            return
    
    print("Enter a new name, or press return to keep the old name:")
    choice = input("> ")

    if choice != "":
        owner.name = choice
    
    print("Enter a new phone number, or press return to keep the old number:")
    choice = input("> ")

    if choice != "":
        owner.phone_number = choice
    
    owner.update()
    print(f"{owner.name} has been successfully updated.")
    pass

def delete_owner(owner = None):
    while owner == None:
        print("Select an owner to delete, or enter c to cancel:")
        owner = select_owner()
        if owner == False:
            return
    
    cats = [cat for cat in Cat.get_all() if cat.owner_id == owner.id]

    if len(cats) > 0:
        print("Owner must have no cats to be deleted.")
        return

    name = owner.name
    owner.delete()
    print(f"{name} has been successfully deleted.")
    pass

def find_owner_by_phone_number():
    print("Enter a phone number to search by, or press c to cancel:")
    choice = input("> ")

    if choice == "c":
        return

    owners = [owner for owner in Owner.get_all() if owner.phone_number == choice]
    if len(owners) > 0:
        owner = owners[0]
        print(f"Found match: {owner.name}")
        view_owner(owner)
    else:
        print("No match found.")

    pass

def find_cat_by_weight():
    weight = None
    while not type(weight) == float:
        print("Enter a weight to search by, or press c to cancel:")
        choice = input("> ")
        print("")
        
        if choice == "c":
            return

        try:
            weight = float(choice)
        except ValueError:
            print("Weight must be a number.")
            pass

    cat = Cat.find_by_weight(weight)# [cat for cat in Cat.get_all() if cat.weight == weight]
    if cat == None:
        print("No match found.")
    else:
        print(f"Found match: {cat.name}")
        view_cat(cat)

    pass

def cats_menu():
    exit = False

    while not exit:
        
        print("Viewing cats:")
        
        cats = Cat.get_all()
        if len(cats) == 0:
            print("No cats registered.")
        else:
            print("--------------------")
            for i, cat in enumerate(cats, start = 1):
                print(f"{i}. {cat.name}")
            print("--------------------")
        owners_len = len(Owner.get_all())
        if owners_len == 0:
            print("You must register an owner before registering a cat.")


        print("Please select an option:")
        print("  b - Go back to previous menu")
        if owners_len > 0:
            print("  c - Register a cat")
        if len(cats) > 0:
            print("  (number) - View cat details")
            print("  u - Update a cat")
            print("  d - Delete a cat")
            print("  f - Search for a cat by weight")

        choice = input("> ")
        print("")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if choice == "b":
            exit = True
        elif choice == "c" and owners_len > 0:
            create_cat()
        elif type(choice) == int and 0 <= choice - 1 < len(cats):
            view_cat(cats[choice - 1])
        elif choice == "u" and len(cats) > 0:
            update_cat()
        elif choice == "d" and len(cats) > 0:
            delete_cat()
        elif choice == "f" and len(cats) > 0:
            find_cat_by_weight()
        else:
            print("Invalid choice")

def create_cat(owner = None):

    while owner == None:
        print("Select an owner to register the cat under, or enter c to cancel:")
        owner = select_owner()


    name = None
    while not (type(name) == str and name != ""):
        print("Enter the new cat's name:")
        name = input("> ")
        print("")
        if name == "":
            print("Name must not be empty.")
    
    weight = None
    while not type(weight) == float:
        print("Enter the new cat's current weight:")
        choice = input("> ")
        print("")
        try:
            weight = float(choice)
        except ValueError:
            print("Weight must be a number.")
            pass

    cat = Cat.create(name, weight, owner.id)
    print(f"{cat.name} has been successfully registered.")
    view_cat(cat)
    pass

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
        print(f"  o - View {owner.name}'s details")
        print(f"  u - Update {cat.name}")
        print(f"  d - Delete {cat.name}")

        choice = input("> ")
        print("")

        if choice == "b":
            exit = True
        elif choice == "o":
            view_owner(owner)
        elif choice == "u":
            update_cat(cat)
        elif choice == "d":
            delete_cat(cat)
        else:
            print("Invalid choice")
        
        if cat.id == None:
            exit = True

def select_cat():
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
        return False
    elif type(choice) == int and 1 <= choice <= len(cats):
        return cats[choice - 1]
    else:
        print("Invalid choice")

def update_cat(cat = None):
    while cat == None:
        print("Select a cat to update, or enter c to cancel:")
        cat = select_cat()
        if cat == False:
            return
    
    owner = Owner.find_by_id(cat.owner_id)
    
    choice = None
    while type(choice) != Owner:
        print("Select a new owner, or press return to keep the old owner:")
        choice = select_owner(owner)
        if choice == False:
            return
    cat.owner_id = choice.id
    
    print("Enter a new name, or press return to keep the old name:")
    choice = input("> ")

    if choice != "":
        cat.name = choice
    
    print("Enter a new weight, or press return to keep the old weight:")
    choice = None
    while not type(choice) == float:
        choice = input("> ")

        if choice == "":
            choice = cat.weight
            break

        try:
            choice = float(choice)
        except ValueError:
            print("Weight must be a number.")
            pass
    cat.weight = choice
    
    cat.update()
    print(f"{cat.name} has been successfully updated.")
        

def delete_cat(cat = None):
    while cat == None:
        print("Select a cat to delete, or enter c to cancel:")
        cat = select_cat()
        if cat == False:
            return
    
    name = cat.name
    cat.delete()
    print(f"{name} has been successfully deleted.")


def exit_program():
    print("Goodbye!")
    exit()
