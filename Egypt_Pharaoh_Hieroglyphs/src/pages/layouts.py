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

import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import logging
import pandas as pd

##########################
# coding
##########################

# set basic, simple console logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pharaoh_hieroglyphs")


# helper functions
def create_dropdownitem(name, id, href):
    ''' returns the dbc.DropdownMenuItem '''
    return dbc.DropdownMenuItem(
            name,
            href=href,
            id=id,
            n_clicks=0,
    )

#
# header
#
def get_header(ech_nof_img_path, first_dynasty_names, decimal_dynasty_names, twenties_dynasty_names):
    """
    Returns the navbar header with introduction title, home icon and dropdowns.
    """
    ECHNATON_NOFRETETE = ech_nof_img_path 
    logger.info('----- echnaton, nofretete img path: %s', ECHNATON_NOFRETETE)

    # for dropdown's see:
    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/dropdown_menu/
    dynasty_items = [
        create_dropdownitem(
            name='All', id='all_dynasties',
            href='/pages/dynasties/all_dynasties.py',
        ),
        dbc.DropdownMenu(
            id='first_dynasties',
            children=[
                create_dropdownitem(
                    name=name, id=name, 
                    #href='/pages/dynasties/'
                    href=''.join(['/pages/dynasties/', name.replace(' ', '_').lower(), '.py']),
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
                create_dropdownitem(
                    name=name, id=name,
                    #href='/pages/dynasties/',
                    href=''.join(['/pages/dynasties/', name.replace(' ', '_').lower(), '.py']),
                ) for name in decimal_dynasty_names
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
                create_dropdownitem(
                    name=name, id=name,
                    #href='/pages/dynasties/',
                    href=''.join(['/pages/dynasties/', name.replace(' ', '_').lower(), '.py']),
                ) for name in twenties_dynasty_names
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
                    #page["name"], href=page["path"],
                    id='thirtith_dynasty',
                    n_clicks=0,
                    #href='/pages/dynasties/',
                    href=''.join(['/pages/dynasties/', "Thirtieth Dynasty".replace(' ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Thirty-First Dynasty",
                    #page["name"], href=page["path"],
                    id='thirtyfirst_dynasty',
                    n_clicks=0,
                    #href='/pages/dynasties/',
                    href=''.join(['/pages/dynasties/', "Thirty-First Dynasty".replace(' ', '_').lower(), '.py']),
                ),
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
    
    period_items = [
        create_dropdownitem(
            name='All', id='all_periods',
            href='/pages/periods/all_periods.py',
        ),
        create_dropdownitem(
            name='Early Dynastic Period', id='early_dynastic_period',
            href='/pages/periods/early_dynastic_period.py',
        ),
        create_dropdownitem(
            name='Old Kingdom', id='old_kingdom',
            href='/pages/periods/old_kingdom.py',
        ),
        dbc.DropdownMenu(
            id='first_intermediate',
            children=[
                dbc.DropdownMenuItem(
                    "First Intermediate Period - general",
                    #page["name"], href=page["path"],
                    id='first_intermediate_period_general',
                    n_clicks=0,
                    href='/pages/periods/first_intermediate_period_general.py',
                ),
                dbc.DropdownMenuItem(
                    "First Intermediate Period - Thebes only",
                    #page["name"], href=page["path"],
                    id='first_intermediate_period_thebes_only',
                    n_clicks=0,
                    href='/pages/periods/first_intermediate_period_thebes_only.py',
                )
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
        create_dropdownitem(
            name='Middle Kingdom', id='middle_kingdom',
            href='/pages/periods/middle_kingdom.py',
        ),
        dbc.DropdownMenu(
            id='second_intermediate',
            children=[
                dbc.DropdownMenuItem(
                    "Second Intermediate Period - Hyksos",
                    #page["name"], href=page["path"],
                    id='second_intermediate_period_hyksos',
                    n_clicks=0,
                    href='/pages/periods/second_intermediate_period_hyksos.py',
                ),
                dbc.DropdownMenuItem(
                    "Second Intermediate Period - rulers based in Thebes",
                    #page["name"], href=page["path"],
                    id='second_intermediate_period_rulers_thebes',
                    n_clicks=0,
                    href='/pages/periods/second_intermediate_period_rulers_thebes.py',
                ),
            ],
            label='Second Intermediate Period',
            toggle_style={
                "background": '#E1DFD6',
                'color': 'black',
            },
            className="px-1",
            align_end=True,
        ),
        create_dropdownitem(
            name='New Kingdom', id='new_kingdom',
            href='/pages/periods/new_kingdom.py',
        ),
        dbc.DropdownMenu(
            id='third_intermediate',
            children=[
                dbc.DropdownMenuItem(
                    "Third Intermediate Period - Tanite",
                    #page["name"], href=page["path"],
                    id='third_intermediate_period_tanite',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Third Intermediate Period - Tanite".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Third Intermediate Period - Bubastite/Libyan",
                    #page["name"], href=page["path"],
                    id='third_intermediate_period_bubastite_libyan',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Third Intermediate Period - Bubastite/Libyan".
                        replace(' ', '_').replace('-','').replace('  ', '_').
                        replace('/', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Third Intermediate Period - Tanite/Libyan",
                    #page["name"], href=page["path"],
                    id='third_intermediate_period_tanite_libyan',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Third Intermediate Period - Tanite/Libyan".
                        replace(' ', '_').replace('-','').replace('  ', '_').
                        replace('/', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Third Intermediate Period - General",
                    #page["name"], href=page["path"],
                    id='third_intermediate_period_general',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Third Intermediate Period - General".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Third Intermediate Period - Kushite",
                    #page["name"], href=page["path"],
                    id='third_intermediate_period_kushite',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Third Intermediate Period - Kushite".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
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
                dbc.DropdownMenuItem(
                    "Late Period - General First",
                    #page["name"], href=page["path"],
                    id='late_period_general_first',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Late Period - General First".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Late Period - First Persian Period",
                    #page["name"], href=page["path"],
                    id='late_period_first_persian_period',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/periods/', "Late Period - First Persian Period".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Late Period - General Second",
                    #page["name"], href=page["path"],
                    id='late_period_general_second',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/', "Late Period - General Second".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
                dbc.DropdownMenuItem(
                    "Late Period - Second Persian Period",
                    #page["name"], href=page["path"],
                    id='late_period_second_persian_period',
                    n_clicks=0,
                    #href='/pages/periods/',
                    href=''.join(['/pages/', "Late Period - Second Persian Period".
                        replace(' ', '_').replace('-','').replace('  ', '_').lower(), '.py']),
                ),
            ],
            label='Late Period',
            toggle_style={
                "background": '#E1DFD6',
                'color': 'black',
            },
            className="mt-1 px-1",
            align_end=True,
        ),
    ]
    
    dynasties_dropdown = dbc.DropdownMenu(
        id='dynasties_dropdown',
        children=dynasty_items,
        label="Dynasties",
        toggle_style={"background": "black"},
        in_navbar=True,
        align_end=True,
    )
    
    periods_dropdown = dbc.DropdownMenu(
        id='periods_dropdown',
        children=period_items,
        label="Periods",
        toggle_style={"background": "black"},
        className="border border-0",
        in_navbar=True,
        align_end=True,
    )
    
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
                align='start',   #'end',
                style={'color': 'dark'},
            ),
            dbc.Col(
                dynasties_dropdown,
                className="me-auto px-2",
                align='start',   #'end',
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
                                        # completely black background and white signs
                                        #src='https://global.discourse-cdn.com/business7/uploads/plot/optimized/3X/b/2/b20398c2f56ade4bbfdbfdb8f2dc09188eac4d86_2_504x500.jpeg',
                                        # link with black signs
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

#
#  to create DashAgGrid
#

# image column filter params
objectFilterParams = {
    "filterOptions": ["contains", "notContains"],
    "debounceMs": 200,
    "suppressAndOrCondition": True,
}

# transliteration of throne names
def get_throne_class_name(throne_class):
    ''' Returns the string name of the used throne class horus or sedge-bee '''
    if isinstance(throne_class, str):
        return f'"field": {throne_class}'
    else: # from 'old_kingdom' period selection can be horus or sedge-bee throne name
        return f'"valueGetter": {'''
            function(params) {
                if (params.data.king_sedge_bee) {
                    return params.data.king_sedge_bee + 'bin in sedge_bee...';
                } else {
                    return params.data.king_horus + 'bin in horus...';
                }
            }
        '''}'

def get_col_defs(throne_class):
    ''' Returns DashAgGrid table structure, means column definitions for data visualisation '''
    return [
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
                    "width": 60
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
                    "width": 48,
                    "height": 10,
                    "cellStyle": {
                        'font-family': 'Trlit_CG Times',
                        'font-size': 16,
                    },
                    "filter": False,
                },
                {
                    "headerName": "Throne",
                    "field": throne_class,
                    "valueGetter": {'function': "params.row.king_sedge_bee if pd.notnull(params.row.sedge_bee) else params.row.king_horus;"},
                    #{"function": '''
                    #    if pd.notnull(params.row.king_sedge_bee): 
                    #        return '${params.row.king_sedge_bee}';
                    #    else:
                    #        return '${params.row.king_horus}';
                    #    '''               
                        # "params.data.king_sedge_bee if pd.notnull(params.data.sedge_bee) else params.data.king_horus;"
                    #},
                    "width": 48,
                    "height": 10,
                    "cellStyle": {
                        'font-family': 'Trlit_CG Times',
                        'font-size': 16,
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
                    "width": 52,
                    "height": 20,
                    "filter": False,
                },
                {
                    "field": "JSesh_throne_praenomen_cartouche",
                    "headerName": "Throne",
                    "cellRenderer": "ImgThumbnail",
                    "width": 52,
                    "height": 20,
                    "filter": False,
                },
            ],
        },
    ]

def get_default_col_def():
    ''' Returns the default column definition for visualisation '''
    return {
        "flex": 1,
        "minWidth": 38,
        "filter": True,
    }
