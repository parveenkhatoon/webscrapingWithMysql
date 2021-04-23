
import mysql.connector #importing the mysql.connector....

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9958975092",
  database="assimgment1"

)
mycursor = mydb.cursor()  #connecting with mysql database....
print(mydb)

mycursor.execute("CREATE DATABASE assimgment1") 
print("Databases is connected successfully")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

 
mycursor.execute("CREATE TABLE Data(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), paragraph TEXT NOT NULL)")
print("Table is created successfully")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)


file1 = open('readme.txt',"r") #Opning and reading the text file in which we have stored are scrape data..
file_content = file1.read() 
# print(file_content)


query = "INSERT INTO Data(name, paragraph) VALUES ('thoery', %s)"
mycursor.execute(query, (file_content,))

sql = "select * from Data"
mycursor.execute(sql)

get all records
records = mycursor.fetchall()
print("Total number of rows in table: ", mycursor.rowcount) #this line for showing how many rows in this table...
for row in records:
  print("Id = ", row[0], )
  print("Name = ", row[1])
  print("Paragraph  = ", row[2], "\n")

mydb.close() #closing the mysql connector after the completing all task
