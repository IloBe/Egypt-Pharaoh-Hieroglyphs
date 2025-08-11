# src/callbacks/dynasty_callbacks.py

"""
Callbacks for the dynasty page.

Note:
Separation of the callbacks is necessary for test logic. The callbacks.py file
shall not be on main.py level, because:
During testing by call of pytest, main Dash app object from src/app.py has not been created.
The register_page function has no app object to register itself with.
So it raises a Dash PageError:
dash.register_page() must be called after app instantiation.

But with pytest call, import of the test file (tests/test_callbacks.py) happens.
That file tries e.g. to import show_dynasty_image_modal from src/pages/dynasty.py.
To do this, Python must execute the dynasty.py file from top to bottom.
It immediately hits the register_page(...) line, which is at the top level of the module.
It needs the Dash app object to do the registration.
"""

##########################
# imports
##########################

from dash import MATCH, Input, Output, callback, html

##########################
# coding
##########################

@callback(
    Output({'type': 'dynasty-modal', 'id': MATCH}, "is_open"),
    Output({'type': 'dynasty-modal', 'id': MATCH}, "children"),
    Input({'type': 'dynasty-grid', 'id': MATCH}, "cellRendererData"),
    prevent_initial_call=True,
)
def show_dynasty_image_modal(cell_data):
    """Shows the image/cartouche in a modal when a cell is clicked."""
    if not cell_data:
        return False, None
    return True, html.Img(src = cell_data["value"], style = {'width': '100%'})
