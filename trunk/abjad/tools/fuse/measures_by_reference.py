from abjad.measure import _Measure
from abjad.measure import RigidMeasure
from abjad.meter import Meter
from abjad.rational import Rational
from abjad.tools import check
from abjad.tools import containertools
from abjad.tools import metertools
from abjad.tools import parenttools
from abjad.tools.parenttools.switch import _switch
from abjad.tools.spannertools.give_dominant_to import _give_dominant_to


def measures_by_reference(measures):
   r'''Fuse `measures`::

      abjad> staff = Staff(measuretools.make([(1, 8), (2, 16)]))
      abjad> measuretools.populate(staff, Rational(1, 16))
      abjad> pitchtools.diatonicize(staff)
      abjad> Beam(staff.leaves)
      abjad> f(staff)
      \new Staff {
         {
            \time 1/8
            c'16 [
            d'16
         }
         {
            \time 2/16
            e'16
            f'16 ]
         }
      }
      
   ::
      
      abjad> fuse.measures_by_reference(staff[:])
      RigidMeasure(2/8, [c'16, d'16, e'16, f'16])

   ::

      abjad> f(staff)
      \new Staff {
         {
            \time 2/8
            c'16 [
            d'16
            e'16
            f'16 ]
         }
      }

   Return new measure.

   Allow parent-contiguous `measures`.

   Allow outside-of-score `measures`.

   Do not define measure fusion across intervening container boundaries.

   Calculate best new time signature.

   Instantiate new measure.

   Give `measures` contents to new measure.

   Give `measures` dominant spanners to new measure.

   Give `measures` parentage to new measure.

   Leave `measures` empty, unspanned and outside-of-score.
   '''

   check.assert_components(measures, 
      klasses = (_Measure), contiguity = 'strict', share = 'parent')

   if len(measures) == 0:
      return None

   ## TODO: Instantiate a new measure, even length is 1 ##

   if len(measures) == 1:
      return measures[0]

   parent, start, stop = parenttools.get_with_indices(measures)

   old_denominators = [ ]
   new_duration = Rational(0)
   for measure in measures:
      effective_meter = measure.meter.effective
      old_denominators.append(effective_meter.denominator)
      new_duration += effective_meter.duration

   new_meter = metertools.make_best(new_duration, old_denominators)

   music = [ ]
   for measure in measures:
      ## scale before reassignment to prevent tie chain scale drama
      multiplier = ~new_meter.multiplier * measure.meter.effective.multiplier
      containertools.scale_container_contents(measure, multiplier)
      measure_music = measure[:]
      _switch(measure_music, None)
      #containertools.scale_container_contents(measure_music, multiplier)
      music += measure_music

   new_measure = RigidMeasure(new_meter, music)

   if parent is not None:
      _give_dominant_to(measures, [new_measure])

   _switch(measures, None)
   if parent is not None:
      parent.insert(start, new_measure)

   return new_measure 
