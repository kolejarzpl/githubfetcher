# w plikach typu repository, przechowuje sie metody i zapytania czysto odpowiedzialne za CRUD zapytan bazodanowych

import sqlite3


# todo we will be working on database during all operations, there
# should be open connection in main class and somehow repos and everything should operate on this to
# avoid opening and closing this everytime

def initiate_db():
    conn = sqlite3.connect('database/gitfetcherdb.db')

    db = conn.cursor()

    db.execute("""CREATE TABLE contributors ( 
                login text,
                id integer,
                node_id text,
                avatar_url text,
                gravatar_id text,
                url text,
                html_url text,
                followers_url text,
                following_url text,
                gists_url text,
                starred_url text,
                subscriptions_url text,
                organizations_url text,
                received_events_url text,
                repos_url text,
                events_url text,
                type text,
                site_admin text,
                contributions integer)""")

    # todo temporary to delete
    db.execute(
        """INSERT INTO contributors VALUES ('Pawel', 123, '', '','','','','','','','','','','','','','','','')""")

    conn.commit()
    conn.close()


def get_all_contributors():
    conn = sqlite3.connect('database/gitfetcherdb.db')

    db = conn.cursor()
    db.execute("""SELECT * FROM contributors""")
    return db.fetchall()
    conn.commit()
    conn.close()


# todo temporary to delete?
def drop_table():
    conn = sqlite3.connect('database/gitfetcherdb.db')

    db = conn.cursor()
    db.execute("""DROP TABLE contributors""")
    conn.commit()
    conn.close()
