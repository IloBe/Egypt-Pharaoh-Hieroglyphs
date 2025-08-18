# src/pages/period.py

"""
Dynamic page generator for displaying a single Egyptian period.
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
from urllib.parse import unquote
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

register_page(__name__, path_template = "/period/<period_name_url>")

def layout(period_name_url: Optional[str] = None) -> html.Div:
    """Generates the static shell layout for a specific period page."""
    if not period_name_url:
        return html.Div(html.H4("No period specified."))
        
    period_name: str = unquote(period_name_url.replace('_', ' '))
    period_data: pd.DataFrame = pharaoh_data_service.get_period(period_name)
    
    if period_data.empty:
        return html.Div(html.H4(f"Sorry, no data was found for the period: {period_name}."))

    if 'king_horus' in period_data and 'king_sedge_bee' in period_data:
        period_data['throne_name_display'] = period_data['king_horus'].combine_first(period_data['king_sedge_bee'])
        throne_class = 'throne_name_display'
    else:
        throne_class = 'king_sedge_bee'

    return html.Div(
        children = [
            html.Br(),
            html.H4(period_name, className = "fw-bolder"),
            html.Br(),
            dcc.Loading(
                id = f"loading-period-{period_name_url}",
                type = "circle",
                children = dag.AgGrid(
                    id={'type': 'pharaoh-data-grid', 'id': f'period-{period_name_url}'},
                    rowData = period_data.to_dict("records"),
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
