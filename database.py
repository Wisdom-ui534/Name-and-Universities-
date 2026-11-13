import sqlite3

def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection



def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS Survey (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    University TEXT
    
    )
    
    
    
    """)

    


    connection.commit()
    connection.close()
    print("database created sucessfully")



init_db()