#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    a function that returns the weighted average of all integers tuple
    """
    if len(my_list) == 0:
        return (0)
    marks = [mark*weight for (mark, weight) in my_list]
    return sum(marks) / sum([weight for (mark, weight) in my_list])
