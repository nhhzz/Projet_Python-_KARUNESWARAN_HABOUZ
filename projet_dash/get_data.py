import os
import requests

def get_data():
    #url du fichier CSV
    url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'

    #User-Agent pour la requete
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
    }

    #effectue la requete
    response = requests.get(url, headers=headers)

    #verifie que la requête a réussi
    if response.status_code == 200:
        #cree le dossier s'il n'existe pas
        os.makedirs('velib-disponibilite-en-temps-reel', exist_ok=True)
        
        #chemin du fichier a sauvegarder
        file_path = os.path.join('velib-disponibilite-en-temps-reel', 'data.csv')
        
        #ecrit le contenu de la reponse dans le fichier
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")

if __name__ == "__main__":
    get_data()
