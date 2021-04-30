
#retrieve sentences based on the input word.
import psycopg2



def main(word):
    #connection to database
    conn_string = "host='198.7.58.147' port='5432' dbname='postgres' user='postgres' password='Post$123'"
    # print(conn_string)

    con = psycopg2.connect(conn_string)
    print(con)
    curs = con.cursor()
    
    #executing the query for retrieval
    curs.execute(f"select sentence from english where word='{word}'")
    x= curs.fetchall()
    print(x)
    return x



main('sink') # function call
