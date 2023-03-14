#import def1
from bs4 import BeautifulSoup
import requests
import os
import glob
import sqlite3



database1 = 'tinventory.db'

def collect_series():
    u = list()
    update1 = 'update Videos set fullpath = ? where film = ?'
    query1 = "select idol_id from idols where link2 like ?"
    
    cn = sqlite3.connect(database1)
    cr = cn.cursor()
    cr.execute("select film, link2, html2 from videos where length(html2) > 20")
    print (4343)
    guru_list = cr.fetchall()
    for jl in guru_list:
        #print (jl[0])
        msoup = BeautifulSoup(jl[2], 'lxml')
        s = msoup.find('div', class_='infoleft')
        for r in s.find_all('a', rel='tag'):
            if "guru/series/" in r['href']:
                for e in r.stripped_strings:
                    nameI = e
                    linkI = r['href']
                    nameF = jl[0]
                    linkF = jl[1]

                    #print (linkI, nameF, linkF)
                    tp1 = nameF, linkI.split('/')[-2]
                    u.append(tp1)

                    #cr.execute(update1, tp1)
                    #print (linkI.split('/')[-2], e, nameF)
                    #trq2 = nameF, linkF, nameI, linkI
                    #cr.execute (insert1, trq2)
                    cn.commit()
    cn.close()
    return u

film_series_list = collect_series()
only_series = [(x,) for y, x in film_series_list]
print (only_series)

conn = sqlite3.connect("series2.db")
cursor = conn.cursor()


# Insert the unique series names into the Series table
cursor.executemany("INSERT or ignore INTO FILMS (FILM,SERIES_NAME) VALUES (?,?)", film_series_list)


conn.commit()
conn.close()


