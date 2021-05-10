
#retrieve sentences based on the input word.
import psycopg2
import nltk.stem as stem



def main(word,language):
    #connection to database
    conn_string = "dbname= 'postgres' user='sdadmin@postgre-psd' host='postgre-psd.postgres.database.azure.com' password='Post$123' port='5432' "
    #print(conn_string)

    con = psycopg2.connect(conn_string)
    curs = con.cursor()
    
    #word = ls.stem("eyes")
    #word = "банковский"
    #language = "russian"
    #executing the query for retrieval
    if language == "english":
        ls = stem.LancasterStemmer()
        word = ls.stem(word)
        curs.execute(f"select sentence from {language} where word='{word}'")
        x= curs.fetchall()
        return x
    if language == "russian":
        curs.execute(f"select sentence from {language} where word='{word}'")
        x = curs.fetchall()
        return x
        

#main() # function call
