#!/usr/bin/env -S python3 -i

"""
Web application about egypt pharaoh names and their dynasties. Main entry point.

The egypt_pharaohs_dynasties.csv dataset includes needed information about
names, transliterations and images
(https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs/blob/main/Egypt_Pharaoh_Hieroglyphs/data/egypt_pharaohs_dynasties.csv).
This csv file is stored in the general projects data directory.
On the landing page, some background information about the pharaoh names is given.
Then with the callback’s State argument we display a ... chart when a dynasty or specific period is selected. 

Note:
All relevant Python libraries are stored in the virtual environment which is activated to run this code.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import (
    Dash, dcc, html, Input, Output, State,
    callback, page_registry, page_container
)
from pages.layouts import get_header, get_footer

import dash
import dash_bootstrap_components as dbc
import sys
import logging
import pandas as pd

from app import app
from pages.not_found_404 import layout as layout_404
from pages.home import layout as layout_home
from pages.all_dynasties.all_dynasties import layout as layout_all_dynasties
from pages.first_dynasty.first_dynasty import layout as layout_first_dynasty

import callbacks
#import config  # necessary for future ML CV&classification feature dealing with own images

##########################
# coding
##########################

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")

# incorporate data
try:
    logging.info("Read in egypt hieroglyphs csv file")
    df = pd.read_csv("../data/egypt_pharaohs_dynasties.csv")
except Exception as e:
    logger.exception("Exit because exception of type %s occurred. Details: %s",
                     type(e).__name__, str(e))
    sys.exit(1)


#
# app layout
#
header = get_header(df)
footer = get_footer()
app.layout = dbc.Container(
    children =[
        dcc.Store(id="store", data={}),
        dcc.Location(id='url', refresh=False),
        header,
        #page_container,
        html.Div(id='page-content',),
        html.Hr(),
        footer,
        html.Br(),
    ],
    fluid=True,
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
)


#
# add controls to build the interaction
# 

# changes layout of the page based on the URL,
# read current URL page "http://127.0.0.1:8050/<page path - name>"
# and return associated layout
@app.callback(Output('page-content', 'children'),  #this changes the content
              [Input('url', 'pathname')])  #this listens for the url in use
def display_page(pathname):
    logging.info('--- Selected page path: %s ---', pathname)
    
    if pathname == '/':
        return layout_home
    elif pathname == '/pages/all_dynasties/':
        return layout_all_dynasties
    elif pathname == '/pages/first_dynasty/':
         return layout_first_dynasty
    else:
        # domain page not found, return 404 page
        return layout_404  


#
# run the app
#
if __name__ == '__main__':
   logging.info("Start pharaoh hieroglyphs app...") 
   app.run(debug=True)