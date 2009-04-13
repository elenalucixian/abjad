from abjad.container.container import Container
from abjad.exceptions.exceptions import ContiguityError
from abjad.tools import clone
from abjad.helpers.excise import excise
from abjad.tools import iterate
from abjad.tools import iterate


def lcopy(expr, start = 0, stop = None):
   '''Copy consecutive leaves from start to stop in expr;
      copy all structure in the parentage of copied leaves,
      trimming and shrinking containers as necessary.
      
      When stop is None, copy all leaves from start in expr.'''

   from abjad.leaf.leaf import _Leaf

   # trivial leaf lcopy
   if isinstance(expr, _Leaf):
      return clone.fracture([expr])[0]

   # copy leaves from sequential containers only.
   if expr.parallel:
      raise ContiguityError('can not lcopy leaves from parallel container.')

   # assert valid start and stop
   leaves = expr.leaves
   assert start <= len(leaves)
   if stop is None:
      stop = len(leaves)
   assert stop > start

   # new: find start and stop leaves in expr
   start_leaf_in_expr = leaves[start]
   stop_leaf_in_expr = leaves[stop - 1]

   # find governor
   governor = leaves[start].parentage.governor

   # new: find start and stop leaves in governor
   governor_leaves = governor.leaves
   start_index_in_governor = governor_leaves.index(start_leaf_in_expr)
   stop_index_in_governor = governor_leaves.index(stop_leaf_in_expr)

   # copy governor
   governor_copy = clone.fracture([governor])[0]
   copy_leaves = governor_copy.leaves

   # new: find start and stop leaves in copy of governor
   start_leaf = copy_leaves[start_index_in_governor]
   stop_leaf = copy_leaves[stop_index_in_governor]

   # trim governor copy forwards from first leaf
   _found_start_leaf = False

   while not _found_start_leaf:
      from abjad.leaf.leaf import _Leaf
      leaf = iterate.naive(governor_copy, _Leaf).next( )
      if leaf == start_leaf:
         _found_start_leaf = True
      else:
         excise(leaf)

   #print 'moved on to trimming backwards ...'

   # trim governor copy backwards from last leaf
   _found_stop_leaf = False

   while not _found_stop_leaf:
      leaf = iterate.backwards(governor_copy, _Leaf).next( )
      if leaf == stop_leaf:
         _found_stop_leaf = True
      else:
         excise(leaf)

   # return trimmed governor copy
   return governor_copy
