import sqlite3

connection = sqlite3.connect("db.sqlite3")

cursor = connection.cursor()

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Sarmista', 'Sharma', 26, 'F', 10000)''')

connection.commit()

connection.close()