from dash import dcc, html

def layout(app, df, map):
    app.layout = html.Div(children=[
    #titre
    html.H1(children='Vélib Insights: Suivi en Temps Réel des Vélos à Paris',  style={'textAlign': 'center'}),

    #menu deroulant pour la selection de la station
    dcc.Dropdown(
        id='station-dropdown',
        #selection des nom de station possible (disponible dans le deroulant)
        #(on ne choisit que la colonne avec les noms de station)
        options=[
            {'label': station, 'value': station} for station in df['Nom station'].unique()
        ],
        #valeur par defaut (premiere station)
        value=df['Nom station'].iloc[0],
        #pour permettre a l'utilisateur de ne selectionner qu'une seule variable a la fois
        multi=False
    ),
    #menu deroulant pour la "valeur numerique"
    dcc.Dropdown(
        id='variable-numerique-dropdown',
        #selection des donnees numerique possible (disponible dans le deroulant)
        options=[
            {'label': col, 'value': col} for col in df.select_dtypes('number').columns
        ],
        #valeur par defaut (premiere colonne)
        value=df.select_dtypes('number').columns[0],
        #pour permettre a l'utilisateur de ne selectionner qu'une seule variable a la fois
        multi=False
    ),

    # premier graphique (barres)
    dcc.Graph(
        id='graphique-station',
        figure={}
    ),

    # deuxieme graphique (barres)
    dcc.Graph(
        id='graphique-total-velos',
        figure={},
        style={'height': '70vh'}
    ),

    # troisieme graphique (camembert)
    dcc.Graph(
        id='graphique-repartition-velos',
        figure={}
    ),

    # quatrieme graphique (barres)
    dcc.Graph(
        id='graphique-stations-par-commune',
        figure={}
    ),

    # cinquième graphique (barres)
    dcc.Graph(
        id='histogram-capacite',
        figure={}
    ),

    # HTML carte
    html.Iframe(
        id='folium-map',
        srcDoc=map.get_root().render(),
        width='100%',
        height='500'
    )
])
