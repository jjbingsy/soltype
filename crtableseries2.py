import sqlite3

conn = sqlite3.connect("series2.db")
cursor = conn.cursor()

# Create the Series table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Series (
    Name TEXT primary key,
    Short TEXT
)
""")


# Create the Films table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Films (
    Film TEXT Primary key,
    Series_Name Text,
    FOREIGN KEY (Series_Name) REFERENCES Series(name)
)
""")


conn.commit()
conn.close()
