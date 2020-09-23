# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# - - - - - - - - - - - - - - #
# Functions definitions
# - - - - - - - - - - - - - - #
def generate_dashtable(dataframe):
    return dash_table.DataTable(
        data=dataframe.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in dataframe.columns],
        page_size=10
    )

# - - - - - - - - - - - - - - #
# Loading data
# - - - - - - - - - - - - - - #

df_merged = pd.read_csv("data/merged_data.csv")

# - - - - - - - - - - - - - - #
# Defining figures
# - - - - - - - - - - - - - - #


# - - - - - - - - - - - - - - #
# App layout
# - - - - - - - - - - - - - - #
app.layout = html.Div(children=[
    html.H1(children='Hello Dash EPF'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),


    generate_dashtable(df_merged)


])

# - - - - - - - - - - - - - - #
# App call backs
# - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - #
# App Main
# - - - - - - - - - - - - - - #

if __name__ == '__main__':
    app.run_server(debug=True)
