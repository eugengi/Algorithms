"""
|| HackerRank
    Problem: Strange Counter
    Level: Easy
    Author: Shafaet
    Implementation: eugengi

    Status: PASSED - 12/12 test cases passed
"""

# Copy and paste all your functional code from
# from the HackerRank platform.

import math
from typing import Iterator

def strange_counter(time: int) -> int:
  for first_value in _generate_cycle_fv_sequence():
    first_second, last_second = _compute_cycle_time(first_value)
    if _is_within_range(time, (first_second, last_second,)):
      relative_position = time - first_second
      return (first_value - relative_position)
  return 0

def _generate_cycle_fv_sequence(start: int = 3) -> Iterator[int]:
  while start < math.pow(10, 12):
    yield start
    start *= 2


def _compute_cycle_time(first_value: int) -> tuple[int, int]:
  first_second = first_value - 2
  last_second = (first_second + first_value) - 1
  return (first_second, last_second,)


def _is_within_range(time: int, cycle: tuple[int, int,]) -> bool:
  first_time, last_time = cycle
  return first_time <= time <= last_time
