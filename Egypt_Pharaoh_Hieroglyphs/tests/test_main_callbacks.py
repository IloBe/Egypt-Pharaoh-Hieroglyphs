"""
Unit tests for the centralized callbacks in src/main.py.

These Pytest unit tests verify the core business logic of grid interaction callbacks
without requiring a running application or browser. They use pytest and mocking
to simulate Dash's context and user inputs.
"""

##########################
# imports
##########################

import pytest
import dash_bootstrap_components as dbc

from dash import no_update, html
from unittest.mock import MagicMock
from pytest_mock import MockerFixture
from typing import Dict, Any, Optional, Literal

# functions to be tested
from src.main import (
    handle_all_grid_clicks,
    close_image_modal_on_click,
    close_detail_modal_on_click,
)


##########################
# coding
##########################

@pytest.fixture
def mock_pharaoh_data() -> Dict[str, Any]:
    """Provides a sample dictionary representing a single pharaoh's data."""
    return {
        "king_birth_son_of_ra": "Teti",
        "king_sedge_bee": "Teti",
        "dynasty_name": "Sixth Dynasty",
        "kingdom_name": "Old Kingdom",
        "jsesh_birth_cartouche": "/assets/images/teti_birth.svg",
    }


def test_handle_grid_clicks_on_text_cell(
    mocker: MockerFixture, 
    mock_pharaoh_data: Dict[str, Any]
) -> None:
    """
    Verifys text cell click correctly opens the PHARAOH DETAIL modal.
    """
    # --- Arrange ---
    mock_cell_clicked = {
        "rowIndex": 0,
        "colId": "king_birth_son_of_ra"
    }
    
    mock_ctx = MagicMock()
    mock_ctx.triggered_id = {
        'type': 'pharaoh-data-grid',
        'id': 'dynasty-6'
    }
    mock_ctx.triggered = [
        {'prop_id': '{"id":"dynasty-6","type":"pharaoh-data-grid"}.cellClicked',
         'value': mock_cell_clicked}
    ]
    mock_ctx.inputs_list = [[
        {'id': {'id': 'dynasty-6', 'type': 'pharaoh-data-grid'}}
    ]]
    mocker.patch('src.main.dash.ctx', mock_ctx)

    # --- Act ---
    is_open_detail, detail_children, is_open_image, image_children = handle_all_grid_clicks(
        cell_clicked_list = [mock_cell_clicked],
        cell_renderer_list = [None],
        all_row_data = [[mock_pharaoh_data]],
        image_modal_is_open = False,
        detail_modal_is_open = False,
    )

    # --- Assert ---
    assert is_open_detail is True
    assert isinstance(detail_children, dbc.Card)
    assert is_open_image is no_update
    assert image_children is no_update


def test_handle_grid_clicks_on_image_cell(mocker: MockerFixture) -> None:
    """
    Verifys image cell click correctly opens the IMAGE VIEWER modal.
    """
    # --- Arrange ---
    mock_cell_renderer_data = {"value": "/assets/images/some_image.svg"}

    mock_ctx = MagicMock()
    mock_ctx.triggered_id = {
        'type': 'pharaoh-data-grid',
        'id': 'dynasty-6'
    }
    mock_ctx.triggered = [
        {'prop_id': '{"id":"dynasty-6","type":"pharaoh-data-grid"}.cellRendererData',
         'value': mock_cell_renderer_data}
    ]
    mocker.patch('src.main.dash.ctx', mock_ctx)

    # --- Act ---
    is_open_detail, detail_children, is_open_image, image_children = handle_all_grid_clicks(
        cell_clicked_list = [None],
        cell_renderer_list = [mock_cell_renderer_data],
        all_row_data = [[]],
        image_modal_is_open = False,
        detail_modal_is_open = False,
    )

    # --- Assert ---
    assert is_open_detail is no_update
    assert detail_children is no_update
    assert is_open_image is True
    assert isinstance(image_children, html.Img)
    assert image_children.src == "/assets/images/some_image.svg"


@pytest.mark.parametrize(
    "n_clicks, is_open, expected",
    [(1, True, False), (1, False, no_update), (None, True, no_update)],
)
def test_close_image_modal_on_click(
    n_clicks: Optional[int], 
    is_open: bool, 
    expected: bool | Literal[no_update]
) -> None:
    """Tests the logic for closing the image modal."""
    result = close_image_modal_on_click(n_clicks, is_open)
    assert result == expected

@pytest.mark.parametrize(
    "n_clicks, is_open, expected",
    [(1, True, False), (1, False, no_update), (None, True, no_update)],
)
def test_close_detail_modal_on_click(
    n_clicks: Optional[int], 
    is_open: bool, 
    expected: bool | Literal[no_update]
) -> None:
    """Tests the logic for closing the detail modal."""
    result = close_detail_modal_on_click(n_clicks, is_open)
    assert result == expected