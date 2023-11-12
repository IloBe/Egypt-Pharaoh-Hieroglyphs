"""
Web applications page not found content. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import (
    dcc, html, no_update, State,
    Input, Output, callback, register_page)
from ..layouts import get_default_col_def, get_col_defs

import dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import dash_mantine_components as dmc
import pandas as pd
import logging

##########################
# coding
##########################

dash.register_page(__name__,)

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")


grid_note = dcc.Markdown(
    """
**Note:**

- Click on image/cartouche to see it in a new window, click on keyboard 'Esc' or on
image/cartouche again to come back to this page.
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
            "Old Kingdom",
            className="fw-bolder text-decoration-underline opacity-75",
        ),
        html.H6('2686 - 2181 BC, includes 3rd, 4th, 5th & 6th Dynasties'),
        html.Br(),
        html.Div(id="grid-output-period_2"),
        dbc.Modal(id="custom-component-img-modal-period_2", size="s"),
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
    Output("grid-output-period_2", "children"),
    Input("store", "data"),
)
def update(store):
    logger.debug('-----  in old_kingdom:  update(store):  store: %s  -----', store)
    if store == {}:
        return "Have you selected old kingdom dropdown item? Dataset is empty ..."

    df_old_kingdom = pd.DataFrame(store)
    return dag.AgGrid(
                id='old_kingdom_img_dag',
                defaultColDef=get_default_col_def(),
                # only for old kingdom, rest is not mixed:
                # first 3 names are horus names, all others sdge bee ones
                columnDefs=get_col_defs(
                    # original distribution: {"king_horus": 3, "king_sedge_bee": 17}
                    throne_class= "king_sedge_bee"
                ),
                rowData=df_old_kingdom.to_dict("records"),
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
    Output("custom-component-img-modal-period_2", "is_open"),
    Output("custom-component-img-modal-period_2", "children"),
    Input('old_kingdom_img_dag', "cellRendererData"),
)
def show_change(data):
    ''' Shows image or cartouche on additional screen after click on such element '''
    if data:
        logger.debug('---  in old_kingdom: callback show_change(data):\n  ==> data: %s', data)
        return True, html.Img(src=data["value"])
    return False, None

