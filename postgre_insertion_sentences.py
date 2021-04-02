import psycopg2


def insert_sentences(word, sentences):
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='Post$123'"

    con = psycopg2.connect(conn_string)
    curs = con.cursor()


    for sentence in sentences:
        curs.execute(f"INSERT INTO english (word, sentence) values ('{word}','{sentence}') ")
    con.commit()
    x = "commited row successfully"
    curs.close()
    con.close()


    return x
