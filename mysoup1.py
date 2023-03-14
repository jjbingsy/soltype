import sqlite3
from bs4 import BeautifulSoup

# Connect to the database
conn = sqlite3.connect('tinventory.db')
cnn = sqlite3.connect('films.db')
c = conn.cursor()
c2 = cnn.cursor()

# Select all rows with "film" and "html1" from the videos table
c.execute("SELECT film, html2 FROM videos where html2 != ''")

# Loop through the rows and extract the html1 text
for row in c.fetchall():
    film_name = row[0]  # assuming the html1 column is the third one
    html = row[1]
    # Use BeautifulSoup to prettify the HTML
    msoup = BeautifulSoup(html, 'lxml')
    soup = msoup.find("div" , class_="infoleft")
    c2.execute("INSERT OR IGNORE INTO Films (film) VALUES (?)", (film_name,))
    if soup is not None:
        i = soup.select ('a[href*="jav.guru/actress/"]')
        idol_count = len(i)
        if idol_count > 0:
            c2.execute("UPDATE Films SET idol_count = ? WHERE film = ? AND idol_count < ?", (idol_count, film_name, idol_count))
            #c2.execute("UPDATE Films SET idol_count = ? WHERE film = ?", (idol_count, film_name))
            for j in i:
                idol = j['href']
                idol_name = str(j.string).strip()
                c2.execute("INSERT OR IGNORE INTO Idols (idol, name, source) VALUES (?, ?, 1)", (idol, idol_name ))
                c2.execute("SELECT idol_id FROM Idols WHERE idol = ? AND source = 1", (idol,))
                idol_id = c2.fetchone()[0]
                 # Insert the idol and film into the Film_Idol table with source = 1
                c2.execute("INSERT OR IGNORE INTO Film_Idol (film, idol_id, source) VALUES (?, ?, 1)", (film_name, idol_id))
                #print (film_name, "lennnnn", idol_count)
                #print (idol_name, idol)
cnn.commit()
cnn.close()
conn.close()
