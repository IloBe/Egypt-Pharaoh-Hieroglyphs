# src/pages/dynasty.py

"""
Dynamic page generator for displaying a single Egyptian dynasty.
"""

##########################
# imports
##########################

import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

from dash import (
    MATCH, Input, Output, State,
    callback, dcc, html, no_update,
    register_page
)
from loguru import logger
from typing import Optional

from src.pages.layouts import (
    get_col_defs, get_default_col_def,
    get_grid_note, get_grid_style
)

from src.services.data_service import pharaoh_data_service

##########################
# coding
##########################

register_page(__name__, path_template = "/dynasty/<dynasty_id>")

def layout(dynasty_id: Optional[str] = None) -> html.Div:
    """Generates the complete layout for a specific dynasty page."""
    if not dynasty_id or not dynasty_id.isdigit():
        return html.Div(html.H4("Invalid Dynasty ID."))
    
    dynasty_no = int(dynasty_id)
    dynasty_data: pd.DataFrame = pharaoh_data_service.get_dynasty(dynasty_no)
    
    if dynasty_data.empty:
        return html.Div(html.H4(f"No data found for Dynasty {dynasty_no}."))

    details: pd.Series = dynasty_data.iloc[0]
    # up to dynasty 4 horus name is prominent
    throne_class = "king_horus" if dynasty_no < 5 else "king_sedge_bee"

    return html.Div(
        children = [
            html.Br(),
            html.H4(details['dynasty_name'], className = "fw-bolder"),
            html.H6(
                f"{details['calendar_period_start']} - {details['calendar_period_end']} BC, belongs to \"{details['kingdom_name']}\""
            ),
            html.Br(),
            dcc.Loading(
                id = f"loading-dynasty-{dynasty_no}",
                type = "circle",
                children = dag.AgGrid(
                    id = {'type': 'pharaoh-data-grid', 'id': f'dynasty-{dynasty_no}'},
                    rowData = dynasty_data.to_dict("records"),
                    columnDefs = get_col_defs(throne_class = throne_class),
                    defaultColDef = get_default_col_def(),
                    columnSize = "sizeToFit",
                    dashGridOptions = {"rowHeight": 64},
                    style = get_grid_style(),
                )
            ),
            get_grid_note(),
        ],
        className = "g-0 ps-5 pe-5",
    )
