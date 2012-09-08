from abjad.tools import durationtools
from abjad.tools import sequencetools
from experimental.selectortools.RatioPartSelector import RatioPartSelector


class CountRatioPartSelector(RatioPartSelector):
    r'''.. versionadded:: 1.0
    
    Partition `selector` by `ratio` of counts. Then select exactly one part.

        >>> from experimental import *

    Select all background measures starting during segment ``'red'`` in ``'Voice 1'``.
    Then partition these measures ``1:1`` by their count.
    Then select part ``0`` of this partition::

        >>> segment_selector = selectortools.SingleSegmentSelector(identifier='red')
        >>> inequality = timespaninequalitytools.expr_2_starts_during_expr_1(expr_1=segment_selector.timespan)
        >>> background_measure_selector = selectortools.BackgroundMeasureSelector(inequality=inequality)

    ::

        >>> count_ratio_part_selector = selectortools.CountRatioPartSelector(
        ... background_measure_selector, (1, 1), 0)

    ::

        >>> z(count_ratio_part_selector)
        selectortools.CountRatioPartSelector(
            selectortools.BackgroundMeasureSelector(
                inequality=timespaninequalitytools.TimespanInequality(
                    'expr_1.start <= expr_2.start < expr_1.stop',
                    expr_1=timespantools.SingleSourceTimespan(
                        selector=selectortools.SingleSegmentSelector(
                            identifier='red'
                            )
                        )
                    )
                ),
            mathtools.Ratio(1, 1),
            0
            )

    All count ratio item selector properties are read-only.
    '''

    ### INITIALIZER ###

    def __init__(self, selector, ratio, part):
        from experimental import selectortools
        assert isinstance(selector, selectortools.SliceSelector)
        RatioPartSelector.__init__(self, selector, ratio, part)

    ### PUBLIC METHODS ###

    def get_duration(self, score_specification, context_name):
        segment_specification = score_specification.get_segment_specification(self)
        time_signatures = segment_specification.time_signatures[:]
        parts = sequencetools.partition_sequence_by_ratio_of_lengths(time_signatures, self.ratio)
        part = parts[self.part]
        durations = [durationtools.Duration(x) for x in part]
        duration = durationtools.Duration(sum(durations))
        return duration

    def get_segment_start_offset(self, score_specification, context_name):
        segment_specification = score_specification.get_segment_specification(self)
        time_signatures = segment_specification.time_signatures[:]
        parts = sequencetools.partition_sequence_by_ratio_of_lengths(time_signatures, self.ratio)
        parts_before = parts[:self.part]
        durations_before = [
            sum([durationtools.Duration(x) for x in part_before]) for part_before in parts_before]
        duration_before = sum(durations_before)
        return durationtools.Offset(duration_before)

    def get_segment_stop_offset(self, score_specification, context_name):
        segment_specification = score_specification.get_segment_specification(self)
        time_signatures = segment_specification.time_signatures[:]
        parts = sequencetools.partition_sequence_by_ratio_of_lengths(time_signatures, self.ratio)
        part = parts[self.part]
        durations = [durationtools.Duration(x) for x in part]
        duration = durationtools.Duration(sum(durations))
        parts_before = parts[:self.part]
        durations_before = [
            sum([durationtools.Duration(x) for x in part_before]) for part_before in parts_before]
        duration_before = sum(durations_before)
        start_offset = durationtools.Offset(duration_before)
        stop_offset = duration_before + duration
        return durationtools.Offset(stop_offset)
