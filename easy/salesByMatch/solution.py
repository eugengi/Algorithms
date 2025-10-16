"""
|| HackerRank
    Problem: Sales by Match
    Level: easy
    Author: Shafaet
    Implementation: Eugene (apexDev37)

    Status: 8/8 of test cases PASSED
"""

# Copy and paste all your functional code from
# from the HackerRank platform.

def sock_merchant(count: int, socks: list[int]) -> int:
  organized_socks = group_by_color(socks)
  pairs = get_pairs(organized_socks)
  return sum(pairs)

  
def group_by_color(socks: list[int]) -> dict[int, int]:
  colors = set(socks)
  return {color: socks.count(color) for color in colors}


def get_pairs(socks: dict[int, int]) -> tuple[int]:
  pairs = [(matching_socks // 2) for color, matching_socks in socks.items()]
  return tuple(pairs)
