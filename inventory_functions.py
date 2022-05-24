# for main program: inventory_tracker.py
import database_module as db
import time

data = ' '
item = ' '
location = ' '
node = ' '
current_time = time.ctime()

def main_menu():
	print("\nPlease choose an option below")
	print("1 - Add item\n"
	"2 - Remove item\n"
	"3 - Find item\n"
	"4 - Update an entry\n"
	"5 - Sort items\n"
	"6 - Print quick list\n"
	"7 - Print formatted list\n"
	"8 - Search by Tag (beta)\n")
	top_menu = input("Choice: ")

	if top_menu == '1':
		add_node(item, location, note=None)
	elif top_menu == '2':
		remove_node(item)
	elif top_menu == '3':
		find_item()
	elif top_menu == '4':
		update_node()
	elif top_menu == '5':
		sort_list()
	elif top_menu == '6':
		quick_list()
		main_menu()
	elif top_menu == '7':
		print_formatted_list()
	elif top_menu == '8':
		print("\nFEATURE COMING SOON!\n"
			  "'Search by Tag'")
		main_menu()


def add_node(item, location, note=None):
    """adds nodes to main inventory list, until user enters 'q' to quit."""
    inv_list = db.read()
    new_node = {}
    num = 0
    print("\n*** ADDING item ***\n")
    while True:
        print("Enter an item")
        print("(Enter 'q' at anytime to quit)")

        item = input("Item: ")
        item = item.lower()
        check_item_num = item
        if item == 'q':
            print("Exiting...\n")
            break
        for node in inv_list:
            check_list = node['item']
            check_list = check_list.lower()
            # checks list for identical name, alerts user, stops entry process.
            # currently broken, 05.18.22
            if item == check_list:
                print(f"\nItem '{item.upper()}' already in list!\n"
                      "Please try again")
                break
                main_menu()
        location = input("Location: ")
        if location == 'q':
            print("Item NOT ADDED")
            print("Exiting...\n")
            break
        note = input("Note (optional): ")
        new_node = {'created': current_time, 'item': item, 'location': location.lower()}
        if note:
            new_node['note'] = note.lower()
            if note == 'q':
                print("Item NOT ADDED")
                print("Exiting...\n")
                break
        elif note not in new_node:
            new_node['note'] = 'none'
        inv_list.append(new_node)
    print("---------------------")
    for key, value in new_node.items():
        #		for key, value in new_node.items():
        print(f"{key.title()}: {value}")
    db.write(inv_list)
    # returning to main menu
    main_menu()


def remove_node(item):
    """remove a node from list"""
    inv_list = db.read()
    print("\n*** REMOVING item ***")
    item = input("Enter item: ")
    found = 0
    # add while loop; for in the case that two item have the same name and you need to remove the second instance.
    # currently, selecting 'no' to removing the first item returns the user to the main menu instead of asking about the second item.
    qty_found = 0
    for node in inv_list:
        check_list = node['item']
        if item.lower() == check_list.lower():
            found = 1
            qty_found += 1
            print(f"\nItem '{item.upper()}' found!\n")
            print(f"INSTANCE {qty_found}")
            for key, value in node.items():
                print(f"\t{key.title()}: {value}")

            yn = input(f"Are you sure you want to permanently delete '{item.upper()}', INSTANCE {qty_found}? (y/n) ")
            if yn == 'y':
                print(f"Removed item: '{item.upper()}'")
                inv_list.remove(node)
                db.write(inv_list)
            elif yn == 'n':
                #				if qty_found > 1:

                print("\nCanceling item removal")
                db.write(inv_list)
                break
            elif yn != 'y' and yn != 'n':
                print("Invalid response")
                continue
    if found == 0:
        print(f"Item '{item}' could not be found!")
    # returning to main menu
    main_menu()


def find_item():
    """A simple search func that displays entire entry (dict) for the specified item"""
    """Trying to change func so that it can search all values with even a partial value 05.19.2022"""
    print("*** FIND an entry ***\n")
    inv_list = db.read()
    item = input("Please enter item name: ")
    item = item.lower()
    item_found = 0
    for node in inv_list:
        for k, v in node.items():
            #			for value in node[key]:
            if item in v:
                print("Yes it's in the list!")
                #				print(node)
                for key, value in node.items():
                    print(f"{key.title()}: {value.upper()}")

                #		if item in node.values():
                #		if node['item'] == item:

                # for key, value in node.items():
                #				print(f"{key.title()}: {value.upper()}")
                item_found = 1
                print("* END *")
        # returning to main menu
    main_menu()
    if item_found == 0:
        print(f"Item '{item.upper()}' not found.")
        retry = input("Search again? (y/n) ")
        if retry == 'n':
            main_menu()
        elif retry == 'y':
            find_item()
        elif retry != 'n' and retry != 'y':
            print("Invalid entry.  Please choose y(es) or n(o).")
            retry = input("Search again? (y/n) ")
            if retry == 'n':
                # returning to main menu
                main_menu()
            elif retry == 'y':
                find_item()
            elif retry != 'n' and retry != 'y':
                print("Invalid entry.  Returning to Main Menu...")
                # returning to main menu
                main_menu()


def update_node():
    """updating an entry node"""
    inv_list = db.read()
    print("*** UPDATE an entry ***")
    quick_list()
    item = input("Please enter item name: ")
    item = item.lower()

    for node in inv_list:
        if node['item'] == item:
            print(f"\nUpdating the '{item.upper()}' node")
            print(f"  Current data:\n"
                  f"\tItem: {node['item']}\n"
                  f"\tLocation: {node['location']}\n"
                  f"\tNotes: {node['note']}\n")
            print(f"What would you like to update? ")
            print("1 - Item name\n"
                  "2 - Location\n"
                  "3 - Notes\n"
                  "4 - CANCEL\n")
            update = input("Choice: ")
            # update item name; for misspelling or just some updating some info
            if update == '1':
                old_info = node['item']
                new_info = input("Enter new item name: ")
                node['modified'] = current_time
                node['item'] = new_info.lower()
                print(f"\nChanged 'item' field of '{item.upper()}' node\n"
                      f"From: '{old_info}'\n"
                      f"To: '{new_info}'\n")
            #				print(node)
            elif update == '2':
                # update location...
                old_info = node['location']
                new_info = input("Enter new location: ")
                node['modified'] = current_time
                node['location'] = new_info.lower()
                print(f"\nChanged 'Location' field of '{item.upper()}' node\n"
                      f"From: '{old_info}'\n"
                      f"To: '{new_info}'\n")
                print(node)
            elif update == '3':
                # update or add notes if none
                old_info = node.get('note', 'none')
                new_info = input("Enter new note: ")
                node['modified'] = current_time
                node['note'] = new_info.lower()
                print(f"\nChanged 'Note' field of '{item.upper()}' node\n"
                      f"From: '{old_info}'\n"
                      f"To: '{new_info}'\n")
                print(node)
            elif update == '4':
                # cancels with no changes
                print("Update canceled")
                break
    db.write(inv_list)
    # returning to main menu
    main_menu()


def sort_by():
	"""Choose by which key to sort the inventory list; to be used with sort_list function"""
	inv_list = db.read()
	print("Sort by:\n"
		  "1 - Item name\n"
		  "2 - Location name\n"
		  "3 - Notes\n")
	choice = input("Choice: ")
	if choice == '1':
		return 1
	elif choice == '2':
		return 2
	elif choice == '3':
		return 3

def sort_list():
	"""Prints to screen the inventory list, sorted by Item or Location"""
	inv_list = db.read()
	num = 1
	print("\n*** Sorted Inventory List ***\n")
	choice = sort_by()
	if choice == 1:
		print("\nSorting by Item Name\n")
		sorter = 'item'
	elif choice == 2:
		print("\nSorting by Location Name\n")
		sorter = 'location'
	elif choice == 3:
		print("\nSorting by Notes field\n")
		sorter = 'note'
	print(f"{current_time}\n")
	sorted_inv_list = sorted(inv_list, key=lambda d: d[sorter])
	#printing out sorted, numbered list, based on user's criteria
	for node in sorted_inv_list:
		print(f"{num} - - - - - - - - - - - - - - - - - ")
		for key, value in node.items():
			print(f"\t{key.title()}: {value}")
		num += 1
	# returning to main menu
	main_menu()


def quick_list():
	"""prints a quick list for item name reference (when updating at least)"""
	print("Quick Listing: ")
	inv_list = db.read()
	for node_item in inv_list:
		print(f"\t{node_item['item'].title()}")


def print_formatted_list():
    """prints to screen, a nicely formatted and numbered inventory list"""
    inv_list = db.read()
    num = 1
    print("\n*** Inventory List ***\n"
          f"{current_time}\n")
    for node in inv_list:
        print(f"{num} - - - - - - - - - - - - - - - - - ")
        for key, value in node.items():
            print(f"\t{key.title()}: {value}")
        num += 1
    # returning to main menu
    main_menu()

