#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""flip"""


def flip_keys(to_flip):
    """flip keys.

    Arg:
        to_flip (list) = this is a list with nested and other sequeces

    Return:
        list: flip list

    Examples:
        >>> LIST = [(1,2,3), 'abc']
        >>> NEW = flip_keys (LIST)
        >>> LIST is NEW
        >>>True
        >>> print LIST
        >>>[(3, 2, 1), 'cba']
    """
    counter = 0
    for item in to_flip:
        to_flip[counter] = item[::-1]
        counter += 1
    return to_flip
