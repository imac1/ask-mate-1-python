"""
This is the layer between the server and the data. 
Functions here are called from `server.py` 
and use generic functions from `connection.py`.
"""

import connection


def get_questions_header():
    items = connection.get_all_questions()
    QUESTIONS_HEADER = list(items[0].keys())
    return QUESTIONS_HEADER


def get_questions():
    qs = connection.get_all_questions()
    return qs