#!/usr/bin/env -S python3 -i

"""
Web application about egypt pharaoh names and their dynasties. Initialise the app instance.
More information is given with file main.py.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import Dash
import dash_bootstrap_components as dbc

##########################
# coding
##########################

#
# initialise the app
#
meta_tags = [
    {
        "name": "author",
        "content": "Ilona Brinkmeier",
    },
    {
        "name": "title",
        "content": "Egyptian pharaoh's",
    },
    {
        "name": "description",
        "content": "BC dynasties from early up to late period",
    },
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1"
    },
    {
        "name": "image",
        "content": "logo.PNG",
    },
]
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=meta_tags,
    use_pages=True,
    suppress_callback_exceptions=True,
)
