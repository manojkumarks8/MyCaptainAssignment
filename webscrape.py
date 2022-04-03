import sqlite3


def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute(" CREATE TABLE IF NOT EXISTS MAGIC_BRICKS (NAME TEXT, TYPE TEXT)")
    print("Table created successfully")
    conn.close()


def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO MAGIC_BRICKS (NAME , TYPE) VALUES (?, ?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()


def get_flat_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM MAGIC_BRICKS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()