import psycopg2



def insert_sentences(word, sentences):
    conn_string = "dbname= 'postgres' user='sdadmin@postgre-psd' host='postgre-psd.postgres.database.azure.com' password='Post$123' port='5432' "

    con = psycopg2.connect(conn_string)
    curs = con.cursor()


    for sentence in sentences:
        curs.execute(f"INSERT INTO english (word, sentence) values ('{word}','{sentence}') ")
    con.commit()
    x = "commited row successfully"
    curs.close()
    con.close()


    return x
