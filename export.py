# for main program: inventory_tracker.py
# 06.13.2022

import csv
import database_module as db
import ast
import time

current_time = time.ctime()

def exportdb(x):
	"""exports inventory to a csv file"""
	print("Filename: 'inventory_list.csv'")
	print("Located in the same directory as this program.\n")
	header = ['created', 'item', 'location', 'note', 'tags', 'modified']
	#pulls in json db and sorts based on item name
	exp_list = db.read()
	sorted_inv_list = sorted(exp_list, key=lambda d: d['item'])
	
	#open csv in write mode
	with open('inventory_list.csv', 'w',newline='') as f:
		#converts str back to dict
		ast_exp_list = ast.literal_eval(f"{sorted_inv_list}")

		writer = csv.DictWriter(f, fieldnames=header)
		writer.writeheader()
		writer.writerows(ast_exp_list)
	
"""
	new_dict = x
	print(f"New_dict: {new_dict}")
	print(f"x = {new_dict}")
	new_path = open("test_invlist3.csv", "w")
	z = csv.DictWriter(new_path, fieldnames = header)
#	z.writerow(header)
	print(f"{new_dict}")
	for node in new_dict:
		print(type(node))
		pause = input("pausing")
		values = node.values()
		z.writerow(values) 
	new_path.close()
"""
#	new_dict = dict(new_dict)
#	keys = new_dict[0].keys()

	#new_dict = [
#	{'item':'bike', 'location':'carport', 'notes':'huffy mountain bike'},
#	{'item':'phone', 'location':'table', 'notes':'none'},
#	{'item':'keys', 'location':'key hooks', 'notes':'truck'},
#	{'item':'python book', 'location':'nightstand', 'notes':'Between n/s and bed'},
#	{'item':'cd case', 'location':'master closet', 'notes':'back top left'},
#	{'item':'watch', 'location':'dresser', 'notes':'none'},
#	{'item':'thing', 'location':'dresser', 'notes':'none'}
#	]
#	with open('test_invlist.csv', 'w', encoding='UTF8') as f: 
#		writer = csv.DictWriter(f, fieldnames=header)
	# write the header 
		#writer.writeheader() 
#		writer.writeheader()
	# write the data 
#	for node in rows:
#		writer.writerows(new_dict)
"""
	try:
		with open('test_invlist3.csv', 'w',newline='') as f:
			ast_new_dict = ast.literal_eval(new_dict)
			print(ast_new_dict)
			writer = csv.DictWriter(f, fieldnames=header)
			writer.writeheader()
#			for key, val in new_dict.items():
			writer.writerows(ast_new_dict)
	except IOError:
		print("***I/O ERROR***")
	#except ValueError:
#		print("Value error...")
"""

#new_path = open("test_invlist3.csv", "w")
#file_dictionary = read()
#z = csv.writer(new_path)
#for node in file_dictionary:
#	for k in node.keys(): 
#		z.writerow(k) 

#	new_path.close()