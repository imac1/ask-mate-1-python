"""
 This layer contains common functions to read, write, or append CSV 
 files without feature-specific knowledge. Only this layer can access long term data storage. 
 In this case, CSV files are used as storage, later this will switch to SQL databases.
"""

import os
import pathlib
import csv


proj_dir_path = pathlib.Path(__file__).parent.resolve()
DATA_FILE_PATH_QS = os.path.join(proj_dir_path, "sample_data/question.csv")
DATA_FILE_PATH_ANS = os.path.join(proj_dir_path, "sample_data/answer.csv")


def get_raw_questions():
    questions = []
    with open(DATA_FILE_PATH_QS) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            questions.append(row)
    return questions
