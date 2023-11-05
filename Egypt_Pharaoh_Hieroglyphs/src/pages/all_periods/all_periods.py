"""
Web applications page content of having selected 'All' periods. 

Author: Ilona Brinkmeier
Date: Nov. 2023
"""

##########################
# imports
##########################

from dash import dcc, html
from dash_iconify import DashIconify

import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

##########################
# coding
##########################

#dash.register_page(__name__, path="/pages/all_dynasties/")


#
# initialise components using Dash Mantine Components, like
# https://www.dash-mantine-components.com/components/timeline
#

# helper functions for timeline creation
def make_icon(icon, color=None):
    """ Returns the timeline theme icon; code from AnneMarieW modified """
    if color:
        children = [DashIconify(icon=icon, width=25, style={'color': color})]
    else:
        children = [DashIconify(icon=icon, width=16,)]
    return [
        dmc.ThemeIcon(
            radius="xl", variant="outline", children=children,
        )
    ]


def create_period_txt(p_name, p_time, dyn_names, hist_txt=None):
    """ Returns specific period information for timeline item """
    if hist_txt:
        children = [
            dmc.HoverCard(
                withArrow=True,
                width=250,
                shadow="md",
                children=[
                    dmc.HoverCardTarget(
                        html.Span(
                            p_name, 
                            style={"fontWeight": "bold", "color": "#666666"}
                        ),
                    ),
                    dmc.HoverCardDropdown(
                        dmc.Text(
                            hist_txt,
                            size="sm",
                        )
                    ),
                ],
            ),
            p_time,
            html.Span("dynasty sequence: ", style={"fontWeight": "bold", "color": "#666666"}),
            dyn_names,
        ]
    else:
        children = [
            html.Span(
                p_name, 
                style={"fontWeight": "bold", "color": "#666666"}
            ),
            html.Br(),
            p_time,
            html.Span("dynasty sequence: ", style={"fontWeight": "bold", "color": "#666666"}),
            dyn_names,
        ]
    
    return children
        


# create timeline visualisation
period_timeline_items = [
    dmc.TimelineItem(
        "Period Overview 3100 - 332 BC",
        className="fw-bold",
        bullet=make_icon("akar-icons:circle-fill", '#d3d0c2'), 
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "Early Dynastic Period", " c. 3100 - 2686 BC, ",
            "1st Dynasty (c. 3100-2890 BC), 2nd Dynasty (c. 2890-2686 BC)",
            "Unification of Upper (southern) and Lower (northern) Egypt. Memphis as Capital.\
 Hieroglyphic invention of script. First architectural elements of stone."
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "Old Kingdom", " c. 2686 - 2181 BC, ",
            "3rd Dynasty (c. 2686-2613 BC), 4th Dynasty (c. 2613-2494 BC),\
 5th Dynasty (c. 2494-2345 BC), 6th Dynasty (c. 2345-2181 BC)",
            "Step Pyramid of King Djoser built at Saqqara. Khufu builds the Great Pyramid at Giza.\
 Pyramid of Unas first to contain religious texts."
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "First Intermediate Period", " c. 2181 - 2055 BC, ",
            "7th&8th Dynasties (c. 2181-2125 BC),\
 9th&10th Dynasties (Heracleopolitan, c. 2160-2025 BC),\
 11th Dynasty (Thebes only, c. 2125-2055 BC)"
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "Middle Kingdom", " c. 2055 - 1650 BC, ",
            "11th Dynasty (all of Egypt, c. 2055-1985 BC), 12th Dynasty (c. 1985-1795 BC),\
 13th Dynasty (c. 17925-after1650 BC), 14th Dynasty (c. 1750-1650 BC)",
            "Mentuhotep II reunited Egypt. Thebes as religious centre. God Amun as dominant deity.\
 Karnak temple begun."
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "Second Intermediate Period", " c. 1650 - 1550 BC, ",
            "15th Dynasty (Hyksos, c. 1650-1550 BC),\
 16th&17th Dynasties (rulers based in Thebes, c. 1650-1550 BC)",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "New Kingdom", " c. 1550 - 1069 BC, ",
            "18th Dynasty (c. 1550-1295 BC, Amarna period),\
 19th Dynasty (c. 1295-1186 BC, Ramesside period),\
 20th Dynasty (c. 1186-1069 BC, Ramesside period)",
            "Egypt became an empire. First tomb in Valley of the Kings. Queen Hatshepsut ruled\
 as female Pharaoh. Luxur Temple begun. Akhenaten founded city of Akhenaten. Tutankhamun returned\
 to Thebes and became king. Clashes with Hittites in Syria. Peace treaty between Ramses II and Hittite\
 King Hattushili. Ramses II: Temple of Abu Simbel (280km south of Aswan). Rameses III repelled the Sea People.",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    
    dmc.TimelineItem(
        children = create_period_txt(
            "Third Intermediate Period", " c. 1069 - 664 BC, ",
            "21st Dynasty (Tanite, c. 1069-945 BC),\
 22nd Dynasty (Bubastite/Libyan, c. 945-715 BC),\
 23rd Dynasty (Tanite/Libyan, c. 818-715 BC), 24th Dynasty (c. 727-715 BC),\
 25th Dynasty (Kushite, c. 747-656 BC)"),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_period_txt(
            "Late Period", " c. 664 - 332 BC, ",
            "26th Dynasty (c. 664-525 BC), 27th Dynasty (First Persian Period, c. 525-404 BC),\
 28th Dynasty (c. 404-399 BC), 29th Dynasty (c. 399-380 BC), 30th Dynasty (c. 380-343 BC),\
 31st Dynasty (Second Persian Period, c. 343-322 BC)",
            "Assyrian invasions. Greek colonies in Egypt. Persians annexed Egypt. Last native Pharaohs."
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
]


#
# all periods layout
#
layout = html.Div(
    children = [
        html.Br(),
        html.H4(
            "Chronological Period Overview",
            className="fw-bolder text-decoration-underline opacity-75",
        ),
        html.H6(
            children = [
                'Given dates are approximate ones. Information about ',
                html.Span("Macedonian (332 - 305 BC) ", style={"fontWeight": "bold", "color": "#666666"}),
                'resp. ',
                html.Span("Ptolemaic dynasties (305 - 30 BC) ", style={"fontWeight": "bold", "color": "#666666"}),
                'and ',
                html.Span("Roman emperors (30 BC - AD 395)", style={"fontWeight": "bold", "color": "#666666"}),
                ', means the Greek and Roman periods, are not mentioned by now.\
 Some period labels show additional historical information if the name element is hovered.'
            ]
        ),
        html.Br(),
        dmc.Timeline(period_timeline_items, active=0,),
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)