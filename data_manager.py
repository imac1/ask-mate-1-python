"""
This is the layer between the server and the data.
Functions here are called from `server.py`
and use generic functions from `connection.py`.
"""

import connection
import util


raw_qs_dict = connection.get_raw_data()
raw_answ_dict = connection.get_raw_data()


def get_questions_header():
    QUESTIONS_HEADER = list(raw_qs_dict[0].keys())
    return QUESTIONS_HEADER


def get_answ_header():
    ANSWERS_HEADER = list(raw_answ_dict[0].keys())
    return ANSWERS_HEADER


def update_timestamp(raw_dict):
    for row in raw_dict:
        for key, value in row.items():
            if key == "submission_time":
                new_time = util.convert_UNIX_to_date(value)
                row.update({"submission_time": new_time})
    return raw_dict


def display_qs():
    return update_timestamp(raw_qs_dict)


def display_answ():
    return update_timestamp(raw_answ_dict)
