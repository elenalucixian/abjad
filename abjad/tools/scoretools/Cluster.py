# -*- coding: utf-8 -*-
from abjad.tools.scoretools.Container import Container


class Cluster(Container):
    '''Cluster.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> cluster = abjad.Cluster("c'8 <d' g'>8 b'8")
            >>> show(cluster) # doctest: +SKIP

        ..  docs::

            >>> f(cluster)
            \makeClusters {
                c'8
                <d' g'>8
                b'8
            }

        ::

            >>> cluster
            Cluster("c'8 <d' g'>8 b'8")

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Containers'

    __slots__ = (
        )

    _is_counttime_component = True

    ### PRIVATE METHODS ###

    def _format_open_brackets_slot(self, bundle):
        result = []
        contributor = ('self_brackets', 'open')
        if self.is_simultaneous:
            brackets_open = ['<<']
        else:
            brackets_open = ['{']
        contributions = [r'\makeClusters {}'.format(brackets_open[0])]
        result.append([contributor, contributions])
        return tuple(result)

    def _get_lilypond_format(self):
        self._update_now(indicators=True)
        return self._format_component()
