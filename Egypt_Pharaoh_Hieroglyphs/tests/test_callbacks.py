# tests/test_callbacks.py

"""
Unit tests for the application's callbacks.

This module tests the Python logic of the callbacks directly,
without requiring a browser.
"""

##########################
# imports
##########################

from dash import html

from src.callbacks.dynasty_callbacks import show_dynasty_image_modal
from src.callbacks.period_callbacks import show_period_image_modal

##########################
# coding
##########################

def test_dynasty_modal_callback_logic():
    """Tests the business logic of the `show_dynasty_image_modal` callback."""
    mock_cell_data = {"value": "/assets/images/narmer_birth_name.svg"}
    is_open, modal_children = show_dynasty_image_modal(mock_cell_data)
    assert is_open is True
    assert isinstance(modal_children, html.Img)
    assert modal_children.src == "/assets/images/narmer_birth_name.svg"

def test_period_modal_callback_no_data():
    """Tests that the period modal callback handles empty input correctly."""
    is_open, modal_children = show_period_image_modal(None)
    assert is_open is False
    assert modal_children is None