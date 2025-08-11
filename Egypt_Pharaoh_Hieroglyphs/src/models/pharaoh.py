# src/models/pharaoh.py

"""
Pydantic models for data validation.

Module defines the data structure for a single pharaoh record to ensure
data loaded from .csv file conforms to expected types and constraints
by using Pydantic V2 syntax.
"""

##########################
# imports
##########################

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

##########################
# coding
##########################

class PharaohRecord(BaseModel):
    """Represents a single record of a pharaoh from the dataset."""
    
    model_config = ConfigDict(
        populate_by_name = True,   # allows aliases like 'JSesh_birth_cartouche'
        coerce_numbers_to_str = True,
    )
    
    calendar_period_start: int
    calendar_period_end: int
    dynasty_no: int
    dynasty_name: str
    kingdom_name: str
    
    # optional fields
    king_horus: Optional[str] = Field(default = None)
    king_sedge_bee: Optional[str] = Field(default = None)
    king_birth_son_of_ra: Optional[str] = Field(default = None)
    
    # image and cartouche fields with aliases for .csv columns
    image_local: Optional[str] = Field(default = None)
    image_url: Optional[str] = Field(default = None)
    image_creator: Optional[str] = Field(default = None)
    jsesh_birth_cartouche: Optional[str] = Field(
        default = None,
        alias = 'JSesh_birth_cartouche',
    )
    jsesh_throne_praenomen_cartouche: Optional[str] = Field(
        default = None,
        alias = 'JSesh_throne_praenomen_cartouche',
    )

    @field_validator('*', mode = 'before')
    @classmethod
    def empty_str_to_none(cls, v):
        """Convert empty strings or pandas NaN/NaT to None."""
        if isinstance(v, str) and not v.strip():
            return None
        try:
            import pandas as pd
            if pd.isna(v):
                return None
        except ImportError:
            pass
        return v