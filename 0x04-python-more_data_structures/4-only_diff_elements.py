#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    return set only in one set
    """
    return((set_1 | set_2) - (set_1 & set_2))
