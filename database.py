import sqlite3

# Initialize the Police Department database and create cursor to be able to interact with it
police = sqlite3.connect('police_depts.db')
pcursor = police.cursor()

# Create the police department table in the database
pcursor.execute('''
    CREATE TABLE IF NOT EXIST police_departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
    )
''')

# Collection of 55 police departments in Rhode Island to be inserted into the database
police_data = [
    (1, 'North Kingstown PD', '8166 Post Rd, North Kingstown, RI 02852'),
    (2, 'East Providence PD', '750 Waterman Ave, East Providence, RI 02914'),
    (3, 'Providence PD', '325 Washington St, Providence, RI 02903'),
    (4, 'Warwick PD', '99 Veterans Memorial Dr, Warwick, RI 02886'),
    (5, 'Cranston PD', '5 Garfield Ave, Cranston, RI 02920'),
    (6, 'Pawtucket PD', '121 Roosevelt Ave, Pawtucket, RI 02860'),
    (7, 'Woonsocket PD', '242 Clinton St, Woonsocket, RI 02895'),
    (8, 'Newport PD', '120 Broadway, Newport, RI 02840'),
    (9, 'Central Falls PD', '160 Illinois St, Central Falls, RI 02863'),
    (10, 'Barrington PD', '100 Federal Rd, Barrington, RI 02806'),
    (11, 'Bristol PD', '395 Metacom Ave, Bristol, RI 02809'),
    (12, 'Burrillville PD', '1477 Victory Hwy, Oakland, RI 02858'),
    (13, 'Charlestown PD', '4901 Old Post Rd, Charlestown, RI 02813'),
    (14, 'Coventry PD', '1075 Main St, Coventry, RI 02816'),
    (15, 'Cumberland PD', '1380 Diamond Hill Rd, Cumberland, RI 02864'),
    (16, 'East Greenwich PD', '176 First Ave, East Greenwich, RI 02818'),
    (17, 'Exeter PD', '675 Ten Rod Rd, Exeter, RI 02822'),
    (18, 'Foster PD', '182 Howard Hill Rd, Foster, RI 02825'),
    (19, 'Glocester PD', '162 Chopmist Hill Rd, Chepachet, RI 02814'),
    (20, 'Hopkinton PD', '406 Woodville Rd, Hopkinton, RI 02833'),
    (21, 'Jamestown PD', '250 Conanicus Ave, Jamestown, RI 02835'),
    (22, 'Johnston PD', '1651 Atwood Ave, Johnston, RI 02919'),
    (23, 'Lincoln PD', '100 Old River Rd, Lincoln, RI 02865'),
    (24, 'Little Compton PD', '60 Simmons Rd, Little Compton, RI 02837'),
    (25, 'Middletown PD', '123 Valley Rd, Middletown, RI 02842'),
    (26, 'Narragansett PD', '40 Caswell St, Narragansett, RI 02882'),
    (27, 'New Shoreham PD', '16 Old Town Rd, Block Island, RI 02807'),
    (28, 'North Providence PD', '1967 Mineral Spring Ave, North Providence, RI 02911'),
    (29, 'North Smithfield PD', '575 Smithfield Rd, North Smithfield, RI 02896'),
    (30, 'Portsmouth PD', '2270 E Main Rd, Portsmouth, RI 02871'),
    (31, 'Richmond PD', '1168 Main St, Wyoming, RI 02898'),
    (32, 'Scituate PD', '116 Main St, Hope, RI 02831'),
    (33, 'Smithfield PD', '215 Pleasant View Ave, Smithfield, RI 02917'),
    (34, 'South Kingstown PD', '1790 Kingstown Rd, South Kingstown, RI 02879'),
    (35, 'Tiverton PD', '20 Industrial Way, Tiverton, RI 02878'),
    (36, 'Warren PD', '1 Joyce St, Warren, RI 02885'),
    (37, 'West Greenwich PD', '280 Victory Hwy, West Greenwich, RI 02817'),
    (38, 'West Warwick PD', '1162 Main St, West Warwick, RI 02893'),
    (39, 'Westerly PD', '60 Airport Rd, Westerly, RI 02891'),
    (40, 'State Police', '311 Danielson Pike, North Scituate, RI 02857'),
    (41, 'Rhode Island Capitol Police', '82 Smith St, Providence, RI 02903'),
    (42, 'Rhode Island College PD', '600 Mount Pleasant Ave, Providence, RI 02908'),
    (43, 'Rhode Island School of Design PD', '15 Westminster St, Providence, RI 02903'),
    (44, 'Rhode Island Hospital PD', '593 Eddy St, Providence, RI 02903'),
    (45, 'Rhode Island State Fire Marshal', '560 Jefferson Blvd, Warwick, RI 02886'),
    (46, 'Rhode Island State Police', '311 Danielson Pike, North Scituate, RI 02857'),
    (47, 'Rhode Island State Police - Wickford Barracks', '7875 Post Rd, North Kingstown, RI 02852'),
    (48, 'Rhode Island State Police - Hope Valley Barracks', '54 Nooseneck Hill Rd, West Greenwich, RI 02817'),
    (49, 'Rhode Island State Police - Lincoln Woods Barracks', '1575 Louisquisset Pike, Lincoln, RI 02865'),
    (50, 'Rhode Island State Police - Portsmouth Barracks', '838 E Main Rd, Portsmouth, RI 02871'),
    (51, 'University of Rhode Island PD', '85 Lower College Rd, Kingston, RI 02881'),
    (52, 'Brown University PD', '75 Charlesfield St, Providence, RI 02912'),
    (53, 'Bryant University PD', '1150 Douglas Pike, Smithfield, RI 02917'),
    (54, 'Community College of Rhode Island PD', '400 East Ave, Warwick, RI 02886'),
    (55, 'Providence College PD', '1 Cunningham Square, Providence, RI 02918'),
]

# Insert the police department data into the database
pcursor.execute('''
    INSERT INTO police_departments (id, name, address)
    VALUES (?, ?, ?)
''', police_data)

# Initialize the Fire Department database and create cursor to be able to interact with it
fireRescue = sqlite3.connect('fire_depts.db')
fcursor = fireRescue.cursor()

# Create the fire department table in the database
fcursor.execute('''
    CREATE TABLE IF NOT EXIST fire_departments (
        id INTEGER PRIMARY KEY
        name TEXT NOT NULL
        address TEXT NOT NULL
    )
''')

# Collection of 39 fire departments in Rhode Island to be inserted into the database
fire_data = [
    (1, 'North Kingstown FD', '8156 Post Rd, North Kingstown, RI 02852'),
    (2, 'East Providence FD', '913 Broadway, East Providence, RI 02914'),
    (3, 'Providence FD', '799 Valley St, Providence, RI 02908'),
    (4, 'Warwick FD', '111 Veterans Memorial Dr, Warwick, RI 02886'),
    (5, 'Cranston FD', '301 Pontiac Ave, Cranston, RI 02910'),
    (6, 'Pawtucket FD', '33 Broadway, Pawtucket, RI 02860'),
    (7, 'Woonsocket FD', '111 Main St, Woonsocket, RI 02895'),
    (8, 'Newport FD', '21 W Marlborough St, Newport, RI 02840'),
    (9, 'Central Falls FD', '575 Dexter St, Central Falls, RI 02863'),
    (10, 'Barrington FD', '100 Federal Rd, Barrington, RI 02806'),
    (11, 'Bristol FD', '4 Annawamscutt Dr, Bristol, RI 02809'),
    (12, 'Burrillville FD', '105 Harrisville Main St, Harrisville, RI 02830'),
    (13, 'Charlestown FD', '50 Old Post Rd, Charlestown, RI 02813'),
    (14, 'Coventry FD', '1675 Flat River Rd, Coventry, RI 02816'),
    (15, 'Cumberland FD', '1379 Diamond Hill Rd, Cumberland, RI 02864'),
    (16, 'East Greenwich FD', '284 Main St, East Greenwich, RI 02818'),
    (17, 'Exeter FD', '305 Nooseneck Hill Rd, West Greenwich, RI 02817'),
    (18, 'Foster FD', '1 Foster Center Rd, Foster, RI 02825'),
    (19, 'Glocester FD', '117 Chestnut Hill Rd, Chepachet, RI 02814'),
    (20, 'Hopkinton FD', '104 Nooseneck Hill Rd, West Greenwich, RI 02817'),
    (21, 'Jamestown FD', '50 Narragansett Ave W, Jamestown, RI 02835'),
    (22, 'Johnston FD', '1520 Atwood Ave, Johnston, RI 02919'),
    (23, 'Lincoln FD', '622 George Washington Hwy, Lincoln, RI 02865'),
    (24, 'Little Compton FD', '60 Simmons Rd, Little Compton, RI 02837'),
    (25, 'Middletown FD', '239 Wyatt Rd, Middletown, RI 02842'),
    (26, 'Narragansett FD', '230 Old Ferry Rd, Narragansett, RI 02882'),
    (27, 'New Shoreham FD', '15 Ocean Ave, Block Island, RI 02807'),
    (28, 'North Providence FD', '2000 Mineral Spring Ave, North Providence, RI 02911'),
    (29, 'North Smithfield FD', '1 Main St, Slatersville, RI 02876'),
    (30, 'Portsmouth FD', '2300 E Main Rd, Portsmouth, RI 02871'),
    (31, 'Richmond FD', '1168 Main St, Wyoming, RI 02898'),
    (32, 'Scituate FD', '384 Hartford Pike, North Scituate, RI 02857'),
    (33, 'Smithfield FD', '3 Pleasant View Ave, Greenville, RI 02828'),
    (34, 'South Kingstown FD', '334 Succotash Rd, Wakefield, RI 02879'),
    (35, 'Tiverton FD', '87 Crandall Rd, Tiverton, RI 02878'),
    (36, 'Warren FD', '1 Joyce St, Warren, RI 02885'),
    (37, 'West Greenwich FD', '830 Nooseneck Hill Rd, West Greenwich, RI 02817'),
    (38, 'West Warwick FD', '1170 Main St, West Warwick, RI 02893'),
    (39, 'Westerly FD', '180 Beach St, Westerly, RI 02891'),
]

# Commit changes and close databases
police.commit()
police.close()

fireRescue.commit()
fireRescue.close()