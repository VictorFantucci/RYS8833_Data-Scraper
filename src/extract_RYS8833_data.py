"""
Script that extracts the data obtained from the RYS8833 module log and save it as an excel file.
"""
import os
import re
import logging
import traceback
import datetime
import pandas as pd
import src.log4me
import src.utils

script_name = os.path.basename(__file__).removesuffix(".py")

def open_NMEA_file(file_path: str) -> list:
    """
    Open the log file containing the NMEA sentences and store them as lists inside a single list.

    Args:
        file_path (str): path to the log file containing the NMEA sentences.

    Returns:
        list: list containing lists  with all the NMEA sentences of the log file.
    """
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            data.append(line)

    return data