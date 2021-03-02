import mysql.connector as sql_connector

mydb  = sql_connector.connect(
    host= "localhost",
    user = "saisriraj123",
    password = "Sql@12345"
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE English')

mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)
