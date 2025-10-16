"""
|| HackerRank
    Problem: Sales by Match
    Level: easy
    Author: Shafaet
    Implementation: Eugene (apexDev37)
"""

# This is main entry point function to complete
# on the HackerRank platform. 
# Rename as per specified
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

  
def main() -> None:
  # Define your actual argument data here
  socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]

  result = sock_merchant(..., socks)
  print(f'Pairs of matching color socks: {result}')


if __name__ == "__main__":
  main()
