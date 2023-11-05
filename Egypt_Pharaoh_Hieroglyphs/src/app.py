"""
Web application about egypt pharaoh names and their dynasties. Initialise the app instance.
More information is given with file main.py.

Set some security configurations (Cross Side Scripting, Cookieaccording this blog post:
https://www.securecoding.com/blog/flask-security-best-practices/
and
https://testdriven.io/blog/csrf-flask/

With meta tags configuration we protect the against cookie attack vectors.

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from cryptography.fernet import Fernet
from dash import Dash
import dash_bootstrap_components as dbc

##########################
# coding
##########################

#
# initialise the app
#
key = Fernet.generate_key()

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

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=meta_tags,
    use_pages=True,
    suppress_callback_exceptions=True,
)

