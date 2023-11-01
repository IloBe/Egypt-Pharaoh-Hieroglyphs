# nested dropdown visibility check

##########################
# imports
##########################

from dash import (
    Dash, html, ctx,
    Input, Output, callback,
)

import dash_bootstrap_components as dbc

##########################
# coding
##########################

# initialise app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


# create components
dropdown_items = [
    dbc.DropdownMenuItem(
        'All',
        id='all_items',
        n_clicks=0,
    ),
    dbc.DropdownMenu(
        id='second_nested',
        children=[
            dbc.DropdownMenuItem(
                'Item 1',
                id='item_one',
                n_clicks=0),
            dbc.DropdownMenuItem(
                'Item 2',
                id='item_two',
                n_clicks=0),
        ],
        label='2nd nested dropdown',
        className="mt-1 px-1",
    ),
]

nested_dropdown = dbc.DropdownMenu(
    id='first_dropdown',
    children=dropdown_items,
    label="Start",
    in_navbar=True,
),

nav_bar = navbar = dbc.Navbar(
    dbc.Container(
        children = [
            dbc.Col(
                children = [
                    html.Br(),
                    html.H2("Nested dropdown visibility check ...", style={'color': 'white'}),
                    html.Br(),
                    dbc.Col(
                        children=[
                            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                            dbc.Collapse(
                                nested_dropdown,
                                id="navbar-collapse",
                                navbar=True,
                            ),
                        ],
                        className="mb-2",
                    ),
                ],
            ),
        ],
    ),
    color="black",
    dark=True,
)


# app layout
app.layout = dbc.Container(
    children = [
        navbar,
        html.Br(),
        html.H4(id='text_change'),
        html.Br(),
    ],
    fluid=True,
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
)


# add controls to build the interaction
@callback(
    Output("text_change", "children"),
    Input("all_items", "n_clicks"),
    Input("item_one", "n_clicks"),
    Input("item_two", "n_clicks"),
)
def update_txt_input(click_all, click_one, click_two):
    item_clicked = ctx.triggered_id
    return f'''You have clicked dropdown item with ID {item_clicked}
            ''' if item_clicked else '''You haven't clicked any dropdown item yet'''


# run app
if __name__ == '__main__':
   app.run(debug=True)
