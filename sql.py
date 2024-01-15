import sqlite3 #By default come along with python setup

#Connection to Sqlite database
connection = sqlite3.connect('student.db')

#Creating cursor object
cursor = connection.cursor()

#Creating a table
table = """
    CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255), MARKS INT);
"""
cursor.execute(table)

#Insering records
cursor.execute("""INSERT INTO STUDENT VALUES('Poorna', 'Data Science', 'A', 82)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Rishi', 'MLOPS', 'A', 72)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Akash', 'Data Science', 'B', 97)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Barat', 'Data Science', 'B', 99)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Prabhu', 'MLOPS', 'C', 95)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Vishnu', 'Data Science', 'C', 92)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Sudhan', 'Data Science', 'D', 98)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Kamal', 'MLOPS', 'D', 96)""")
print("Data inserted successfully")
data = cursor.execute(""" SELECT * FROM STUDENT """)

for row in data:
    print(row)

# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()
