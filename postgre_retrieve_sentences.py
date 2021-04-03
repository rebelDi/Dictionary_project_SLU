
#retrieve sentences based on the input word.
import psycopg2



def main():
    #connection to database
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='Post$123'"
    #print(conn_string)

    con = psycopg2.connect(conn_string)
    curs = con.cursor()
    a = 'recommend' #input the required word
    #executing the query for retrieval
    curs.execute(f"select sentence from english where word='{a}'")
    x= curs.fetchall()
    print(x)



main() # function call
