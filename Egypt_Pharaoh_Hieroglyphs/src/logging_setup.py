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

from datetime import datetime
from pathlib import Path
from typing import Any, Dict
from loguru import logger

##########################
# coding
##########################

def setup_logging() -> None:
    """
    Setup of Loguru based on config file and programmatic additions.

    Loads base console configuration from the JSON file, then
    padds a file handler with a unique, timestamped name for each
    application session.
    It sets a retention policy to keep 5 most recent log files only.
    """
    config_path = Path(__file__).parent.parent / "config" / "logging_config.json"
    
    try:
        with open(config_path) as config_file:
            config: Dict[str, Any] = json.load(config_file)

        # handles sys.stderr sink
        if "handlers" in config:
            for handler in config["handlers"]:
                if handler.get("sink") == "sys.stderr":
                    handler["sink"] = sys.stderr
        
        # base (console) logger config
        logger.configure(**config)
        
        # add file logger
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok = True)

        # unique filename for session via timestamp
        session_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file_path = log_dir / f"app_{session_timestamp}.log"

        # add file sink with retention, rotation policies
        logger.add(
            sink = log_file_path,
            level = "DEBUG",
            format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation = "10 MB",      # size-based rotation
            retention = 5,           # keep 5 most recent files
            compression = "zip",     # keep compression for archived logs
            enqueue = True,          # logging non-blocking
            backtrace = True,        # full stack trace on exceptions
            diagnose = True
        )

        logger.info("Success: Logger configured with console and session-file handlers.")

    except Exception as e:
        logger.remove()
        logger.add(sys.stderr, level = "INFO")
        logger.error(
            f"Could not configure logging. Error: {e}. "
            "Using basic fallback logging."
        )

# logger initialisation during first module import
setup_logging()