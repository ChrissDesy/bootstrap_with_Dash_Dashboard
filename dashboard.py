from dash import Dash
from layout import layout2 as dashboard

app = Dash(__name__)

app.title = 'Dashboard'
app.layout = dashboard

if __name__ == '__main__':
    app.run_server(debug=True, port=1234)
