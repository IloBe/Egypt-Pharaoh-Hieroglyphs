# src/services/data_service.py

"""
Data service for loading, validating and providing access to the pharaohs dataset.
"""

##########################
# imports
##########################

import pandas as pd

from pathlib import Path
from typing import List
from loguru import logger
from pydantic import ValidationError

from src.models.pharaoh import PharaohRecord

##########################
# coding
##########################

class DataService:
    """Manages the application's dataset."""
    _df: pd.DataFrame
    _data_path: Path

    def __init__(self, data_path: Path) -> None:
        """Initializes the DataService and triggers the data loading process."""
        self._data_path = data_path
        self._load_and_validate_data()

    def _load_and_validate_data(self) -> None:
        """Loads data from CSV, validates it, and formats asset paths."""
        try:
            logger.info(f"Attempting to load data from '{self._data_path}'")
            if not self._data_path.is_file():
                logger.critical(f"Data file not found at '{self._data_path}'.")
                self._df = pd.DataFrame()
                return
            raw_df = pd.read_csv(self._data_path)
            
            validated_records: List[PharaohRecord] = []
            for index, row in raw_df.iterrows():
                try:
                    validated_records.append(PharaohRecord.model_validate(row.to_dict()))
                except ValidationError as e:
                    logger.warning(f"Skipping row {index+2} due to validation error: {e.errors()}")

            self._df = pd.DataFrame([rec.model_dump() for rec in validated_records])
            
            image_columns = [
                'image_local',
                'jsesh_birth_cartouche',
                'jsesh_throne_praenomen_cartouche',
            ]
            for col in image_columns:
                if col in self._df.columns:
                    self._df[col] = self._df[col].apply(
                        lambda filename: f"/assets/images/{filename}" if pd.notna(filename) else None
                    )

            logger.success(f"Successfully loaded, validated, and formatted {len(self._df)} records.")

        except Exception as e:
            logger.exception(f"A critical error occurred while processing data: {e}")
            self._df = pd.DataFrame()

    def is_data_loaded(self) -> bool:
        """Checks if the data was loaded successfully."""
        return hasattr(self, '_df') and not self._df.empty

    @property
    def df(self) -> pd.DataFrame:
        """Provides safe, read-only access to the DataFrame."""
        return self._df.copy() if self.is_data_loaded() else pd.DataFrame()

    def get_dynasty(self, dynasty_no: int) -> pd.DataFrame:
        """Retrieves all records for a specific dynasty."""
        if not self.is_data_loaded():
            return pd.DataFrame()
        return self.df[self.df['dynasty_no'] == dynasty_no]

    def get_all_dynasties(self) -> pd.DataFrame:
        """Retrieves a unique list of all dynasties."""
        if not self.is_data_loaded():
            return pd.DataFrame()
        return self.df[['dynasty_no', 'dynasty_name']].drop_duplicates().sort_values('dynasty_no')

    def get_all_periods(self) -> pd.DataFrame:
        """Retrieves a unique list of all kingdom/period names."""
        if not self.is_data_loaded():
            return pd.DataFrame()
        return self.df[['kingdom_name']].drop_duplicates().sort_values('kingdom_name')

    def get_period(self, period_name: str) -> pd.DataFrame:
        """
        Retrieves all records for a specific period/kingdom name.

        Args:
            period_name (str): name of the period to filter by

        Returns:
            pd.DataFrame: DataFrame containing records for the requested period
        """       
        if not self.is_data_loaded(): 
            return pd.DataFrame()
        return self.df.query(f'kingdom_name == "{period_name}"')

# singleton instance
data_file_path = Path(__file__).parent.parent.parent / "data" / "egypt_pharaohs_dynasties.csv"
pharaoh_data_service = DataService(data_file_path)