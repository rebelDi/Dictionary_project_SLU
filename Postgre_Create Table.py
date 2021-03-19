
#Creating tables in database.
import psycopg2



def main():
    #connecting to database
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='Post$123'"
    print("Opened database successfully")
    con = psycopg2.connect(conn_string)
    curs = con.cursor()

    #executing queries for creating tables for different languages.
    curs.execute('''CREATE TABLE ENGLISH(word  TEXT PRIMARY KEY NOT NULL, sentence TEXT  NOT NULL)''')
    curs.execute('''CREATE TABLE TURKISH(word  TEXT PRIMARY KEY NOT NULL, sentence TEXT  NOT NULL)''')
    curs.execute('''CREATE TABLE HINDI(word  TEXT PRIMARY KEY NOT NULL, sentence TEXT  NOT NULL)''')
    curs.execute('''CREATE TABLE RUSSIAN(word  TEXT PRIMARY KEY NOT NULL, sentence TEXT  NOT NULL)''')
    curs.execute('''CREATE TABLE UKRAINIAN(word  TEXT PRIMARY KEY NOT NULL, sentence TEXT  NOT NULL)''')

    con.commit() # to commit all changes into the db
    print("Tables created successfully")
    con.close()


main() #function call