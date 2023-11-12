"""
Web application about egypt pharaoh names and their dynasties. Callback interactions.
More information is given with file main.py.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import callback, Input, Output, no_update, ctx
from pathlib import Path

import dash
import logging
import pandas as pd
import numpy as np

##########################
# coding
##########################

# project path
PROJ_PATH = Path(__file__).parent
print(f'====   callbacks.py: PROJ_PATH: {PROJ_PATH}')
# local image path
IMG_PATH = ''.join([str(PROJ_PATH), '/assets/images/'])
print(f'====   callbacks.py: IMG_PATH: {IMG_PATH}')

# set basic, simple console logger
log_level = logging.DEBUG
logging.basicConfig(level=log_level)
logger = logging.getLogger("pharaoh_hieroglyphs")

# read in data again (doesn work without ? => store is unknown)
try:
    df = pd.read_csv("../data/egypt_pharaohs_dynasties.csv")
    df = df.drop(columns=['king_two_ladies', 'king_horus_gold'])
except Exception as e:
    logger.exception(
        "Callbacks dataframe creation - Exception of type %s occurred. Details: %s",
        type(e).__name__, str(e)
    )


def get_df_query_part(no):
    ''' Returns the df query result of the given dynasty number '''
    return df.query(f'dynasty_no == {no}')


def get_dynasty_df(dyn_no):
    ''' Returns the prepared dataframe of specific dynasty given by integer parm dyn_no'''

    #dyn_no = dyn_no[0]
    logger.debug('get_dynasty_df - dyn_no param: %s', dyn_no)
    df_mod = get_df_query_part(dyn_no)

    # add image path name of plotly dash - /assets/images/ - to (svg) images
    # together with concept to create an image as cell content
    img_cols = [
        'image_local',
        'JSesh_birth_cartouche',
        'JSesh_throne_praenomen_cartouche',
    ]
    for col in img_cols:
        df_mod[col] = df_mod[col].apply(
            # add thumbnail renderer info
            lambda x: f"{dash.get_asset_url('images/' + str(x))}" if pd.notna(x) else x
        )
    
    return df_mod


def print_callback(debug_mode):
    """ Logs callback trigger info, used for debugging """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if debug_mode:
                logger.debug("--- Function called: %s", func.__name__)
                logger.debug("--- Triggered by: %s", dash.callback_context.triggered[0]['prop_id'])
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
    Output("all_periods", "href"),
    Input("all_periods", "n_clicks"),
)
@print_callback(log_level)
def search_all_periods(click_all_periods):
    if click_all_periods is None or click_all_periods == 0:
        return dash.no_update
    return f"/pages/all_periods/"


@callback(
    Output("store", "data", allow_duplicate=True),
    Input("First Dynasty", "n_clicks"),
    Input("Second Dynasty", "n_clicks"),
    prevent_initial_call='initial_duplicate',
)
@print_callback(log_level)
def search_page_dynasty(click_first, click_second):
    ''' 
        Do necessary preprocessing according dropdown value like "First Dynasty" 
        for store results in a dcc.Store in app instance of main.py.
        Returns selected dynasty layout page too, if clicked, nothing changed if not.
    '''
    item_clicked = ctx.triggered_id
    logger.debug('---  item_clicked: %s ---', item_clicked)
    
    if (click_first is None or click_first == 0) and (click_second is None or click_second == 0):
        return dash.no_update

    if item_clicked == "First Dynasty":
        dyn_no = 1,
    if item_clicked == "Second Dynasty":
        dyn_no = 2,

    try:
        df_mod = get_dynasty_df(dyn_no)  # delivers a tuple to function, why not integer ?
    except Exception as e:
        # toDo - fallback solution and user information
        logger.exception(
            "Creating Dynasty Dataframe - Exception of type %s occurred. Details: %s",
            type(e).__name__, str(e)
        )

    logger.debug('callback search_page_dynasty ===>  2 first rows of mod dataframe ...')
    logger.debug(df_mod.head(2))

    # return df dictionary
    return  df_mod.to_dict("records")


@callback(
    Output("store", "data", allow_duplicate=True),
    Input("early_dynastic_period", "n_clicks"),
    Input("old_kingdom", "n_clicks"),
    prevent_initial_call='initial_duplicate',
)
@print_callback(log_level)
def search_page_period(click_early, click_old):
    ''' 
        Do necessary preprocessing according dropdown value like "Early Dynastic Period" 
        for store results in a dcc.Store in app instance of main.py.
        Returns selected period layout page too, if clicked, nothing changed if not.
    '''
    item_clicked = ctx.triggered_id
    logger.debug('---  item_clicked: %s ---', item_clicked)
    
    if (click_early is None or click_early == 0) and (click_old is None or click_old == 0):
        return dash.no_update

    if item_clicked == "early_dynastic_period":
        dyn_no_list = [1, 2],
    if item_clicked == "old_kingdom":
        dyn_no_list = [3, 4, 5, 6],

    # list is first element of a tuple ?
    logger.debug('---  search_page_period:   dyn_no_list: %s', dyn_no_list[0])
    
    try:
        dfs = []
        for element in dyn_no_list[0]:
            logger.debug(f'-----> callback: search_page_period: element of dyn_no_list: {element}  -----')
            df = get_dynasty_df(element)
            dfs.append(df)

        df_mod = pd.concat(dfs)   
    except Exception as e:
        # toDo - fallback solution and user information
        logger.exception(
            "Creating Dynasty Dataframe - Exception of type %s occurred. Details: %s",
            type(e).__name__, str(e)
        )

    logger.debug('callback search_page_period ===>  2 last rows of mod dataframe ...')
    logger.debug(df_mod.tail(2))

    # return df dictionary
    return  df_mod.to_dict("records")
