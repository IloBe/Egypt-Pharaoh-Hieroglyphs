# src/pages/timeline.py

"""
Dynamic page for displaying an interactive, vertical timeline of Pharaoh's
with interactive cards including images if available via timeline services.
"""

##########################
# imports
##########################

import pandas as pd
from dash import html, register_page

from src.services.timeline_services import timeline_service, BANNERS

##########################
# coding
##########################

register_page(__name__, path="/timeline", name="Timeline")

def generate_timeline_layout() -> html.Div:
    """
    Generates the Dash component layout for the timeline page with
    structure period banners and their consistent padding.
    """
    df = timeline_service.df
    period_dates = timeline_service.get_period_dates()
    
    # list holds all top-level page components
    page_elements = [
        html.Br(),
        # header is in its own padded container to match other pages structure
        html.Div(
            children = [html.H4(
                "Living Timeline of the Pharaoh's",
                className = "fw-bolder")],  # class_name
            className = "g-0 ps-5 pe-5",
        ),
        html.Br(),
    ]
    
    current_period = ""
    card_counter = 0
    

    for _, row in df.iterrows():
        
        #
        # period banner creation
        #
        period = row.get('kingdom_name')
        if period != current_period and pd.notna(period) and period in BANNERS:
            current_period = period               # main header
            subtext, bg_image = BANNERS[period]   # subheader with date range 
            dates = period_dates.get(period)
            if dates:
                subtext += f" ({dates['start']}-{dates['end']} BC)"
            
            # outer banner of periods
            banner = html.Div(
                className = "kingdom-banner",
                style = {'backgroundImage': f'url({bg_image})'},
                children = [
                    html.Div(className = "banner-overlay"),
                    # inner text container gets padding classes for alignment
                    html.Div(
                        className = "banner-text g-0 ps-5 pe-5",
                        children = [
                            html.H2(period),
                            html.P(subtext)
                        ]
                    )
                ]
            )
            page_elements.append(banner)
            
            # timeline-wrapper (centered by CSS) is a top-level element
            timeline_wrapper = html.Div(
                className = "timeline-wrapper",
                children = [html.Div(className = "timeline-line")])
            page_elements.append(timeline_wrapper)

        #
        # pharaoh card creation
        #
        main_name_display = timeline_service.get_display_name(row)
        if pd.isna(main_name_display):
            continue

        img_url, credit = timeline_service.get_image_html(row)
        # add image and its source info
        if img_url:
            image_component = [html.Img(
                src = img_url,
                alt = f"Image of {main_name_display}",
                className = "pharaoh-image",
            )]
            if credit and credit[0]:
                if credit[1]:
                    credit_p = html.P(
                        className = "image-credit",
                        children = ["Source: ",
                                    html.A(
                                        credit[0],
                                        href = credit[1],
                                        target = "_blank",
                                        rel = "noopener noreferrer"
                                    )]
                    )
                else:
                    credit_p = html.P(
                        f"Source: {credit[0]}",
                        className = "image-credit"
                    )
                image_component.append(credit_p)
        else:
            image_component = html.Div(
                className = "no-image-placeholder",
                children = [html.P("No image available")]
            )
        
        # card details, if expanded
        details_parts = []
        if pd.notna(row.get('king_horus')): details_parts.append(
            html.P([html.Span("Horus Name: "), row['king_horus']])
        )
        if pd.notna(row.get('king_sedge_bee')): details_parts.append(
            html.P([html.Span("Throne Name: "), row['king_sedge_bee']])
        )
        if pd.notna(row.get('king_birth_son_of_ra')): details_parts.append(
            html.P([html.Span("Birth Name: "), row['king_birth_son_of_ra']])
        )
        
        dynasty_info = f"Dynasty {row['dynasty_no']} ({row['calendar_period_start']}-{row['calendar_period_end']} BC)"
        alignment = "timeline-item-left" if card_counter % 2 == 0 else "timeline-item-right"
        
        # final card and point connection creation
        timeline_card = html.Div(
            className = f"timeline-item {alignment}",
            children = [
                html.Div(
                    className = "timeline-card",
                    children = [
                        html.P(dynasty_info, className = "card-meta"),
                        html.H3(main_name_display, className = "card-title"),
                        *(image_component if isinstance(image_component, list) else [image_component]),
                        html.Div(details_parts, className = "details-content"),
                        html.Div("▾", className = "card-expand-arrow")
                    ]
                ),
                html.Div(className = "timeline-point")
            ]
        )
        
        for item in reversed(page_elements):
            if isinstance(item, html.Div) and item.className == "timeline-wrapper":
                item.children.append(timeline_card)
                break
        card_counter += 1

    # final layout is a single Div containing all structured elements
    return html.Div(page_elements)

# assign generated layout to the page
layout = generate_timeline_layout()