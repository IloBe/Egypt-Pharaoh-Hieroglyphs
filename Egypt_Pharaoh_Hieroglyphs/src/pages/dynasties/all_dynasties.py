"""
Web applications page content of having selected 'All' dynasties. 

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
import dash_mantine_components as dmc

##########################
# coding
##########################

dash.register_page(__name__)

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


def create_dyn_txt(dyn_name, dyn_time, throne_names):
    """ Returns specific dynastic information for timeline item """
    return [
        html.Span(dyn_name, style={"fontWeight": "bold", "color": "#666666"}),
        dyn_time,
        html.Span("throne names: ", style={"fontWeight": "bold", "color": "#666666"}),
        throne_names,
    ]


def create_dyn_anchor(dyn_name, dyn_time, throne_names_dict):
    """ Returns specific dynastic information with some anchor pharaoh names for timeline item """
    names_record = [
        html.Span(dyn_name, style={"fontWeight": "bold", "color": "#666666"}),
        dyn_time,
        html.Span("throne names: ", style={"fontWeight": "bold", "color": "#666666"}),
    ]

    # create appropriate list item - name as text or dmc Anchor element
    for item in throne_names_dict.items():
        if item[1]:  # dict value is not None
            name_item = dmc.Anchor(
                item[0] + ', ',  # key - pharaoh name
                href=item[1],  # value - URL 
                underline=False,
            )
        else:
            name_item = item[0] + ', '

        names_record.append(name_item)

    # removes the last ', ' signs from the last pharao name element of the list
    last_item = names_record[-1]
    if isinstance(last_item, str):
        names_record[-1] = last_item[:-2]
    else: # last item is Anchor type
        last_item.children = last_item.children[:-2]
        names_record[-1] = last_item
    
    return names_record


# create time line visualisation
dyn_timeline_items = [
    dmc.TimelineItem(
        "Dynastic Overview 3100 - 332 BC",
        className="fw-bold",
        bullet=make_icon("akar-icons:circle-fill", '#d3d0c2'), 
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "1st Dynasty", " c. 3100 - 2890 BC, ",
            "Narmer, Aha, Djer, Djet, Den, Adjib, Semerkhet, Qa'a"),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "2nd Dynasty", " c. 2890 - 2686 BC, ",
            "Hetepsekhemwy, Nebra, Nlnetjer, Peribsen, Sekhemib, Khasekhem",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "3rd Dynasty", " c. 2686 - 2613 BC, ",
            {
                 "Djoser": "https://en.wikipedia.org/wiki/Pyramid_of_Djoser",
                 "Sekhemkhet": None,
                 "Sanakht": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "4th Dynasty", " c. 2613 - 2494 BC, ",
            {
                "Sneferu": "https://en.wikipedia.org/wiki/Sneferu",
                "Khufu": None,
                "Djedefra": None,
                "Khafra": None,
                "Menkaura": None,
                "Shepseskaf": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "5th Dynasty", " c. 2494 - 2345BC, ",
            {
                "UserKaf": None,
                "Sahura": None,
                "Neferirkara": None,
                "Neuserra": None,
                "Menkauhor": None,
                "Djedkara": None,
                "Unas": "https://en.wikipedia.org/wiki/Unas",
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "6th Dynasty", " c. 2345 - 2181 BC, ",
            "Teti, Meryra, Merenra, Neferkara",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "7th & 8th Dynasties", " c. 2181 - 2125 BC, ",
            " n/a ",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "9th & 10th Dynasties (Heracleopolitan)", " c. 2160 - 2025 BC, ",
            " n/a ",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "11th Dynasty (Thebes only)", " c. 2125 - 2055 BC, ",
            "Sehertawy, Wahankh, Nakhtnebtepnefer",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "11th Dynasty (all of Egypt)", " c. 2055 - 1985 BC, ",
            {
                "Nebhepetra": None,
                "Sankhkara": "https://en.wikipedia.org/wiki/Mentuhotep_III",
                "Nebtawyra": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "12th Dynasty", " c. 1985 - 1795 BC, ",
            {
                "Sehetepibra": None,
                "Kheperkara": None,
                "Nubkaura": None,
                "Khakheperra": None,
                "Khakaura": None,
                "Nimaatra": None,
                "Maakherura": None,
                "Sobekkara": "https://en.wikipedia.org/wiki/Sobekneferu",
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "13th Dynasty", " c. 1795 - after 1650 BC, ",
            {
                "Khutawayra": None,
                "Sankhibra": None,
                "Auibra": None,
                "Sekhemra-Khutawy": None,
                "Userkara": "https://en.wikipedia.org/wiki/Khendjer",
                "Sekhemra-Sewadjtawy": None,
                "Khasekhemra": None,
                "Menwadjra": None,
                "Khaneferra": None,
                "Merneferra": None,
                "Sekhemra-Sankhtawy": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "14th Dynasty", " c. 1750 - 1650 BC, ",
            "Aasehra",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "15th Dynasty (Hyksos)", " c. 1650 - 1550 BC, ",
            "Seuserenra, Aauserra",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "16th & 17 Dynasties (rulers based in Thebes)", " c. 1650 - 1550 BC, ",
            "Anather, Yakobaam, Nubkheperra, Sekhemra-Wadjkhau, Seqnenra, Wadjkheperra",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "18th Dynasty", " c. 1550 - 1295 BC, ",
            {
                "Nebpehtyra": None,
                "Djeserkara": None,
                "Aakheperkara": None,
                "Aakheperenra": None,
                "Maatkara": "https://en.wikipedia.org/wiki/Hatshepsut",
                "Menkheperra": "https://en.wikipedia.org/wiki/Thutmose_III",
                "Aakheperura": None,
                "Menkheperura": "https://en.wikipedia.org/wiki/Dream_Stele",
                "Nebmaatra": None,
                "Neferkheperura-Waenra": "https://en.wikipedia.org/wiki/Akhenaten",
                "Ankhkheperura": "https://en.wikipedia.org/wiki/Smenkhkare",
                "Nebkheperura": "https://en.wikipedia.org/wiki/Tutankhamun",
                "Kheperkheperura-Irmaat": None,
                "Djeserkheperura-Setepenra": "https://en.wikipedia.org/wiki/Horemheb",
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "19th Dynasty", " c. 1295 - 1186 BC, ",
            {
                "Menpehtyra": None,
                "Mennaatra": "https://en.wikipedia.org/wiki/Seti_I",
                "Usermaatra-Setepenra": "https://en.wikipedia.org/wiki/Ramesses_II",
                "Baenra-Merynetjeru": None,
                "Userkheperura-Setepenra": None,
                "Menmira-Setepenra": None,
                "Akhenra-Setepenra": None,
                "Sitra-Meryamun": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "20th Dynasty", " c. 1186 - 1069 BC, ",
            "Userkhaura-Setepenra, Usermaatra-Meryamun, Heqamaatra, Nebmaatra-Meryamun, Neferkara-Setepenra,\
 Menmaatra-Setepenptah, Hemnetjertepyenamun",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "21st Dynasty", " c. 1069 - 945 BC, ",
            "Hedjkheperra-Setepenra, Aakheperra-Setepenamun, Usermaatra-Meryamun-Setepenamun, Netjerkheperr-Setepenamun,\
 Titkheperura, Khakheperra-Setepenamun, Hemnetjertepyenamun",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "22th Dynasty", " c. 945 - 715 BC, ",
            {
                "Hedjkheperra-Setepenra": "https://en.wikipedia.org/wiki/Shoshenq_I",
                "Sekhemkheperra": None,
                "Heqakheperra-Setepenra": None,
                "Usermaatra-Setepenamun": None,
                "Hedjkheperra-Setepenra": None,
                "Usermaatra-Setepenra": None,
                "Usermaatra-Setepenamun": None,
                "Hedjkheperra-Setepenamun": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "23rd Dynasty", " c. 818 - 715 BC, ",
            "Usermaatra-Setepenamun, Usermaatra, n/a (Nlmlot - birth name)",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "24th Dynasty", " c. 727 - 715 BC, ",
            "Shepsesra, Wahkara",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "25th Dynasty", " c. 747 - 656 BC, ",
            {
                "Menkheperra": "https://en.wikipedia.org/wiki/Piye",
                "Neferkara": None,
                "Djedkaura": None,
                "Nefertemkhura": None,
                "Bakara": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "26th Dynasty", " c. 664 - 525 BC, ",
            {
                "Wahibra": None,
                "Wehemibra": "https://en.wikipedia.org/wiki/Necho_II",
                "Neferibra": None,
                "Haaibra": None, 
                "Khnemibra": "https://en.wikipedia.org/wiki/Amasis_II",
                "Ankhkara": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "27th Dynasty", " c. 525 - 404 BC, ",
            {
                "Mesutira": None,
                "Setutra": "https://en.wikipedia.org/wiki/Darius_the_Great",
                "Xerxes I": None,
                "Artaxerxes I": None,
                "Seheribra": None,
                "n/a (Inaros - birth name)": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "28th Dynasty", " c. 404 - 399 BC, ",
            "n/a (Amyrtaeus - birth name)",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_txt(
            "29th Dynasty", " c. 399 - 380 BC, ",
            "Baenra-Merynetjeru, Maatibra",
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "30th Dynasty", " c. 380 - 343 BC, ",
            {
                "Kheperkara": "https://en.wikipedia.org/wiki/Nectanebo_I",
                "Irmaatenra": None,
                "Senedjemibra-Setepeninhur": None,
            },
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
    dmc.TimelineItem(
        children = create_dyn_anchor(
            "31st Dynasty", " c. 343 - 332 BC, ",
            {
                "Artaxerxes III": None,
                "Darius III": "https://en.wikipedia.org/wiki/Darius_III",
            }
        ),
        bullet=make_icon("openmoji:great-pyramid-of-giza"),
    ),
]


#
# all dynasties layout
#
layout = html.Div(
    children = [
        html.Br(),
        html.H4(
            "Chronological Dynastic Overview",
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
                ', means the Greek and Roman periods, are not mentioned by now. Blue names are links to other specific pages.'
            ]
        ),
        html.Br(),
        dmc.Timeline(dyn_timeline_items, active=0,),
    ],
    style={
        'background-color': '#f7f7f4',
        'background-size': '100%',
        'padding': 5,
    },
    className="g-0 ps-5 pe-5",
)
