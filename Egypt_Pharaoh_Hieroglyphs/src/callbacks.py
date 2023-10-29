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
import logging

##########################
# coding
##########################

# set basic, simple console logger
log_level = logging.DEBUG
logging.basicConfig(level=log_level)
logger = logging.getLogger("pharaoh_hieroglyphs")


def print_callback(debug_mode):
    """ Logs callback trigger info, used for debugging """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if debug_mode:
                logger.info("--- Function called: %s", func.__name__)
                logger.info("--- Triggered by: %s", dash.callback_context.triggered[0]['prop_id'])
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

#
# add controls to build the interaction
#

@callback(
    Output("button_link_home", "href"),
    Input("button_link_home", "n_clicks"),
)
@print_callback(log_level)
def search_home(click_home):
    if click_home is None or click_home == 0:
        return dash.no_update
    return f"/"


@callback(
    Output("all_dynasties", "href"),
    Input("all_dynasties", "n_clicks"),
)
@print_callback(log_level)
def search_all_dynasties(click_all_dynasties):
    if click_all_dynasties is None or click_all_dynasties == 0:
        return dash.no_update
    return f"/pages/all_dynasties/"


@callback(
    Output("First Dynasty", "href"),
    Input("First Dynasty", "n_clicks"),
)
@print_callback(log_level)
def search_first_dynasty(click_first_dynasty):
    if click_first_dynasty is None or click_first_dynasty == 0:
        return dash.no_update
    return f"/pages/first_dynasty/"

