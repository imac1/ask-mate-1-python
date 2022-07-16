""" Helper functions that can be 
called from any other layer, 
but mainly from the business logic layer."""

import datetime
from dateutil.parser import parse


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False


def convert_UNIX_to_date(UNIX_timestamp):
    if is_date(UNIX_timestamp, fuzzy=False):
        return UNIX_timestamp
    else:
        date = datetime.datetime.fromtimestamp(int(UNIX_timestamp))
        return str(date)