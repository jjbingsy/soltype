import sqlite3

conn = sqlite3.connect("series.db")
cursor = conn.cursor()

cursor.execute("""
SELECT Series.Series_Name, Series.Id, COUNT(Films.id)
FROM Series
LEFT JOIN Films ON Series.id = Films.Series_Name_id
GROUP BY Series.id
ORDER BY COUNT(Films.id)
""")

series_film_count = cursor.fetchall()

for series_name_id, series_name, film_count in series_film_count:
    print(f"{series_name_id} {series_name}: {film_count}")

series_id = 119 # example value, replace with your desired series_id

cursor.execute("""
SELECT Film
FROM Films
WHERE Series_Name_id = ?
""", (series_id,))

films = cursor.fetchall()

for film in films:
    print(film[0])



conn.close()
