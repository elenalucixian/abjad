from abjad.tools import *
from experimental import *


def test_single_segment_solo_timespan_boundary_cases_01():
    '''Second division setting overwrites first division setting.
    Settings stop and start at same time.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8)])
    segment.set_divisions([(3, 16)])
    segment.set_divisions([(1, 16)])
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_timespan_boundary_cases_02():
    '''Second division setting overrides first division setting.
    First setting smaller than second setting.
    Settings start at same time.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8)])
    first_measure = segment.select_background_measure(0)
    segment.set_divisions_new([(3, 16)], timespan=first_measure)
    segment.set_divisions_new([(1, 16)])
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_timespan_boundary_cases_03():
    '''Second division setting overrides first division setting.
    First setting smaller than second setting.
    First setting starts after second setting.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8)])
    first_measure = segment.select_background_measure(1)
    segment.set_divisions_new([(3, 16)], timespan=first_measure)
    segment.set_divisions_new([(1, 16)])
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_timespan_boundary_cases_04():
    '''Second division overlaps and shortens the first.
    Result is two separate division regions that both express in score.
    Both the (compositional) order of specification
    and the (temporal) order of performance matter in this example.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8)])
    last_measure = segment.select_background_measure(1)
    segment.set_divisions_new([(3, 16)])
    segment.set_divisions_new([(1, 16)], timespan=last_measure)
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_timespan_boundary_cases_05():
    '''Second division sits in the middle of the first.
    Three division regions result.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    middle_measure = segment.select_background_measure(1)
    segment.set_divisions_new([(3, 16)])
    segment.set_divisions_new([(1, 16)], timespan=middle_measure)
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo_timespan_boundary_cases_06():
    '''Second division sits in the middle of the first.
    Three division regions result.
    Same as above but with a different selector.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template) 
    segment = score_specification.append_segment('red') 
    segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    middle_measure = segment.select_timespan_ratio_part((4, 3, 2), 1)
    segment.set_divisions_new([(3, 16)])
    segment.set_divisions_new([(1, 16)], timespan=middle_measure)
    segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)
