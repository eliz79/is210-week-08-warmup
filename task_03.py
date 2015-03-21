#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Docstring"""

import decimal


def lexicographics(to_analyze):
    """This is a docstring.

    Arg:
        to_analyze(str): a required string
    Return:
        To return values as tuples, in the order defined
    Example:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))

        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    split_one = to_analyze.split('\n')
    length = []

    for words in split_one:
        split_two = words.split()
        length.append(len(split_two))
        t_length = len(split_one)
        overall_length = ((max(length), min(length)),
                          (sum(length) / decimal.Decimal(t_length)))
    return overall_length
