# src/pages/all_periods.py

"""
Layout for displaying all periods as a wrapper around the shared browse_all layout.
"""

##########################
# imports
##########################

from dash import register_page
from src.pages.layouts import create_browse_all_layout

##########################
# coding
##########################

register_page(__name__)
layout = create_browse_all_layout(title = "All Periods")