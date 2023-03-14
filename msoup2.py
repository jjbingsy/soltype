import os
from bs4 import BeautifulSoup
import sqlite3

# Set the path to the directory containing the HTML files
#html_dir = 'htm1'

#cnn = sqlite3.connect('films.db')
#c2 = cnn.cursor()




def get_secondsource (film):
    conn = sqlite3.connect('tinventory.db')
    c = conn.cursor()

    # Select all rows with "film" and "html1" from the videos table
    c.execute("SELECT html1 FROM videos where film = ?", (film,))
    htmls = c.fetchone()
    if htmls is not None:
        print ("fuck you", film)
        soup = BeautifulSoup(htmls[0], 'lxml',  multi_valued_attributes=None)

    

    # # Loop through the rows and extract the html1 text
    # for row in c.fetchall():
    # film_name = row[0]  # assuming the html1 column is the third one
    # html = row[1]

    # # Iterate over all the files in the directory
    # # Check if the file is an HTML file

    # Process the file with Beautiful Soup
    # For example, you could print the title of the HTML page
    if "Not Found" not in soup.title.string:   
        y = soup.find_all("figure")         
        if len(y) > 0:
            #print (file_name, '*******************************************')
            for i in y:
                #print (i.prettify())
                #print (i.img['src'])
                return i.a['href'],  i.div.string, i.img['src']
                #i.descendants['href']


#get_secondsource ("STARS-293")
print (get_secondsource ("JUL-975"))