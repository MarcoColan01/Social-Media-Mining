from audioop import avg
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import networkx.algorithms.community as community
import scipy.stats as sp

with open('viral.txt', 'w') as file:

    for z in range (1,16):

        grafo = nx.read_gpickle(f'dati_ordinati\\viral-pkl\\viral{z}.pkl')

        degree = dict(grafo.degree(weight = 'weight'))
        campione_grado = list(degree.values()) #campione grado twitter
        file.write(f'--INIZIO--{z}-06--INIZIO-- \n')
        file.write(f'Numero di archi: {grafo.size()} \n')
        file.write(f'Grado medio non pesato: {(grafo.size()*2)/grafo.order()} \n')
        degree = dict(grafo.degree(weight = 'weight'))
        file.write(f'Grado medio pesato: {np.mean(list(degree.values()))} \n')
        file.write(f'Mediana: {np.median(campione_grado)} \n')
        file.write(f'Moda: {sp.mode(campione_grado).mode[0]} \n')
        file.write(f'Densità: {(2*grafo.size())/(grafo.order()*(grafo.order()-1))} \n')

        max_degree = max(degree.values())
        max_country = ''
        for k,v in grafo.degree(weight = 'weight'):
            if v == max_degree:
                max_country = k
                break
        file.write(f'Nodo grado massimo: {grafo.nodes.data("label")[max_country]} valore: {max_degree} \n')

        min_degree = min(degree.values())
        min_country = ''
        for k,v in grafo.degree(weight = 'weight'):
            if v == min_degree:
                min_country = k
                break
        file.write(f'Nodo grado minimo: {grafo.nodes.data("label")[min_country]} valore: {min_degree} \n')

        edges = list(grafo.edges.data("weight"))
        max_archi = (sorted(edges, key=lambda x:x[2], reverse=True))[:5]
        for i,j,k in max_archi:
            file.write(f'Arco peso maggiore tra: {grafo.nodes.data("label")[i]} e {grafo.nodes.data("label")[j]} con valore: {k} \n')

        min_archi = (sorted(edges, key=lambda x:x[2], reverse=True))[len(edges)-5:]
        for i,j,k in min_archi:
            file.write(f'Arco peso minore tra: {grafo.nodes.data("label")[i]} e {grafo.nodes.data("label")[j]} con valore: {k} \n')


        degree = dict(grafo.degree(weight = 'weight')) #pechino_all_degree
        campione_grado = list(degree.values()) #campione grado twitter
        percentile_95 = np.percentile(campione_grado,95)
        hub_nodi = [k for k,v in degree.items() if v>= percentile_95]
        file.write(f'Hub:')
        for k in hub_nodi:
            file.write(f' {grafo.nodes.data("label")[k]}')

        file.write(f'\nIl grafo è connesso: {nx.is_connected(grafo)}')

        file.write(f'\nTransitività: {nx.transitivity(grafo)}')

        eigen_con_pesi = nx.eigenvector_centrality(grafo, weight='weight')
        max5_pesi = sorted(eigen_con_pesi, key=eigen_con_pesi.get, reverse=True)[:5]
        min5_pesi = sorted(eigen_con_pesi, key=eigen_con_pesi.get, reverse=True)[67:]
        file.write(f'\nEigenvector massima:')
        for k in max5_pesi:
            file.write(f' {grafo.nodes.data("label")[k]}')
        file.write(f'\nEigenvector minima:')
        for k in min5_pesi:
            file.write(f' {grafo.nodes.data("label")[k]}')

        Closeness = nx.closeness_centrality(grafo, u=None, distance=None, wf_improved=True)
        max_Close = max(Closeness, key=Closeness.get)
        min_Close = min(Closeness, key=Closeness.get)
        avg_Close = sum(Closeness.values())/grafo.order()

        file.write(f'\nCloseness massima: {grafo.nodes.data("label")[max_Close]} {Closeness[max_Close]}')
        file.write(f'\nCloseness media: {avg_Close}')
        file.write(f'\nCloseness minima: {grafo.nodes.data("label")[min_Close]} {Closeness[min_Close]}')

        file.write(f'\n--FINE--{z}-06--FINE-- \n\n')

        l_coms = community.louvain_communities(grafo, seed=67, resolution = 1.1)
        community_louvain = {i:e for i, e in enumerate(l_coms)}
        for i, com in community_louvain.items():
            for n in com: # per ogni nodo nella community con id "i"
                grafo.nodes[n]['com'] = i 
        
        nx.write_gexf(grafo, f'Grafici_viral\\Gephi\\Viral_community {z}.gexf')


with open('global.txt', 'w') as file:

    for z in range (1,16):

        grafo = nx.read_gpickle(f'dati_ordinati\\global-pkl\\global{z}.pkl')

        degree = dict(grafo.degree(weight = 'weight'))
        campione_grado = list(degree.values()) #campione grado twitter
        file.write(f'--INIZIO--{z}-06--INIZIO-- \n')
        file.write(f'Numero di archi: {grafo.size()} \n')
        file.write(f'Grado medio non pesato: {(grafo.size()*2)/grafo.order()} \n')
        degree = dict(grafo.degree(weight = 'weight'))
        file.write(f'Grado medio pesato: {np.mean(list(degree.values()))} \n')
        file.write(f'Mediana: {np.median(campione_grado)} \n')
        file.write(f'Moda: {sp.mode(campione_grado).mode[0]} \n')
        file.write(f'Densità: {(2*grafo.size())/(grafo.order()*(grafo.order()-1))} \n')

        max_degree = max(degree.values())
        max_country = ''
        for k,v in grafo.degree(weight = 'weight'):
            if v == max_degree:
                max_country = k
                break
        file.write(f'Nodo grado massimo: {grafo.nodes.data("label")[max_country]} valore: {max_degree} \n')

        min_degree = min(degree.values())
        min_country = ''
        for k,v in grafo.degree(weight = 'weight'):
            if v == min_degree:
                min_country = k
                break
        file.write(f'Nodo grado minimo: {grafo.nodes.data("label")[min_country]} valore: {min_degree} \n')


        edges = list(grafo.edges.data("weight"))
        max_archi = (sorted(edges, key=lambda x:x[2], reverse=True))[:5]
        for i,j,k in max_archi:
            file.write(f'Arco peso maggiore tra: {grafo.nodes.data("label")[i]} e {grafo.nodes.data("label")[j]} con valore: {k} \n')

        min_archi = (sorted(edges, key=lambda x:x[2], reverse=True))[len(edges)-5:]
        for i,j,k in min_archi:
            file.write(f'Arco peso minore tra: {grafo.nodes.data("label")[i]} e {grafo.nodes.data("label")[j]} con valore: {k} \n')


        degree = dict(grafo.degree(weight = 'weight')) #pechino_all_degree
        campione_grado = list(degree.values()) #campione grado twitter
        percentile_95 = np.percentile(campione_grado,95)
        hub_nodi = [k for k,v in degree.items() if v>= percentile_95]
        file.write(f'Hub:')
        for k in hub_nodi:
            file.write(f' {grafo.nodes.data("label")[k]}')
        
        file.write(f'\nIl grafo è connesso: {nx.is_connected(grafo)}')

        file.write(f'\nTransitività: {nx.transitivity(grafo)}')

        eigen_con_pesi = nx.pagerank(grafo)
        max5_pesi = sorted(eigen_con_pesi, key=eigen_con_pesi.get, reverse=True)[:5]
        for k in max5_pesi:
            print(f' {grafo.nodes.data("label")[k]}')
        print('\n')

        eigen_con_pesi = nx.eigenvector_centrality(grafo, weight='weight')
        max5_pesi = sorted(eigen_con_pesi, key=eigen_con_pesi.get, reverse=True)[:5]
        min5_pesi = sorted(eigen_con_pesi, key=eigen_con_pesi.get, reverse=True)[67:]
        file.write(f'\nEigenvector massima:')
        for k in max5_pesi:
            file.write(f' {grafo.nodes.data("label")[k]}')
        file.write(f'\nEigenvector minima:')
        for k in min5_pesi:
            file.write(f' {grafo.nodes.data("label")[k]}')

        Closeness = nx.closeness_centrality(grafo, u=None, distance=None, wf_improved=True)
        max_Close = max(Closeness, key=Closeness.get)
        min_Close = min(Closeness, key=Closeness.get)
        avg_Close = sum(Closeness.values())/grafo.order()

        file.write(f'\nCloseness massima: {grafo.nodes.data("label")[max_Close]} {Closeness[max_Close]}')
        file.write(f'\nCloseness media: {avg_Close}')
        file.write(f'\nCloseness minima: {grafo.nodes.data("label")[min_Close]} {Closeness[min_Close]}')

        file.write(f'\n--FINE--{z}-06--FINE-- \n\n')

        l_coms = community.louvain_communities(grafo, seed=67, resolution = 1.15)
        community_louvain = {i:e for i, e in enumerate(l_coms)}
        for i, com in community_louvain.items():
            for n in com: # per ogni nodo nella community con id "i"
                grafo.nodes[n]['com'] = i 

        nx.write_gexf(grafo, f'Grafici_global\\Gephi\\Global_community {z}.gexf')