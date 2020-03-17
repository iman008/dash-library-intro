import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv('S&P.csv')
x = data['Date']
y = data['Close']

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash tutorials'),
    dcc.Graph(
        id = 'example',
        figure = {
            'data':[
                {'x':x,'y':y, 'type':'line', 'name':'Closed price'},
            ]
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)