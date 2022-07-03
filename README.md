
Screenshot_20220702-212026_Pydroid 3.jpg

# mini-inventory-tracker
Just a small inventory program. I'm very new to python and thought this would be a fun little project.  My inspiration for this started with "where the hell did I put that thing?" Lol. But this could be used for many inventory and location-tracking purposes. Or "I put that thing somewhere so the kids couldn't mess with it and now i can't remember where I put it..."-type purposes.

Files / purposes:
  
  inventory_tracker.py
    - This is the main program to run
  
  inventory_functions.py
    - Contains most functions
  
  database_module.py
    - This contains the functions dealing with the creating, reading and writing to the json file that contains the inventory data
  
  export.py
    - This contains the export functionality; exports to a csv file to save, print, etc.
    I may be moving this part into the database_module.py
    
As mentioned above, the inventory data resides in a json file; if no file found, it creates and writes to inventory_db.json. Creates it in the same dir as the main program.
