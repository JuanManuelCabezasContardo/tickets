import sqlite3


def connect():
    try:
        conn = sqlite3.connect('src/tickets.db')
    except e:
        print(e)
        return 0
    return conn

def db_insert(insert_query: str):
    try:
        conn = connect()
        conn.execute(insert_query)
        conn.commit()
        conn.close()
    except:
        return 0
    return 1

def db_select(query: str):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        cursor= cur.fetchall()
        conn.close()
    except e:
        print(e)
        cursor= []
    return cursor

def db_backup():
    return 1

def db_delete():
    return 1

def create_tables():
    try:
        conn = connect()
        conn.execute('''CREATE TABLE TICKET(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name    TEXT    NOT NULL,token    TEXT    NOT NULL,status    TEXT    NOT NULL);''')
        conn.close()
    except e:
        print(e)

