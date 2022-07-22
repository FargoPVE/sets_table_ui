import sqlite3


class Connection:
    db = sqlite3.connect(database='table_db12')
    cur = db.cursor()