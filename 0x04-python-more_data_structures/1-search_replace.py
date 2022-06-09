#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Replace all instances of search with replace
    """
    return([elem if elem != search else replace for elem in my_list])
