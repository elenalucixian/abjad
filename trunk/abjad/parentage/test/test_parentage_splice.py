from abjad import *


def test_parentage_splice_01( ):
   '''Splice leaves after leaf.'''

   notes = scale(4)
   first = notes[:2]
   t = Voice(first)
   Beam(t[:])

   r'''
   \new Voice {
      c'8 [
      d'8 ]
   }
   '''

   last = notes[2:]
   t[1].parentage._splice(last)

   r'''
   \new Voice {
      c'8 [
      d'8 ]
      e'8
      f'8
   }
   '''

   assert check(t)
   assert t.format == "\\new Voice {\n\tc'8 [\n\td'8 ]\n\te'8\n\tf'8\n}"
