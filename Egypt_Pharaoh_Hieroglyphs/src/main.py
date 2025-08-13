# src/main.py

"""
Main application entry point.

It initialises the Dash application, registers all callbacks,
defines the overall page layout structure and runs the web server.
"""

##########################
# imports
##########################

import dash
import dash_bootstrap_components as dbc
from dash import (
    dcc, html, page_container,
    no_update,callback,
    MATCH, ALL,
    Input, Output, State
)
from loguru import logger
from typing import List, Dict, Any, Tuple, Optional, Literal

from src.app import app, server
from src.callbacks import dynasty_callbacks, period_callbacks
from src.pages.layouts import get_footer, get_header, create_pharaoh_detail_card

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
            page_container,  # dynamic pages content to be rendered, router target
            html.Hr(),
            get_footer(),
            html.Br(),
            
            # add new detailed info card
            dbc.Modal(
                id = "pharaoh-detail-modal",
                children = html.Div(id = "detail-modal-content-wrapper"), # static clickable wrapper
                is_open = False,
                size = "lg",       # large disply size for details
                centered = True,
                scrollable = True, # scrolling for long content
            ),
            
            # add second, smaller modal to show enlarged images
            dbc.Modal(
                id = "image-view-modal",
                children = html.Div(id = "image-modal-content-wrapper"), # static clickable wrapper
                is_open = False,
                size = "s",  # small, centered look
                centered = True,
            ),
            
            # add a dummy Div for callback, without it
            # throws MismatchedIdException for ID browse-all-grid- parts
            html.Div(
                id = 'dummy-div-for-callback',
                style = {'display': 'none'}
            ),
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
    # render a simple error page
    app.layout = html.Div([
        html.H1("Critical Layout Error"),
        html.P("The main application layout failed to build. Please check the logs."),
        html.Pre(f"{e}")
    ])


# single global callback for all grid cell clicks (image, text)
@callback(
    Output("pharaoh-detail-modal", "is_open"),
    Output("detail-modal-content-wrapper", "children"),
    Output("image-view-modal", "is_open"),
    Output("image-modal-content-wrapper", "children"),
    Input({'type': 'pharaoh-data-grid', 'id': ALL}, "cellClicked"),
    Input({'type': 'pharaoh-data-grid', 'id': ALL}, "cellRendererData"),
    State({'type': 'pharaoh-data-grid', 'id': ALL}, "rowData"),
    State("image-view-modal", "is_open"),
    State("pharaoh-detail-modal", "is_open"),
    prevent_initial_call=True,
)
def handle_all_grid_clicks(
    cell_clicked_list: List[Optional[Dict[str, Any]]], 
    cell_renderer_list: List[Optional[Dict[str, Any]]],
    all_row_data: List[List[Dict[str, Any]]],
    image_modal_is_open: bool,
    detail_modal_is_open: bool
) -> Tuple[
    bool | Literal[no_update],
    dbc.Card | Literal[no_update],
    bool | Literal[no_update],
    html.Img | Literal[no_update]
]:
    """
    Handles all cell clicks from any pharaoh data grid page of the application.
    It uses rowIndex from cellClicked to look up full row data from grid's rowData state.
    """
    ctx = dash.ctx
    if not ctx.triggered_id:
        return no_update, no_update, no_update, no_update

    triggered_prop = ctx.triggered[0]['prop_id']
    triggered_value = ctx.triggered[0]['value']

    if not triggered_value:
        return no_update, no_update, no_update, no_update

    #
    # route logic based on fired event
    #
    # Case 1: clicked Image cell (from custom JS component)
    if "cellRendererData" in triggered_prop:
        image_src = triggered_value.get("value")
        if not image_src:
            return no_update, no_update, no_update, no_update
        
        logger.debug(f"Image click detected. Toggling image viewer for: {image_src}")
        return no_update, no_update, not image_modal_is_open, html.Img(src = image_src, style = {'width': '100%'})

    # Case 2: clicked Text cell
    elif "cellClicked" in triggered_prop:
        row_index = triggered_value.get("rowIndex")
        if row_index is None:
            return no_update, no_update, no_update, no_update

        # dict ID of specific clicked grid
        triggered_id = ctx.triggered_id
        
        # list of all context grid IDs
        all_grid_ids = [component['id'] for component in ctx.inputs_list[0]]
        
        try:
            # find grid index to get associated rowData
            grid_index = all_grid_ids.index(triggered_id)
        except ValueError:
            logger.error(f"Could not find triggered_id {triggered_id} in the list of grid IDs.")
            return no_update, no_update, no_update, no_update
        
        # Get the specific rowData for the grid that was clicked
        target_rowData = all_row_data[grid_index]
        if not target_rowData or row_index >= len(target_rowData):
            logger.error(f"Row index {row_index} is out of bounds for the target grid's data.")
            return no_update, no_update, no_update, no_update

        pharaoh_data = target_rowData[row_index]
        pharaoh_name = pharaoh_data.get('king_birth_son_of_ra', 'Unknown Pharaoh')
        logger.info(f"Text cell click detected. Displaying details for: {pharaoh_name}")
        
        detail_card = create_pharaoh_detail_card(pharaoh_data)
        logger.info(f"Pharaoh detail card is toggled.")
        return not detail_modal_is_open, detail_card, no_update, no_update
    
    return no_update, no_update, no_update, no_update


# callbacks for image and details card handling of UI vanishing
@callback(
    Output("image-view-modal", "is_open", allow_duplicate = True),
    Input("image-modal-content-wrapper", "n_clicks"),
    State("image-view-modal", "is_open"),
    prevent_initial_call=True,
)
def close_image_modal_on_click(
    n_clicks: Optional[int], 
    is_open: bool
) -> bool | Literal[no_update]:
    """Closes the image modal if its content is clicked while open."""
    if n_clicks and is_open:
        return False
    return no_update

@callback(
    Output("pharaoh-detail-modal", "is_open", allow_duplicate = True),
    Input("detail-modal-content-wrapper", "n_clicks"),
    State("pharaoh-detail-modal", "is_open"),
    prevent_initial_call=True,
)
def close_detail_modal_on_click(
    n_clicks: Optional[int], 
    is_open: bool
) -> bool | Literal[no_update]:
    """Closes the detail modal if its content is clicked while open."""
    if n_clicks and is_open:
        return False
    return no_update
    

if __name__ == '__main__':
    logger.info("\nStarting Pharaoh Hieroglyphs WSGI application server...")
    app.run(debug = True, host = '0.0.0.0')