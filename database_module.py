# main program: inventory_tracker.py
# this module handles the database;
# checking for db file, creates one if none found, reads and writes to file
import json
import csv
import ast

database = 'inventory_db.json'

def db_check():
	"""Checks for json file. Creates one  and initializes inv_list, if none."""
#	database = 'inventory_db.json'
	try:
		with open(database) as db:
			data = json.load(db)
	except FileNotFoundError:
		with open(database, 'w') as db:
			inv_list = []
			json.dump(inv_list, db)
			print("Database created!\n")
	else:
		print("Database ready...\n")
		inv_list = data


def write(data):
	"""Writes the inventory list to json file; inventory_db.json"""
	with open(database, 'w') as db:
		json.dump(data, db, indent=2)
		print("\nWriting to database...")


def read():
	"""Loads inventory list from json file (inventory_db.json) into python object"""
	with open(database, 'r') as db:
		data = json.load(db)
	return data


def export(x):
	"""exports inventory to a csv file"""
	header = ['created', 'item', 'location', 'note', 'tags', 'modified']
	new_dict = x
	print(f"New_dict: {new_dict}")
	print(f"x = {new_dict}")
	new_path = open("test_invlist3.csv", "w")
	new_dict = read()
	z = csv.writer(new_path)
	z.writerow(header)
	for node in new_dict:
		values = node.values()
		z.writerow(values) 
	new_path.close()

