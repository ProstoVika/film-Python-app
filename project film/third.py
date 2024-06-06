import sqlite3

def create_db():
    con = sqlite3.connect('filmflix.db')
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tblfilms (
        filmID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        yearReleased INTEGER NOT NULL,
        rating TEXT NOT NULL,
        duration INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
    ''')
    con.commit()
    # con.close()

create_db()