# main program
# 06.13.2022
import inventory_functions as funcs
import database_module as db

database = 'inventory_db.json'
version = '1.32'

data = ' '
item = ' '
location = ' '
node = ' '
print("\nInventory Tracker\n"
	  f"Version {version}\n")
print("Fitzie Enterprises, LLC.\n"
"Copyright 2022; All rights reserved\n")

db.db_check()

print("Enter 'h' for HELP")
print("Enter 'q' to QUIT")

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

funcs.main_menu()


funcs.main_menu()