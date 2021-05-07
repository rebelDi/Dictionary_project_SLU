
#retrieve sentences based on the input word.
import psycopg2
import nltk.stem as stem



def main():
    #connection to database
    #conn_string = "host='localhost' dbname='postgres' user='postgres' password='Post$123'"
    conn_string = "dbname= 'postgres' user='sdadmin@postgre-psd' host='postgre-psd.postgres.database.azure.com' password='Post$123' port='5432' "
    print(conn_string)

    con = psycopg2.connect(conn_string)
    curs = con.cursor()
    ls = stem.LancasterStemmer()
    word = ls.stem("eyes")
    #executing the query for retrieval
    curs.execute(f"select sentence from english where word='{word}'")
    x= curs.fetchall()
    print(x)

main() # function call
