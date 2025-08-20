# src/services/timeline_services.py

"""
Data service for generating the pharaohs timeline.

This service encapsulates the business logic for fetching, curating and preparing
the data required for the interactive timeline page. It leverages the base
pharaoh_data_service and enriches the data with curated images and period info.

Note:
The Met Museum images are free of use,
the British Museum has been asked for usage and it has been allowed until the app is free, which is the case
(on Readme of the github repo it is stated that the SW is not allowed to sell).
"""

##########################
# imports
##########################

import os
import re
import pandas as pd
from pathlib import Path
from typing import Dict, Tuple, List, Optional, Any

from src.services.data_service import pharaoh_data_service, DataService

##########################
# coding
##########################

# --- Constants (PEP 8 Compliant) ---
# Define paths relative to the project root for robustness
PROJECT_ROOT = Path(__file__).parent.parent.parent
LOCAL_IMAGE_WEB_PATH = '/assets/images'

# --- Curated Data Layer ---
# future toDo: transfer to appropriate storage location
MUSEUM_IMAGES: Dict[str, Tuple[str, str, str]] = {
    # The Met Museum
    'Amenhotep I': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544453/1084273/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544453'),
    'Amenhotep III': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544186/1216912/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544186'),
    'Hatshepsut': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544449/1179859/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544449'),
    'Haremhab': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544692/1212612/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544692'),
    'Tutankhamun': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544690/1151837/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544690'),
    'Sety (merenptah) II': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544752/2110293/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544752'),
    'Thutmose III': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/547772/1151825/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/547772'),
    'Thutmose IV': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544826/1906708/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544826'),
    'Senusret II': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544232/1151819/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544232'),
    'Senusret III': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544184/1364529/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544184'),
    'Mentuhotep II': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/548212/1348549/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/548212'),
    'Nikare': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/543901/1214210/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/543901'),
    'Memi': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/543899/1151883/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/543899'),
    'Sahura': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/543882/1624707/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/543882'),
    'Khafra': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/543896/1177714/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/543896'),
    'Nectanebo II': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/544887/1157847/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/544887'),
    'Ptolemy III': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/547773/2108543/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/547773'),
    'Ptolemy II': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/548230/2110830/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/548230'),
    'Kushite': ('https://collectionapi.metmuseum.org/api/collection/v1/iiif/545027/1151824/main-image', 'The Met Museum', 'https://www.metmuseum.org/art/collection/search/545027'),
    # The British Museum
    'Narmer': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-08/3100BC_stone_palette_500x400.jpg?itok=PfnVyxUj', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA2051'),
    'Neferusobek': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-07/1795BC_cylinder_seal_500x400.jpg?itok=n0-wD5eq', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA16585'),
    'Ahmose': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-07/1550-1525BC_statue_ahmose_500x550.jpg?itok=kt766H9v', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA24953'),
    'Akhenaten': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-09/akhenaten_500x567.jpg?itok=DAchhGm7', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA59438'),
    'Ramses (meryamun) II': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-07/1279-1213BC_ramses_ii_statue_500x500.jpg?itok=RfCMWCOu', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA19'),
    'Ptolemy I': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-09/ptolemaic_king.jpg?itok=-GWrmbZw', 'The British Museum', 'https://www.britishmuseum.org/collection/object/Y_EA987'),
    'Cleopatra VII': ('https://www.britishmuseum.org/sites/default/files/styles/uncropped_small/public/2023-08/51-30BC_cleopatra_coin_500x400.jpg?itok=nlX1Unin', 'The British Museum', 'https://www.britishmuseum.org/collection/object/C_1847-0412-1'),
    # Wikipedia
    'Darius III': ('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Darius_III_of_Persia.jpg/250px-Darius_III_of_Persia.jpg', 'Wikipedia', 'https://en.wikipedia.org/wiki/Darius_III'),
    'Artaxerxes III': ('https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Artaxerxes_III_Pharao.jpg/250px-Artaxerxes_III_Pharao.jpg', 'Wikipedia', 'https://en.wikipedia.org/wiki/Artaxerxes_III')
}

# subtext from The Met Museum
BANNERS: Dict[str, Tuple[str, str]] = {
    'Early Dynastic Period': ("The Unification of Egypt", "https://images.metmuseum.org/CRDImages/eg/original/DT227483.jpg"),
    'Old Kingdom': ("The Age of the Pyramids", "https://images.metmuseum.org/CRDImages/eg/original/DT207389.jpg"),
    'First Intermediate Period': ("A Time of Division", "https://images.metmuseum.org/CRDImages/eg/original/DT207389.jpg"),
    'Middle Kingdom': ("Reunification & Golden Age", "https://images.metmuseum.org/CRDImages/eg/original/DT227483.jpg"),
    'Second Intermediate Period': ("The Hyksos' Rule", "https://images.metmuseum.org/CRDImages/eg/original/DT227483.jpg"),
    'New Kingdom': ("The Golden Age of Empire", "https://images.metmuseum.org/CRDImages/eg/original/DT207383.jpg"),
    'Third Intermediate Period': ("Fragmentation & Foreign Rulers", "https://images.metmuseum.org/CRDImages/eg/original/DT207383.jpg"),
    'Late Period': ("The Final Native Dynasties", "https://images.metmuseum.org/CRDImages/eg/original/DP-13669-015.jpg")
}


class TimelineService:
    """Manages the data and business logic for the pharaohs timeline."""

    def __init__(self, base_service: DataService):
        self._base_service = base_service
        self.df = self._prepare_dataframe()

    def _prepare_dataframe(self) -> pd.DataFrame:
        """
        Loads the base data, performs necessary cleaning and calculates
        period date ranges.
        """
        df = self._base_service.df.copy()
        df.dropna(subset = ['kingdom_name'], inplace = True)
        df['dynasty_no'] = pd.to_numeric(df['dynasty_no'], errors = 'coerce')
        return df

    def get_period_dates(self) -> Dict[str, Dict[str, int]]:
        """Calculates the min/max BC dates for each period."""
        period_dates_df = self.df.groupby('kingdom_name').agg(
            start = ('calendar_period_start', 'max'),
            end = ('calendar_period_end', 'min')
        ).astype(int)
        return period_dates_df.to_dict('index')

    @staticmethod
    def get_display_name(row: pd.Series) -> Optional[str]:
        """
        Determines the primary display name for a pharaoh based on dynasty.
        Early dynasties often used the Horus name more prominently.
        """
        horus = row.get('king_horus')
        sedge_bee = row.get('king_sedge_bee')
        birth_son_of_ra = row.get('king_birth_son_of_ra')
        dynasty = row.get('dynasty_no')
        
        # up to fourth dynasty, horus name is prominent
        if dynasty is not None and dynasty < 5:
            return horus if pd.notna(horus) else (sedge_bee if pd.notna(sedge_bee) else birth_son_of_ra)
        # afterwards birth son of ra is prominent
        else:
            return birth_son_of_ra if pd.notna(birth_son_of_ra) else (sedge_bee if pd.notna(sedge_bee) else horus)
        return None

    def get_image_html(self, row: pd.Series) -> Tuple[str, Optional[str]]:
        """
        Provides the associated image URL and source credit for a pharaoh based on a tiered system.
        It starts with Museum images, they have a higher quality. Local images are a fallback solution.
        Returns a tuple of (image_url, credit_html_string).
        """
        potential_names = [
            str(name) for name in [row.get('king_horus'), row.get('king_sedge_bee'), row.get('king_birth_son_of_ra')] if pd.notna(name)
        ]

        # Tier 1: Curated Museum Images
        for key, (img_url, source_name, source_url) in MUSEUM_IMAGES.items():
            pattern = r'\b' + re.escape(key) + r'\b'
            for name in potential_names:
                if re.search(pattern, name, re.IGNORECASE):
                    credit = (source_name, source_url)
                    return img_url, credit

        # Tier 2: Local File from 'image_local'
        if pd.notna(row.get('image_local')) and str(row.get('image_local')).strip():
            filename = str(row['image_local']).split('/')[-1] # Ensure we only have the filename
            if self._is_filename_valid_for_pharaoh(filename, potential_names):
                web_path = f"{LOCAL_IMAGE_WEB_PATH}/{filename}"
                credit = (row.get('image_creator'), None) if pd.notna(row.get('image_creator')) else (None, None)
                return web_path, credit

        # Tier 3: Fallback (no image available)
        return None, None

    @staticmethod
    def _is_filename_valid_for_pharaoh(filename: str, potential_names: List[str]) -> bool:
        """
        Validates if a local image filename matches a pharaoh's name.
        
        It handle roman numbers, if necessary.
        Pharaoh names can be substrings of a longer string including additional name parts in brackets;
        example: Ramses (meryamun) II
        """
        roman_numeral_pattern = re.compile(r'\s+(I{1,3}|IV|V|VI{1,3}|IX|X)$')
        for name in potential_names:
            cleaned_name = re.sub(r'\(.*\)', '', name).strip()
            match = roman_numeral_pattern.search(cleaned_name)
            valid_substrings = set()
            if match:
                numeral = match.group(1).lower()
                name_part = roman_numeral_pattern.sub('', cleaned_name).strip().lower().replace(' ', '-')
                valid_substrings.add(f"{name_part}-{numeral}")
                valid_substrings.add(f"{name_part}{numeral}")
                valid_substrings.add(name_part)
            else:
                valid_substrings.add(cleaned_name.lower().replace(' ', '-'))
            
            for substr in valid_substrings:
                if substr in filename.lower():
                    return True
        return False

# Singleton instance for use across Dash app
timeline_service = TimelineService(pharaoh_data_service)