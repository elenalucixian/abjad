# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class Marimba(Instrument):
    r'''Marimba.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> marimba = abjad.instrumenttools.Marimba()
            >>> abjad.attach(marimba, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { Marimba }
                \set Staff.shortInstrumentName = \markup { Mb. }
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
        instrument_name='marimba',
        short_instrument_name='mb.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=('treble', 'bass'),
        middle_c_sounding_pitch=None,
        pitch_range='[F2, C7]',
        ):
        Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            )
        self._performer_names.extend([
            'percussionist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets marimba's allowable clefs.

        ..  container:: example

            ::

                >>> marimba.allowable_clefs
                ClefList([Clef('treble'), Clef('bass')])

            ::

                >>> show(marimba.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets marimba's name.

        ..  container:: example

            ::

                >>> marimba.instrument_name
                'marimba'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets marimba's instrument name markup.

        ..  container:: example

            ::

                >>> marimba.instrument_name_markup
                Markup(contents=['Marimba'])

            ::

                >>> show(marimba.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets marimba's range.

        ..  container:: example

            ::

                >>> marimba.pitch_range
                PitchRange('[F2, C7]')

            ::

                >>> show(marimba.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets marimba's short instrument name.

        ..  container:: example

            ::

                >>> marimba.short_instrument_name
                'mb.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets marimba's short instrument name markup.

        ..  container:: example

            ::

                >>> marimba.short_instrument_name_markup
                Markup(contents=['Mb.'])

            ::

                >>> show(marimba.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of marimba's written middle C.

        ..  container:: example

            ::

                >>> marimba.middle_c_sounding_pitch
                NamedPitch("c'")

            ::

                >>> show(marimba.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
