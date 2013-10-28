# -*- encoding: utf-8 -*-
from abjad import *


def test_spannertools_BeamSpanner_detach_01():
    r'''Detach length-one spanner.
    '''

    staff = Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = spannertools.BeamSpanner()
    attach(beam, staff[0])

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8 [ ]
            cs'8
            d'8
            ef'8
            e'8
            f'8
            fs'8
            g'8
        }
        '''
        )

    beam.detach()

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8
            cs'8
            d'8
            ef'8
            e'8
            f'8
            fs'8
            g'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_spannertools_BeamSpanner_detach_02():
    r'''Detach length-four spanner.
    '''

    staff = Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = spannertools.BeamSpanner()
    attach(beam, staff[:4])

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8 [
            cs'8
            d'8
            ef'8 ]
            e'8
            f'8
            fs'8
            g'8
        }
        '''
        )

    beam.detach()

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8
            cs'8
            d'8
            ef'8
            e'8
            f'8
            fs'8
            g'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()
