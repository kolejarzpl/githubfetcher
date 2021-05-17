import sqlite3
from utils.constans import database

# todo we will be working on database during all operations, there
# should be open connection in main class and somehow repos and everything should operate on this to
# avoid opening and closing this everytime

def initiate_db():
    conn = sqlite3.connect(database)

    db = conn.cursor()
    db.execute('DROP TABLE IF EXISTS contributors')
    db.execute("""
    CREATE TABLE IF NOT EXISTS contributors ( 
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
                contributions integer)
                     """)
    print(f"Table contributors created")

    conn.commit()
    conn.close()


def get_all_contributors():
    conn = sqlite3.connect(database)
    db = conn.cursor()
    db.execute("""SELECT * FROM contributors""")
    return db.fetchall()


def get_contributor_by_name(name):
    conn = sqlite3.connect(database)

    sql = """SELECT * FROM contributors WHERE login = ?"""

    db = conn.cursor()
    db.execute(sql, (name,))
    return db.fetchall()

def save_contributors(resp):
    conn = sqlite3.connect(database)

    initiate_db()
    sql = """ INSERT INTO contributors(
                login,
                id,
                node_id,
                avatar_url,
                gravatar_id,
                url,
                html_url,
                followers_url,
                following_url,
                gists_url,
                starred_url,
                subscriptions_url,
                organizations_url,
                received_events_url,
                repos_url,
                events_url,
                type,
                site_admin,
                contributions) VALUES (
                :login,
                :id,
                :node_id,
                :avatar_url,
                :gravatar_id,
                :url,
                :html_url,
                :followers_url,
                :following_url,
                :gists_url,
                :starred_url,
                :subscriptions_url,
                :organizations_url,
                :received_events_url,
                :repos_url,
                :events_url,
                :type,
                :site_admin,
                :contributions)
                     """

    for contributor in resp:
        db = conn.cursor()
        db.execute(sql, contributor)
        conn.commit()

    conn.close()
