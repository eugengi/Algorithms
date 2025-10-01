"""
Tests for problem: Beautiful Triplets
Script: main.py
"""

import unittest

from main import (
  beautiful_triplets,
  compute_beautiful_triplets,
  compute_bt_variations,
  count_val_frequency,
  get_first_triplets,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You want to skip these tests if your approach changes.
  """

  def test_should_get_first_values_for_potential_bt(self) -> None:
    # Given
    match, vals = 3, [1, 1, 2, 4, 4, 5, 5, 5, 7, 7, 8, 10]
    expected = (1, 1, 2, 4, 4)
    
    # When
    actual = get_first_triplets(match, vals)
    
    # Then
    self.assertIsInstance(actual, tuple)
    self.assertEqual(actual, expected)

  def test_should_compute_unique_bt_with_arithmetic_formula(self) -> None:
    # Given
    match, first_triplets = 3, (1, 1, 2, 4, 4)
    vals = [1, 1, 2, 4, 4, 5, 5, 5, 7, 7, 8, 10]
    expected = (
      (1, 4, 7),
      (2, 5, 8),
      (4, 7, 10),
    )
    
    # When
    actual = compute_beautiful_triplets(match, first_triplets, vals)
    
    # Then
    self.assertIsInstance(actual, tuple)
    self.assertCountEqual(
      [triplets[0] for triplets in expected], set(first_triplets))
    self.assertEqual(actual, expected)
  
  def test_should_count_frequency_of_each_value_for_values_list(self) -> None:
    # Given
    vals = [1, 1, 2, 4, 4, 5, 7]
    expected = {1: 2, 2: 1, 4: 2, 5: 1, 7: 1}
    
    # When
    actual = count_val_frequency(vals)
    
    # Then
    self.assertIsInstance(actual, dict)
    self.assertDictEqual(actual, expected)

  def test_should_count_all_triplet_variations_for_duplicate_values(self) -> None:
    # Given
    frequency = {1: 2, 2: 1, 4: 3, 5: 1, 7: 2}
    triplet = (1, 4, 7,)
    expected = 12
    
    # When
    actual = compute_bt_variations(triplet, frequency)
    
    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)

class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = beautiful_triplets

  def test_should_count_the_number_of_bt_in_the_given_sequence(self) -> None:
    # Given
    step, seq = 3, [1, 2, 4, 5, 7, 8, 10]
    expected = 3
    
    # When
    actual = self.under_test(step, seq)
    
    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()