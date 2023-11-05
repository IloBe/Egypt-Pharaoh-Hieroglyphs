"""
Delivers the projects root path.

Author: Ilona Brinkmeier
Date: Nov. 2023
"""

##########################
# imports
##########################

from pathlib import Path

##############################
# coding
##############################

def get_project_root() -> Path:
    ''' Returns path to project "Egypt_Pharaoh_Hieroglyphs" '''
    return Path(__file__).parent.parent
