# src/pages/home.py

"""
Applications landing page content,
also reached by click on home-button.
"""

##########################
# imports
##########################

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, register_page

##########################
# coding
##########################

register_page(__name__, path = '/')

# relative path to 'assets' folder specified in app.py
# '/assets/images/RosettaStoneCartouche2_TrusteesBritishMuseum.png'
CARTOUCHE_IMG = dash.get_asset_url('images/RosettaStoneCartouche2_TrusteesBritishMuseum.png')

# direct downstream is too slow
#ABYDOS = 'https://upload.wikimedia.org/wikipedia/commons/3/31/Abydos_K%C3%B6nigsliste_stitched_1.jpg'
# '/assets/images/Abydos_kinglist_stitched_1.jpg'
ABYDOS_IMG = dash.get_asset_url('images/Abydos_kinglist_stitched_1.jpg')

# entry page components
txt_intro = dcc.Markdown(
    """
    The world of the ancient Egyptians is fascinating. Most people have seen images of the pyramids, burial objects, hieroglyphs or other objects of everyday life in films, pictures, documents, museums or perhaps even directly in Egypt.
    But the first thing that comes to mind are the kings and queens, called pharaohs with names framed by cartouches. For example, the right part image of the [Rosetta Stone](https://www.britishmuseum.org/blog/everything-you-ever-wanted-know-about-rosetta-stone), created by the _British Museum_, shows the [cartouche name of _Ptolemy V_](https://www.britishmuseum.org/collection/image/385347001).
    """,
    link_target = "_blank" # opens all links in a new tab
)

txt_names = dcc.Markdown(
     """
    Names are important to establish identity, particularly for royals. In general, Egyptian pharaohs received five names to emphasise their power compared to ordinary people. They got the first one at birth and four additional ones at accession. In classical order, the royal name titles were:
    - **Horus** - rectangular box with _horus falcon_ in front of it called _serech_, it has been the only framed royal name up to the fourth dynasty
    - **He of the Two Ladies** - starts with hieroglyphs for upper- and lower-Egypt, the _falcon Nechbet_ and the _cobra Wadjet_
    - **(Horus of) Gold** - starts with _horus falcon_ sitting on the _hieroglyph sign for gold_
    - **He of the Sedge and Bee** - throne name in general as cartouche, used from the fourth dynasty on
    - **Son of Ra** - birth name of the king, shown as cartouche as well, can be modified by an added epithet (note: indicated on our pages in brackets)

    So, their five names are an elaboration of names, titles and epithets. On monuments you will find mainly the three common ones, which are the _Horus_ name and the _praenomen_ (assigned on accession) resp. _nomen_ (birth name), both contained in cartouches. The cartouche contents may look a little bit different for kings or queens depending on specific king list visualisation.
        """
)

king_lists_part = dcc.Markdown(
    """
    Few king lists are found. As this major ones, they include rows of pharaoh name cartouches. The basis for this application is the [Abydos list](https://commons.wikimedia.org/wiki/File:Abydos_K%C3%B6nigsliste_stitched_1.jpg) (object image created by _Olaf Tausch_).
    - **Karnak** - inscribed in stone during the reign of Thutmose II
    - **Abydos** - inscribed in stone during the reign of Seti I
    - **Saqqara** - inscribed in stone during the reign of Ramesses II
    """,
    link_target = "_blank" # opens Abydos list link in a new tab
)


# layout structure
layout = html.Div(
    children = [
        html.Br(),
        html.A(dbc.Row([
            dbc.Col(
                dbc.Row([
                    html.H4('Do you know them?'),
                    html.Div(txt_intro),
                ])
            ),
            dbc.Col(
                html.Img(
                    title = "© The Trustees of the British Museum. Shared under a CC BY-NC-SA 4.0 licence.",
                    src = CARTOUCHE_IMG,
                    height = "160px",
                ),
                width = 'auto',
            ),
        ])),
        html.Br(),
        html.A(dbc.Row([
            html.H5('The Five Names of Pharaoh'),
            html.Div(txt_names),
        ])),
        html.Br(),
        html.A(dbc.Row([
            dbc.Row([html.H5('King Lists')]),
            dbc.Col(html.Div(king_lists_part)),
            dbc.Col(
                html.Img(
                    src = ABYDOS_IMG,
                    height = "150px",
                    className = 'pt-1',),
                width = 'auto',
            ),
        ])),
    ],
    className = "g-0 ps-5 pe-5",
)