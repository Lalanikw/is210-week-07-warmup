#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""looping lists with for loop"""


def process_data(data):
    """calculates the total and average of a list of numbers.
    Args:
        data (list): list of int

    Return:
        list: list of int

    Example:
        >>> process_data([1,2,3])
        >>>(6, 2.0)
    """
    total = 0
    for item in data:
        total += item
    average = total / float(len(data))
    return (total, average)
