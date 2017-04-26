# -*- coding: utf-8 -*-
from abjad import *


def test_timespantools_Timespan___and___01():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(-10, -5)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([])

def test_timespantools_Timespan___and___02():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(-10, 0)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([])

def test_timespantools_Timespan___and___03():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(-10, 5)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 5)
    ])

def test_timespantools_Timespan___and___04():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(-10, 15)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 15)
    ])

def test_timespantools_Timespan___and___05():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(-10, 25)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 15)
    ])

def test_timespantools_Timespan___and___06():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(0, 10)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 10)
    ])

def test_timespantools_Timespan___and___07():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(0, 15)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 15)
    ])

def test_timespantools_Timespan___and___08():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(5, 10)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(5, 10)
    ])

def test_timespantools_Timespan___and___09():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(5, 15)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(5, 15)
    ])

def test_timespantools_Timespan___and___10():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(0, 25)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(0, 15)
    ])

def test_timespantools_Timespan___and___11():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(5, 25)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([
        timespantools.Timespan(5, 15)
    ])

def test_timespantools_Timespan___and___12():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(15, 25)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([])

def test_timespantools_Timespan___and___13():
    timespan_1 = timespantools.Timespan(0, 15)
    timespan_2 = timespantools.Timespan(20, 25)
    result = timespan_1 & timespan_2
    assert result == timespantools.TimespanList([])
