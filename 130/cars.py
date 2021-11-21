from collections import Counter

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    models = set(
        [
            entry["model"]
            for entry in data
            if entry["automaker"] == automaker and entry["year"] == year
        ]
    )
    return models


def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    automakers = list(set([entry["automaker"] for entry in data]))
    num_models_per_automaker = {}
    for automaker in automakers:
        num_models_per_automaker[automaker] = get_models(automaker, year)
    high_score = 0
    high_scorer = ""
    for automaker in automakers:
        if len(num_models_per_automaker[automaker]) > high_score:
            high_score = len(num_models_per_automaker[automaker])
            high_scorer = automaker
    return high_scorer
