"""
Web applications page content of having selected dynasties. 

Author: Ilona Brinkmeier
Date: Nov. 2023
"""

##########################
# imports
##########################

from dash import (
    dcc, html, no_update,
    Input, Output, callback, register_page)
from ..layouts import get_default_col_def, get_col_defs

import dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
import logging

##########################
# coding
##########################

dash.register_page(__name__)

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")


grid_note = dcc.Markdown(
    """
**Note:**
- Click on image/cartouche to see it in a new window, click on keyboard 'Esc' or image/cartouche again 
to come back to this page.
- To filter on Object column, enter i(mage) in the editable filter text field.
- If you don't see the diacritic transliteration marks, check if you have installed the
[CGT_2023.TTF font](https://dmd.wepwawet.nl/fonts.htm) file properly.
- Sneferu image created by [Carina Felske](https://www.selket.de/), shown with permission.
    """
)


# subtitle includes BC calendar period and period kingdom name
layout = html.Div(
    children = [
        html.Br(),
        html.H4(
            "Fourth Dynasty",
            className="fw-bolder text-decoration-underline opacity-75",
        ),
        html.H6('2613 - 2494 BC, belongs to the "Old Kingdom"'),
        html.Br(),
        html.Div(id="grid-output_4"),
        dbc.Modal(id="custom-component-img-modal_4", size="s"),
        html.Div(grid_note),
        html.Br(),
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)


#
# add controls to build the interaction
# 

@callback(
    Output("grid-output_4", "children"),
    Input("store", "data"),
)
def update(store):
    if store == {}:
        return "Have you selected fourth dynasty dropdown item? Dataset is empty ..."
        
    df_dyn = pd.DataFrame(store)
    logger.debug('-----  in fourth dyn: callback update(store): store: %s -----', store)

    return dag.AgGrid(
                id='fourth_dynasty_img_dag',
                defaultColDef=get_default_col_def(),
                columnDefs=get_col_defs(throne_class="king_sedge_bee"),
                rowData=df_dyn.to_dict("records"),
                dashGridOptions={"rowHeight": 64},
                style={
                    # see e.g.
                    # https://www.color-hex.com/color/bdb8a4  (french green)
                    # https://www.color-hex.com/color/000000  (black)
                    '--ag-header-background-color': '#d3d0c2',
                    '--ag-header-foreground-color': '#666666',
                    'height': '550px',
                },
                columnSize="sizeToFit",  # 'autoSize',
           )

@callback(
    Output("custom-component-img-modal_4", "is_open"),
    Output("custom-component-img-modal_4", "children"),
    Input('fourth_dynasty_img_dag', "cellRendererData"),
)
def show_change(data):
    ''' Shows image or cartouche on additional screen after click on such element '''
    if data:
        logger.debug('--- in fourth dyn: callback show_change(data):\n  ==> data: %s  -----', data)
        return True, html.Img(src=data["value"])
    return False, None
