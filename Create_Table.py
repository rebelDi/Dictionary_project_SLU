import mysql.connector as sql_connector

mydb  = sql_connector.connect(
    host= "localhost",
    user = "saisriraj123",
    password = "Sql@12345",
    database = "English"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE table1 (id INT AUTO_INCREMENT PRIMARY KEY, sentence VARCHAR (255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)