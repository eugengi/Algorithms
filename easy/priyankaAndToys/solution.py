"""
|| HackerRank
    Problem: Priyanka and Toys
    Level: Easy
    Author: amititkgp
    Implementation: Eugene (apexDev37) & Ndeda (ndedakaduki)

    Status: SUCCESS - All test cases passed!
"""

# Copy and paste all your functional code from
# from the HackerRank platform.


def toys(shipping_items):
  containers, current_min = 0, 0
  for item in sorted(shipping_items):
    if not current_min or item > current_min:
      current_min = item + 4
      containers += 1
  return containers
