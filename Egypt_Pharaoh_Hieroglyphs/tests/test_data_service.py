# tests/test_data_service.py

"""
Unit tests for the DataService class.

The module uses pytest to test the core functionality of the data service,
including data loading, validation and querying, 
using controlled, temporary data files.
"""

##########################
# imports
##########################

import pandas as pd
import pytest
from pathlib import Path

from src.services.data_service import DataService

##########################
# coding
##########################

@pytest.fixture
def good_csv_path(tmp_path: Path) -> Path:
    """Creates a temporary, valid CSV file for testing."""
    # tmp_path is a built-in pytest fixture that provides a temporary directory
    csv_content = """calendar_period_start,calendar_period_end,dynasty_no,dynasty_name,kingdom_name,king_horus,king_sedge_bee,king_birth_son_of_ra,JSesh_birth_cartouche
3100,2890,1,First Dynasty,Early Dynastic Period,Narmer,Meni,,narmer.svg
2890,2686,2,Second Dynasty,Early Dynastic Period,Nebra,Kakau,,nebra.svg
2613,2494,4,Fourth Dynasty,Old Kingdom,,Sneferu,,sneferu.svg
"""
    csv_file = tmp_path / "good_data.csv"
    csv_file.write_text(csv_content)
    return csv_file

@pytest.fixture
def mixed_csv_path(tmp_path: Path) -> Path:
    """Creates a temporary CSV with both valid and invalid rows."""
    csv_content = """calendar_period_start,calendar_period_end,dynasty_no,dynasty_name,kingdom_name,king_horus
3100,2890,1,First Dynasty,Early Dynastic Period,Narmer
invalid_date,2686,2,Second Dynasty,Early Dynastic Period,Nebra
2613,2494,4,Fourth Dynasty,Old Kingdom,Khufu
"""
    csv_file = tmp_path / "mixed_data.csv"
    csv_file.write_text(csv_content)
    return csv_file

@pytest.fixture
def empty_csv_path(tmp_path: Path) -> Path:
    """Creates a temporary, empty CSV file."""
    csv_content = "calendar_period_start,dynasty_no,dynasty_name,kingdom_name\n"
    csv_file = tmp_path / "empty_data.csv"
    csv_file.write_text(csv_content)
    return csv_file


# --- Test Cases ---

def test_successful_data_load_and_format(good_csv_path: Path):
    """
    Tests that the DataService correctly loads a valid CSV and formats image paths.
    """
    # Act
    service = DataService(good_csv_path)
    df = service.df

    # Assert
    assert service.is_data_loaded() is True
    assert len(df) == 3
    # Check that the path formatting was applied correctly
    narmer_record = df.iloc[0]
    assert narmer_record['jsesh_birth_cartouche'] == "/assets/images/narmer.svg"

def test_file_not_found_graceful_failure():
    """
    Tests that the DataService handles a non-existent file path without crashing.
    """
    # Arrange
    non_existent_path = Path("path/that/does/not/exist.csv")

    # Act
    service = DataService(non_existent_path)

    # Assert
    assert service.is_data_loaded() is False
    assert service.df.empty is True

def test_validation_skips_bad_rows(mixed_csv_path: Path):
    """
    Tests that Pydantic validation correctly skips rows with invalid data types.
    """
    # Act
    service = DataService(mixed_csv_path)
    df = service.df

    # Assert
    assert service.is_data_loaded() is True
    # Should load the 2 good rows and skip the 1 bad row
    assert len(df) == 2
    # Check that the correct pharaohs were loaded
    assert "Narmer" in df['king_horus'].values
    assert "Nebra" not in df['king_horus'].values # This row had the bad date
    assert "Khufu" in df['king_horus'].values

def test_empty_file_graceful_failure(empty_csv_path: Path):
    """
    Tests that the DataService handles an empty (but valid) CSV file.
    """
    # Act
    service = DataService(empty_csv_path)

    # Assert
    assert service.is_data_loaded() is False
    assert service.df.empty is True

def test_get_dynasty_returns_correct_data(good_csv_path: Path):
    """
    Tests the get_dynasty filtering method.
    """
    # Arrange
    service = DataService(good_csv_path)

    # Act
    dynasty_df = service.get_dynasty(4)

    # Assert
    assert len(dynasty_df) == 1
    assert dynasty_df.iloc[0]['king_sedge_bee'] == "Sneferu"

def test_get_dynasty_returns_empty_for_no_match(good_csv_path: Path):
    """
    Tests that get_dynasty returns an empty DataFrame for a non-existent dynasty.
    """
    # Arrange
    service = DataService(good_csv_path)

    # Act
    dynasty_df = service.get_dynasty(99) # A dynasty that doesn't exist in our test data

    # Assert
    assert dynasty_df.empty is True

def test_get_all_periods_returns_unique_sorted_data(good_csv_path: Path):
    """
    Tests that get_all_periods returns a unique, sorted list of periods.
    """
    # Arrange
    service = DataService(good_csv_path)

    # Act
    periods_df = service.get_all_periods()

    # Assert
    assert len(periods_df) == 2
    # Check for correct sorting
    assert periods_df.iloc[0]['kingdom_name'] == "Early Dynastic Period"
    assert periods_df.iloc[1]['kingdom_name'] == "Old Kingdom"