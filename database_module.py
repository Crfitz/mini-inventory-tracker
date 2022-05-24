# main program: inventory_tracker.py
# this module handles the database;
# checking for db file, creates one if none found, reads and writes to file
import json

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
			print("Database created!")
	else:
		print("Database ready...")
		inv_list = data


def write(data):
	"""Writes the inventory list to json file; inventory_db.json"""
	with open(database, 'w') as db:
		json.dump(data, db, indent=2)
		print("\nWriting to database...")


def read():
	"""Loads inventory list from json file (inventory_db.json) into python object"""
#	database = 'inventory_db.json'
	with open(database, 'r') as db:
		data = json.load(db)
	return data