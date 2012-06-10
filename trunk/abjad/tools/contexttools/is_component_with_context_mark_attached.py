from abjad.tools.componenttools.Component import Component
from abjad.tools.contexttools.ContextMark import ContextMark
from abjad.tools.contexttools.get_context_marks_attached_to_component import get_context_marks_attached_to_component


def is_component_with_context_mark_attached(expr, klasses=(ContextMark,)):
    r'''.. versionadded:: 2.0

    True when `expr` is a component with context mark of `klasses` attached::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> contexttools.TimeSignatureMark((4, 8))(staff[0])
        TimeSignatureMark((4, 8))(c'8)
        >>> f(staff)
        \new Staff {
            \time 4/8
            c'8
            d'8
            e'8
            f'8
        }
        >>> contexttools.is_component_with_context_mark_attached(staff[0])
        True

    Otherwise false::

        >>> contexttools.is_component_with_context_mark_attached(staff)
        False

    Return boolean.
    '''

    if isinstance(expr, Component):
        if len(get_context_marks_attached_to_component(expr, klasses=klasses)) == 1:
            return True

    return False
