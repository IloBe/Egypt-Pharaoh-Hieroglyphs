# src/pages/not_found_404.py

"""
Applications page 404 not found content. 
"""

##########################
# imports
##########################

from dash import html, register_page
import dash

##########################
# coding
##########################

register_page(__name__)

layout = html.Div(
    children = [
        html.Br(),
        html.H4("Custom 404 - Sorry, the page you have selected has not been found.")
    ],
    style = {
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className = "g-0 ps-5 pe-5",
)