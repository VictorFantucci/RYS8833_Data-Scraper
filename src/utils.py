"""
Script that contains functions beneficial to multiple modules.
"""

import pandas as pd

def get_NMEA_sentences() -> list:
    """
    Returns a list of the NMEA sentences types.
    """
    return ["GGA", "GLL", "GNS", "GSA", "GSV", "RMC", "VTG", "ZDA"]

def GGA_header() -> list:
    """
    Return a list of the parameters of the GGA : Global Positioning System Fix Data.
    """
    return ["Sentence_ID",
            "UTC_of_Position",
            "lat",
            "[N/S]",
            "lng",
            "[E/W]",
            "Quality Indicator",
            "Number_Satellites_in_Use",
            "HDOP",
            "Altitude_[m]",
            "Geodial_Separation_[m]",
            "Age_Of_DGPS_Data",
            "Checksum"]

def GLL_header() -> list:
    """
    Return a list of the parameters of the GLL : Geographic Position - Latitude / Longitude.
    """
    return ["Sentence_ID",
            "lat",
            "[N/S]",
            "lng",
            "[E/W]",
            "UTC_of_Position",
            "Status",
            "Checksum"]

def GNS_header() -> list:
    """
    Return a list of the parameters of the GNS: GNSS Fix Data.
    """
    return ["Sentence_ID",
            "UTC_of_Position",
            "lat",
            "[N/S]",
            "lng",
            "[E/W]",
            "Mode Indicator",
            "Number_Satellites_in_Use",
            "HDOP",
            "Altitude_[m]",
            "Geodial_Separation_[m]",
            "Checksum"]

def GSA_header() -> list:
    """
    Return a list of parameters of the GSA: GNSS DOP and Active Satellites.
    """
    return ["Sentence_ID",
            "2D/3D Mode",
            "Mode",
            "Used satellite #1",
            "Used satellite #2",
            "Used satellite #3",
            "Used satellite #4",
            "Used satellite #5",
            "Used satellite #6",
            "Used satellite #7",
            "Used satellite #8",
            "Used satellite #9",
            "Used satellite #10",
            "Used satellite #11",
            "Used satellite #12",
            "PDOP",
            "HDOP",
            "VDOP",
            "Checksum"]

def GSV_header() -> list:
    """
    Return a list of parameter of the GSV: GNSS Satellites In View.
    """
    return ["Sentence_ID",
            "Total_Number_of_Sentences",
            "Sentence_Number",
            "Total_Number_of_Satellites",
            "SV1_Satellite ID",
            "SV1_Elevation",
            "SV1_Azimuth",
            "SV1_C/N",
            "SV2_Satellite ID",
            "SV2_Elevation",
            "SV2_Azimuth",
            "SV2_C/N",
            "SV3_Satellite ID",
            "SV3_Elevation",
            "SV3_Azimuth",
            "SV3_C/N",
            "SV4_Satellite ID",
            "SV4_Elevation",
            "SV4_Azimuth",
            "SV4_C/N",
            "Checksum"]

def RMC_header() -> list:
    """
    Return a list of parameter of the RMC: Recommended Minimum Specific GNSS Data.
    """
    return ["Sentence_ID",
            "UTC_of_Position",
            "Status",
            "lat",
            "[N/S]",
            "lng",
            "[E/W]",
            "Speed_Over_Ground_[knot]",
            "Course_Over_Ground_[degree]",
            "Date",
            "Magnetic_Variation_[degree]",
            "Magnetic_Variation_E/W",
            "Mode_Indicator",
            "Checksum"]

def VTG_header() -> list:
    """
    Return a list of parameters of the VTG: Course Over Ground & Ground Speed.
    """
    return ["Sentence_ID",
            "Course_Over_Ground_True_[degree]",
            "Course_Over_Ground_Magnetic",
            "Speed_Over_Ground_[knot]",
            "Speed_Over_Ground_[km/h]",
            "Checksum"]

def ZDA_header() -> list:
    """
    Returns a list of parameters of the ZDA: Time & Date.
    """
    return ["Sentence_ID",
            "UTC_of_Position",
            "Day",
            "Month",
            "Year",
            "Local_Zone_Hours",
            "Checksum"]

