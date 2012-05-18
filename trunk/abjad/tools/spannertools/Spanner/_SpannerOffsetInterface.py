from abjad.tools.abctools import AbjadObject
from abjad.tools import durationtools


class _SpannerOffsetInterface(AbjadObject):

    def __init__(self, client):
        self._client = client

    ### PUBLIC PROPERTIES ###

    @property
    def start(self):
        client = self._client
        if len(client):
            return client[0].start
        else:
            return Duration(0)

    @property
    def stop(self):
        client = self._client
        if len(client):
            last = client[-1]
            return last.stop
        else:
            return Duration(0)
