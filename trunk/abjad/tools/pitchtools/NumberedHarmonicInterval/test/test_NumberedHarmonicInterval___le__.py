# -*- encoding: utf-8 -*-
from abjad import *


def test_NumberedHarmonicInterval___le___01():
    r'''Compare two ascending chromatic intervals.
    '''

    interval_1 = pitchtools.NumberedHarmonicInterval(2)
    interval_2 = pitchtools.NumberedHarmonicInterval(6)

    assert interval_1 <= interval_2
    assert not interval_2 <= interval_1


def test_NumberedHarmonicInterval___le___02():
    r'''Compare two descending chromatic intervals.
    '''

    interval_1 = pitchtools.NumberedHarmonicInterval(-2)
    interval_2 = pitchtools.NumberedHarmonicInterval(-6)

    assert interval_1 <= interval_2
    assert not interval_2 <= interval_1


def test_NumberedHarmonicInterval___le___03():
    r'''Compare two ascending chromatic intervals.
    '''

    interval_1 = pitchtools.NumberedHarmonicInterval(2)
    interval_2 = pitchtools.NumberedHarmonicInterval(2)

    assert interval_1 <= interval_2
    assert interval_2 <= interval_1


def test_NumberedHarmonicInterval___le___04():
    r'''Compare two descending chromatic intervals.
    '''

    interval_1 = pitchtools.NumberedHarmonicInterval(-2)
    interval_2 = pitchtools.NumberedHarmonicInterval(-2)

    assert interval_1 <= interval_2
    assert interval_2 <= interval_1
