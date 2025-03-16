from flask import Flask  
from dash import dcc, html, Dash  
import plotly.graph_objects as go  
import pandas as pd  

# Load the dataset  
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')  

# Prepare the choropleth figure  
fig = go.Figure(data=go.Choropleth(  
    locations=df['CODE'],  
    z=df['GDP (BILLIONS)'],  
    text=df['COUNTRY'],  
    colorscale='oranges',  
    autocolorscale=False,  
    reversescale=True,  
    marker_line_color='orange',  
    marker_line_width=0.5,  
    colorbar_title='GDP Billions USD',  
))  

# Update layout  
fig.update_layout(  
    title_text='World Map By Aman Khan',  
    geo=dict(  
        showframe=False,  
        showcoastlines=True,  
        projection_type='equirectangular',  
    ),  
    annotations=[dict(  
        x=0.55,  
        y=0.1,  
        xref='paper',  
        yref='paper',  
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">CIA World Factbook</a>',  
        showarrow=False  
    )]  
)  

# Create a Flask application  
server = Flask(__name__)  

# Create the Dash app  
app = Dash(__name__, server=server, routes_pathname_prefix='/')  

app.layout = html.Div(children=[  
    dcc.Graph(  
        id='gdp-map',  
        figure=fig  
    )  
])  

# Run the Flask application  
if __name__ == '__main__':  
    app.run()
