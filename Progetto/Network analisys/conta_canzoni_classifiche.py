import csv
import glob

def count_titles_in_csv_files():
    # Dizionario per memorizzare il conteggio dei titoli
    title_count = {}

    # Cerca tutti i file CSV nella stessa cartella del sorgente Python che iniziano con "z-global.csv"
    for i in range(1,16):
        #print("ciao")
        with open(f'0{i}-global.csv', 'r', encoding = 'utf-16') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Ottiene il titolo dalla riga
                #print(row[2])
                title = row[2:]
                print(title)
                # Aggiorna il conteggio del titolo nel dizionario
                title_count[title[0]] = title_count.get(title[0], 0) + 1

    return title_count

# Ottieni il conteggio dei titoli nei file CSV
titles_count = count_titles_in_csv_files()

sorted_titles_count = dict(sorted(titles_count.items(), key=lambda item: item[1], reverse=True))

# Stampare il conteggio dei titoli
for title, count in sorted_titles_count.items():
    print(f"{title}: {count}")
