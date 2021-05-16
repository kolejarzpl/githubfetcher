def drop_table(table_name):
    conn = sqlite3.connect(database)

    db = conn.cursor()
    sql = "DROP TABLE " + table_name
    db.execute(sql)
    conn.commit()
    conn.close()
    print(f"Table " + table_name + " dropped")
