import sqlite3

conn = sqlite3.connect("series.db")
cursor = conn.cursor()

# Create the Series table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Series_Name TEXT NOT NULL,
    Short_Name TEXT NOT NULL
)
""")

# Create the Films table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Film TEXT NOT NULL,
    Series_Name_id INTEGER,
    FOREIGN KEY (Series_Name_id) REFERENCES Series(id)
)
""")

conn.commit()
conn.close()
