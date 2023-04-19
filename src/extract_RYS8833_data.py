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

