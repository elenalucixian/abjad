# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class SopraninoSaxophone(Instrument):
    r'''Sopranino saxophone.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> sopranino_saxophone = abjad.instrumenttools.SopraninoSaxophone()
            >>> abjad.attach(sopranino_saxophone, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { "Sopranino saxophone" }
                \set Staff.shortInstrumentName = \markup { "Sopranino sax." }
                c'4
                d'4
                e'4
                fs'4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        instrument_name='sopranino saxophone',
        short_instrument_name='sopranino sax.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[Db4, F#6]',
        middle_c_sounding_pitch='Eb4',
        ):
        Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            pitch_range=pitch_range,
            middle_c_sounding_pitch=\
                middle_c_sounding_pitch,
            )
        self._performer_names.extend([
            'wind player',
            'reed player',
            'single reed player',
            'saxophonist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets sopranino saxophone's allowable clefs.

        ..  container:: example

            ::

                >>> sopranino_saxophone.allowable_clefs
                ClefList([Clef('treble')])

            ::

                >>> show(sopranino_saxophone.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets sopranino saxophone's name.

        ..  container:: example

            ::

                >>> sopranino_saxophone.instrument_name
                'sopranino saxophone'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets sopranino saxophone's instrument name markup.

        ..  container:: example

            ::

                >>> sopranino_saxophone.instrument_name_markup
                Markup(contents=['Sopranino saxophone'])

            ::

                >>> show(sopranino_saxophone.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets sopranino saxophone's range.

        ..  container:: example

            ::

                >>> sopranino_saxophone.pitch_range
                PitchRange('[Db4, F#6]')

            ::

                >>> show(sopranino_saxophone.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets sopranino saxophone's short instrument name.

        ..  container:: example

            ::

                >>> sopranino_saxophone.short_instrument_name
                'sopranino sax.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets sopranino saxophone's short instrument name markup.

        ..  container:: example

            ::

                >>> sopranino_saxophone.short_instrument_name_markup
                Markup(contents=['Sopranino sax.'])

            ::

                >>> show(sopranino_saxophone.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of sopranino saxophone's written middle C.

        ..  container:: example

            ::

                >>> sopranino_saxophone.middle_c_sounding_pitch
                NamedPitch("ef'")

            ::

                >>> show(sopranino_saxophone.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
