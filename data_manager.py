"""
This is the layer between the server and the data. 
Functions here are called from `server.py` 
and use generic functions from `connection.py`.
"""

import connection
import util


raw_qs_dict = connection.get_raw_questions()


def get_questions_header():
    items = connection.get_raw_questions()
    QUESTIONS_HEADER = list(items[0].keys())
    return QUESTIONS_HEADER


def update_timestamp():
    for row in raw_qs_dict:
        for key, value in row.items():
            if key == "submission_time":
                new_time = util.convert_UNIX_to_date(value)
                row.update({"submission_time": new_time})
    return raw_qs_dict
