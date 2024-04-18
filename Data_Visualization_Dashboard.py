import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Sample financial data
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-12-31'),
    'Price': [100, 120, 110, 130, 125, 140, 145, 135, 130, 120, 110, 100] * 2,
    'Volume': [1000, 1200, 1100, 1300, 1250, 1400, 1450, 1350, 1300, 1200, 1100, 1000] * 2
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Financial Data Visualization Dashboard"),
    dcc.Graph(
        id='price-chart',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Price'],
                    mode='lines',
                    name='Price'
                )
            ],
            'layout': go.Layout(
                title='Price Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Price'},
                hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='volume-chart',
        figure={
            'data': [
                go.Bar(
                    x=df['Date'],
                    y=df['Volume'],
                    name='Volume'
                )
            ],
            'layout': go.Layout(
                title='Volume Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Volume'},
                hovermode='closest'
            )
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
