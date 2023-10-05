#per lavorare con le api di spotify in python serve installare una libreria
#che si chiama spotipy si installa con questo comando: 
#pip install spotipy --upgrade
#link github libreria: https://github.com/plamere/spotipy

#mail: wohit36816@tourcc.com username: wohit
#password: Ciao123! 
#questo è il profilo creato appositamente per usare le api di spotify
#per lavorare con le api di spotify abbiamo bisogno di due codici
#che otteniamo creando una app dal nostro profilo nell'area sviluppatori

from traceback import print_tb
import networkx as nx
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#----INIZIO----API-SPOTIFY----INIZIO----

#ID della mia applicazione su account spotify
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="afff80ae387b42f8836ae2d2d138343c",client_secret="350216c50b194805b52cb62369d8f136"))

#apro il file playlist che contiene il nome dell'utente e il link alla sua playlist
#metto i dati nella lista people
people = list()
with open('global.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)
        break

people2 = list()
with open('viral.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people2.append(row)
        break

aux = {}
aux2 = {}

#prendo il link della playlist da person 
playlist = spotify.playlist(people[0]["Link"])
#dal link estraggo l'id della playlist
songs = spotify.playlist_items(playlist["id"]) 
    
for i in range (10):
    isrc = songs["items"][i]["track"]["external_ids"]["isrc"]

    track_uri = songs["items"][i]["track"]["uri"]
    track_name = songs["items"][i]["track"]["name"]

    artist_name = songs["items"][i]["track"]["artists"][0]["name"]

    album = spotify.album(songs["items"][i]["track"]["album"]["external_urls"]["spotify"])
    data = album["release_date"]
    
    aux[i] = {"isrc":isrc,"uri":track_uri,"titolo":track_name,"artista":artist_name,"pubblicazione":data}


#prendo il link della playlist da person 
playlist = spotify.playlist(people2[0]["Link"])
#dal link estraggo l'id della playlist
songs = spotify.playlist_items(playlist["id"]) 
    
for i in range (10):
    isrc = songs["items"][i]["track"]["external_ids"]["isrc"]

    track_uri = songs["items"][i]["track"]["uri"]
    track_name = songs["items"][i]["track"]["name"]

    artist_name = songs["items"][i]["track"]["artists"][0]["name"]

    album = spotify.album(songs["items"][i]["track"]["album"]["external_urls"]["spotify"])
    data = album["release_date"]
    
    aux2[i] = {"isrc":isrc,"uri":track_uri,"titolo":track_name,"artista":artist_name,"pubblicazione":data}

with open('10-global.csv', 'w+', newline='', encoding='utf-16') as file:
    writer = csv.DictWriter(file,fieldnames=["isrc","uri","titolo","artista","pubblicazione"])
    #scrive Id Label nel file csv come intestazione
    writer.writeheader()
    #scrive id affiancato da nome nel file
    for i in range (10) :
        writer.writerow(aux[i])

with open('10-viral.csv', 'w+', newline='', encoding='utf-16') as file:
    writer = csv.DictWriter(file,fieldnames=["isrc","uri","titolo","artista","pubblicazione"])
    #scrive Id Label nel file csv come intestazione
    writer.writeheader()
    #scrive id affiancato da nome nel file
    for i in range (10) :
        writer.writerow(aux2[i])

#----FINE----API-SPOTIFY----FINE----











  