#!/usr/bin/env -S python3 -i

"""
Web applications pages header and footer content. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import dcc, html
from dash_iconify import DashIconify
from app import app

import dash
import dash_bootstrap_components as dbc

##########################
# coding
##########################

#
# header
#
def get_header(df):
    """
    Returns the navbar header with introduction title, home icon and dropdowns.
    """
    # for local image see: https://dash.plotly.com/dash-enterprise/static-assets?de-version=5.1
    ECHNATON_NOFRETETE = app.get_asset_url('images/EchnatonNofretete_AegyptischesMuseumBerlin_small-18.PNG')
    
    def get_dynasty_names(start_no, end_no):
        dynasty_list = df.query('@start_no <= dynasty_no <= @end_no')['dynasty_name'].unique()
        return dynasty_list
        
    first_dynasty_names = get_dynasty_names(1,9)
    decimal_dynasty_names = get_dynasty_names(10,19)
    twenties_dynasty_names = get_dynasty_names(20,29)
    
    
    # for dropdown's see:
    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/dropdown_menu/
    dynasty_items = [
        dbc.DropdownMenuItem(
            'All',
            id='all_dynasties',
            n_clicks=0,
            href='/pages/all_dynasties/',
        ),
        dbc.DropdownMenu(
            id='first_dynasty',
            children=[
                dbc.DropdownMenuItem(
                    name,
                    id=name,
                    n_clicks=0,
                    href='/pages/first_dynasty/',
                ) for name in first_dynasty_names
            ],
            label='1st Dynasties',
            toggle_style={
                #"textTransform": "uppercase",
                # https://creativebooster.net/blogs/colors/shades-of-green-color
                # https://creativebooster.net/blogs/colors/shades-of-azure-color
                # https://www.color-hex.com/color/b6b19a
                # Tints of french grey, French Grey, color Azure Sky
                "background": '#E1DFD6',   # '#dad8cc'  # '#B6B19A'   # "#B0E0F6",  
                'color': 'black',
            },
            className="px-1",
            align_end=True,
        ),    
        dbc.DropdownMenu(
            id='decimal_dynasties',
            children=[
                dbc.DropdownMenuItem(name, id=name, n_clicks=0) for name in decimal_dynasty_names
            ],
            label='10th Dynasties',
            toggle_style={
                # Tints of french grey, French Grey, color Azure Sky
                "background": '#E1DFD6', 
                'color': 'black',
            },
            className="mt-1 px-1",
            align_end=True,
        ),
        dbc.DropdownMenu(
            id='twenties_dynasties',
            children=[
                dbc.DropdownMenuItem(name, id=name, n_clicks=0) for name in twenties_dynasty_names
            ],
            label='20s Dynasties',
            toggle_style={
                # Tints of french grey, French Grey, color Azure Sky
                "background": '#E1DFD6',
                'color': 'black',
            },
            className="mt-1 px-1",
            align_end=True,
        ),
        dbc.DropdownMenu(
            id='thirties_dynasties',
            children=[
                dbc.DropdownMenuItem(
                    "Thirtieth Dynasty",
                    id='thirtith_dynasty',
                    n_clicks=0),
                dbc.DropdownMenuItem(
                    "Thirty-First Dynasty",
                    id='thirtyfirst_dynasty',
                    n_clicks=0),
            ],
            label='30s Dynasties',
            toggle_style={
                # Tints of french grey, color Azure Sky
                "background": '#E1DFD6',
                'color': 'black',
            },
            className="mt-1 px-1",
            align_end=True,
        ),
    ]
    
    period_items = html.Div(
        children = [
            dbc.DropdownMenuItem(
                'All',
                id='all_periods',
                n_clicks=0,
            ),
            dbc.DropdownMenuItem("Early Dynastic Period"),
            dbc.DropdownMenuItem("Old Kingdom"),
            dbc.DropdownMenu(
                id='first_intermediate',
                children=[
                    dbc.DropdownMenuItem("First Intermediate Period - general"),
                    dbc.DropdownMenuItem("First Intermediate Period - Thebes only"),
                ],
                label='First Intermediate Period',
                toggle_style={
                    # Tints of french grey, French Grey, color Azure Sky
                    "background": '#E1DFD6',
                    'color': 'black',
                },
                className="px-1",
                align_end=True,
            ),
            dbc.DropdownMenuItem("Middle Kingdom"),
            dbc.DropdownMenu(
                id='second_intermediate',
                children=[
                    dbc.DropdownMenuItem("Second Intermediate Period - Hyksos"),
                    dbc.DropdownMenuItem("Second Intermediate Period - rulers based in Thebes"),
                ],
                label='Second Intermediate Period',
                toggle_style={
                    "background": '#E1DFD6',
                    'color': 'black',
                },
                className="px-1",
                align_end=True,
            ),
            dbc.DropdownMenuItem("New Kingdom"),
            dbc.DropdownMenu(
                id='third_intermediate',
                children=[
                    dbc.DropdownMenuItem("Third Intermediate Period - Tanite"),
                    dbc.DropdownMenuItem("Third Intermediate Period - Bubastite/Libyan"),
                    dbc.DropdownMenuItem("Third Intermediate Period - Tanite/Libyan"),
                    dbc.DropdownMenuItem("Third Intermediate Period - General"),
                    dbc.DropdownMenuItem("Third Intermediate Period - Kushite"),
                ],
                label='Third Intermediate Period',
                toggle_style={
                    "background": '#E1DFD6',
                    'color': 'black',
                },
                className="px-1",
                align_end=True,
            ),
            dbc.DropdownMenu(
                id='late_period',
                children=[
                    dbc.DropdownMenuItem("Late Period - General First"),
                    dbc.DropdownMenuItem("Late Period - First Persian Period"),
                    dbc.DropdownMenuItem("Late Period - General Second"),
                    dbc.DropdownMenuItem("Late Period - Second Persian Period"),
                ],
                label='Late Period',
                toggle_style={
                    "background": '#E1DFD6',
                    'color': 'black',
                },
                className="mt-1 px-1",
                align_end=True,
            ),
        ],
    )
    
    dynasties_dropdown = dbc.DropdownMenu(
        id='dynasties_dropdown',
        children=dynasty_items,
        label="Dynasties",
        toggle_style={"background": "black"},
        in_navbar=True,
        align_end=True,
    ),
    
    periods_dropdown = dbc.DropdownMenu(
        id='periods_dropdown',
        children=period_items,
        label="Periods",
        toggle_style={"background": "black"},
        className="border border-0",
        in_navbar=True,
        align_end=True,
    ),
    
    selection_bar = dbc.Row(
        children=[
            dbc.Col(
                dbc.NavItem(
                    dbc.Button(
                        children=[
                            DashIconify(
                                icon='bi:house',
                                width=20,
                                height=20,
                                color='white',
                            ),
                        ],
                        id="button_link_home",
                        n_clicks=0,
                        outline=True,
                        color= "primary",
                        href="/"
                    ),
                ),
                className="me-auto px-2",
                align='end',
                style={'color': 'bg-dark'}
            ),
            dbc.Col(
                periods_dropdown,
                className="me-auto",
                align='end',
                style={'color': 'dark'},
            ),
            dbc.Col(
                dynasties_dropdown,
                className="me-auto px-2",
                align='end',
            ),
        ],
        className="g-0 ms-auto",
        align="end",
    )
    
    
    # horizontally aligned navigation bar at the top of the page
    # right block - egyptian image and brand title
    # left block - dropdown menues and plotly icon
    navbar = dbc.Navbar(
        dbc.Container(
            [
                # left block for introduction title
                html.Div(
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.Img(
                                        src=ECHNATON_NOFRETETE,
                                        height="110px",
                                    ),
                                ],
                                width='auto',
                            ),
                            dbc.Col(
                                children=[
                                    html.H1(
                                        id="navbar-title",
                                        children=["Egyptian Pharaoh's"],
                                        style={"color" : "white", 'padding': 5},
                                    ),
                                    html.H5(
                                        id="navbar-subtitle",
                                        children=["BC dynasties from early up to late period"],
                                        style={"color" : "white", 'padding': 5},
                                    ),
                                ],
                                className='px-1'
                            ),
                        ],
                        align="end",
                        className="ps-0",
                    ),
                ),
                # right block for user selection 
                dbc.Col(
                    children=[
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            selection_bar,
                            id="navbar-collapse",
                            navbar=True,
                        ),
                    ],
                    align="end",
                    className="mb-2",
                ),
            ],
        ),
        color="black",
        dark=True,
        sticky='top',
        expand='lg',
    )

    return navbar


#
# footer
#
def get_footer():
    """
    Returns the footer with github and plotly icons together with licence and author information. 
    """
    return html.Div(
        children = [
            dbc.Row(
                children = [
                    dbc.Col(
                        children = [
                            html.A(
                                [
                                    DashIconify(
                                        icon='charm:github',
                                        width=20,
                                        height=20,
                                        color='#000000',  # black; origin default: blue
                                    ),
                                ],
                                href='https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs',
                            ),
                            html.H6(
                                children=['MIT Licence, I. Brinkmeier 2023'],
                                style={"display": "inline"},
                                className='px-2',
                            ),
                        ],
                        width=11,
                        className="text-muted fs-6",
                        style = {'float': 'right'},
                    ),
                    dbc.Col(
                        children = [
                            html.A(
                                [
                                    html.Img(
                                        src='https://global.discourse-cdn.com/business7/uploads/plot/original/3X/f/3/f3da33405ee7e693abfd12bd4ae334a55e8345d0.png',
                                        height='25px',
                                    ),
                                ],
                                href='https://dash.plotly.com/',
                            ),
                        ],
                        width=1,
                    ),
                ],
                justify='start',
            ),
       ],
       className="g-0 ps-5 pe-5",
    )
