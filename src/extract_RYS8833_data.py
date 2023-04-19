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

def NMEA_sentence_filter(NMEA_type: str ,sentences_list: list, filter_list: list) -> list[str]:
    """
    Filters a list containing all NMEA sentences generated by the RYS8833 module.

    Args:
        NMEA_type (str): The type of NMEA sentence to be filtered.

        sentences_list (list): List containing all  NMEA sentences generated by the RYS8833 module.

        filter_list (list): List containing all NMEA sentence filtered by type.

    Returns:
        list[str]: List containing all NMEA sentences  of a specific type generated by the
        RYS8833 module
    """

    for i in range(len(sentences_list)):
        if sentences_list[i][3:6] == NMEA_type:
            filter_list.append(sentences_list[i])

    return filter_list

def get_NMEA_type_attributes(NMEA_type: str) -> list[str]:
    """
    Get the attributes of a specific NMEA sentence type as list to be used as headers for this
    NMEA type dataframe object.

    Args:
        NMEA_type (str): NMEA sentence type whose attributes are gone be fetched.

    Returns:
        list[str]: List containing all attributes of a specific NMEA sentence type.
    """
    NMEA_type_attributes = getattr(src.utils, NMEA_type + "_header")
    return NMEA_type_attributes()

def NMEA_comma_splitter(sentence: str) -> str:
    """
    Split a NMEA sentence string by commas, but ignore exceptions characters listed in
    exceptions_string.

    Args:
        sentence (str): NMEA sentence string to be splited by comma.

    Returns:
        str: NMEA sentence string split by comma with exceptions ignored.
    """
    return re.split(r',(?![KMNT])', sentence)

def manipulate_UTC_of_Position(df_NMEA_type: pd.DataFrame, GMT: int) -> pd.DataFrame:
    """
    Transform the UTC of the position information into the HH:MM:SS format for both UTC
    and local time.

    Args:
        df_NMEA_type (pd.DataFrame): Pandas DataFrame object of a specific NMEA sentence type.

        GMT (int): Greenwich Mean Time (GMT) as an signed integer.

    Returns:
        pd.DataFrame: Pandas DataFrame object of a specific NMEA sentence type.
    """
    if "UTC_of_Position" in df_NMEA_type.columns:
        UTC_of_Position_list = df_NMEA_type["UTC_of_Position"].astype(str).to_list()

        UTC_of_Position_list = \
            [x.split(".")[0] for x in UTC_of_Position_list]
        UTC_of_Position_list = \
            [x[0:2] + ":" + x[2:4] + ":" + x[4:6] for x in UTC_of_Position_list]
        UTC_of_Position_list = \
            [datetime.datetime.strptime(x, "%H:%M:%S").time() for x in UTC_of_Position_list]
        GMT_of_Position_list = \
            [x.replace(hour=x.hour + GMT) for x in UTC_of_Position_list]

        df_NMEA_type["UTC"] = UTC_of_Position_list
        df_NMEA_type["GMT"] = GMT_of_Position_list

        return df_NMEA_type

    else:
        return df_NMEA_type