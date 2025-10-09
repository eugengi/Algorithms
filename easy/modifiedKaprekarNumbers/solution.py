"""
|| HackerRank
    Problem: Modified Kaprekar Numbers
    Level: easy
    Author: PRASHANTB1984
    Implementation: apexDev37

    Status: 6/6 test cases PASSED
"""

import math

# Copy and paste all your functional code from
# from the HackerRank platform.

def kaprekar_numbers(lower: int, upper: int) -> None:
  mkn = 0
  for val in range(lower, upper + 1):
    if _is_mkn(val):
      mkn += 1
      print(val, end=" ")
  print("INVALID RANGE") if mkn < 1 else print()


def _is_mkn(value: int) -> bool:
  square = int(math.pow(value, 2))
  digits = len(str(value))
  left, right = _split(square, digits)
  return (left + right) == value


def _split(value: int, digits: int) -> tuple[int]:
  stringy = str(value)
  left, right = stringy[:-digits], stringy[-digits:]
  left = 0 if left == "" else left
  return int(left), int(right)
