# src/logging_setup.py

"""
Initializes the Loguru logger for the application.

Configures a centralized logger based on a JSON configuration file.
Should be imported once at the beginning of the main application entry point.
"""

##########################
# imports
##########################

import json
import sys

from pathlib import Path
from typing import Any
from loguru import logger

##########################
# coding
##########################

def setup_logging() -> None:
    """
    Setup of Loguru based on config file.

    Reads config from `config/logging_config.json`, then
    configures logger and handles potential errors by fall back to basic
    console logger.
    """
    config_path = Path(__file__).parent.parent / "config" / "logging_config.json"
    
    try:
        with open(config_path) as config_file:
            config: dict[str, Any] = json.load(config_file)
        
        logger.configure(**config)
        logger.info("Logger configured successfully from file.")

    except Exception as e:
        logger.add(sys.stderr, level="INFO")
        logger.error(
            f"Could not load logging config from {config_path}. Error: {e}. "
            "Using basic fallback logging."
        )

# logger initialisation during first module import
setup_logging()