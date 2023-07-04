import csv
import json

SLOUPCE = ["TITLE", "DIRECTOR", "CAST", "GENRES", "RELEASE_YEAR"]
seznam = []

with open("netflix_titles.tsv", encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter="\t")
    for radek in data:
        slovnik = {}
        for sloupec in SLOUPCE:
            if sloupec in ['CAST', 'DIRECTOR']:
                hodnota = radek[sloupec].split(", ")
                if hodnota == [""]:
                    hodnota = []
                slovnik[sloupec.lower()] = hodnota
            else:
                slovnik[sloupec.lower()] = radek[sloupec]
        seznam.append(slovnik)
for slovnik in seznam:        
    decade = str((int(slovnik["release_year"]) // 10) * 10)
    slovnik["decade"] = decade
    del slovnik["release_year"]

with open("movies.json", mode="w", encoding="utf-8") as soubor:
    json.dump(seznam, soubor, ensure_ascii=False, indent=4)