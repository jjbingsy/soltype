import sqlite3
from msoup2 import get_secondsource 
cnn = sqlite3.connect('films.db')
c = cnn.cursor()

# Execute the SQL query to get all film and idol_id pairs
c.execute("SELECT Film_Idol.film, Film_Idol.idol_id FROM Film_Idol INNER JOIN Films ON Film_Idol.film = Films.film WHERE Films.idol_count = 1")

# Fetch all the rows from the query result
rows = c.fetchall()

# Loop through the rows and print the results
for row in rows:
    film = row[0]
    idol_id = row[1]
    #print(film, idol_id)
    c.execute("SELECT idol_id2 FROM Idol_Idol WHERE idol_id1 = ?", (idol_id,))


    idol_id2 = c.fetchone()
    if idol_id2 is None:
        new_idol = get_secondsource (film)
        if new_idol is not None:
            print (new_idol[0], new_idol[1] )
            c.execute("INSERT or ignore INTO Idols (idol, name, source) VALUES (?, ?, 2)", (new_idol[0], new_idol[1]))
            cnn.commit()

            c.execute("""
                INSERT or ignore INTO Idol_Idol (idol_id1, idol_id2)
                SELECT ?, idol_id
                FROM Idols i1
                WHERE i1.idol = ?
                """, (idol_id, new_idol[0]))
            cnn.commit()
            
# Loop through the rows and print the idol_id2 values
cnn.close()


