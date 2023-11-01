#!/usr/bin/env -S python3 -i

"""
Web applications page content of having selected second dynasties. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import (
    dcc, html, no_update,
    Input, Output, callback, register_page)
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
import logging

##########################
# coding
##########################

#dash.register_page(__name__, path="/pages/first_dynasty/")
#dash.register_page(__name__)


# project path
PROJ_PATH = Path(__file__).parent.parent.parent
print(f'====   second dyn: PROJ_PATH: {PROJ_PATH}')
# local image path
IMG_PATH = ''.join([str(PROJ_PATH), '/assets/images/'])
print(f'====   second dyn: IMG_PATH: {IMG_PATH}')


# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")

# create table structure for visualisation data 
col_defs = [
    {
        "headerName": "Object",
        "stickyLabel": True,
        "field": "image_local",
        "cellRenderer": "ImgThumbnail",
        "width": 20,
        "height": 20,
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
                }
            },
            {
                "field": "image_throne_transliteration",
                "headerName": "Throne",
                "width": 50,
                "height": 10,
                "cellStyle": {
                    'font-family': 'Trlit_CG Times',
                    'font-size': 20,
                }
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
            },
            {
                "field": "JSesh_throne_praenomen_cartouche",
                "headerName": "Throne",
                "cellRenderer": "ImgThumbnail",
                "width": 20,
                "height": 10,
            },
        ],
    },
]


# subtitle includes BC calendar period and period kingdom name
layout = html.Div(
    children = [
        html.Br(),
        html.H4(
            "Second Dynasty",
            className="fw-bolder text-decoration-underline opacity-75",
        ),
        html.H6('2890 - 2686 BC, belongs to "Early Dynastic Period"'),
        html.Br(),
        html.Div(id="grid-output_2"),
        dbc.Modal(id="custom-component-img-modal_2", size="s"),
        html.H6("Click on image/cartouche to see it in a new window, click on keyboard 'Esc' or image/cartouche again to come back to this page."),
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
    Output("grid-output_2", "children"),
    Input("store", "data"),
)
def update(store):
    if store == {}:
        return "Have you selected second dynasty dropdown item? Dataset is empty ..."
        
    df_first_dyn = pd.DataFrame(store)
    print('-------------------------------------')
    birth_cartouches = df_first_dyn['JSesh_birth_cartouche'].tolist()
    data_dict = df_first_dyn.to_dict('records')
    logger.info('sec dyn: data dict: %s', data_dict)
    logger.info('sec dyn: birth cartouche img sequence: %s', birth_cartouches)
    print('-------------------------------------')

    return dag.AgGrid(
                id='second_dynasty_img_dag',
                columnDefs=col_defs,
                rowData=df_first_dyn.to_dict("records"),
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
    Output("custom-component-img-modal_2", "is_open"),
    Output("custom-component-img-modal_2", "children"),
    Input('second_dynasty_img_dag', "cellRendererData"),
)
def show_change(data):
    if data:
        logger.info(f' ==> Sec Dyn Page callback: show_change: ==> data: %s', data)
        return True, html.Img(src=data["value"])
    return False, None
