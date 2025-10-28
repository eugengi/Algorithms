"""
Tests for problem: Minimum Distances
Script: main.py
"""

import unittest

from main import (
  get_indices,
  get_minimum_distance,
  minimum_distances,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You might want to skip these tests if your approach changes.
  """

  def test_should_get_all_indices_for_recurring_element_in_list(self) -> None:
    # Given
    target, values = 3, [3, 2, 1, 2, 3]
    expected = (0, 4,)
    
    # When
    actual = get_indices(target, values)
    
    # Then
    self.assertIsInstance(actual, tuple)
    self.assertEqual(actual, expected)

  def test_should_return_the_minimum_difference_in_indices_sequence(self) -> None:
    # Given
    indices = [0, 4, 6, 8, 11, 12]
    excepted = 1
    
    # When
    actual = get_minimum_distance(indices)
    
    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, excepted)


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = minimum_distances
  

  def test_should_find_minimum_distance_between_pair_of_equal_elements(self) -> None:
    # Given
    values = [7, 1, 3, 4, 1, 7]
    expected = 3

    # When
    actual = self.under_test(values)

    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)

  def test_should_return_negative_for_no_minimum_distance_between_elements(self) -> None:
    # Given
    values = [1, 2, 3, 4]
    expected = -1
    
    # When
    actual = self.under_test(values)
    
    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
