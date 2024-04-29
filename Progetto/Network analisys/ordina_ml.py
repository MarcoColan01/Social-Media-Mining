data = [
    "arabiasaudita 100", "argentina 0", "australia 0", "austria 8", "belgio 0",
    "bielorussia 27", "bolivia 0", "brasile 20", "bulgaria 0", "canada 0",
    "cile 21", "colombia 0", "coreasud 19", "costarica 0", "danimarca 0",
    "eau 0", "ecuador 0", "egitto 100", "elsalvador 0", "estonia 17",
    "filippine 0", "finlandia 100", "francia 0", "germania 25", "giappone 100",
    "grecia 100", "guatemala 0", "honduras 0", "hongkong 0", "india 100",
    "indonesia 24", "irlanda 14", "islanda 0", "israele 100", "italia 100",
    "kazakistan 0", "lettonia 0", "lussemburgo 4", "malesia 0", "marocco 67",
    "nigeria 50", "norvegia 23", "nuovazelanda 0", "paesibassi 6", "pakistan 86",
    "panama 67", "paraguay 0", "peru 0", "polonia 45", "portogallo 29",
    "regnounito 0", "repubblicaceca 0", "repubblicadominicana 19", "romania 81",
    "singapore 5", "slovacchia 0", "spagna 100", "statiuniti 8", "sudafrica 64",
    "svezia 75", "svizzera 5", "taiwan 38", "thailandia 62", "turchia 100",
    "ucraina 0", "ungheria 79", "uruguay 7", "venezuela 0", "vietnam 38"
]
print(len(data))

# Dividi i dati in una lista di tuple (paese, numero)
split_data = [line.split() for line in data]

sum = 0
for data in split_data:
    sum = sum + int(data[1])

print(sum)
# Ordina le tuple in base al secondo elemento (il numero) e quindi crea una nuova lista di stringhe
sorted_data = sorted(split_data, key=lambda x: int(x[1]))

# Stampa i dati ordinati
for country, number in sorted_data:
    print(f"{country}: {number}")
