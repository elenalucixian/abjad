from abjad import *
import copy


def test_pitch___deepcopy___01( ):

   pitch = Pitch(13)
   new = copy.deepcopy(pitch)

   assert new is not pitch
   assert new.accidental is not pitch.accidental
