import os
import django
from django.conf import settings

# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "backend_bistro_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from app_backend_bistro.models import MenuItem

def display_menu():
    print("1: Add Item")
    print("2: Update Item")
    print("3: Delete Item")
    print("4: Show all Items")
    print("5: Exit")

def create_item(name, price, spice_level, category):
    try:
        item = MenuItem.objects.create(name=name, price=price, spice_level=spice_level, category=category)
        print(f"{category.title()} added successfully.")
        return item
    except Exception as e:
        print(f'An error has occurred: {e}')

def update_item():
    try:
        item_id = int(input("Enter Menu Item ID: "))
        item = MenuItem.objects.get(id=item_id)
        name = input("Enter new name (leave blank to keep current): ")
        price = input("Enter new price (leave blank to keep current): ")
        spice_level = input("Enter new spice level (leave blank to keep current): ")
        category = input("Enter new category (entree/app) (leave blank to keep current): ")

        if name:
            item.name = name
        if price:
            item.price = float(price)
        if spice_level:
            item.spice_level = int(spice_level)
        if category in ['entree', 'app']:
            item.category = category

        item.save()
        print(f'Menu Item with ID {item_id} updated successfully!')
    except MenuItem.DoesNotExist:
        print("Menu Item with given ID does not exist.")
    except Exception as e:
        print(f'An error has occurred: {e}')

def delete_item():
    try:
        item_id = int(input("Enter Menu Item ID to Delete: "))
        item = MenuItem.objects.get(id=item_id)
        item.delete()
        print(f'Menu Item with ID {item_id} has been deleted!')
    except MenuItem.DoesNotExist:
        print('Menu Item with given ID does not exist.')
    except Exception as e:
        print(f'An error has occurred: {e}')

def show_items():
    items = MenuItem.objects.all()
    if items:
        print("All Menu Items: ")
        for item in items:
            print(f'ID: {item.id}, Name: {item.name}, Price: {item.price}, Spice Level: {item.spice_level}, Category: {item.category}')
    else:
        print("No menu items found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter Name: ")
            price = float(input("Enter Price: "))
            spice_level = int(input("Enter Spice Level (1-10): "))
            category = input("Enter category (entree/app): ").strip().lower()
            if category in ['entree', 'app']:
                create_item(name, price, spice_level, category)
            else:
                print("Invalid category.")
        elif choice == '2':
            update_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            show_items()
        elif choice == '5':
            break
        else:
            print("Choose a real option")

main()










