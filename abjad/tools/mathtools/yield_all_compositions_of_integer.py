# -*- coding: utf-8 -*-
import itertools


def yield_all_compositions_of_integer(n):
    r'''Yields all compositions of positive integer `n`.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> for tuple_ in abjad.mathtools.yield_all_compositions_of_integer(5):
            ...     tuple_
            ...
            (5,)
            (4, 1)
            (3, 2)
            (3, 1, 1)
            (2, 3)
            (2, 2, 1)
            (2, 1, 2)
            (2, 1, 1, 1)
            (1, 4)
            (1, 3, 1)
            (1, 2, 2)
            (1, 2, 1, 1)
            (1, 1, 3)
            (1, 1, 2, 1)
            (1, 1, 1, 2)
            (1, 1, 1, 1, 1)

    Lists parts in descending lex order.

    Parts sum to `n`.

    Finds small values of `n` easily.

    Takes around 4 seconds for `n` equal to 17.

    Returns integer tuple generator.
    '''
    from abjad.tools import mathtools
    compositions = []
    x = 0
    string_length = n
    while x < 2 ** (n - 1):
        binary_string = mathtools.integer_to_binary_string(x)
        binary_string = binary_string.zfill(string_length)
        l = [int(c) for c in list(binary_string)]
        partition = []
        g = itertools.groupby(l, lambda x: x)
        for value, group in g:
            partition.append(list(group))
        sublengths = [len(part) for part in partition]
        composition = tuple(sublengths)
        compositions.append(composition)
        x += 1
    for composition in reversed(sorted(compositions)):
        yield composition
