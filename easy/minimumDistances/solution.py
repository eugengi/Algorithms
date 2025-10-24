"""
|| HackerRank
    Problem: Minimum Distances
    Level: Easy
    Author: Shafaet
    Implementation: Albert (achore26) & Eugene (eugengi)

    Status: 9/9 HackerRank test cases PASSED
"""

from collections.abc import Sequence

# Copy and paste all your functional code from
# from the HackerRank platform.

def minimum_distances(values: list[int]) -> int:
  distances = []
  for key in set(values):
    indices = get_indices(key, values)
    distance = get_minimum_distance(indices)
    distances.append(distance) if distance > 0 else ...
  return -1 if distances == [] else min(distances)
  

def get_indices(target: int, values: list[int]) -> tuple[int, ...]:
  return tuple(index for index, value in enumerate(values) if value == target)


def get_minimum_distance(values: Sequence[int]) -> int:
  minimum = 0
  if len(values) > 1:
    minimum = values[1] - values[0]
    for n in range(1, len(values) - 1):
      difference = values[n + 1] - values[n]
      if difference < minimum:
        minimum = difference
  return minimum
