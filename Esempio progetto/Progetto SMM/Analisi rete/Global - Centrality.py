import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv

brani = set()
file = open(f'dati_ordinati\\machine-global\\machine-global.csv', 'r')
reader = csv.reader(file)

try:
    for row in reader:
        if row[0] != 'paese':
            key = row[0]+' '+row[1]
            brani.add(key)
except csv.Error:
        file.close()

print(len(brani))

#uso array per risalvare nel file finale