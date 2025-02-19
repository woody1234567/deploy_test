import dash
from dash import html, dcc
import plotly.express as px

app = dash.Dash(__name__)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

app.layout = html.Div([
    html.H1("Plotly Dash App"),
    dcc.Graph(figure=fig)
])

server = app.server  # Required for Heroku

if __name__ == "__main__":
    app.run_server(debug=True)