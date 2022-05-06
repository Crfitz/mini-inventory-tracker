from inv_classes import Inventory as inv
import json

# Not sure why this is uploading with 
# double tabs...

database = 'inventory_db.json'
#inv_list = []
#prefilled list just for testing
inv_list = [
	{'item':'bike', 'location':'carport', 'notes':'huffy mountain bike'},
	{'item':'phone', 'location':'table'},
	{'item':'keys', 'location':'key hooks', 'notes':'truck'},
	{'item':'python book', 'location':'nightstand', 'notes':'Between n/s and bed'}
	]
item = ' '
location = ' '
node = ' '
print("Inventory Project\n")
print("Fitzie Enterprises, LLC.\n"
"Copyright 2022; All rights reserved\n")

def main_menu():
	print("\nPlease choose an option below")
	print("1 - Add item\n"
	"2 - Remove item\n"
	"3 - Find item\n"
	"4 - Update an entry\n"
	"5 - Sort items\n"
	"6 - Print formatted list\n")
	top_menu = input("Choice: ")

	if top_menu == '1':
#		print("*** ADDING item ***\n")
		add_node(item, location, note=None)
	elif top_menu == '2':
		remove_node(item)
	elif top_menu == '3':
		print("*** FIND item ***\n")
	elif top_menu == '4':
		print("*** UPDATE an entry ***\n")
		update_node()
	elif top_menu == '5':
		print("*** SORT list ***\n")
	elif top_menu == '6':
		print_formatted_list()

#def write(data):
#	database = 'inventory_db.json'
#	with open(database, 'w') as db:
#		json.dump(data, db)
#		print("Writing to database...")
#		
#def read(data):
#	database = 'inventory_db.json'
#	with open(database) as db:
#		json.load(db)
#		print("Loading database...")

def add_node(item, location, note=None):
	"""adds nodes to main inventory list."""
#	read(inv_list)
	print("\n*** ADDING item ***\n")
	while True:
		print("Enter an item")
		print("(Enter 'q' at anytime to quit)")
		item = input("Item: ")
		if item == 'q':
			print("Exiting...\n")
			print(inv_list)
			break
		location = input("Location: ")
		if item == 'q':
			print("Item NOT ADDED")
			print("Exiting...\n")
			print(inv_list)
			break
		note = input("Note (optional): ")
		new_node = {'item':item.lower(), 'location':location.lower()}
		if note:
			new_node['note'] = note.lower()
			if item == 'q':
				print("Item NOT ADDED")
				print("Exiting...\n")
				print(inv_list)
				break
		inv_list.append(new_node)
#		write(inv_list)
	main_menu()

def remove_node(item):
	"""remove a node from list"""
	print("\n*** REMOVING item ***")
	item = input("Enter item: ")
	for node_item in inv_list:
		if node_item['item'] == item:
			print(f"Item '{item}' found!")
			yn = input(f"Are you sure you want to delete '{item.upper()}'? ")
			if yn == 'y':
				print(f"Removed item: '{item.upper()}'")
				inv_list.remove(item)
			elif yn == 'n':
				print("\nCanceling item removal")
				print(inv_list)
				break
			elif yn != 'y' and yn != 'n':
				print("Invalid response")
				continue
			#elif yn == '*':
#				print("Invalid response")
#				continue
		elif node_item != item:
			print(f"Item '{item}' could not be found!")
	main_menu()

def quick_list():
	print("Quick Listing: ")
	for node_item in inv_list:
		print(f"\t{node_item['item'].title()}")

def update_node():
	"""updating an entry node"""
	quick_list()
	item = input("Please enter item name: ")
	item = item.lower()
	
	for node in inv_list:
		if node['item'] == item:
			print(f"Let's update {item.title()}!")
			print(f"What would you like to update?")
			print("1 - Item\n"
				"2 - Location\n"
				"3 - Notes\n"
				"4 - CANCEL\n"
				f"Currently: Item: {node['item']}; Location: {node['location']} ")
			update = input("Choice: ")
			if update == '1':
				old_info = node['item']
				new_info = input("Enter new item name: ")
				node['item'] = new_info.lower()
				print(f"Changed 'item' field\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '2':
				old_info = node['location']
				new_info = input("Enter new location: ")
				node['location'] = new_info.lower()
				print(f"Changed 'Location' field\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '3':
				old_info = node['notes']
				new_info = input("Enter new note: ")
				node['notes'] = new_info.lower()
				print(f"Changed 'Notes' field\n"
						  f"From: '{old_info}'\n"
						  f"To: '{new_info}'\n")
				print(node)
			elif update == '4':
				print("Update canceled")
				break
	main_menu()
		
	
def print_formatted_list():
	"""prints to screen, a nicely formatted and numbered inventory list"""
	num = 1
	print("Inventory List\n")
	for entry in inv_list:
		print(f"{num} - - - - - - - - - - - - - - - - - ")
		for key, value in entry.items():
			print(f"\t{key.title()}: {value}")
		num += 1
	main_menu()
	

main_menu()



