# src/main.py

"""
Main application entry point.

It initialises the Dash application,
defines the overall page layout structure and runs the web server.
"""

##########################
# imports
##########################

import dash_bootstrap_components as dbc
from dash import dcc, html, page_container
from loguru import logger

from src.app import app, server
from src.pages.layouts import get_footer, get_header
from src.callbacks import dynasty_callbacks, period_callbacks

##########################
# coding
##########################

# --- Main App Layout ---
# `page_container` is central Dash pages location to render active page content

try:
    logger.info("Main.py - Assembling main application layout.")
    app.layout = dbc.Container(
        children = [
            get_header(),
            page_container,  # dynamic pages content to be rendered
            html.Hr(),
            get_footer(),
            html.Br(),
        ],
        fluid = True,
        style = {
            'background-color': '#f7f7f4',
            'background-size': '100%',
            'padding': 5,
        },
    )
    logger.success("Main layout assembled successfully.")
except Exception as e:
    logger.critical(f"Failed to assemble layout from main.py app.layout. Application cannot start. Error: {e}")
    # render a simple error page.
    app.layout = html.Div([
        html.H1("Critical Layout Error"),
        html.P("The main application layout failed to build. Please check the logs."),
        html.Pre(f"{e}")
    ])

if __name__ == '__main__':
    logger.info("\nStarting Pharaoh Hieroglyphs application server...")
    app.run(debug = True, host = '0.0.0.0')