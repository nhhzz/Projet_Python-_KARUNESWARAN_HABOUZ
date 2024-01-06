import plotly.express as px
from dash.dependencies import Input, Output

def callbacks(app, df):
    #premier graphique

    #permet la mise a jour du graphique en fonction de la station selectionnee et de la variable numerique
    @app.callback(
        Output('graphique-station', 'figure'),
        [Input('station-dropdown', 'value'),
         Input('variable-numerique-dropdown', 'value')]
    )
    def update_graph_station(selected_station, selected_variable_numerique):
        #filtre la base de donnees en fonction de la station selectionnee
        filtered_df = df[df['Nom station'] == selected_station]

        #creation du graphique (barres)
        fig = px.bar(filtered_df, x='Nom station', y=selected_variable_numerique, title=f'Données pour {selected_station}')

        return fig
    
    #deuxieme graphique

    #permet la mise a jour du graphique en fonction de la variable numerique
    @app.callback(
        Output('graphique-total-velos', 'figure'),
        [Input('variable-numerique-dropdown', 'value')]
    )
    def update_graph_total_velos(selected_variable_numerique):
        #regroupement des donnees par commune, somme des velos disponibles
        aggregated_data = df.groupby('Nom communes équipées', as_index=False)['Nombre total vélos disponibles'].sum()

        #creation du graphique (barres)
        fig = px.bar(aggregated_data, x='Nom communes équipées', y='Nombre total vélos disponibles',
                     color='Nom communes équipées',
                     title='Nombre total de vélos disponibles par ville',
                     labels={'Nombre total vélos disponibles': 'Total des vélos disponibles'})
        fig.update_layout(yaxis_type='log')
        return fig

    #troisieme graphique

    #permet la mise a jour du graphique de repartition des types de vélos
    @app.callback(
        Output('graphique-repartition-velos', 'figure'),
        [Input('variable-numerique-dropdown', 'value')]
    )
    def update_graph_repartition_velos(selected_variable_numerique):
        #somme des velos mecaniques et electriques disponibles
        repartition_velos = df[['Vélos mécaniques disponibles', 'Vélos électriques disponibles']].sum()

        #creation du graphique (camembert)
        fig = px.pie(repartition_velos, names=repartition_velos.index, values=repartition_velos.values,
                     title='Répartition des vélos mécaniques et électriques')
        
        return fig

    #quatrieme graphique

    #permet la mise a jour du graphique representant le nombre de stations en fonctionnement par commune
    @app.callback(
        Output('graphique-stations-par-commune', 'figure'),
        [Input('variable-numerique-dropdown', 'value')],
    )
    def update_graph_stations_par_commune(selected_variable_numerique):
        #copie temporaire
        temp_df = df.copy()

        #change les valeurs "OUI" et "NON" de la colonne 'Station en fonctionnement' en valeur numerique 1, 0
        #(pour pouvoir etudier les donnees plus facilement et mieux les interpreter visuellement)
        temp_df['Station en fonctionnement'] = temp_df['Station en fonctionnement'].apply(lambda x: 1 if x == 'OUI' else 0)
        #regroupement des donnees par commune apres changement, somme des station en fonctionnement
        stations_par_commune = temp_df.groupby('Nom communes équipées')['Station en fonctionnement'].sum().reset_index()

        #creation du graphique (barres)
        fig = px.bar(stations_par_commune, x='Nom communes équipées', y='Station en fonctionnement',
                     title='Stations en fonctionnement par commune',
                     labels={'Station en fonctionnement': 'Nombre de stations en fonctionnement'})
        fig.update_layout(yaxis_type='log')

        return fig
    
    #cinquieme graphique

    #permet la mise a jour du graphique representant la capacite des stations
    @app.callback(
    Output('histogram-capacite', 'figure'),
    [Input('histogram-capacite', 'id')]
    )
    def update_histogram(selected_variable):
        #creation du graphique (barres/histogramme)
        fig = px.histogram(df, x='Capacité de la station', title='Histogramme de la Capacité des Stations')
        fig.update_traces(marker_line=dict(width=1, color='black'))
        fig.update_layout(yaxis_title='Nombre de Stations')

        return fig
