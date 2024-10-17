# lib/helpers.py
from models.owner import Owner;
from models.cat import Cat;

def owners_menu():
    print("Viewing owners:")
    for owner in Owner.get_all():
        
        print(f"- {owner.name}, {owner.phone_number}")
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
