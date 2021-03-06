# -*- coding: utf-8 -*-
import collections
import copy
from abjad.tools.abctools.AbjadObject import AbjadObject


class LilyPondFile(AbjadObject):
    r'''A LilyPond file.

    ::

        >>> import abjad

    ..  container:: example

        Makes LilyPond file:

        ::

            >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
            >>> comments = [
            ...     'File construct as an example.',
            ...     'Parts shown here for positioning.',
            ...     ]
            >>> includes = [
            ...     'external-settings-file-1.ly',
            ...     'external-settings-file-2.ly',
            ...     ]
            >>> lilypond_file = abjad.LilyPondFile.new(
            ...     music=staff,
            ...     default_paper_size=('a5', 'portrait'),
            ...     comments=comments,
            ...     includes=includes,
            ...     global_staff_size=16,
            ...     )

        ::

            >>> lilypond_file.header_block.composer = abjad.Markup('Josquin')
            >>> lilypond_file.header_block.title = abjad.Markup('Missa sexti tonus')
            >>> lilypond_file.layout_block.indent = 0
            >>> lilypond_file.layout_block.left_margin = 15
            >>> show(lilypond_file) # doctest: +SKIP

        ::

            >>> print(format(lilypond_file)) # doctest: +SKIP
            % 2004-01-14 17:29

            % File construct as an example.
            % Parts shown here for positioning.

            \version "2.19.0"
            \language "english"

            \include "external-settings-file-1.ly"
            \include "external-settings-file-2.ly"

            #(set-default-paper-size "a5" 'portrait)
            #(set-global-staff-size 16)

            \header {
                composer = \markup { Josquin }
                title = \markup { Missa sexti toni }
            }

            \layout {
                indent = #0
                left-margin = #15
            }

            \paper {
            }

            \new Staff {
                c'8
                d'8
                e'8
                f'8
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_comments',
        '_date_time_token',
        '_default_paper_size',
        '_global_staff_size',
        '_includes',
        '_items',
        '_lilypond_language_token',
        '_lilypond_version_token',
        '_use_relative_includes',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        comments=None,
        date_time_token=None,
        default_paper_size=None,
        global_staff_size=None,
        includes=None,
        items=None,
        lilypond_language_token=None,
        lilypond_version_token=None,
        use_relative_includes=None,
        ):
        from abjad.tools import lilypondfiletools
        comments = comments or ()
        comments = tuple(comments)
        self._comments = comments
        self._date_time_token = None
        if date_time_token is not False:
            self._date_time_token = lilypondfiletools.DateTimeToken()
        self._default_paper_size = default_paper_size
        self._global_staff_size = global_staff_size
        includes = includes or ()
        includes = tuple(includes)
        self._includes = includes
        self._items = items or []
        self._lilypond_language_token = None
        if lilypond_language_token is not False:
            token = lilypondfiletools.LilyPondLanguageToken()
            self._lilypond_language_token = token
        self._lilypond_version_token = None
        if lilypond_version_token is not False:
            token = lilypondfiletools.LilyPondVersionToken()
            self._lilypond_version_token = token
        self._use_relative_includes = use_relative_includes

    ### SPECIAL METHODS ###

    def __format__(self, format_specification=''):
        r'''Formats LilyPond file.

        ..  container:: example

            Gets format:

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> print(format(lilypond_file)) # doctest: +SKIP
                % 2016-01-31 20:29
                <BLANKLINE>
                \version "2.19.35"
                \language "english"
                <BLANKLINE>
                \header {}
                <BLANKLINE>
                \layout {}
                <BLANKLINE>
                \paper {}

        ..  container:: example

            Works with empty layout and MIDI blocks:

                ::

                    >>> score = abjad.Score([abjad.Staff("c'8 d'8 e'8 f'8")])
                    >>> score_block = abjad.Block(name='score')
                    >>> layout_block = abjad.Block(name='layout')
                    >>> midi_block = abjad.Block(name='midi')
                    >>> score_block.items.append(score)
                    >>> score_block.items.append(layout_block)
                    >>> score_block.items.append(midi_block)
                  
                ::

                    >>> f(score_block)
                    \score {
                        \new Score <<
                            \new Staff {
                                c'8
                                d'8
                                e'8
                                f'8
                            }
                        >>
                        \layout {}
                        \midi {}
                    }

        Returns string.
        '''
        from abjad.tools import systemtools
        if format_specification in ('', 'lilypond'):
            return self._get_lilypond_format()
        elif format_specification == 'storage':
            return systemtools.StorageFormatAgent(self).get_storage_format()
        return str(self)

    def __getitem__(self, name):
        r'''Gets item with `name`.

        ..  container:: example

            Gets header block:

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file['header']
                <Block(name='header')>

        ..  container:: example

            Searches score:

            ::

                >>> voice_1 = abjad.Voice("c''4 b' a' g'", name='Custom Voice 1')
                >>> abjad.attach(abjad.LilyPondCommand('voiceOne'), voice_1)
                >>> voice_2 = abjad.Voice("c'4 d' e' f'", name='Custom Voice 2')
                >>> abjad.attach(abjad.LilyPondCommand('voiceTwo'), voice_2)
                >>> staff = abjad.Staff(
                ...     [voice_1, voice_2],
                ...     is_simultaneous=True,
                ...     name='Custom Staff',
                ...     )
                >>> score = abjad.Score([staff], name='Custom Score')
                >>> lilypond_file = abjad.LilyPondFile.new(score)
                >>> show(score) # doctest: +SKIP

            ..  docs::

                >>> f(score)
                \context Score = "Custom Score" <<
                    \context Staff = "Custom Staff" <<
                        \context Voice = "Custom Voice 1" {
                            \voiceOne
                            c''4
                            b'4
                            a'4
                            g'4
                        }
                        \context Voice = "Custom Voice 2" {
                            \voiceTwo
                            c'4
                            d'4
                            e'4
                            f'4
                        }
                    >>
                >>
                
            ::

                >>> lilypond_file['score']
                <Block(name='score')>

            ::

                >>> lilypond_file['Custom Score']
                <Score-"Custom Score"<<1>>>

            ::

                >>> lilypond_file[abjad.Score]
                <Score-"Custom Score"<<1>>>

            ::

                >>> lilypond_file['Custom Staff']
                <Staff-"Custom Staff"<<2>>>

            ::

                >>> lilypond_file[abjad.Staff]
                <Staff-"Custom Staff"<<2>>>

            ::

                >>> lilypond_file['Custom Voice 1']
                Voice("c''4 b'4 a'4 g'4", name='Custom Voice 1')

            ::

                >>> lilypond_file['Custom Voice 2']
                Voice("c'4 d'4 e'4 f'4", name='Custom Voice 2')

            ::

                >>> lilypond_file[abjad.Voice]
                Voice("c''4 b'4 a'4 g'4", name='Custom Voice 1')

        Returns item.

        Raises key error when no item with `name` is found.
        '''
        import abjad
        if self.score_block and self.score_block.items:
            score = self.score_block.items[0]
        else:
            score = None
        if isinstance(name, str):
            for item in self.items:
                if getattr(item, 'name', None) == name:
                    return item
            if score is not None:
                if score.name == name:
                    return score
                context = score[name]
                return context
            message = 'can not find item with name: {!r}.'
            message = message.format(name)
            raise KeyError(message)
        else:
            for item in self.items:
                if isinstance(item, name):
                    return item
            if score is not None:
                if isinstance(score, name):
                    return score
                prototype = abjad.scoretools.Context
                for context in abjad.iterate(score).by_class(prototype):
                    if isinstance(context, name):
                        return context
            message = 'can not find item of class: {!r}.'
            message = message.format(name)
            raise KeyError(message)

    def __illustrate__(self):
        r'''Illustrates LilyPond file.

        Returns LilyPond file unchanged.
        '''
        return self

    def __repr__(self):
        r'''Gets interpreter representation of LilyPond file.

        ..  container:: example

            Gets interpreter representation:

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file
                LilyPondFile(comments=[],
                date_time_token=DateTimeToken(date_string='...'), includes=[],
                items=[<Block(name='header')>, <Block(name='layout')>,
                <Block(name='paper')>, <Block(name='score')>],
                lilypond_language_token=LilyPondLanguageToken(),
                lilypond_version_token=LilyPondVersionToken(version_string='...'))

        Returns string.
        '''
        superclass = super(LilyPondFile, self)
        return superclass.__repr__()

    ### PRIVATE METHODS ###

    def _get_format_pieces(self):
        result = []
        if self.date_time_token is not None:
            string = '% {}'.format(self.date_time_token)
            result.append(string)
        result.extend(self._get_formatted_comments())
        includes = []
        if self.lilypond_version_token is not None:
            string = '{}'.format(self.lilypond_version_token)
            includes.append(string)
        if self.lilypond_language_token is not None:
            string = '{}'.format(self.lilypond_language_token)
            includes.append(string)
        includes = '\n'.join(includes)
        if includes:
            result.append(includes)
        if self.use_relative_includes:
            string = "#(ly:set-option 'relative-includes #t)"
            result.append(string)
        result.extend(self._get_formatted_includes())
        result.extend(self._get_formatted_scheme_settings())
        result.extend(self._get_formatted_blocks())
        return result

    ### PRIVATE METHODS ###

    def _get_formatted_blocks(self):
        result = []
        for x in self.items:
            if '_get_lilypond_format' in dir(x) and not isinstance(x, str):
                lilypond_format = format(x)
                if lilypond_format:
                    result.append(lilypond_format)
            else:
                result.append(str(x))
        return result

    def _get_formatted_comments(self):
        result = []
        for comment in self.comments:
            if ('_get_lilypond_format' in dir(comment) and
                not isinstance(comment, str)):
                lilypond_format = format(comment)
                if lilypond_format:
                    string = '% {}'.format(comment)
                    result.append(string)
            else:
                string = '% {!s}'.format(comment)
                result.append(string)
        if result:
            result = ['\n'.join(result)]
        return result

    def _get_formatted_includes(self):
        result = []
        for include in self.includes:
            if isinstance(include, str):
                string = r'\include "{}"'.format(include)
                result.append(string)
            else:
                result.append(format(include))
        if result:
            result = ['\n'.join(result)]
        return result

    def _get_formatted_scheme_settings(self):
        result = []
        default_paper_size = self.default_paper_size
        if default_paper_size is not None:
            dimension, orientation = default_paper_size
            string = "#(set-default-paper-size \"{}\" '{})"
            string = string.format(dimension, orientation)
            result.append(string)
        global_staff_size = self.global_staff_size
        if global_staff_size is not None:
            string = '#(set-global-staff-size {})'
            string = string.format(global_staff_size)
            result.append(string)
        if result:
            result = ['\n'.join(result)]
        return result

    def _get_lilypond_format(self):
        return '\n\n'.join(self._get_format_pieces())

    @staticmethod
    def _make_time_signature_context_block(
        font_size=3,
        minimum_distance=10,
        padding=4,
        ):
        import abjad
        assert isinstance(font_size, (int, float))
        assert isinstance(padding, (int, float))
        block = abjad.ContextBlock(
            type_='Engraver_group',
            name='TimeSignatureContext',
            )
        block.consists_commands.append('Axis_group_engraver')
        block.consists_commands.append('Time_signature_engraver')
        time_signature_grob = abjad.override(block).time_signature
        time_signature_grob.X_extent = (0, 0)
        time_signature_grob.X_offset = abjad.Scheme(
            'ly:self-alignment-interface::x-aligned-on-self'
            )
        time_signature_grob.Y_extent = (0, 0)
        time_signature_grob.break_align_symbol = False
        time_signature_grob.break_visibility = abjad.Scheme(
            'end-of-line-invisible',
            )
        time_signature_grob.font_size = font_size
        time_signature_grob.self_alignment_X = abjad.Scheme('center')
        spacing_vector = abjad.SpacingVector(
            0,
            minimum_distance,
            padding,
            0,
            )
        grob = abjad.override(block).vertical_axis_group
        grob.default_staff_staff_spacing = spacing_vector
        return block

    ### PUBLIC PROPERTIES ###

    @property
    def comments(self):
        r'''Gets comments of Lilypond file.

        ..  container:: example

            Gets comments:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.comments
                []

        Returns list.
        '''
        return list(self._comments)

    @property
    def date_time_token(self):
        r'''Gets date-time token.

        ..  container:: example

            Gets date-time token:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.date_time_token
                DateTimeToken()

        Returns date-time token or none.
        '''
        return self._date_time_token

    @property
    def default_paper_size(self):
        r'''Gets default paper size of LilyPond file.

        ..  container:: example

            Gets default paper size:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.default_paper_size is None
                True

        Set to pair or none.

        Defaults to none.

        Returns pair or none.
        '''
        return self._default_paper_size

    @property
    def global_staff_size(self):
        r'''Gets global staff size of LilyPond file.

        ..  container:: example

            Gets global staff size:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.global_staff_size is None
                True

        Set to number or none.

        Defaults to none.

        Returns number or none.
        '''
        return self._global_staff_size

    @property
    def header_block(self):
        r'''Gets header block.

        ..  container:: example

            Gets header block:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.header_block
                <Block(name='header')>

        Returns block or none.
        '''
        from abjad.tools import lilypondfiletools
        for item in self.items:
            if isinstance(item, lilypondfiletools.Block):
                if item.name == 'header':
                    return item

    @property
    def includes(self):
        r'''Gets includes of LilyPond file.

        ..  container:: example

            Gets includes:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.includes
                []

        Returns list.
        '''
        return list(self._includes)

    @property
    def items(self):
        r'''Gets items in LilyPond file.

        ..  container:: example

            Gets items:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> for item in lilypond_file.items:
                ...     item
                ...
                <Block(name='header')>
                <Block(name='layout')>
                <Block(name='paper')>
                <Block(name='score')>

        ..  container:: example

            Returns list:

            >>> isinstance(lilypond_file.items, list)
            True

        Returns list.
        '''
        return self._items

    @property
    def layout_block(self):
        r'''Gets layout block.

        ..  container:: example

            Gets layout block:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.layout_block
                <Block(name='layout')>

        Returns block or none.
        '''
        from abjad.tools import lilypondfiletools
        for item in self.items:
            if isinstance(item, lilypondfiletools.Block):
                if item.name == 'layout':
                    return item

    @property
    def lilypond_language_token(self):
        r'''Gets LilyPond language token.

        ..  container:: example

            Gets LilyPond language token:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.lilypond_language_token
                LilyPondLanguageToken()

        Returns LilyPond language token or none.
        '''
        return self._lilypond_language_token

    @property
    def lilypond_version_token(self):
        r'''Gets LilyPond version token.

        ..  container:: example

            Gets LilyPond version token:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.lilypond_version_token # doctest: +SKIP
                LilyPondVersionToken('2.19.35')

        Returns LilyPond version token or none.
        '''
        return self._lilypond_version_token

    @property
    def paper_block(self):
        r'''Gets paper block.

        ..  container:: example

            Gets paper block:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.paper_block
                <Block(name='paper')>

        Returns block or none.
        '''
        from abjad.tools import lilypondfiletools
        for item in self.items:
            if isinstance(item, lilypondfiletools.Block):
                if item.name == 'paper':
                    return item

    @property
    def score_block(self):
        r'''Gets score block.

        ..  container:: example

            Gets score block:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.score_block
                <Block(name='score')>

        Returns block or none.
        '''
        from abjad.tools import lilypondfiletools
        for item in self.items:
            if isinstance(item, lilypondfiletools.Block):
                if item.name == 'score':
                    return item

    @property
    def use_relative_includes(self):
        r'''Is true when LilyPond file should use relative includes.

        ..  container:: example

            Gets relative include flag:

            ::

                >>> lilypond_file = abjad.LilyPondFile.new()

            ::

                >>> lilypond_file.use_relative_includes is None
                True

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._use_relative_includes

    ### PUBLIC METHODS ###

    @classmethod
    def floating(class_, music=None):
        r'''Makes basic LilyPond file.

        ..  container:: example

            ::

                >>> score = abjad.Score()
                >>> time_signature_context = abjad.Context(
                ...     context_name='TimeSignatureContext',
                ...     )
                >>> durations = [(2, 8), (3, 8), (4, 8)]
                >>> maker = abjad.MeasureMaker()
                >>> measures = maker(durations)
                >>> time_signature_context.extend(measures)
                >>> score.append(time_signature_context)
                >>> staff = abjad.Staff()
                >>> staff.append(abjad.Measure((2, 8), "c'8 ( d'8 )"))
                >>> staff.append(abjad.Measure((3, 8), "e'8 ( f'8  g'8 )"))
                >>> staff.append(abjad.Measure((4, 8), "fs'4 ( e'8 d'8 )"))
                >>> score.append(staff)
                >>> lilypond_file = abjad.LilyPondFile.floating(score)
                >>> show(lilypond_file) # doctest: +SKIP

            ::

                >>> f(lilypond_file) # doctest: +SKIP
                % 2014-01-07 18:22

                \version "2.19.0"
                \language "english"

                #(set-default-paper-size "letter" 'portrait)
                #(set-global-staff-size 12)

                \header {}

                \layout {
                    \accidentalStyle forget
                    indent = #0
                    ragged-right = ##t
                    \context {
                        \name TimeSignatureContext
                        \type Engraver_group
                        \consists Axis_group_engraver
                        \consists Time_signature_engraver
                        \override TimeSignature.X-extent = #'(0 . 0)
                        \override TimeSignature.X-offset = #ly:self-alignment-interface::x-aligned-on-self
                        \override TimeSignature.Y-extent = #'(0 . 0)
                        \override TimeSignature.break-align-symbol = ##f
                        \override TimeSignature.break-visibility = #end-of-line-invisible
                        \override TimeSignature.font-size = #1
                        \override TimeSignature.self-alignment-X = #center
                        \override VerticalAxisGroup.default-staff-staff-spacing = #'((basic-distance . 0) (minimum-distance . 12) (padding . 6) (stretchability . 0))
                    }
                    \context {
                        \Score
                        \remove Bar_number_engraver
                        \accepts TimeSignatureContext
                        \override Beam.breakable = ##t
                        \override SpacingSpanner.strict-grace-spacing = ##t
                        \override SpacingSpanner.strict-note-spacing = ##t
                        \override SpacingSpanner.uniform-stretching = ##t
                        \override TupletBracket.bracket-visibility = ##t
                        \override TupletBracket.minimum-length = #3
                        \override TupletBracket.padding = #2
                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                        autoBeaming = ##f
                        proportionalNotationDuration = #(ly:make-moment 1 32)
                        tupletFullLength = ##t
                    }
                    \context {
                        \StaffGroup
                    }
                    \context {
                        \Staff
                        \remove Time_signature_engraver
                    }
                    \context {
                        \RhythmicStaff
                        \remove Time_signature_engraver
                    }
                }

                \paper {
                    left-margin = #20
                    system-system-spacing = #'((basic-distance . 0) (minimum-distance . 0) (padding . 12) (stretchability . 0))
                }

                \score {
                    \new Score <<
                        \new TimeSignatureContext {
                            {
                                \time 2/8
                                s1 * 1/4
                            }
                            {
                                \time 3/8
                                s1 * 3/8
                            }
                            {
                                \time 4/8
                                s1 * 1/2
                            }
                        }
                        \new Staff {
                            {
                                \time 2/8
                                c'8 (
                                d'8 )
                            }
                            {
                                \time 3/8
                                e'8 (
                                f'8
                                g'8 )
                            }
                            {
                                \time 4/8
                                fs'4 (
                                e'8
                                d'8 )
                            }
                        }
                    >>
                }

            ..  docs::

                >>> block = lilypond_file.layout_block.items[1]
                >>> f(block)
                \context {
                    \name TimeSignatureContext
                    \type Engraver_group
                    \consists Axis_group_engraver
                    \consists Time_signature_engraver
                    \override TimeSignature.X-extent = #'(0 . 0)
                    \override TimeSignature.X-offset = #ly:self-alignment-interface::x-aligned-on-self
                    \override TimeSignature.Y-extent = #'(0 . 0)
                    \override TimeSignature.break-align-symbol = ##f
                    \override TimeSignature.break-visibility = #end-of-line-invisible
                    \override TimeSignature.font-size = #1
                    \override TimeSignature.self-alignment-X = #center
                    \override VerticalAxisGroup.default-staff-staff-spacing = #'((basic-distance . 0) (minimum-distance . 10) (padding . 6) (stretchability . 0))
                }

        Makes LilyPond file.

        Wraps `music` in LilyPond ``\score`` block.

        Adds LilyPond ``\header``, ``\layout``, ``\paper`` and ``\score``
        blocks to LilyPond file.

        Defines layout settings for custom ``\TimeSignatureContext``.

        (Note that you must create and populate an Abjad context with name
        equal to ``'TimeSignatureContext'`` in order for
        ``\TimeSignatureContext`` layout settings to apply.)

        Applies many file, layout and paper settings.

        Returns LilyPond file.
        '''
        import abjad
        lilypond_file = LilyPondFile.new(
            music=music,
            default_paper_size=('letter', 'portrait'),
            global_staff_size=16,
            )
        lilypond_file.paper_block.left_margin = 20
        vector = abjad.SpacingVector(0, 0, 12, 0)
        lilypond_file.paper_block.system_system_spacing = vector
        lilypond_file.layout_block.indent = 0
        lilypond_file.layout_block.ragged_right = True
        command = abjad.LilyPondCommand('accidentalStyle forget')
        lilypond_file.layout_block.items.append(command)
        block = LilyPondFile._make_time_signature_context_block(
            font_size=1,
            padding=6,
            )
        lilypond_file.layout_block.items.append(block)
        block = abjad.ContextBlock(source_context_name='Score')
        lilypond_file.layout_block.items.append(block)
        block.accepts_commands.append('TimeSignatureContext')
        block.remove_commands.append('Bar_number_engraver')
        abjad.override(block).beam.breakable = True
        abjad.override(block).spacing_spanner.strict_grace_spacing = True
        abjad.override(block).spacing_spanner.strict_note_spacing = True
        abjad.override(block).spacing_spanner.uniform_stretching = True
        abjad.override(block).tuplet_bracket.bracket_visibility = True
        abjad.override(block).tuplet_bracket.padding = 2
        scheme = abjad.Scheme('ly:spanner::set-spacing-rods')
        abjad.override(block).tuplet_bracket.springs_and_rods = scheme
        abjad.override(block).tuplet_bracket.minimum_length = 3
        scheme = abjad.Scheme('tuplet-number::calc-fraction-text')
        abjad.override(block).tuplet_number.text = scheme
        abjad.setting(block).autoBeaming = False
        moment = abjad.SchemeMoment((1, 24))
        abjad.setting(block).proportionalNotationDuration = moment
        abjad.setting(block).tupletFullLength = True
        # provided as a stub position for user customization
        block = abjad.ContextBlock(source_context_name='StaffGroup')
        lilypond_file.layout_block.items.append(block)
        block = abjad.ContextBlock(source_context_name='Staff')
        lilypond_file.layout_block.items.append(block)
        block.remove_commands.append('Time_signature_engraver')
        block = abjad.ContextBlock(source_context_name='RhythmicStaff')
        lilypond_file.layout_block.items.append(block)
        block.remove_commands.append('Time_signature_engraver')
        return lilypond_file

    @classmethod
    def new(
        class_,
        music=None,
        date_time_token=None,
        default_paper_size=None,
        comments=None,
        includes=None,
        global_staff_size=None,
        lilypond_language_token=None,
        lilypond_version_token=None,
        use_relative_includes=None,
        ):
        r'''Makes basic LilyPond file.

        ..  container:: example

            Makes basic LilyPond file:

            ::

                >>> score = abjad.Score([abjad.Staff("c'8 d'8 e'8 f'8")])
                >>> lilypond_file = abjad.LilyPondFile.new(score)
                >>> lilypond_file.header_block.title = abjad.Markup('Missa sexti tonus')
                >>> lilypond_file.header_block.composer = abjad.Markup('Josquin')
                >>> lilypond_file.layout_block.indent = 0
                >>> lilypond_file.paper_block.top_margin = 15
                >>> lilypond_file.paper_block.left_margin = 15

            ::

                >>> f(lilypond_file) # doctest: +SKIP
                \header {
                    composer = \markup { Josquin }
                    title = \markup { Missa sexti tonus }
                }

                \layout {
                    indent = #0
                }

                \paper {
                    left-margin = #15
                    top-margin = #15
                }

                \score {
                    \new Score <<
                        \new Staff {
                            c'8
                            d'8
                            e'8
                            f'8
                        }
                    >>
                }

            ::

                >>> show(lilypond_file) # doctest: +SKIP

        Wraps `music` in LilyPond ``\score`` block.

        Adds LilyPond ``\header``, ``\layout``, ``\paper`` and ``\score``
        blocks to LilyPond file.

        Returns LilyPond file.
        '''
        from abjad.tools import lilypondfiletools
        if isinstance(music, lilypondfiletools.LilyPondFile):
            return music
        lilypond_file = class_(
            date_time_token=date_time_token,
            default_paper_size=default_paper_size,
            comments=comments,
            includes=includes,
            items=[
                lilypondfiletools.Block(name='header'),
                lilypondfiletools.Block(name='layout'),
                lilypondfiletools.Block(name='paper'),
                lilypondfiletools.Block(name='score'),
                ],
            global_staff_size=global_staff_size,
            lilypond_language_token=lilypond_language_token,
            lilypond_version_token=lilypond_version_token,
            use_relative_includes=use_relative_includes,
            )
        if music is not None:
            lilypond_file.score_block.items.append(music)
        return lilypond_file

    @classmethod
    def rhythm(
        class_,
        selections,
        divisions=None,
        attach_lilypond_voice_commands=None,
        implicit_scaling=None,
        pitched_staff=None,
        simultaneous_selections=None,
        time_signatures=None,
        ):
        r'''Makes rhythm-maker-style LilyPond file.

        ::

            >>> import abjad
            >>> from abjad.tools import rhythmmakertools

        ..  container:: example

            Makes rhythmic staff:

            ::

                >>> maker = rhythmmakertools.EvenRunRhythmMaker(exponent=1)
                >>> divisions = [(3, 4), (4, 8), (1, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = abjad.LilyPondFile.rhythm(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> score = lilypond_file[abjad.Score]
                >>> f(score)
                \new Score <<
                    \new TimeSignatureContext {
                        {
                            \time 3/4
                            s1 * 3/4
                        }
                        {
                            \time 4/8
                            s1 * 1/2
                        }
                        {
                            \time 1/4
                            s1 * 1/4
                        }
                    }
                    \new RhythmicStaff {
                        {
                            \time 3/4
                            {
                                c'8 [
                                c'8
                                c'8
                                c'8
                                c'8
                                c'8 ]
                            }
                        }
                        {
                            \time 4/8
                            {
                                c'16 [
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16 ]
                            }
                        }
                        {
                            \time 1/4
                            {
                                c'8 [
                                c'8 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Set time signatures explicitly:

            ::

                >>> maker = rhythmmakertools.EvenRunRhythmMaker(exponent=1)
                >>> divisions = [(3, 4), (4, 8), (1, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = abjad.LilyPondFile.rhythm(
                ...     selections,
                ...     [(6, 8), (4, 8), (2, 8)],
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> score = lilypond_file[abjad.Score]
                >>> f(score)
                \new Score <<
                    \new TimeSignatureContext {
                        {
                            \time 6/8
                            s1 * 3/4
                        }
                        {
                            \time 4/8
                            s1 * 1/2
                        }
                        {
                            \time 2/8
                            s1 * 1/4
                        }
                    }
                    \new RhythmicStaff {
                        {
                            \time 6/8
                            {
                                c'8 [
                                c'8
                                c'8
                                c'8
                                c'8
                                c'8 ]
                            }
                        }
                        {
                            \time 4/8
                            {
                                c'16 [
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16 ]
                            }
                        }
                        {
                            \time 2/8
                            {
                                c'8 [
                                c'8 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Makes pitched staff:

            ::

                >>> maker = rhythmmakertools.EvenRunRhythmMaker(exponent=1)
                >>> divisions = [(3, 4), (4, 8), (1, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = abjad.LilyPondFile.rhythm(
                ...     selections,
                ...     divisions,
                ...     pitched_staff=True,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> score = lilypond_file[abjad.Score]
                >>> f(score)
                \new Score <<
                    \new TimeSignatureContext {
                        {
                            \time 3/4
                            s1 * 3/4
                        }
                        {
                            \time 4/8
                            s1 * 1/2
                        }
                        {
                            \time 1/4
                            s1 * 1/4
                        }
                    }
                    \new Staff {
                        {
                            \time 3/4
                            {
                                c'8 [
                                c'8
                                c'8
                                c'8
                                c'8
                                c'8 ]
                            }
                        }
                        {
                            \time 4/8
                            {
                                c'16 [
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16 ]
                            }
                        }
                        {
                            \time 1/4
                            {
                                c'8 [
                                c'8 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Makes simultaneous voices:

            ::

                >>> maker_1 = rhythmmakertools.EvenRunRhythmMaker(exponent=1)
                >>> divisions = [(3, 4), (4, 8), (1, 4)]
                >>> selection_1 = abjad.select(maker_1(divisions))
                >>> for note in abjad.iterate(selection_1).by_class(abjad.Note):
                ...     note.written_pitch = abjad.NamedPitch("e'")
                ...
                >>> maker_2 = rhythmmakertools.EvenRunRhythmMaker(exponent=2)
                >>> selection_2 = abjad.select(maker_2(divisions))
                >>> selections = {
                ...     'Voice 1': selection_1,
                ...     'Voice 2': selection_2,
                ... }
                >>> lilypond_file = abjad.LilyPondFile.rhythm(
                ...     selections,
                ...     divisions,
                ...     )
                >>> voice_1 = lilypond_file['Voice 1']
                >>> abjad.attach(abjad.LilyPondCommand('voiceOne'), voice_1)
                >>> voice_2 = lilypond_file['Voice 2']
                >>> abjad.attach(abjad.LilyPondCommand('voiceTwo'), voice_2)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> f(lilypond_file[abjad.Score])
                \new Score <<
                    \new TimeSignatureContext {
                        {
                            \time 3/4
                            s1 * 3/4
                        }
                        {
                            \time 4/8
                            s1 * 1/2
                        }
                        {
                            \time 1/4
                            s1 * 1/4
                        }
                    }
                    \new Staff <<
                        \context Voice = "Voice 1" {
                            \voiceOne
                            {
                                e'8 [
                                e'8
                                e'8
                                e'8
                                e'8
                                e'8 ]
                            }
                            {
                                e'16 [
                                e'16
                                e'16
                                e'16
                                e'16
                                e'16
                                e'16
                                e'16 ]
                            }
                            {
                                e'8 [
                                e'8 ]
                            }
                        }
                        \context Voice = "Voice 2" {
                            \voiceTwo
                            {
                                c'16 [
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16
                                c'16 ]
                            }
                            {
                                c'32 [
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32
                                c'32 ]
                            }
                            {
                                c'16 [
                                c'16
                                c'16
                                c'16 ]
                            }
                        }
                    >>
                >>

        Used in rhythm-maker docs.

        Returns LilyPond file.
        '''
        import abjad
        if isinstance(selections, list):
            for selection in selections:
                if not isinstance(selection, abjad.Selection):
                    message = 'must be selection: {!r}.'
                    message = message.format(selection)
                    raise TypeError(message)
        elif isinstance(selections, dict):
            for selection in selections.values():
                if not isinstance(selection, abjad.Selection):
                    message = 'must be selection: {!r}.'
                    message = message.format(selection)
                    raise TypeError(message)
        else:
            message = 'must be list or dictionary: {!r}.'
            message = message.format(selections)
            raise TypeError(message)
        score = abjad.Score()
        package = abjad.lilypondfiletools
        lilypond_file = abjad.LilyPondFile.floating(score)
        if pitched_staff is None:
            for note in abjad.iterate(selections).by_class(
                abjad.Note,
                with_grace_notes=True,
                ):
                if note.written_pitch != abjad.NamedPitch("c'"):
                    pitched_staff = True
                    break
        if isinstance(selections, list):
            if divisions is None:
                duration = sum([_.get_duration() for _ in selections])
                divisions = [duration]
            time_signatures = time_signatures or divisions
            maker = abjad.MeasureMaker(implicit_scaling=implicit_scaling)
            measures = maker(time_signatures)
            if pitched_staff:
                staff = abjad.Staff(measures)
            else:
                staff = abjad.Staff(measures, context_name='RhythmicStaff')
            selections = abjad.Sequence(selections).flatten()
            selections_ = copy.deepcopy(selections)
            try:
                agent = abjad.mutate(staff)
                measures = agent.replace_measure_contents(selections)
            except StopIteration:
                if pitched_staff:
                    staff = abjad.Staff(selections_)
                else:
                    staff = abjad.Staff(
                        selections_,
                        context_name='RhythmicStaff',
                        )
        elif isinstance(selections, dict):
            voices = []
            for voice_name in sorted(selections):
                selections_ = selections[voice_name]
                selections_ = abjad.Sequence(selections_).flatten()
                selections_ = copy.deepcopy(selections_)
                voice = abjad.Voice(selections_, name=voice_name)
                if attach_lilypond_voice_commands:
                    voice_name_to_command_string = {
                        'Voice 1': 'voiceOne',
                        'Voice 2': 'voiceTwo',
                        'Voice 3': 'voiceThree',
                        'Voice 4': 'voiceFour',
                        }
                    command_string = voice_name_to_command_string.get(
                        voice_name,
                        )
                    if command_string:
                        command = abjad.LilyPondCommand(command_string)
                        abjad.attach(command, voice)
                voices.append(voice)
            staff = abjad.Staff(voices, is_simultaneous=True)
            if divisions is None:
                duration = abjad.inspect(staff).get_duration()
                divisions = [duration]
        else:
            message = 'must be list or dictionary of selections: {!r}.'
            message = message.format(selections)
            raise TypeError(message)
        score.append(staff)
        assert isinstance(divisions, collections.Sequence), repr(divisions)
        time_signatures = time_signatures or divisions
        context = abjad.scoretools.Context(context_name='TimeSignatureContext')
        maker = abjad.MeasureMaker(implicit_scaling=implicit_scaling)
        measures = maker(time_signatures)
        context.extend(measures)
        score.insert(0, context)
        return lilypond_file
