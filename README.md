

# Inventory Tracker
A repository to help you keep track of where you store your items.

## Getting Started
### Dependencies
* sys
* datetime
* csv
* ast
* time
* json
### Installing
* Git clone repository
### Executing Program
Store all files of this repository in a single directory. Then execute inventor_tracker.py to use the program.


### Notes
Files / purposes:
* inventory_tracker.py: This is the main program to run
  
* inventory_functions.py: Contains most functions
  
* database_module.py: This contains the functions dealing with the creating, reading and writing to the json file that contains the inventory data
  
* export.py: This contains the export functionality; exports to a csv file to save, print, etc.
             (I may be moving this part into the database_module.py)
    
As mentioned above, the inventory data resides in a json file; if no file found, it creates and writes to inventory_db.json. Creates it in the same dir as the main program.


## Author
Crfitz

Also, a big thanks to shivang-b for contributing to the readme.md.  A great improvement! 
