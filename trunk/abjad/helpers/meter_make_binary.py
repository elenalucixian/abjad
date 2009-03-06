from abjad.helpers.in_terms_of import _in_terms_of
from abjad.helpers.next_least_power_of_two import _next_least_power_of_two
from abjad.meter.meter import Meter
from abjad.rational.rational import Rational


def meter_make_binary(nonbinary_meter, contents_multiplier = Rational(1)):
   '''Change nonbinary meter to binary.
      Return meter.

      meter_make_binary(Meter(3, 12))
      Meter(2, 8)'''
   
   # check input
   assert isinstance(nonbinary_meter, Meter)
   assert isinstance(contents_multiplier, Rational)

   # save nonbinary meter and denominator
   nonbinary_denominator = nonbinary_meter.denominator

   # find binary denominator
   if contents_multiplier == Rational(1):
      binary_denominator = _next_least_power_of_two(nonbinary_denominator)
   else:
      binary_denominator = _next_least_power_of_two(nonbinary_denominator, 1)

   # find binary pair
   nonbinary_pair = (nonbinary_meter.numerator, nonbinary_meter.denominator)
   binary_pair = _in_terms_of(nonbinary_pair, binary_denominator)

   # update meter numerator and denominator
   nonbinary_meter.numerator = binary_pair[0]
   nonbinary_meter.denominator = binary_pair[1]

   # return meter
   return nonbinary_meter
