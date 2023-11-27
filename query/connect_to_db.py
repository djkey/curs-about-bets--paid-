import sqlite3

def query(str: str):
    db = sqlite3.connect('db/curs.db')
    curs = db.cursor()
    curs.execute(str)
    ans = curs.fetchall()
    db.commit()
    db.close()
    return ans

