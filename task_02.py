#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Docstring"""


def bool_to_str(bval):
    """This is a docstring.

    Arg:
        bval(boolean): a boolean/boolean-like value that can evaluate
                       for true or false

    Return:
        To return a string 'Yes' for True, otherwise 'No' for False

    Example:
        >>>impot task_02
        >>>import task_02.bool_to_str(True)
        'Yes'

        >>>import task_02
        >>>import task_02.bool_to_str(")
        'No'
    """
    answer = True
    if answer:
        return 'Yes'
    else:
        return 'No'
