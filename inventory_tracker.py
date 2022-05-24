import inventory_functions as funcs
import database_module as db
#from inventory_functions import add_node
import json
import time

database = 'inventory_db.json'
version = '1.2'

#database = ' '
data = ' '
item = ' '
location = ' '
node = ' '
print("Inventory Tracker\n"
	  f"Version {version}\n")
print("Fitzie Enterprises, LLC.\n"
"Copyright 2022; All rights reserved\n")

current_time = time.ctime()

"""
username = ' '
print("Enter your name to create and load database\n"
	"*Note: Your name identifies which database to load*\n")
username = input("Enter name: ")

def db_create_load(username):
	database = f'inventory_db_{username.lower()}.json'

db_create_load(username)
print(f"{database}")
"""


db.db_check()

funcs.main_menu()


funcs.main_menu()