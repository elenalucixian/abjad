from abjad.components import Note
from abjad.components import Rest
from abjad.tools import durtools
from abjad.tools.leaftools._construct_tied_leaf import _construct_tied_leaf
from abjad.tools.leaftools._construct_tied_note import _construct_tied_note
from abjad.tools.leaftools._construct_tied_rest import _construct_tied_rest
from fractions import Fraction


def make_percussion_note(pitch, total_duration, max_note_duration = (1, 8)):
   '''Make percussion note::

      abjad> make_percussion_note(2, (1, 4), (1, 8))
      [Note(d', 8), Rest(8)]

   ::

      abjad> make_percussion_note(2, (1, 64), (1, 8))
      [Note(d', 64)]

   ::

      abjad> make_percussion_note(2, (5, 64), (1, 8))
      [Note(d', 16), Rest(64)]

   ::

      abjad> make_percussion_note(2, (5, 4), (1, 8))
      [Note(d', 8), Rest(1), Rest(8)]

   Return list of newly constructed note followed by zero or more newly constructed rests.

   Durations of note and rests returned will sum to `total_duration`.

   Duration of note returned will be no greater than `max_note_duration`.

   Duration of rests returned will sum to note duration taken from `total_duration`.

   Useful for percussion music where attack duration is negligible and tied notes undesirable.

   .. versionchanged:: 1.1.2
      renamed ``construct.percussion_note( )`` to
      ``notetools.make_percussion_note( )``.
   '''

   total_duration = Fraction(*durtools.duration_token_to_duration_pair(total_duration))
   max_note_duration = Fraction(*durtools.duration_token_to_duration_pair(max_note_duration))

   if max_note_duration < total_duration:
      rest_duration = total_duration - max_note_duration
      r = _construct_tied_rest(rest_duration)
      n = _construct_tied_note(pitch, max_note_duration)
   else:
      #n = _construct_tied_note(pitch, total_duration)
      n = _construct_tied_leaf(Note, total_duration, 
         pitches = pitch, tied = False)
      if 1 < len(n):
         for i in range(1, len(n)):
            n[i] = Rest(n[i])
      r = [ ]
   return n + r
