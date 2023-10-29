#!/usr/bin/env -S python3 -i

"""
Web application about egypt pharaoh names and their dynasties. Callback interactions.
More information is given with file main.py.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import callback, Input, Output, no_update
import dash

##########################
# coding
##########################

#
# add controls to build the interaction
#

@callback(
    Output("button_link_home", "href"),
    Input("button_link_home", "n_clicks"),
)
def search_home(click_home):
    if click_home is None or click_home == 0:
        return dash.no_update
    return f"/"


@callback(
    Output("all_dynasties", "href"),
    Input("all_dynasties", "n_clicks"),
)
def search_all_dynasties(click_all_dynasties):
    if click_all_dynasties is None or click_all_dynasties == 0:
        return dash.no_update
    return f"/pages/all_dynasties/"


@callback(
    Output("First Dynasty", "href"),
    Input("First Dynasty", "n_clicks"),
)
def search_first_dynasty(click_first_dynasty):
    if click_first_dynasty is None or click_first_dynasty == 0:
        return dash.no_update
    return f"/pages/first_dynasty/"