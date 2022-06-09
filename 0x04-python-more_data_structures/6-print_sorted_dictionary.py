#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys
    """
    [print("{}: {}".format(key, a_dictionary[key]))
        for key in sorted(a_dictionary)]
