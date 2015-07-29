# -*- encoding: utf-8 -*-
from abjad.tools import abctools


class CodeBlockSpecifier(abctools.AbjadValueObject):
    r'''A code block specifier.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_exceptions',
        '_hide',
        '_strip_prompt',
        '_text_width',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_exceptions=None,
        hide=None,
        strip_prompt=None,
        text_width=None,
        ):
        self._allow_exceptions = bool(allow_exceptions) or None
        self._hide = bool(hide) or None
        self._strip_prompt = bool(strip_prompt) or None
        if text_width is not None:
            if text_width is True:
                text_width = 80
            text_width = abs(int(text_width))
            if text_width < 1:
                text_width = None
        self._text_width = text_width

    ### PUBLIC PROPERTIES ###

    @property
    def allow_exceptions(self):
        r'''Is true if code block allows exceptions. Otherwise false.

        Returns boolean.
        '''
        return self._allow_exceptions

    @property
    def hide(self):
        r'''Is true if code block should be hidden. Otherwise false.
        
        Returns boolean.
        '''
        return self._hide

    @property
    def strip_prompt(self):
        r'''Is true if code block should strip Python prompt from output.
        Otherwise false.

        Returns boolean.
        '''
        return self._strip_prompt

    @property
    def text_width(self):
        r'''Gets text width wrap of code block.

        Returns integer or none.
        '''
        return self._text_width