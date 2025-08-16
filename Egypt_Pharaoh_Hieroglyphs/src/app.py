# src/app.py

"""
Main entry point for the Dash application instance.

It initialices the Dash app, configures it with necessary
stylesheets and plugins (like Dash Pages) and sets meta tags.
"""

##########################
# imports
##########################

import dash_bootstrap_components as dbc

from pathlib import Path
from dash import Dash
from cryptography.fernet import Fernet
from src.logging_setup import logger

##########################
# coding
##########################

#
# initialise the app
#
key = Fernet.generate_key()
logger.info("Initializing Dash application instance.")

# general meta tags for the application
meta_tags = [
    # general
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
    # cookie protection
    {
        "name": "set-cookie",
        "content": "SESSION_COOKIE_SECURE=1",
    },
    {
        "name": "set-cookie",
        "content": "SESSION_COOKIE_HTTPONLY=1",
    },
    {
        "name": "set-cookie",
        "content": "",
    },
    {
        "name": "set-cookie",
        "content": f"SECRET_KEY={key}",
    },
]

# Plotly-Dash needs 'assets' dir for images
# src -> parent -> project_root -> dashboard/assets
ASSETS_PATH = Path(__file__).parent.parent / 'dashboard' / 'assets'      #'../dashboard/assets' - both possible

app = Dash(
    __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP],
    meta_tags = meta_tags,
    use_pages = True,                      # dash: True; relevant for modular pages router architecture
    suppress_callback_exceptions = True,   # False, for development
    assets_folder = ASSETS_PATH,
)

# server object needed for WSGI servers like Gunicorn/Uvicorn in production
# get underlying Flask server instance
server = app.server

