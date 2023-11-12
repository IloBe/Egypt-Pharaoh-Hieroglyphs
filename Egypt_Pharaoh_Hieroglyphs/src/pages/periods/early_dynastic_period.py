"""
Web applications page content of having selected first dynasties. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import (
    dcc, html, no_update, State,
    Input, Output, callback, register_page)
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import dash_mantine_components as dmc
import pandas as pd
import logging

##########################
# coding
##########################

dash.register_page(__name__)

# project path
#PROJ_PATH = Path(__file__).parent.parent.parent
#print(f'====   early dynatic period: PROJ_PATH: {PROJ_PATH}')
# local image path
#IMG_PATH = ''.join([str(PROJ_PATH), '/assets/images/'])
#print(f'====   early dynastic period: IMG_PATH: {IMG_PATH}')

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")

# image column filter params
objectFilterParams = {
    "filterOptions": ["contains", "notContains"],
    "debounceMs": 200,
    "suppressAndOrCondition": True,
}

# create table structure for visualisation data 
col_defs = [
    {
        "headerName": "Object",
        "stickyLabel": True,
        "field": "image_local",
        "cellRenderer": "ImgThumbnail",
        "width": 20,
        "height": 20,
        "filterParams": objectFilterParams,
    },
    {
        "headerName": "Throne Name",
        "stickyLabel": True,
        "children": [
            {
                "field": "king_horus", 
                "headerName": "Horus", 
                "width": 70
            },
            {
                "field": "king_sedge_bee",
                "headerName": "Sedge Bee",
                "width": 50
            },
        ],
    },
    {
        "headerName": "Birth Name",
        "stickyLabel": True,
        "children": [
            {
                "field": "king_birth_son_of_ra",
                "headerName": "Son of Ra",
                "width": 70,
            },
        ]
    },
    {
        "headerName": "Name Transliteration",
        "stickyLabel": True,
        "children": [
            {
                "field":  "king_birth_son_of_ra",
                "headerName": "Birth",
                "width": 50,
                "height": 10,
                "cellStyle": {
                    'font-family': 'Trlit_CG Times',
                    'font-size': 20,
                },
                "filter": False,
            },
            {
                "field": "king_horus",
                "headerName": "Throne",
                "width": 50,
                "height": 10,
                "cellStyle": {
                    'font-family': 'Trlit_CG Times',
                    'font-size': 20,
                },
                "filter": False,
            },
        ],
    },
    {
        "headerName": "Cartouche",
        "stickyLabel": True,
        "children": [
            {
                "field": "JSesh_birth_cartouche",
                "headerName": "Birth",
                "cellRenderer": "ImgThumbnail",
                "width": 20,
                "height": 10,
                "filter": False,
            },
            {
                "field": "JSesh_throne_praenomen_cartouche",
                "headerName": "Throne",
                "cellRenderer": "ImgThumbnail",
                "width": 20,
                "height": 10,
                "filter": False,
            },
        ],
    },
]

defaultColDef = {
    "flex": 1,
    "filter": True,
}

grid_note = dcc.Markdown(
    """
**Note:**

- Click on image/cartouche to see it in a new window, click on keyboard 'Esc' or on
image/cartouche again to come back to this page.
- To filter on Object column, enter i(mage) in the editable filter text field.
- If you don't see the diacritic transliteration marks, check if you have installed the
[CGT_2023.TTF font](https://dmd.wepwawet.nl/fonts.htm) file properly.
    """
)


# subtitle includes BC calendar period and period kingdom name
layout = html.Div(
    children = [
        html.Br(),
        html.H4(
            "Early Dynastic Period",
            className="fw-bolder text-decoration-underline opacity-75",
        ),
        html.H6('3100 - 2686 BC, includes 1st & 2nd Dynasty'),
        html.Br(),
        html.Div(id="grid-output-period_1"),
        dbc.Modal(id="custom-component-img-modal-period_1", size="s"),
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
    Output("grid-output-period_1", "children"),
    Input("store", "data"),
)
def update(store):
    logger.debug('-----  in early_dynastic_period:  update(store):  store: %s  -----', store)
    if store == {}:
        return "Have you selected early dynastic period dropdown item? Dataset is empty ..."

    df_early_period = pd.DataFrame(store)
    return dag.AgGrid(
                id='early_dynastic_period_img_dag',
                defaultColDef = defaultColDef,
                columnDefs=col_defs,
                rowData=df_early_period.to_dict("records"),
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
    Output("custom-component-img-modal-period_1", "is_open"),
    Output("custom-component-img-modal-period_1", "children"),
    Input('early_dynastic_period_img_dag', "cellRendererData"),
)
def show_change(data):
    if data:
        logger.debug(' ==> early_dynastic_period.py  callback show_change(data):\n   ==> data: %s', data)
        return True, html.Img(src=data["value"])
    return False, None
