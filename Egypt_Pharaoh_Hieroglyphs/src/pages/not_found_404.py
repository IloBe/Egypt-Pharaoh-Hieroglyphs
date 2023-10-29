#!/usr/bin/env -S python3 -i

"""
Web applications page not found content. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import html
import dash

##########################
# coding
##########################

#dash.register_page(__name__, path="/pages/")

layout = html.Div(
    children = [
        html.Br(),
        html.H4("Custom 404 - Sorry, the page you have selected has not been found.")
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)