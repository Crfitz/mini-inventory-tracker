from inv_classes import Inventory as inv
import json

# all funcs included; have not moved to separate file yet
database = 'inventory_db.json'
#prefilled list just for testing
inv_list = [
	{'item':'bike', 'location':'carport', 'notes':'huffy mountain bike'},
	{'item':'phone', 'location':'table', 'notes':'none'},
	{'item':'keys', 'location':'key hooks', 'notes':'truck'},
	{'item':'python book', 'location':'nightstand', 'notes':'Between n/s and bed'},
	{'item':'cd case', 'location':'master closet', 'notes':'back top left'},
	{'item':'watch', 'location':'dresser', 'notes':'none'},
	]
#inv_list = []
item = ' '
location = ' '
node = ' '
print("Inventory Project\n")
print("Fitzie Enterprises, LLC.\n"
"Copyright 2022; All rights reserved\n")

"""
def write(data):
	database = 'inventory_db.json'
	try:
		with open(database, 'w') as db:
			json.dump(data, db, indent=2)
			print("Writing to database...")
	except FileNotFoundError:
		print(f"Sorry, the file '{database}' does not exist.")
	
def append(data):
	database = 'inventory_db.json'
	with open(database, 'a') as db:
		json.dump(data, db, indent=2)
		print("Writing to database...")
		
def read(data):
	database = 'inventory_db.json'
	with open(database) as db:
		data = json.load(db)
		print("Loading database...")
		print(f"Reading from json file:\n"
		f"{data}")
"""

#read(inv_list)

def main_menu():
	print("\nPlease choose an option below")
	print("1 - Add item\n"
	"2 - Remove item\n"
	"3 - Find item\n"
	"4 - Update an entry\n"
	"5 - Sort items\n"
	"6 - Print quick list\n"
	"7 - Print formatted list\n")
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

def add_node(item, location, note=None):
	"""adds nodes to main inventory list, until user enters 'q' to quit."""
#	read(inv_list)
	print("\n*** ADDING item ***\n")
	while True:
		print("Enter an item")
		print("(Enter 'q' at anytime to quit)")
		item = input("Item: ")
		if item == 'q':
			print("Exiting...\n")
			break
		for node_item in inv_list:
			check_list = node_item['item']
			if item.lower() == check_list.lower():
				print(f"\nItem '{item.upper()}' already in list!")
				for key, value in node_item.items():
					print(f"\t{key.title()}: {value}")
					break
		location = input("Location: ")
		if location == 'q':
			print("Item NOT ADDED")
			print("Exiting...\n")
			break
		note = input("Note (optional): ")
		new_node = {'item':item.lower(), 'location':location.lower()}
		if note:
			new_node['note'] = note.lower()
			if note == 'q':
				print("Item NOT ADDED")
				print("Exiting...\n")
				break
		elif note not in new_node:
			new_node['note'] = 'none'
		inv_list.append(new_node)
	for node in inv_list:
		print("---------------------")
		for key, value in node.items():
			print(f"{key.title()}: {value}")
#	write(inv_list)
	# returning to main menu
	main_menu()

def remove_node(item):
	"""remove a node from list"""
#	read(inv_list)
	print("\n*** REMOVING item ***")
	item = input("Enter item: ")
	found = 0
	for node_item in inv_list:
		if node_item['item'] == item:
			found = 1
			print(f"Item '{item}' found!")
			yn = input(f"Are you sure you want to permanently delete '{item.upper()}'? (y/n) ")
			if yn == 'y':
				print(f"Removed item: '{item.upper()}'")
				inv_list.remove(node_item)
#				write(inv_list)
#				print(inv_list)
			elif yn == 'n':
				print("\nCanceling item removal")
#				write(inv_list)
#				print(inv_list)
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
	print("*** FIND an entry ***\n")
	#	quick_list()
	item = input("Please enter item name: ")
	item = item.lower()

	item_found = 0
	for node in inv_list:
		if node['item'] == item:
			for key, value in node.items():
				print(f"{key.title()}: {value.upper()}")
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

def quick_list():
	"""prints a quick list for item name reference (when updating at least)"""
	print("Quick Listing: ")
#	read(inv_list)
	for node_item in inv_list:
		print(f"\t{node_item['item'].title()}")
#	write(inv_list)

def update_node():
	"""updating an entry node"""
#	read(inv_list)
	print("*** UPDATE an entry ***\n")
	quick_list()
	item = input("Please enter item name: ")
	item = item.lower()
	
	for node in inv_list:
		if node['item'] == item:
			print(f"\nUpdating the '{item.upper()}' node")
			print(f"What would you like to update? ")
			print("1 - Item name\n"
				"2 - Location\n"
				"3 - Notes\n"
				"4 - CANCEL\n"
# add get() for notes, for the case where the node has no 'notes' field
# or might just use an IF...
				f"Currently: Item: {node['item']}; Location: {node['location']} ")
			update = input("Choice: ")
			# update item name; for misspelling or just a name change
			if update == '1':
				old_info = node['item']
				new_info = input("Enter new item name: ")
				node['item'] = new_info.lower()
				print(f"\nChanged 'item' field of '{item.upper()}' node\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '2':
				# update location...
				old_info = node['location']
				new_info = input("Enter new location: ")
				node['location'] = new_info.lower()
				print(f"\nChanged 'Location' field of '{item.upper()}' node\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '3':
				# update or add notes if none
				old_info = node.get('notes', 'none')
				new_info = input("Enter new note: ")
				node['notes'] = new_info.lower()
				print(f"\nChanged 'Notes' field of '{item.upper()}' node\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '4':
				# cancels with no changes
				print("Update canceled")
				break
#	write(inv_list)
	# returning to main menu
	main_menu()

def sort_by():
	"""Choose by which key to sort the inventory list; to be used with sort_list function"""
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
	num = 1
	alpha_sorted = []
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
		sorter = 'notes'
	sorted_inv_list = sorted(inv_list, key=lambda d: d[sorter])
	for node in sorted_inv_list:
		print(f"{num} - - - - - - - - - - - - - - - - - ")
		for key, value in node.items():
			print(f"\t{key.title()}: {value}")
		num += 1
	main_menu()

def print_formatted_list():
	"""prints to screen, a nicely formatted and numbered inventory list"""
#	read(inv_list)
	num = 1
	print("Inventory List\n")
	for entry in inv_list:
		print(f"{num} - - - - - - - - - - - - - - - - - ")
		for key, value in entry.items():
			print(f"\t{key.title()}: {value}")
		num += 1
	main_menu()
	

main_menu()


