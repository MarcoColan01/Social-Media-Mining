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
with open('prova.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

del people[0]
#questo è il mio dataset a ogni indice corrisponde una lista di codici ISRC (30 per playlist tranne in rari casi)
dataset = list()

#prendo il link della playlist dalla lista people creata prima
#dal link estraggo l'id della playlist
#dall'id della playlist estraggo tutti i brani da ogni brano estraggo il codice ISRC
j = 0
aux = {}
for person in people:

    #prendo il link della playlist da person 
    playlist = spotify.playlist(person["Link"])
    #dal link estraggo l'id della playlist
    songs = spotify.playlist_items(playlist["id"]) 
    
    for i in range (len(songs["items"])):
        print(j)
        isrc = songs["items"][i]["track"]["external_ids"]["isrc"]
        track_uri = songs["items"][i]["track"]["uri"]
        artist_uri = songs["items"][i]["track"]["artists"][0]["uri"]
        genres = spotify.artist(artist_uri)["genres"]

        danceability = 0
        try:
            danceability = spotify.audio_features(track_uri)[0]['danceability']
        except:
            pass

        energy = 0
        try:
            energy = spotify.audio_features(track_uri)[0]['energy']
        except:
            pass

        specchiness = 0
        try:
            speechiness = spotify.audio_features(track_uri)[0]['speechiness']
        except:
            pass

        acousticness = 0
        try:
            acousticness = spotify.audio_features(track_uri)[0]['acousticness']
        except:
            pass

        instrumentalness = 0
        try:
            instrumentalness = spotify.audio_features(track_uri)[0]['instrumentalness']
        except:
            pass

        valence = 0
        try:
            valence = spotify.audio_features(track_uri)[0]['valence']
        except:
            pass

        tempo = 0
        try:
            tempo = spotify.audio_features(track_uri)[0]['tempo']
        except:
            pass
        
        aux[j] = {"paese": person["Name"],"isrc":isrc,"uri":track_uri,"genres":genres,"danceability":danceability,"energy":energy,"speechiness":speechiness,"acousticness":acousticness,"instrumentalness":instrumentalness,"valence":valence,"tempo":tempo}
        j = j+1


with open('machine-global.csv', 'w+', newline='') as file:
    writer = csv.DictWriter(file,fieldnames=["paese","isrc","uri","genres","danceability","energy","speechiness","acousticness","instrumentalness","valence","tempo"])
    #scrive Id Label nel file csv come intestazione
    writer.writeheader()
    #scrive id affiancato da nome nel file
    for i in range (j) :
        print(i)
        writer.writerow(aux[i])

#----FINE----API-SPOTIFY----FINE----











  