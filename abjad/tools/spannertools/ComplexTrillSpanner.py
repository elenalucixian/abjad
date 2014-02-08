# -*- encoding: utf-8 -*-
from abjad.tools import pitchtools
from abjad.tools.spannertools.Spanner import Spanner
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import override


class ComplexTrillSpanner(Spanner):
    r'''A complex trill spanner.

    ..  container:: example

        ::

            >>> staff = Staff("c'4 ~ c'8 d'8 r8 e'8 ~ e'8 r8")
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff {
                c'4 ~
                c'8
                d'8
                r8
                e'8 ~
                e'8
                r8
            }

        ::

            >>> complex_trill = spannertools.ComplexTrillSpanner(
            ...     interval='P4',
            ...     )
            >>> attach(complex_trill, staff.select_leaves())
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff {
                \pitchedTrill
                c'4 ~ \startTrillSpan f'
                c'8
                <> \stopTrillSpan
                \once \override TrillSpanner.bound-details.left.text = \markup {
                    \null
                    }
                \pitchedTrill
                d'8 \startTrillSpan g'
                <> \stopTrillSpan
                r8
                \pitchedTrill
                e'8 ~ \startTrillSpan a'
                e'8
                <> \stopTrillSpan
                r8
            }

    Allows for specifying a trill pitch via a named interval.

    Avoids silences.

    Restarts the trill on every new pitched logical tie.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_interval',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        overrides=None,
        interval=None,
        ):
        Spanner.__init__(
            self,
            overrides=overrides,
            )
        if interval is not None:
            interval = pitchtools.NamedInterval(interval)
        self._interval = interval

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        new._interval = self.interval

    def _get_lilypond_format_bundle(self, leaf):
        from abjad.tools import lilypondnametools
        from abjad.tools import markuptools
        from abjad.tools import scoretools
        from abjad.tools import systemtools
        lilypond_format_bundle = systemtools.LilyPondFormatBundle()
        prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            scoretools.Skip,
            )
        if not isinstance(leaf, prototype):
            leaf_ids = [id(x) for x in self._leaves]
            logical_tie = inspect_(leaf).get_logical_tie()
            if leaf is logical_tie.head:
                previous_leaf = leaf._get_leaf(-1)
                if id(previous_leaf) in leaf_ids and \
                    not isinstance(previous_leaf, prototype):
                    grob_override = lilypondnametools.LilyPondGrobOverride(
                        grob_name='TrillSpanner',
                        is_once=True,
                        property_path=(
                            'bound-details',
                            'left',
                            'text',
                            ),
                        value=markuptools.Markup(r'\null'),
                        )
                    string = '\n'.join(grob_override.override_format_pieces)
                    lilypond_format_bundle.grob_overrides.append(string)
                if self.interval is not None:
                    string = r'\pitchedTrill'
                    lilypond_format_bundle.before.spanners.append(string)
                    if hasattr(leaf, 'written_pitch'):
                        written_pitch = leaf.written_pitch
                    elif hasattr(leaf, 'written_pitches'):
                        written_pitch = leaf.written_pitches[0]
                    trill_pitch = written_pitch.transpose(self.interval)
                    string = r'\startTrillSpan {!s}'.format(trill_pitch)
                else:
                    string = r'\startTrillSpan'
                lilypond_format_bundle.right.spanner_starts.append(string)
            if leaf is logical_tie.tail:
                next_leaf = leaf._get_leaf(1)
                if next_leaf is not None:
                    string = r'<> \stopTrillSpan'
                    lilypond_format_bundle.after.commands.append(string)
                else:
                    string = r'\stopTrillSpan'
                    lilypond_format_bundle.right.spanner_stops.append(string)
        if self._is_my_first_leaf(leaf):
            contributions = override(self)._list_format_contributions(
                'override',
                is_once=False,
                )
            lilypond_format_bundle.grob_overrides.extend(contributions)
        if self._is_my_last_leaf(leaf):
            contributions = override(self)._list_format_contributions(
                'revert',
                )
            lilypond_format_bundle.grob_reverts.extend(contributions)
        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def interval(self):
        r'''Gets optional interval of trill spanner.

        ..  container:: example

            ::

                >>> staff = Staff("c'4 d'4 e'4 f'4")
                >>> interval = pitchtools.NamedInterval('m3')
                >>> complex_trill = spannertools.ComplexTrillSpanner(
                ...     interval=interval)
                >>> attach(complex_trill, staff[1:-1])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> print format(staff)
                \new Staff {
                    c'4
                    \pitchedTrill
                    d'4 \startTrillSpan f'
                    <> \stopTrillSpan
                    \once \override TrillSpanner.bound-details.left.text = \markup {
                        \null
                        }
                    \pitchedTrill
                    e'4 \startTrillSpan g'
                    <> \stopTrillSpan
                    f'4
                }

            ::

                >>> complex_trill.interval
                NamedInterval('+m3')

        '''
        return self._interval
