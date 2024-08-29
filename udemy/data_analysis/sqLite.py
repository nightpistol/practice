# import sqlite first in terminal
import sqlite3

# create and connect to sqlite dtaabase
connection = sqlite3.connect('example.db')
connection

cursor = connection.cursor()

#create a table
cursor.execute('''

create table if not exists employees(
               id Integer Primary Key,
               name Text not null,
               age Integer,
               department Text
               )

''')
connection.commit()

#inserting the data
cursor.execute('''

insert into employees(name,age,department)
               values('saqlain',24,'data science')

''')
cursor.execute('''

insert into employees(name,age,department)
               values('sravvu',32,'automation')

''')
connection.commit()

#updating the rows
cursor.execute('''

update employees
               set age = 34
               where name = 'sravvu'

''')
connection.commit()

#deleteing the data
cursor.execute('''

delete from employees
               where name = 'saqlain'
''')
connection.commit()

#query the data from the table
cursor.execute('select * from employees')
rows = cursor.fetchall()
#printing the queried rows
for row in rows:
  print(row)

connection.close()
