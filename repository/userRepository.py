import sqlite3
from utils.constans import database

# todo we will be working on database during all operations, there
# should be open connection in main class and somehow repos and everything should operate on this to
# avoid opening and closing this everytime

def initiate_db():
    conn = sqlite3.connect(database)

    db = conn.cursor()
    db.execute('DROP TABLE IF EXISTS users')
    db.execute("""
    CREATE TABLE IF NOT EXISTS users ( 
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
                repos_url text,
                events_url text,
                received_events_url text,
                type text,
                site_admin text,
                name text,
                company text,
                blog text,
                location text,
                email text ,
                hireable text,
                bio text,
                twitter_username text,
                public_repos integer,
                public_gists integer,
                followers integer,
                following integer,
                created_at text,
                updated_at text)
                     """)
    print(f"Table users is created")

    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect(database)
    db = conn.cursor()
    db.execute("""SELECT * FROM users""")
    return db.fetchall()


def get_user_by_name(name):
    conn = sqlite3.connect(database)

    sql = """SELECT * FROM users WHERE login = ?"""

    db = conn.cursor()
    db.execute(sql, (name,))
    return db.fetchall()

def save_users(user_resp):
    conn = sqlite3.connect(database)

    initiate_db()
    sql = """ INSERT INTO users(
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
                repos_url,
                events_url,
                received_events_url,
                type,
                site_admin,
                name,
                company,
                blog,
                location,
                email ,
                hireable,
                bio,
                twitter_username,
                public_repos,
                public_gists,
                followers,
                following,
                created_at,
                updated_at) VALUES (
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
                :repos_url,
                :events_url,
                :received_events_url,
                :type,
                :site_admin,
                :name,
                :company,
                :blog,
                :location,
                :email,
                :hireable,
                :bio,
                :twitter_username,
                :public_repos,
                :public_gists,
                :followers,
                :following,
                :created_at,
                :updated_at)
                     """


    db = conn.cursor()
    db.execute(sql, user_resp)
    conn.commit()
    conn.close()
