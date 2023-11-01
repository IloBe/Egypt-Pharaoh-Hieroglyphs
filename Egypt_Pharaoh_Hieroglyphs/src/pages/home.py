#!/usr/bin/env -S python3 -i

"""
Web applications home page content. 

Author: Ilona Brinkmeier
Date: Oct. 2023
"""

##########################
# imports
##########################

from dash import dcc, html
from dash_iconify import DashIconify

import dash
import dash_bootstrap_components as dbc

##########################
# coding
##########################

#dash.register_page(__name__, path='/pages/')
#dash.register_page(__name__)

#
# initialise components
#
txt_intro = dcc.Markdown(
    """
The world of the ancient Egyptians is fascinating. Most people have seen images of the pyramids, burial objects, hieroglyphs or other objects of everyday life in films, pictures, documents, museums or perhaps even directly in Egypt.
But the first thing that comes to mind are the kings and queens, called pharaohs with names framed by cartouches. For example, the right part image of the [Rosetta Stone](https://www.britishmuseum.org/blog/everything-you-ever-wanted-know-about-rosetta-stone), created by the _British Museum_, shows the cartouche name of _Ptolemy V_.
    """
)
CARTOUCHE = dash.get_app().get_asset_url('images/RosettaStoneCartouche2_TrusteesBritishMuseum.png')

txt_names = dcc.Markdown(
    """
Names are important to establish identity, particularly for royals. In general, Egyptian pharaohs received five names to emphasise their power compared to ordinary people. They got the first one at birth and four additional ones at accession. In classical order, the royal name titles were:
- **Horus** - rectangular box with _horus falcon_ in front of it called _serech_, it has been the only framed royal name up to the fourth dynasty
- **He of the Two Ladies** - starts with hieroglyphs for upper- and lower-Egypt, the _falcon Nechbet_ and the _cobra Wadjet_
- **(Horus of) Gold** - starts with _horus falcon_ sitting on the _hieroglyph sign for gold_
- **He of the Sedge and Bee** - throne name in general as cartouche, used from the fourth dynasty on
- **Son of Ra** - birth name of the king, shown as cartouche as well, can be modified by an added epithet (note: indicated on our pages in brackets).

So, their five names are an elaboration of names, titles and epithets. On monuments you will find mainly the three common ones, which are the _Horus_ name and the _praenomen_ (assigned on accession) resp. _nomen_ (birth name), both contained in cartouches. The cartouche contents may look a little bit different for kings or queens depending on specific king list visualisation.
    """
)

king_lists_part = dcc.Markdown(
    """
Few king lists are found. As this major ones, they include rows of pharaoh name cartouches. The basis for this application is the [Abydos list](https://commons.wikimedia.org/wiki/File:Abydos_K%C3%B6nigsliste_stitched_1.jpg) (object image created by _Olaf Tausch_).
- **Karnak** - inscribed in stone during the reign of Thutmose II
- **Abydos** - inscribed in stone during the reign of Seti I
- **Saqqara** - inscribed in stone during the reign of Ramesses II
    """
)
ABYDOS = dash.get_app().get_asset_url('images/Abydos_kinglist_stitched_1.jpg')
# direct downstream is too slow
#ABYDOS = 'https://upload.wikimedia.org/wikipedia/commons/3/31/Abydos_K%C3%B6nigsliste_stitched_1.jpg'

#
# home layout
#
layout = html.Div(
    children = [
        html.Br(),
        # first block with title, introduction and cartouche image
        html.A(
            dbc.Row(
                children = [
                    dbc.Col(
                        dbc.Row(
                            children = [
                                html.H4('Do you know them?'),
                                html.Div(txt_intro),
                            ]
                        ),
                    ),
                    dbc.Col(
                        children = [
                            html.Img(
                                src=CARTOUCHE,
                                height="160px",
                            ),
                        ],
                        width='auto',
                    ),
                ],
            ),
        ),
        # second block explains 5 names
        html.A(
            dbc.Row(
                children = [
                    html.H5('The Five Names of Pharaoh'),
                    html.Div(txt_names),
                ],
            ),
        ),
        html.Br(),
        # third block shows the main king lists
        html.A(
            dbc.Row(
                children = [
                    dbc.Row([html.H5('King Lists'),]),
                    dbc.Col(
                        children = [
                            html.Div(king_lists_part),
                        ],
                    ),
                    dbc.Col(
                        children = [
                            html.Img(
                                src=ABYDOS,
                                height="150px",
                                className='pt-1',
                            ),
                        ],
                        width='auto',
                    ),
                ],
            ),
        ),
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)
