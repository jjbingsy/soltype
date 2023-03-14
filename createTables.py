import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('films.db')
c = conn.cursor()

# Create the Films table
c.execute('''CREATE TABLE Films
             (film TEXT PRIMARY KEY, description TEXT, idol_count INTEGER default 0)''')

# Create the Idols table
c.execute('''CREATE TABLE Idols
             (idol_id INTEGER PRIMARY KEY,
              idol TEXT,
              source INTEGER,
              name TEXT,
              UNIQUE (idol, source))''')

# Create the Film_Idol table
c.execute('''CREATE TABLE Film_Idol
             (film TEXT,
              idol_id INTEGER,
              source INTEGER,
              PRIMARY KEY (film, idol_id),
              FOREIGN KEY (film) REFERENCES Films(film),
              FOREIGN KEY (idol_id, source) REFERENCES Idols(idol_id, source))''')

c.execute('''CREATE TABLE Idol_Idol
             (idol_id1 INTEGER,
              idol_id2 INTEGER,
              PRIMARY KEY (idol_id1, idol_id2),
              FOREIGN KEY (idol_id1) REFERENCES Idols(idol_id),
              FOREIGN KEY (idol_id2) REFERENCES Idols(idol_id)
              
              )''')




# Commit the changes and close the connection
conn.commit()
conn.close()
