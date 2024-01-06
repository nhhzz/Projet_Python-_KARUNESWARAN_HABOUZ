import folium
import branca
from folium import plugins

def create_folium_map(df):
    #coordonnees initiale
    coords = (48.858844, 2.294350)
    #zoom initiale
    zoom_level = 14

    #creation de la carte folium avec les coordonnes et le zoom specifies
    folium_map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=zoom_level)
    aggregated_values = {}

    #iteration sur chaque ligne de la base de donnees
    for _, row in df.iterrows():
        #extraction des coordonnees geographiqe
        lat, lon = map(float, row['Coordonnées géographiques'].split(','))

        #arrondissement des donnees extraites
        position = (round(lat, 6), round(lon, 6))

        #initialisation des valeurs associees a chaque position
        if position not in aggregated_values:
            aggregated_values[position] = {
                'sum_values': 0,
                'count': 0
            }

        #association du nombre de velo disponible a chaque position 
        aggregated_values[position]['sum_values'] += row['Nombre total vélos disponibles']
        aggregated_values[position]['count'] += 1
    
    #coloration des marqueurs en fontion du nombre de velos disponible
    cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=min(aggregated_values.values(), key=lambda x: x['sum_values'])['sum_values'],
                                        vmax=max(aggregated_values.values(), key=lambda x: x['sum_values'])['sum_values'])
    folium_map.add_child(cm)

    #marqueurs
    for position, values in aggregated_values.items():
        lat, lon = position
        size = values['sum_values'] / values['count']  
        color = cm(values['sum_values'])

        #marqueur en cercle
        marker = folium.CircleMarker(
            location=[lat, lon],
            radius=size,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6
        )

        #contenu da la popup de chaque marqueur
        popup_content = f"Vélos disponibles : {values['sum_values']}"
        popup = folium.Popup(popup_content, max_width=300)
        marker.add_child(popup)

        #ajout du marqueur a la carte
        marker.add_to(folium_map)

    #pour regrouper les marqueurs sur la carte (en cas de dezoom)
    plugins.MarkerCluster().add_to(folium_map)

    return folium_map
