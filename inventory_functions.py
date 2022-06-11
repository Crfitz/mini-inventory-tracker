## inventory_functions.py ##
# for main program: inventory_tracker.py
import sys
import database_module as db
import datetime
import export as ex

version = '1.32'
data = ' '
item = ' '
location = ' '
note = ' '
node = ' '
x = ' '
current_time = datetime.date.today()


def main_menu():
	print("\nPlease choose an option below")
	print("1 - Add item\n"
	"2 - Remove item\n"
	"3 - Find item\n"
	"4 - Update an entry\n"
	"5 - Sort items\n"
	"6 - Print quick list\n"
	"7 - Print formatted list\n"
	"8 - Search by Tag (beta)\n"
	"9 - Export to CSV/Excel file\n")
	top_menu = input("Choice: ")

	if top_menu == 'h':
		help()
	elif top_menu == 'q':
		sys.exit("Exiting Inventory Tracker...")
	elif top_menu == '1':
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
		print("\nIn beta\n"
			"FEATURE COMING SOON!\n"
			"'Search by Tag'")
	elif top_menu == '9':
		print("\n*** Export to CSV/Excel file ***\n")
		ex.exportdb(x)
		main_menu()


def add_node(item, location, note=None):
    """adds nodes to main inventory list, until user enters 'q' to quit."""
    inv_list = db.read()
    new_node = {}
    tags = []
    num = 0
    print("\n*** ADDING item ***\n")
    while True:
        print("Enter an item")
        print("(Enter 'q' at anytime to quit)")

        item = input("Item: ")
        item = item.lower().strip()
        item = item.strip()
        if item == 'q':
            print("Exiting...\n")
            break
        for node in inv_list:
            active_add = True
            check_list = node['item']
            check_list = check_list.lower()
            # checks list for identical name, alerts user, stops entry process.
            if item == check_list:
                print(f"\nItem '{item.upper()}' already in list!")
                print("Please try again")
                active_add = False
                break
        if not active_add:
        	break
        location = input("Location: ")
        if location == 'q':
            print("Item NOT ADDED")
            print("Exiting...\n")
            break
        note = input("Note (optional): ")
        new_node = {'created': current_time.strftime("%Y-%m-%d"), 'item': item, 'location': location.lower()}
        if note:
            new_node['note'] = note.lower()
            if note == 'q':
                print("\nItem NOT ADDED")
                print("Exiting...\n")
                break
        elif note == '':
            note = 'none'
            new_node['note'] = note
        print("Tags (optional): ")
        print("\tPress Enter skip (no tag)")
        print("\tEnter one tag at a time")
        print("\tEnter 'f' to finish")
        new_node = {'created': current_time.strftime("%Y-%m-%d"), 'item': item, 'location': location.lower(), 'note': note.lower(), 'tags': []}
        while True:
        	tags = input("Tags (optional): ")
        	# f to finish adding tags and write node to list in db
        	# q to quit and cancel addition; last chance to cancel
        	if tags == 'f':
        		break
        	elif tags == 'q':
        		break
        	elif tags == '':
        		new_node['tags'].append('none')
        		break
        	else:
        		tags = tags.strip()
        		new_node['tags'].append(tags.lower())
        		continue
        if tags == 'q':
        	print("\nItem NOT ADDED")
        	print("Exiting...\n")
        	break
        else:
        	inv_list.append(new_node)
        	print("---------------------")
        	for key, value in new_node.items():
        		print(f"{key.title()}: {value}")
        	db.write(inv_list)
    # returning to main menu
    main_menu()


def remove_node(item):
    """remove a node from list"""
    inv_list = db.read()
    print("\n*** REMOVING item ***")
    item = input("Enter item: ")
    item = item.strip()
    found = 0
    #qty_found = 0
    for node in inv_list:
        check_list = node['item']
        if item.lower() == check_list.lower():
            found = 1
            #qty_found += 1
            print(f"\nItem '{item.upper()}' found!\n")
            for key, value in node.items():
                print(f"\t{key.title()}: {value}")

            yn = input(f"Are you sure you want to permanently delete '{item.upper()}'? (y/n) ")
            if yn == 'y':
                print(f"Removed item: '{item.upper()}'")
                inv_list.remove(node)
                db.write(inv_list)
            elif yn == 'n':
                print("\nCanceling item removal")
                #db.write(inv_list)
                break
            elif yn != 'y' and yn != 'n':
                print("Invalid response")
                continue
    if found == 0:
        print(f"Item '{item}' could not be found!")
    # returning to main menu
    main_menu()


def find_item():
    """A simple search func that displays entire entry (dict) for the specified item; can search all values with even a partial search term"""
    print("*** FIND an entry ***\n")
    inv_list = db.read()
    item = input("Please enter item name: ")
    print()
    item = item.lower()
    item = item.strip()
    item_found = 0
    #searches for the search term in each value in each node (list element)
    for node in inv_list:
        for k, v in node.items():
            if item in v:
                print("Yes it's in the list!")
                for key, value in node.items():
                    print(f"{key.title()}: {value.upper()}")
                item_found = 1
                print("* * * * * * END * * * * * *\n")
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
    item = item.strip()
    for node in inv_list:
        if node['item'] == item:
            print(f"\nUpdating the '{item.upper()}' node")
            print("Current data:\n")
            for key, value in node.items():
            	print(f"\t{key.title()}: {value}")
            print()
            print("What would you like to update? ")
            print("1 - Item name\n"
                  "2 - Location\n"
                  "3 - Notes\n"
                  "4 - Tags\n"
                  "5 - CANCEL\n")
            update = input("Choice: ")
            # update item name; for misspelling or just some updating some info
            if update == '1':
                old_info = node['item']
                new_info = input("Enter new item name: ")
                node['modified'] = current_time.strftime("%Y-%m-%d")
                node['item'] = new_info.lower()
                print(f"\nChanged 'item' field of '{item.upper()}' node\n"
                f"From: '{old_info}'\n"
                f"To: '{new_info}'\n")
                for key, value in node.items():
                	print(f"\t{key.title()}: {value}")
            elif update == '2':
                # update location...
                old_info = node['location']
                new_info = input("Enter new location: ")
                #adds a new key - timestamp for 'modified'; doesn't replace or update 'created' timestamp
                node['modified'] = current_time.strftime("%Y-%m-%d")
                node['location'] = new_info.lower()
                print(f"\nChanged 'Location' field of '{item.upper()}' node\n"
                f"From: '{old_info}'\n"
                f"To: '{new_info}'\n")
                for key, value in node.items():
                	print(f"\t{key.title()}: {value}")
            elif update == '3':
                # update or add notes if none
                old_info = node.get('note', 'none')
                new_info = input("Enter new note: ")
                node['modified'] = current_time.strftime("%Y-%m-%d")
                node['note'] = new_info.lower()
                print(f"\nChanged 'Note' field of '{item.upper()}' node\n"
                f"From: '{old_info}'\n"
                f"To: '{new_info}'\n")
                for key, value in node.items():
                	print(f"\t{key.title()}: {value}")
            elif update == '4':
            	#adding or updating tags
            	print("This option is in the works...")
            	print("Tags: ")
            	print("\tEnter one tag at a time")
            	print("\tEnter 'n' to finish")
            	new_node = {'created': current_time.strftime("%Y-%m-%d"), 'item': item, 'location': location.lower(), 'note': note.lower(), 'tags': []}
            	old_info = node.get('tags', 'none')
            	node['modified'] = current_time.strftime("%Y-%m-%d")
            	while True:
            		tags = input("Tags (optional): ")
            		if tags == 'n' or tags == 'q':
            			break
            		elif tags == '':
            			tags = 'none'
            			new_node['tags'].append(tags.lower())
            			break
            		else:
            			tags = tags.strip()
            			new_node['tags'].append(tags.lower())
            			continue
            	print(f"\nChanged 'Tags' field of '{item.upper()}' node\n")
            	print(f"From: '{old_info}'\n")
            	print(f"To: '{tags}'\n")
            	for key, value in node.items():
                	print(f"\t{key.title()}: {value}")
            elif update == '5':
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
	print(f"{current_time.strftime('%Y-%m-%d')}\n")
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
	"""prints a quick list for item name reference (item only)"""
	print("Quick Listing: ")
	inv_list = db.read()
	sorted_inv_list = sorted(inv_list, key=lambda d: d['item'])
	for node_item in sorted_inv_list:
		print(f"\t{node_item['item'].title()}")


def print_formatted_list():
    """prints to screen, a nicely formatted and numbered inventory list"""
    inv_list = db.read()
    num = 1
    print("\n*** Inventory List ***\n"
          f"{current_time.strftime('%Y-%m-%d')}\n")
    sorted_inv_list = sorted(inv_list, key=lambda d: d['item'])
    for node in sorted_inv_list:
        print(f"{num} - - - - - - - - - - - - - - - - - ")
        for key, value in node.items():
            print(f"\t{key.title()}: {value}")
        num += 1
    # returning to main menu
    main_menu()
	
	
def help():
	print(f"\nInventory Tracker v{version}")
	print("Help Section\n")
	print("\th - Displays this help section")
	print("\tq - quit")
	print("\t\tEntering 'q' while in the Main Menu EXITS the program.")
	print("\t\tEntering 'q' while in the Add Item section cancels the add and returns you to the Main Menu.\n")
	print("* All inputs are case-insensitive\n")
	print("\tAdding Item:\n"
	"\t\tEnter ITEM, LOCATION. Notes and Tags are optional (press Enter to skip). \n")
	print("\tRemoving Item:\n"
	"\t\tEnter ITEM to be removed.  Enter y(es) or n(o) at confirmtion.\n")
	print("\tFind Item: \n"
	"\t\tEnter a search term, full or partial. This will search the entire list and every section of each node.\n")
	print("\tUpdate Item: \n"
	"\t\tEnter the item and then at the next prompt, choose which part of the node you want to update, e.g., Item or Location. You may still cancel at this point. After updating, a 'modified' date/timestamp will be added to the node.\n")
	print("\tSort item: \n"
	"\t\tChoose a sort-by option and the entire list will be sorted alphabetically by said option.\n")
	print("\tQuick list: \n"
	"\t\tPrints to screen a simple list of item names only.\n")
	print("\tPrint formatted list: \n"
	"\t\tPrints to screen a formatted, sorted and numbered list with all of the data of each node.\n")
	print("\tExport to CSV/Excel format: \n")
	print("\t\tExports entire inventory list to a CSV / Excel spreadsheet format for saving or printing to hardcopy.\n")
	main_menu()