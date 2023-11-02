#!/usr/bin/env -S python3 -i

"""
Web applications page content of having selected 'All' periods. 

Author: Ilona Brinkmeier
Date: Nov. 2023
"""

##########################
# imports
##########################

from dash import dcc, html

import dash
import dash_bootstrap_components as dbc

##########################
# coding
##########################

#dash.register_page(__name__, path="/pages/all_dynasties/")

layout = html.Div(
    children = [
        html.Br(),
        html.H4("In dropdown: 'All' periods selected..."),
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)