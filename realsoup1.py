import sqlite3
from bs4 import BeautifulSoup

# Connect to the databases
conn = sqlite3.connect('tinventory.db')
cnn = sqlite3.connect('films.db')
crSource = conn.cursor()
crDetination = cnn.cursor()


# Select all rows with "film" and "html1" from the videos table
crSource.execute("SELECT film, html1 FROM videos")

for row in crSource.fetchall():
    film = row[0]
    html = row[1]

    msoup = BeautifulSoup(html, 'lxml')
    if "Page Not Found" not in msoup.title.string:
        crDetination.execute("INSERT OR IGNORE INTO Films (film) VALUES (?)", (film,))
        idols = msoup.find_all("figure")
        idol_count = len (idols)    
        crDetination.execute("UPDATE Films SET idol_count = ? WHERE film = ? AND idol_count < ?", (idol_count, film, idol_count))
        for i in idols:
            print (i.a['href'],  i.div.string, i.img['src']) #img['src'] is the image link
            idol = i.a['href']
            name = i.div.string

 
