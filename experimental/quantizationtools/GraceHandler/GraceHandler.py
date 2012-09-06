import abc
from abjad.tools import abctools


class GraceHandler(abctools.AbjadObject):
    '''Abstract base class.

    Determines what pitch, if any, will be selected from a list of QEvents to
    be applied to an attack-point generated by a QGrid, and whether there should be
    a GraceContainer attached to that attack-point.

    When called on a sequence of QEvents, GraceHandler subclasses should return a pair,
    where the first item of the pair is a sequence of pitch tokens or None, and where the
    second item of the pair is a GraceContainer instance or None.
    '''

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self, q_events):
        raise NotImplemented
