"""
|| HackerRank
    Problem: Halloween Sale
    Level: Easy
    Author: kevinsogo
    Implementation: eugengi
    
    Status: PASSED - 51/51 test cases passed'
"""

# Copy and paste all your functional code from
# from the HackerRank platform.

def how_many_games(
  starting_price: int,
  discount_price: int,
  minimum_price: int,
  budget: int
) -> int:
  discount_prices = _get_discount_game_prices(starting_price, discount_price, minimum_price)
  if sum(discount_prices) > budget:
    return len(_get_prices_within_budget(discount_prices, budget))
  return len(discount_prices) + _compute_minimum_price_games(discount_prices, minimum_price, budget)
  

def _get_discount_game_prices(
  starting_price: int, 
  discount_price: int, 
  minimum_price: int
) -> tuple[int, ...]:
  prices = tuple(reversed(range(minimum_price, starting_price + 1)))
  discount_prices = [prices[n] for n in range(0, len(prices), discount_price)]
  return tuple(discount_prices)


def _get_prices_within_budget(
    prices: tuple[int, ...], 
    budget: int
) -> tuple[int, ...]:
  counter, within_budget = 0, []
  while amount := (sum(within_budget) + prices[counter]) <= budget:
    within_budget.append(prices[counter])
    counter += 1
  return tuple(within_budget)


def _compute_minimum_price_games(
  discount_prices: tuple[int, ...],
  minimum_price: int,
  budget: int
) -> int:
  balance = budget - sum(discount_prices)
  return balance // minimum_price
