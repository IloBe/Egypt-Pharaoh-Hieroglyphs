# tests/test_timeline_service

"""
Unit tests for the TimelineService class.

Tested is the core business logic of the TimelineService, including
data preparation, name selection, image tiering and filename validation.
It uses pytest fixtures and mocking to isolate the service from real data
and external dependencies.
"""

##########################
# imports
##########################

import pandas as pd
import pytest
from typing import Dict, Any
from unittest.mock import MagicMock

from src.services.timeline_services import TimelineService

##########################
# coding
##########################

@pytest.fixture
def mock_base_service() -> MagicMock:
    """A mock of the base pharaoh_data_service."""
    mock_service = MagicMock()
    mock_df = pd.DataFrame({
        'kingdom_name': ['Early Dynastic Period', 'New Kingdom', 'Old Kingdom', 'New Kingdom'],
        'dynasty_no': [1, 18, 4, 20],
        'calendar_period_start': [3100, 1550, 2613, 1129],
        'calendar_period_end': [2890, 1295, 2494, 1111],
        'king_horus': ['Narmer', None, 'Userib', 'Kanakht Khaemwaset'],
        'king_sedge_bee': ['Meni', 'Nebmaatra', None, 'Neferkare Setepenre'],
        'king_birth_son_of_ra': [None, 'Amenhotep III', 'Khufu', 'Ramses IX'],
        'image_local': ['narmer_palette.jpg', None, None, 'RamsesIX_Aegypten99442.jpg'],
        'image_creator': ['Some Creator', None, None, 'A German Photographer']
    })
    mock_service.df = mock_df
    return mock_service

@pytest.fixture
def early_dynasty_pharaoh() -> pd.Series:
    """A mock pharaoh from an early dynasty (Horus name is primary)."""
    return pd.Series({
        'dynasty_no': 1,
        'king_horus': 'HorusName',
        'king_sedge_bee': 'SedgeName',
        'king_birth_son_of_ra': 'BirthName'
    })

@pytest.fixture
def late_dynasty_pharaoh() -> pd.Series:
    """A mock pharaoh from a later dynasty (Birth name is primary)."""
    return pd.Series({
        'dynasty_no': 18,
        'king_horus': 'HorusName',
        'king_sedge_bee': 'SedgeName',
        'king_birth_son_of_ra': 'BirthName'
    })

@pytest.fixture
def pharaoh_with_roman_numeral() -> pd.Series:
    """A mock pharaoh with a Roman numeral in their name."""
    return pd.Series({'king_birth_son_of_ra': 'Ramses II'})

# --- Test Cases ---

def test_service_initialization(mock_base_service: MagicMock) -> None:
    """
    Tests that the TimelineService initializes correctly, loading and preparing
    the DataFrame from the base service.
    """
    service = TimelineService(mock_base_service)
    assert not service.df.empty
    assert len(service.df) == 4

def test_get_period_dates(mock_base_service: MagicMock) -> None:
    """
    Tests that period start and end dates are aggregated correctly.
    """
    # Arrange
    service = TimelineService(mock_base_service)
    
    # Act
    period_dates = service.get_period_dates()
    
    # Assert
    assert period_dates['New Kingdom']['start'] == 1550
    assert period_dates['New Kingdom']['end'] == 1111    # could be updated to reflect new data

def test_get_display_name_prefers_horus_for_early_dynasty(early_dynasty_pharaoh: pd.Series) -> None:
    """
    Given an early dynasty pharaoh (up to fourth dynasty), 
    when get_display_name is called, it should return the Horus name.
    """
    display_name = TimelineService.get_display_name(early_dynasty_pharaoh)
    assert display_name == 'HorusName'

def test_get_display_name_prefers_birth_name_for_late_dynasty(late_dynasty_pharaoh: pd.Series) -> None:
    """
    Given a later dynasty pharaoh,
    when get_display_name is called, it should return the Son of Ra (Birth) name.
    """
    display_name = TimelineService.get_display_name(late_dynasty_pharaoh)
    assert display_name == 'BirthName'

def test_get_image_html_tier1_museum_image(mock_base_service: MagicMock) -> None:
    """
    Tests that a pharaoh with a curated museum image (Narmer) returns the correct URL.
    """
    # Arrange
    service = TimelineService(mock_base_service)
    narmer_row = service.df[service.df['king_horus'] == 'Narmer'].iloc[0]
    
    # Act
    img_url, credit = service.get_image_html(narmer_row)
    
    # Assert
    assert 'britishmuseum.org' in img_url
    assert credit is not None
    assert credit[0] == 'The British Museum'

def test_get_image_html_tier2_local_image(mocker: Any, mock_base_service: MagicMock) -> None:
    """
    Tests that a pharaoh with a valid local image BUT NO museum image
    (Ramses IX) returns the correct web path.
    """
    # Arrange
    mocker.patch.object(TimelineService, '_is_filename_valid_for_pharaoh', return_value=True)
    service = TimelineService(mock_base_service)
    ramses_ix_row = service.df[service.df['king_birth_son_of_ra'] == 'Ramses IX'].iloc[0]

    # Act
    img_url, credit = service.get_image_html(ramses_ix_row)

    # Assert
    assert img_url == '/assets/images/RamsesIX_Aegypten99442.jpg'
    assert credit is not None
    assert credit[0] == 'A German Photographer'

def test_get_image_html_tier3_fallback(mock_base_service: MagicMock) -> None:
    """
    Tests that a pharaoh with no available image (Khufu) returns None.
    """
    # Arrange
    service = TimelineService(mock_base_service)
    khufu_row = service.df[service.df['king_birth_son_of_ra'] == 'Khufu'].iloc[0]
    
    # Act
    img_url, credit = service.get_image_html(khufu_row)
    
    # Assert
    assert img_url is None
    assert credit is None

@pytest.mark.parametrize(
    "filename, expected",
    [
        ("ramses-ii-statue.png", True),
        ("ramsesii.jpg", True),
        ("ramses-statue.svg", True),
        ("thutmose-iii-mural.gif", False),
        ("random-pharaoh.png", False),
    ]
)
def test_is_filename_valid_for_pharaoh(pharaoh_with_roman_numeral: pd.Series, filename: str, expected: bool) -> None:
    """
    Tests the filename validation logic with various formats for a name
    containing a Roman numeral.
    """
    potential_names = [pharaoh_with_roman_numeral['king_birth_son_of_ra']]
    is_valid = TimelineService._is_filename_valid_for_pharaoh(filename, potential_names)
    assert is_valid == expected