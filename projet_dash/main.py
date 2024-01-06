import dash
import pandas as pd
from callback import callbacks
from map import create_folium_map
from layout import layout

#donnees
df = pd.read_csv("velib-disponibilite-en-temps-reel/data.csv", delimiter=';')

#application
app = dash.Dash(__name__)

#carte
create_folium_map(df)

#layout
layout(app, df, create_folium_map(df))

#callbacks
callbacks(app, df)

#application
if __name__ == '__main__':
    app.run_server(debug=True)
