# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class ClarinetInEFlat(Instrument):
    r'''Clarinet in E-flat.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> clarinet = abjad.instrumenttools.ClarinetInEFlat()
            >>> abjad.attach(clarinet, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { "Clarinet in E-flat" }
                \set Staff.shortInstrumentName = \markup { "Cl. E-flat" }
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
        instrument_name='clarinet in E-flat',
        short_instrument_name='cl. E-flat',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        middle_c_sounding_pitch='Eb4',
        pitch_range='[F3, C7]',
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
            'wind player',
            'reed player',
            'single reed player',
            'clarinettist',
            'clarinetist',
            ])

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets clarinet in E-flat's allowable clefs.

        ..  container:: example

            ::

                >>> clarinet.allowable_clefs
                ClefList([Clef('treble')])

            ::

                >>> show(clarinet.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets clarinet in E-flat's name.

        ..  container:: example

            ::

                >>> clarinet.instrument_name
                'clarinet in E-flat'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets clarinet in E-flat's instrument name markup.

        ..  container:: example

            ::

                >>> clarinet.instrument_name_markup
                Markup(contents=['Clarinet in E-flat'])

            ::

                >>> show(clarinet.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets clarinet in E-flat's range.

        ..  container:: example

            ::

                >>> clarinet.pitch_range
                PitchRange('[F3, C7]')

            ::

                >>> show(clarinet.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets clarinet in E-flat's short instrument name.

        ..  container:: example

            ::

                >>> clarinet.short_instrument_name
                'cl. E-flat'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets clarinet in E-flat's short instrument name markup.

        ..  container:: example

            ::

                >>> clarinet.short_instrument_name_markup
                Markup(contents=['Cl. E-flat'])

            ::

                >>> show(clarinet.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of clarinet in E-flat's written middle C.

        ..  container:: example

            ::

                >>> clarinet.middle_c_sounding_pitch
                NamedPitch("ef'")

            ::

                >>> show(clarinet.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)
