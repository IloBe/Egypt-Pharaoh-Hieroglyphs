# src/pages/layouts.py

"""
Factory module to generate the reusable UI components.
"""

##########################
# imports
##########################

import dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd

from dash import dcc, html
from dash_iconify import DashIconify
from typing import Any, Dict, List, Optional
from urllib.parse import quote
from loguru import logger

from src.services.data_service import pharaoh_data_service

##########################
# coding
##########################

# Type aliases
ColumnDef = Dict[str, Any]
NavChildren = List[dbc.NavItem | dbc.DropdownMenu]
DropdownChildren = List[dbc.DropdownMenuItem | dbc.DropdownMenu]

def get_grid_style() -> Dict[str, str]:
    """Returns the standard style dictionary for all AG Grids."""
    return {
        "height": "800px",
        "--ag-header-background-color": "#d3d0c2",   # brown/beige color
        "--ag-header-foreground-color": "#333333",   # darker text for better contrast
    }

def get_header() -> dbc.Navbar:
    """Builds and returns the application's main navigation bar."""
    logger.info("Creating application header component.")
    
    navigation_items: NavChildren = []

    # Home button
    navigation_items.append(
        dbc.NavItem(dbc.Button(
            DashIconify(
                icon = 'bi:house',
                width = 20,
                height = 20,
            ),
            href = "/",
            color = "primary",
            outline = True,
        ))
    )

    # Dynamic menu generation
    if pharaoh_data_service.is_data_loaded():
        # initialisation
        period_menu_items: DropdownChildren = []
        dynasty_main_children: DropdownChildren = []
        
        try:
            # Periods dropdown
            all_periods_df = pharaoh_data_service.get_all_periods()
            period_menu_items.extend([
                dbc.DropdownMenuItem('All Periods', href = '/all-periods',),
                dbc.DropdownMenuItem(divider = True,)
            ])
            for _, row in all_periods_df.iterrows():
                period_menu_items.append(
                    dbc.DropdownMenuItem(
                        children = row['kingdom_name'],
                        href = f"/period/{quote(row['kingdom_name'].replace(' ', '_'))}",
                    )
                )
            
            navigation_items.append(
                dbc.DropdownMenu(
                    label = "Periods",
                    children = period_menu_items,
                    nav = True,
                    align_end = True,
                    toggle_class_name = "nav-dropdown-outline ms-2",
                    class_name = "themed-dropdown",
                )
            )

            # nested Dynasties dropdown
            dynasty_main_children.extend([
                dbc.DropdownMenuItem("All Dynasties", href = "/all-dynasties",),
                dbc.DropdownMenuItem(divider = True,),
            ])
            all_dynasties_df = pharaoh_data_service.get_all_dynasties()
            dynasty_groups = {
                'Dynasties 1-9': (1, 9),
                'Dynasties 10-19': (10, 19),
                'Dynasties 20-31': (20, 31),
            }
            
            for label, (start, end) in dynasty_groups.items():
                group_df = all_dynasties_df.query("@start <= dynasty_no <= @end")
                if not group_df.empty:
                    dynasty_sub_menu_items = [
                        dbc.DropdownMenuItem(
                            children = row['dynasty_name'],
                            href = f"/dynasty/{row['dynasty_no']}",
                        )
                        for _, row in group_df.iterrows()
                    ]
                    
                    dynasty_main_children.append(
                        dbc.DropdownMenu(
                            label = label,
                            children = dynasty_sub_menu_items,
                       )
                    )

            navigation_items.append(
                dbc.DropdownMenu(
                    label = "Dynasties",
                    children = dynasty_main_children,
                    nav = True,
                    align_end = True,
                    toggle_class_name = "nav-dropdown-outline ms-2",
                    class_name = "themed-dropdown",
                )
            )

        except Exception as e:
            logger.exception(f"Failed to build dynamic navigation menus: {e}")
            navigation_items = [dbc.NavItem(dbc.Label("Error: Menus failed to load", color = "danger",))]
    else:
        navigation_items = [dbc.NavItem(dbc.Label("Data failed to load", color = "danger",))]
        
    # 
    # Entire Header
    # 
    header_brand = html.A(
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src = dash.get_asset_url('images/EchnatonNofretete_AegyptischesMuseumBerlin_small-18.PNG'),
                        height = "110px",
                    ),
                    width = "auto",
                ),
                dbc.Col([
                    html.H1(
                        id = "navbar-title",
                        children = ["Egyptian Pharaoh's"],
                        style = {"color" : "white", 'padding': 5},
                    ),
                    html.H5(
                        id = "navbar-subtitle",
                        children = ["BC dynasties from early up to late period"],
                        style = {"color" : "grey", 'padding': 5},
                    ),
                ],
                className = "ms-3"),
            ],
            align = "center",
            className = "g-0",
        ),
        href = "/",
        style = {"textDecoration": "none"},
    )
    
    return dbc.Navbar(
        dbc.Container(
            [
                header_brand,
                dbc.NavbarToggler(id = "navbar-toggler"),
                dbc.Collapse(                   
                    dbc.Nav(
                        navigation_items,
                        navbar = True,
                        # see: https://getbootstrap.com/docs/5.1/utilities/spacing/
                        class_name = "ms-auto mb-3"
                    ),
                    id = "navbar-collapse",
                    is_open = False,
                    navbar = True,
                    class_name = "align-self-end",
                ),
            ],
            fluid = True,
        ),
        color = "black",
        dark = True,
        sticky = 'top',
    )

#
# Footer
#
def get_footer() -> html.Div:
    """
    Builds and returns the application's footer.

    Returns:
        html.Div: A Div component containing footer information and links.
    """
    return html.Div(
        children = [
            dbc.Row(
                children = [
                    dbc.Col(
                        children = [
                            html.A(
                                [DashIconify(
                                    icon = 'charm:github',
                                    width = 20,
                                    height = 20,
                                    color = '#000000',)
                                ],
                                href = 'https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs',
                                target = "_blank",           # opens in new tab
                                rel = "noopener noreferrer", # security practice
                            ),
                            html.H6(
                                children = ['MIT Licence, I. Brinkmeier 2025; images shared under CC BY-NC-SA 4.0 licence'],
                                style = {"display": "inline"},
                                className = 'px-2',
                            ),
                        ],
                        width = 11,
                        className = "text-muted fs-6",
                        style = {'float': 'right'},
                    ),
                    dbc.Col(
                        children = [
                            html.A(
                                [html.Img(
                                    src = dash.get_asset_url('plotly_icon.JPG'),
                                    height = '25px',)
                                ],
                                href = 'https://dash.plotly.com/',
                                target = "_blank",           # opens in new tab
                                rel = "noopener noreferrer", # security practice
                            ),
                        ],
                        width = 1,
                    ),
                ],
                justify = 'start',
            ),
       ],
       className = "g-0 ps-5 pe-5",
    )

#
# For Pages 
#
def get_grid_note() -> dcc.Markdown:
    """
    Returns the standardised note displayed below the AgGrid component.

    Returns:
        dcc.Markdown: Markdown component with usage notes for the data grid
    """
    return dcc.Markdown(
        """
        **Note:**
        - To filter, type directly below the column headers.
        - To get Pharaoh's details card click on text cell (disappears with second click)
        - To view object images and cartouches with bigger size, click on them (disappears with second click)
        - The special font 'CGT_2023.TTF' is required for proper transliteration display.
        - Image assets are for educational and demonstrative purposes.
        """,
        className = "small text-muted mt-3",
    )


def get_col_defs(throne_class: str) -> List[ColumnDef]:
    """
    Returns the column definitions that match the required grid layout.

    Args:
        throne_class (str): column name to use for the throne name transliteration

    Returns:
        List[ColumnDef]: list of dictionaries defining the AgGrid columns
    """
    return [
        {"headerName": "Object",
         "field": "image_local",
         "cellRenderer": "ImgThumbnail",
         "width": 100,
         "filter": False,
         "sortable": False},
        {"headerName": "Throne Name",
         "children": [
            {"headerName": "Horus",
             "field": "king_horus",
             "width": 150},
            {"headerName": "Sedge Bee",
             "field": "king_sedge_bee",
             "width": 150},
        ]},
        {"headerName": "Birth Name",
         "children": [
            {"headerName": "Son of Ra",
             "field": "king_birth_son_of_ra",
             "width": 180},
        ]},
        {"headerName": "Name Transliteration",
         "children": [
            {"headerName": "Birth",
             "field": "king_birth_son_of_ra",
             "width": 120,
             "cellStyle": {'font-family': 'Trlit_CG Times', 'font-size': 16}},
            {"headerName": "Throne",
             "field": throne_class,
             "width": 120,
             "cellStyle": {'font-family': 'Trlit_CG Times', 'font-size': 16}},
        ]},
        {"headerName": "Cartouche",
         "children": [
            {"headerName": "Birth",
             "field": "jsesh_birth_cartouche",
             "cellRenderer": "ImgThumbnail",
             "width": 150,
             "filter": False,
             "sortable": False},
            {"headerName": "Throne",
             "field": "jsesh_throne_praenomen_cartouche",
             "cellRenderer": "ImgThumbnail",
             "width": 150,
             "filter": False,
             "sortable": False},
        ]},
    ]


def get_default_col_def() -> Dict[str, Any]:
    """
    Returns the default column definition for all grids.

    Returns:
        Dict[str, Any]: dictionary of default properties for AgGrid columns
    """
    return {"filter": True, "resizable": True, "sortable": True, "minWidth": 100}


def create_browse_all_layout(title: str) -> html.Div:
    """
    Generates the layout for the pages displaying the entire pharaoh dataset.
    This function is reusable for both the "All Periods" and "All Dynasties" views.
    It fulfills the DRY (Dont-Repeat-Yourself) principle for both dropdown items.

    Args:
        title (str): title to display at the top of the specific page (e.g., "All Periods")

    Returns:
        html.Div: Dash component tree for the specific page
    """
    # fetch whole DataFrame
    full_dataset = pharaoh_data_service.df.copy()

    # unified throne name column for consistent display
    full_dataset['throne_name_display'] = full_dataset['king_horus'].combine_first(full_dataset['king_sedge_bee'])

    # page layout
    return html.Div(
        children = [
            html.Br(),
            html.H4(title, className = "fw-bolder"),
            html.Br(),
            dag.AgGrid(
                id = {'type': 'pharaoh-data-grid', 'id': f'browse-{title.replace(" ", "-")}'},
                rowData = full_dataset.to_dict("records"),
                columnDefs = get_col_defs(throne_class = 'throne_name_display'),
                defaultColDef = get_default_col_def(),
                columnSize = "sizeToFit",
                dashGridOptions = {"rowHeight": 64},
                style = get_grid_style(),
            ),
            get_grid_note(),
        ],
        className = "g-0 ps-5 pe-5",
    )


def create_pharaoh_detail_card(pharaoh_data: Dict[str, Any]) -> dbc.Card:
    """
    Creates a detailed information card for a single pharaoh.

    Args:
        pharaoh_data (Dict[str, Any]): dictionary representing one row of pharaoh data,
                                   typically from the `cellClicked` event of an AG Grid

    Returns:
        dbc.Card: Dash Bootstrap Card component with detailed information.
    """
    if not pharaoh_data:
        return dbc.Card(dbc.CardBody("No data provided."))

    # helper function creates list group items only if data exists
    def create_list_item(label: str, value: Any) -> Optional[dbc.ListGroupItem]:
        return dbc.ListGroupItem([html.B(f"{label}: "), value]) if value and pd.notna(value) else None

    # primary header name
    card_header_title: str = pharaoh_data.get('king_birth_son_of_ra') or \
        pharaoh_data.get('king_sedge_bee') or \
        pharaoh_data.get('king_horus') or \
        "Details"

    # details list for card body
    details_list: List[Optional[dbc.ListGroupItem]] = [
        create_list_item("Dynasty", pharaoh_data.get('dynasty_name')),
        create_list_item("Period", pharaoh_data.get('kingdom_name')),
        create_list_item("Horus Name", pharaoh_data.get('king_horus')),
        create_list_item("Sedge and Bee Name", pharaoh_data.get('king_sedge_bee')),
        create_list_item("Son of Ra Name (Birth Name)", pharaoh_data.get('king_birth_son_of_ra')),
    ]

    # card component
    card = dbc.Card(
        [
            dbc.CardHeader(
                html.H4(
                    card_header_title,
                    className = "mb-0"
                )
            ),
            dbc.CardBody(
                dbc.Row(
                    [
                        # left column for cartouche images
                        dbc.Col(
                            [
                                html.H6("Birth Name Cartouche", className = "mt-2"),
                                html.Img(
                                    src = pharaoh_data.get('jsesh_birth_cartouche'),
                                    className = "w-100"
                                ) if pharaoh_data.get('jsesh_birth_cartouche') else html.Em("Not available"),
                                html.Hr(),
                                html.H6("Throne Name Cartouche", className = "mt-2"),
                                html.Img(
                                    src = pharaoh_data.get('jsesh_throne_praenomen_cartouche'),
                                    className = "w-100"
                                ) if pharaoh_data.get('jsesh_throne_praenomen_cartouche') else html.Em("Not available"),
                            ],
                            md = 4,
                            className = "text-center",
                        ),
                        # right column for textual details
                        dbc.Col(
                            dbc.ListGroup(
                                # filter out any None values
                                [item for item in details_list if item is not None],
                                flush = True,
                            ),
                            md = 8,
                        ),
                    ]
                )
            ),
        ]
    )
    return card