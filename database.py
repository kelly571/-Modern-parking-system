import sqlite3

DATABASE_PATH = "automated_garage.db"

def initialize_tables():
    connection = sqlite3.connect(DATABASE_PATH)
    db_cursor = connection.cursor()
    
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS live_garage (
        plate_id TEXT PRIMARY KEY,
        check_in_epoch TEXT NOT NULL
    )
    """)
    
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS billing_ledger (
        entry_index INTEGER PRIMARY KEY AUTOINCREMENT,
        plate_id TEXT NOT NULL,
        logged_hours INTEGER NOT NULL,
        settled_fee REAL NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()

def log_vehicle_check_in(plate_id, time_string):
    connection = sqlite3.connect(DATABASE_PATH)
    db_cursor = connection.cursor()
    try:
        db_cursor.execute("INSERT INTO live_garage VALUES (?, ?)", (plate_id, time_string))
        connection.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        connection.close()

def drop_active_and_archive(plate_id, target_hours, target_fee):
    connection = sqlite3.connect(DATABASE_PATH)
    db_cursor = connection.cursor()
    db_cursor.execute("DELETE FROM live_garage WHERE plate_id = ?", (plate_id,))
    db_cursor.execute("""
        INSERT INTO billing_ledger (plate_id, logged_hours, settled_fee) 
        VALUES (?, ?, ?)
    """, (plate_id, target_hours, target_fee))
    connection.commit()
    connection.close()
