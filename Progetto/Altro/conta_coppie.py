from collections import defaultdict

def conteggio_coppie(dati):
    conteggio = defaultdict(list)

    # Analizziamo i dati e contiamo le occorrenze per ogni coppia di paesi
    for dato in dati:
        # Estraiamo i dati dalla stringa
        inizio = dato.find(":")
        fine = dato.rfind(":")
        coppia = dato[inizio + 1:fine].strip()
        valore = int(dato[fine + 1:].strip())

        # Estraiamo i nomi dei paesi dalla coppia
        paese1, paese2 = coppia.split(' e ')

        # Ordiniamo i nomi dei paesi in modo da avere una rappresentazione uniforme della coppia
        coppia_ordinata = tuple(sorted([paese1, paese2]))

        conteggio[coppia_ordinata].append(valore)

    # Ordiniamo le coppie per il numero di occorrenze
    coppie_ordinate = sorted(conteggio.items(), key=lambda x: len(x[1]), reverse=True)

    # Selezioniamo le prime 5 coppie
    prime_5_coppie = coppie_ordinate[:5]

    # Stampiamo le informazioni richieste per ciascuna delle prime 5 coppie
    for coppia, valori in prime_5_coppie:
        max_valore = max(valori)
        min_valore = min(valori)
        numero_occorrenze = len(valori)
        paese1, paese2 = coppia
        print(f"Coppia: {paese1} - {paese2}, Max: {max_valore}, Min: {min_valore}, Numero di occorrenze: {numero_occorrenze}")

# Esempio di dati nel formato "Arco peso minore tra: paese1 e paese2 con valore: n"
dati = [
    "Arco peso minore tra: Svizzera e Uruguay con valore: 1",
    "Arco peso minore tra: Svizzera e Vietnam con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Venezuela con valore: 1",
    "Arco peso minore tra: Svizzera e Vietnam con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Ungheria e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Venezuela e Vietnam con valore: 1",
    "Arco peso minore tra: Svizzera e Vietnam con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Ungheria e Venezuela con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Taiwan e Venezuela con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Uruguay con valore: 1",
    "Arco peso minore tra: Thailandia e Ucraina con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Ucraina e Uruguay con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Vietnam con valore: 1",
    "Arco peso minore tra: Thailandia e Ungheria con valore: 1",
    "Arco peso minore tra: Thailandia e Uruguay con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Thailandia e Uruguay con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Uruguay e Vietnam con valore: 1",
    "Arco peso minore tra: Thailandia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Uruguay e Vietnam con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Vietnam con valore: 1",
    "Arco peso minore tra: Uruguay e Vietnam con valore: 1",
    "Arco peso minore tra: Turchia e Ungheria con valore: 1",
    "Arco peso minore tra: Turchia e Venezuela con valore: 1",
    "Arco peso minore tra: Ucraina e Venezuela con valore: 1",
    "Arco peso minore tra: Ungheria e Vietnam con valore: 1",
    "Arco peso minore tra: Uruguay e Vietnam con valore: 1"
]


conteggio_coppie(dati)
