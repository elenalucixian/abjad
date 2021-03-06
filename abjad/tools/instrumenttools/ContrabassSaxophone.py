# -*- coding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.Instrument import Instrument


class ContrabassSaxophone(Instrument):
    r'''Contrabass saxophone.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> contrabass_saxophone = abjad.instrumenttools.ContrabassSaxophone()
            >>> abjad.attach(contrabass_saxophone, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { "Contrabass saxophone" }
                \set Staff.shortInstrumentName = \markup { "Cbass. sax." }
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
        instrument_name='contrabass saxophone',
        short_instrument_name='cbass. sax.',
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range='[C1, Ab3]',
        sounding_pitch_of_written_middle_c='Eb1',
        ):
        Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            pitch_range=pitch_range,
            sounding_pitch_of_written_middle_c=\
                sounding_pitch_of_written_middle_c,
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
        r'''Gets contrabass saxophone's allowable clefs.

        ..  container:: example

            ::

                >>> contrabass_saxophone.allowable_clefs
                ClefList([Clef(name='treble')])

            ::

                >>> show(contrabass_saxophone.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def instrument_name(self):
        r'''Gets contrabass saxophone's name.

        ..  container:: example

            ::

                >>> contrabass_saxophone.instrument_name
                'contrabass saxophone'

        Returns string.
        '''
        return Instrument.instrument_name.fget(self)

    @property
    def instrument_name_markup(self):
        r'''Gets contrabass saxophone's instrument name markup.

        ..  container:: example

            ::

                >>> contrabass_saxophone.instrument_name_markup
                Markup(contents=['Contrabass saxophone'])

            ::

                >>> show(contrabass_saxophone.instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.instrument_name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets contrabass saxophone's range.

        ..  container:: example

            ::

                >>> contrabass_saxophone.pitch_range
                PitchRange('[C1, Ab3]')

            ::

                >>> show(contrabass_saxophone.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_instrument_name(self):
        r'''Gets contrabass saxophone's short instrument name.

        ..  container:: example

            ::

                >>> contrabass_saxophone.short_instrument_name
                'cbass. sax.'

        Returns string.
        '''
        return Instrument.short_instrument_name.fget(self)

    @property
    def short_instrument_name_markup(self):
        r'''Gets contrabass saxophone's short instrument name markup.

        ..  container:: example

            ::

                >>> contrabass_saxophone.short_instrument_name_markup
                Markup(contents=['Cbass. sax.'])

            ::

                >>> show(contrabass_saxophone.short_instrument_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_instrument_name_markup.fget(self)

    @property
    def sounding_pitch_of_written_middle_c(self):
        r'''Gets sounding pitch of contrabass_saxophone's written middle C.

        ..  container:: example

            ::

                >>> contrabass_saxophone.sounding_pitch_of_written_middle_c
                NamedPitch('ef,,')

            ::

                >>> show(contrabass_saxophone.sounding_pitch_of_written_middle_c) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.sounding_pitch_of_written_middle_c.fget(self)
