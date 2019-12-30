"""
Solution for 528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/

Runtime: 232 ms, faster than 91.10% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 17.2 MB, less than 60.00% of Python3 online submissions for Random Pick with Weight.
"""
import random
import itertools
import bisect
from typing import List

class Solution:
  """
  Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

  Note:

  1 <= w.length <= 10000
  1 <= w[i] <= 10^5
  pickIndex will be called at most 10000 times.
  Example 1:

  Input:
  ["Solution","pickIndex"]
  [[[1]],[]]
  Output: [null,0]
  Example 2:

  Input:
  ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
  [[[1,3]],[],[],[],[],[]]
  Output: [null,0,1,1,1,0]
  Explanation of Input Syntax:

  The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
  """
  def __init__(self, w: List[int]):
    self.cum_sum = list(itertools.accumulate(w))

  def pickIndex(self) -> int:
    num = random.randint(1, self.cum_sum[-1])
    return bisect.bisect_left(self.cum_sum, num)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()