"""
Tests for problem: Halloween Sale
Script: main.py
"""

import unittest

from main import (
  how_many_games,
  _get_discount_game_prices,
  _get_prices_within_budget,
  _compute_minimum_price_games,

)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You might want to skip these tests if your approach changes.
  """

  def setUp(self) -> None:
    self.starting_price = 20
    self.discount_price = 3
    self.minimum_price = 6
    self.budget = 80
    return super().setUp()

  def test_should_get_all_discount_game_prices_prior_minimum_discount_price(self) -> None:
    # Given
    expected = (20, 17, 14, 11, 8,)

    # When
    actual = _get_discount_game_prices(self.starting_price, self.discount_price, self.minimum_price)
    
    # Then
    self.assertIsInstance(actual, tuple)
    self.assertEqual(len(actual), ((self.starting_price - self.minimum_price) // self.discount_price) + 1)
    self.assertSequenceEqual(actual, expected)
  
  def test_should_filter_and_only_return_prices_within_customer_budget(self) -> None:
    # Given
    prices = (20, 17, 14, 11, 8,)
    budget = 40
    expected = (20, 17,)
    
    # When
    actual = _get_prices_within_budget(prices, budget)
    
    # Then
    self.assertIsInstance(actual, tuple)
    self.assertSequenceEqual(actual, expected)

  def test_should_compute_number_of_games_that_can_be_bought_at_minimum_price(self) -> None:
    # Given
    discount_prices = (20, 17, 14, 11, 8,)
    expected = 1
    
    # When
    actual = _compute_minimum_price_games(
      discount_prices, self.minimum_price, self.budget
    )
    
    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)

class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = how_many_games

    self.starting_price = 20
    self.discount_price = 3
    self.minimum_price = 6
    self.budget = 80
    return super().setUp()

  def test_should_compute_number_of_games_a_customer_can_buy_on_sale(self) -> None:
    # Given
    expected = 6
    
    # When
    actual = self.under_test(
      self.starting_price, self.discount_price, self.minimum_price, self.budget
    )

    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
