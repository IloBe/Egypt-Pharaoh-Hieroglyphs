# src/callbacks/period_callbacks.py

"""
Callbacks for the period page.
"""

##########################
# imports
##########################

from dash import MATCH, Input, Output, callback, html

##########################
# coding
##########################

@callback(
    Output({'type': 'period-modal', 'id': MATCH}, "is_open"),
    Output({'type': 'period-modal', 'id': MATCH}, "children"),
    Input({'type': 'period-grid', 'id': MATCH}, "cellRendererData"),
    prevent_initial_call = True,
)
def show_period_image_modal(cell_data):
    """Shows the image/cartouche in a modal when a cell is clicked."""
    if not cell_data:
        return False, None
    return True, html.Img(src = cell_data["value"], style = {'width': '100%'})