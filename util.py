""" Helper functions that can be 
called from any other layer, 
but mainly from the business logic layer."""

import datetime


def convert_UNIX_to_date(UNIX_timestamp):
    date = datetime.datetime.fromtimestamp(int(UNIX_timestamp))
    return str(date)


