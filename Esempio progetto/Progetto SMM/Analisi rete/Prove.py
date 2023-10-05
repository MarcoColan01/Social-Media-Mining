import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from statsmodels.distributions.empirical_distribution import ECDF

import os
from matplotlib import font_manager as fm, rcParams
import matplotlib as mpl

grafo = nx.read_gpickle('dati_ordinati\\viral-pkl\\viral1.pkl')
degree = dict(grafo.degree(weight = 'weight'))
campione_degree = list(degree.values())

min_t = min(campione_degree)
max_t = max(campione_degree)

count_rete, bins_rete = np.histogram(campione_degree, bins = np.arange(min_t,max_t+2))

pdf_rete = count_rete / grafo.order()

cdf_fb = ECDF(campione_degree)
x = np.unique(campione_degree)
y = cdf_fb(x)

# Visualizzazione

fig_pdf_fb = plt.figure(figsize=(21,9))
assi = fig_pdf_fb.gca()
assi.plot(bins_rete[:-1], pdf_rete, marker = 'o', linestyle='None', ms = 5, color = '#00d95a')

fig_pdf_fb.set_facecolor('#1c1e21')
assi.set_facecolor('#1c1e21')

fpath = os.path.join(mpl.get_data_path(), "fonts/ttf/Gotham.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

assi.set_xlabel('X-axis')
assi.set_ylabel('Y-axis')

assi.spines['left'].set_color('white')  
assi.spines['right'].set_color('white')         # setting up Y-axis tick color to red
assi.spines['top'].set_color('white')
assi.spines['bottom'].set_color('white')   
assi.tick_params(colors='white', which='both')

assi.set_xlabel('Grado'.format(fname), fontproperties=prop, size = 30, color='#00d95a')
assi.set_ylabel('PDF Linear'.format(fname), fontproperties=prop, size = 30, color='#00d95a')

plt.show()