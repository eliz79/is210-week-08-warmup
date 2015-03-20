#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Docstring"""

bval = raw_input('Is the sky blue? ')


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
    return bval

if bval == True:
    print 'Yes'

else:
    print 'No'
