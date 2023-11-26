#!/usr/bin/env -S python3 -i

"""
Web application about egypt pharaoh names and their dynasties. Main entry point.

The egypt_pharaohs_dynasties.csv dataset includes needed information about
names, transliterations and images
(https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs/blob/main/Egypt_Pharaoh_Hieroglyphs/data/egypt_pharaohs_dynasties.csv).
This csv file is stored in the general projects data directory.
On the landing page, some background information about the pharaoh names is given.
Then with the callback’s Input, Output arguments we display another page when a dynasty or period is selected. 

Note:
All relevant Python libraries are stored in the virtual environment which is activated to run this code.
Regarding Cross-Site Request Forgery (CSRF) protection, which is an attack that uses the
victim’s credentials to perform undesired actions on behalf of the victim, by default this protection is
automatically applied to all forms in a Dash app. The CSRF token is included in the form submission and
validated on the server side to prevent cross-site request forgery attacks.
Furthermore, this main.py file is modified, so, SSL handling can be activated if cert files are available.

Author: Ilona Brinkmeier
Date: Nov. 2023
"""

##########################
# imports
##########################

from dash import (
    Dash, dcc, html, Input, Output, State,
    callback, page_registry, page_container
)
from flask_wtf.csrf import CSRFProtect

from app import app
from pages.layouts import get_header, get_footer
from pages.not_found_404 import layout as layout_404
from pages.home import layout as layout_home
from pages.dynasties.all_dynasties import layout as layout_all_dynasties
from pages.dynasties.first_dynasty import layout as layout_first_dynasty
from pages.dynasties.second_dynasty import layout as layout_second_dynasty
from pages.dynasties.third_dynasty import layout as layout_third_dynasty
from pages.dynasties.fourth_dynasty import layout as layout_fourth_dynasty
from pages.dynasties.fifth_dynasty import layout as layout_fifth_dynasty
from pages.dynasties.sixth_dynasty import layout as layout_sixth_dynasty
from pages.dynasties.seventh_dynasty import layout as layout_seventh_dynasty
from pages.dynasties.eighth_dynasty import layout as layout_eighth_dynasty
from pages.dynasties.ninth_dynasty import layout as layout_ninth_dynasty
from pages.dynasties.tenth_dynasty import layout as layout_tenth_dynasty
from pages.dynasties.eleventh_dynasty import layout as layout_eleventh_dynasty
from pages.periods.all_periods import layout as layout_all_periods
from pages.periods.early_dynastic_period import layout as layout_early_dynastic_period
from pages.periods.old_kingdom import layout as layout_old_kingdom

import ssl
import dash
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import sys
import logging
import pandas as pd

import callbacks
#import config  # necessary for future ML CV&classification feature dealing with own images

##########################
# coding
##########################

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")

# create an SSL context  (future toDo: certificate and key files don't exist yet)
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#ssl_context.load_cert_chain(certfile='path/to/certificate.pem', keyfile='path/to/private_key.pem'

# incorporate data
try:
    logging.info("Read in egypt hieroglyphs csv file")
    df = pd.read_csv("../data/egypt_pharaohs_dynasties.csv")

    # remove empty columns
    df = df.drop(columns=['king_two_ladies', 'king_horus_gold'])

except Exception as e:
    logger.exception("Exit because exception of type %s occurred. Details: %s",
                     type(e).__name__, str(e))
    sys.exit(1)

logging.info('--- MAIN: Dataset content overview ...\n %s \n----------', df.info())

    
def get_dynasty_names(start_no, end_no):
    ''' Returns specific dynasties from start up to end params as unique list '''
    dynasty_list = df.query('@start_no <= dynasty_no <= @end_no')['dynasty_name'].unique()
    return dynasty_list
    
first_dynasty_names = get_dynasty_names(1,9)
decimal_dynasty_names = get_dynasty_names(10,19)
twenties_dynasty_names = get_dynasty_names(20,29)


#
# app layout
#

# for local image see: https://dash.plotly.com/dash-enterprise/static-assets?de-version=5.1
echnaton_nofretete_img_path = app.get_asset_url(
    'images/EchnatonNofretete_AegyptischesMuseumBerlin_small-18.PNG'
)
header = get_header(echnaton_nofretete_img_path,
                    first_dynasty_names, decimal_dynasty_names, twenties_dynasty_names)
footer = get_footer()
app.layout = dbc.Container(
    children =[
        dcc.Location(id='url', refresh='callback-nav'),
        dcc.Store(id="store", data={}),
        header,
        #dmc.Container(page_container),
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
# read current URL page "http://127.0.0.1:8050/<page path - name.py>"
# and return associated layout
@app.callback(Output('page-content', 'children'),  # changes the content
              [Input('url', 'pathname')])          # listens for the url in use
def display_page(pathname):
    logger.info('--- MAIN - Selected page path: %s ---', pathname)
    
    if pathname == '/':
        return layout_home
    elif pathname == '/pages/periods/all_periods.py':
        return layout_all_periods
    elif pathname == '/pages/periods/early_dynastic_period.py':
        return layout_early_dynastic_period
    elif pathname == '/pages/periods/old_kingdom.py':
        return layout_old_kingdom
    elif pathname == '/pages/dynasties/all_dynasties.py':
        return layout_all_dynasties
    elif pathname == '/pages/dynasties/first_dynasty.py':
        return layout_first_dynasty
    elif pathname == '/pages/dynasties/second_dynasty.py':
        return layout_second_dynasty
    elif pathname == '/pages/dynasties/third_dynasty.py':
        return layout_third_dynasty
    elif pathname == '/pages/dynasties/fourth_dynasty.py':
        return layout_fourth_dynasty
    elif pathname == '/pages/dynasties/fifth_dynasty.py':
        return layout_fifth_dynasty
    elif pathname == '/pages/dynasties/sixth_dynasty.py':
        return layout_sixth_dynasty
    elif pathname == '/pages/dynasties/seventh_dynasty.py':
        return layout_seventh_dynasty
    elif pathname == '/pages/dynasties/eighth_dynasty.py':
        return layout_eighth_dynasty
    elif pathname == '/pages/dynasties/ninth_dynasty.py':
        return layout_ninth_dynasty
    elif pathname == '/pages/dynasties/tenth_dynasty.py':
        return layout_tenth_dynasty
    elif pathname == '/pages/dynasties/eleventh_dynasty.py':
        return layout_eleventh_dynasty
    else:
        # domain page not found, return 404 page
        return layout_404  


#
# run the app
#
if __name__ == '__main__':
    logger.info(" ***  Start pharaoh hieroglyphs app...  *** ")
    # run on local machine with default http://127.0.0.1:8050/
    app.run(debug=True)

    # run the app on server with SSL/TLS encryption
    #app.run_server(ssl_context=ssl_context)