def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is not None:
        beg = a
        end = b
    else:
        beg = 0
        end = a

    if c is not None:
        right = c
    else:
        right = 1

    while True:
        if (right > 0 and beg >= end) or (right < 0 and beg <= end):
            break
        yield beg
        beg += right
