"""
|| HackerRank
    Problem: Beautiful Triplets
    Level: easy
    Author: Shafaet
    Implementation: apexDev37
"""

# This is main entry point function to complete
# on the HackerRank platform. 
# Rename as per specified

def beautiful_triplets(step: int, vals: list[int]) -> int:
  first = get_first_triplets(step, vals)
  bt = compute_beautiful_triplets(step, first, vals)
  freq_map = count_val_frequency(vals)
  return sum(compute_bt_variations(triplet, freq_map) for triplet in bt)


def get_first_triplets(step: int, vals: list[int]) -> tuple[int]:
  upper_bound = vals[-1] - (step * 2)
  return tuple(filter(lambda x: x <= upper_bound, vals))


def compute_beautiful_triplets(step: int, first_triplets: tuple[int], vals: list[int]) -> tuple[tuple[int]]:
  triplets = []
  for first in set(first_triplets):
    triplet = first, first + step, first + (step * 2) 
    if set(triplet).issubset(vals):
      triplets.append(triplet)
  return tuple(triplets)


def count_val_frequency(vals: list[int]) -> dict[int, int]:
  freq = dict.fromkeys(set(vals), 0)
  for val in vals:
    freq[val] += 1
  return freq


def compute_bt_variations(triplet: tuple[int], frequency: dict[int, int]) -> int:
  return frequency[triplet[0]] * (frequency[triplet[1]] * frequency[triplet[2]])


def main() -> None:
  # Define your actual argument data here.
  match, vals = 3, [1, 2, 4, 5, 7, 8, 10]

  result = beautiful_triplets(match, vals)
  print(f"Number of beautiful triplets: {result}")


if __name__ == "__main__":
  main()
