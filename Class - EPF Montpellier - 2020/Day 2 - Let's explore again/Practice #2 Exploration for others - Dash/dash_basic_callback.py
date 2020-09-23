# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# - - - - - - - - - - - - - - #
# Functions definitions
# - - - - - - - - - - - - - - #

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

    html.H6("1/ Callback demo : change the value in the text box to see callbacks in action !"),
    html.Div(["Here an Input: ",
                dcc.Input(id="my-input", value="initial value", type="text")]),
    html.Br(),
    html.Div(id="my-output"),

    html.Br(),
    html.H6("2/ Here we are goind to do some changes"),

    dcc.Slider(
        id='year-slider',
        min=1950,
        max=2019,
        value=1950,
        step=10,
        marks={
            1950: '1950',
            1960: '1960',
            1970: '1970',
            1980: '1980',
            1990: '1990',
            2000: '2000',
            2010: '2010',
            2019: '2019'
        },
    ),
    # Add a div that will contain our new output


])

# - - - - - - - - - - - - - - #
# App call backs
# - - - - - - - - - - - - - - #
@app.callback(
    Output(component_id="my-output", component_property="children"),
    [Input(component_id="my-input", component_property="value")]
)
def update_output_div(input_value):
    return 'This is the Output : {}'.format(input_value)

#add here a new callback



# App Main
# - - - - - - - - - - - - - - #

if __name__ == '__main__':
    app.run_server(debug=True)
