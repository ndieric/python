import sqlite3
from sqlite3.dbapi2 import Cursor
con   = sqlite3.connect("base.db")
Cursor = con.cursor()
myone=("bwayaze ")
cursor.execute('select * from elve where nom_elve =', myone)
con.close()
