import csv
import sqlite3

conn = sqlite3.connect("luffy.db")
c = conn.cursor()


#Create tables for app (if they don't exist)
"""query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
c.execute(query)"""

#For adding app to database
"""query = "INSERT INTO sys_command VALUES (null,'discord', 'C:\\Users\\prade\\Desktop\\Discord.lnk')"
c.execute(query)
conn.commit()
"""
#Create tables for web (if they don't exist)
"""query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
c.execute(query)"""

#For adding web command to database
"""query = "INSERT INTO web_command VALUES (null,'whatsapp', 'https://web.whatsapp.com/')"
c.execute(query)
conn.commit()
"""

# For app commands
# This line ensures the table exists so you don't get the "no such table" error
"""c.execute('''CREATE TABLE IF NOT EXISTS sys_command
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT, 
              path TEXT)''')

# Now you can safely run your other commands
query = "DELETE FROM sys_command WHERE name = 'discord'"
c.execute(query)

conn.commit()
conn.close()"""

#For web commands
"""# This line ensures the table exists so you don't get the "no such table" error
c.execute('''CREATE TABLE IF NOT EXISTS sys_command
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT, 
              path TEXT)''')

# Now you can safely run your other commands
query = "DELETE FROM web_command WHERE name = 'youtube'"
c.execute(query)

conn.commit()
conn.close()"""


"""app= "discord"
c.execute("SELECT path FROM sys_command WHERE name IN (?)", (app,))
result = c.fetchall()
print(result[0][0])"""


# Create a table with the desired columns
# c.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


#### 3. Import CSV file into database

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
"""desired_columns_indices = [0, 18]

# Read data from CSV and insert into SQLite table for the desired columns
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = []
        for i in desired_columns_indices:
            selected_data.append(row[i])

        c.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
conn.commit()
conn.close()
"""
#For one by one adding contact
"""q= "INSERT INTO contacts VALUES (null, 'Muskan', '+14169910024', null)"
c.execute(q)
conn.commit()"""


#### 5. Search Contacts from database

"""query = 'Muskan'
query = query.strip().lower()

c.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = c.fetchall()
print(results[0][0])"""



