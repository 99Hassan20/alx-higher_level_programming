#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = max(list(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value == max_score:
            break
    return key
