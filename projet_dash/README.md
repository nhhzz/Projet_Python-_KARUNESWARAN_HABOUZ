# Projet Dashboard Open Data avec Python 👩‍💻

Notre projet porte sur l'analyse des données Velib en temps réel. Ces données, accessibles via l'Open Data, ont été exploitées pour créer un tableau de bord interactif présentant la disponibilité des vélos. Notre tableau de bord inclut un graphique en camembert, quatres histogrammes ainsi qu'une représentation géolocalisée pour une meilleure visualisation de certaines données. La structure de notre projet facilite sa compréhension et sa maintenance, étant séparée en plusieurs fichiers. Le tableau de bord est développé en utilisant plusieurs bibliothèques telles que : Dash, Plotly Express et Folium pour la visualisation des données géographiques.



# Installation des dépendances 

Pour cloner le projet exécutez la commande :

`$ https://github.com/nhhzz/Projet_Python-_KARUNESWARAN_HABOUZ.git`

Pour installer les dépendances requises, exécutez la commande suivante :

`$ python -m pip install -r requirements.txt`

Pour récupérer les données du fichier CSV, exécutez la commande suivante :

`$ python get_data.py`


# Exécution du dashboard 💻

Pour lancer le tableau de bord, exécutez le fichier main.py avec la commande :

`$ python main.py`

Le tableau de bord sera accessible à l'adresse http://127.0.0.1:8050/ dans un navigateur web.

Voici une description des fichier présent dans notre projet : 

    Le fichier README fournissant des instructions sur le projet.
    Le fichier CSV contenant notre de base de données soit les données Velib (velib-disponibilite-en-temps-reel/data.csv).
    Le fichier get_data.py permettant de télécharger les données Velib en temps réel et les sauvegarder localement dans le dossier.
    Le code source main.py rassemblant tous les modules pour exécuter le tableau de bord.
    Le fichier callback.py contenant toutes les fonctions de rappel utilisées pour mettre à jour les composants de l'application en réponse aux interactions de l'utilisateur.
    Le fichier layout.py contenant la définition de la mise en page du bord.
    Le fichier map.py contenant les fonctions utilisées pour créer la carte avec Folium. 
        

        
    ├── velib-disponibilite-en-temps-reel
    │   └── data.csv
    │
    ├── __pycache__
    ├── callback.py
    ├── get_data.py
    ├── layout.py
    ├── main.py
    ├── map.py
    ├── README.md
    └── requirements.txt




# Rapport d'analyse 📊 🗺


**Graphique de la station** 

 Ce graphique est un diagramme à barres qui affiche des informations sur une station de vélo spécifique sélectionnée par l’utilisateur. La variable numérique (par exemple, le nombre total de vélos disponibles) pour cette station est affichée sur l’axe des y. Ce graphique permet de visualiser rapidement les données pour une station spécifique.

**Graphique du total des vélos** 
    
 Ce graphique est un diagramme à barres qui affiche le nombre total de vélos disponibles par ville. Chaque barre représente une ville, la hauteur de la barre est proportionnelle au nombre total de vélos disponibles dans cette ville. Ce graphique permet de comparer rapidement le nombre total de vélos disponibles entre les différentes villes.

**Graphique en camembert**

 Ce graphique présente la répartition des vélos mécaniques et électriques disponibles, avec chaque tranche représentant un type de vélo. Ainsi, l'utilisateur peut observer facilement la répartition relative des deux catégories de vélos.

**Graphique des stations en fonctionnement par Commune**

 Il s'agit d'un graphique à barres, où chaque barre représente une commune spécifique et où la hauteur de chaque barre représente le nombre de stations en activité dans la commune en question.

**Histogramme Numérique de la Capacité de Stationnement**
    
 L'histogramme numérique présente la capacité de stationnement pour chaque station. Cette représentation graphique offre une vue  de la capacité de chaque station de manière numérique, ce qui va permettre à l'utilisateur de voir la disponibilité d'emplacements de stationnement pour les vélos.

**Visualisation Géographique avec Carte Folium**

 La carte créée avec Folium permet de visualiser géographiquement toutes les stations de vélos disponibles. Chaque station est représentée par un marqueur sur la carte. Lorsque vous cliquez sur un marqueur, le nom de la station s’affiche. Cela permet de voir rapidement et facilement où se trouvent les stations et de comprendre leur distribution géographique et leur emplacement dans la ville.

Ces différentes visualisations, travaillent ensemble pour fournir une vue l’ensemble des données de disponibilité des vélos, tout en permettant également des analyses plus détaillées au niveau de la station ou de la ville. Ils permettent à l’utilisateur de comprendre les données plus simplement et de différentes manières.