"""
Tests for problem: Sales by Match
Script: main.py
"""

import unittest

from main import (
  sock_merchant,
  get_pairs,
  group_by_color,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You might want to skip these tests if your approach changes.
  """

  def test_should_group_unorganized_socks_by_color(self) -> None:
    # Given
    socks = [1, 2, 5, 4, 5, 2, 1, 1, 1]
    expected = {1: 4, 2: 2, 4: 1, 5: 2}

    # When
    actual = group_by_color(socks)

    # Then
    self.assertIsInstance(actual, dict)
    self.assertDictEqual(actual, expected)

  def test_should_compute_pairs_for_organized_socks_grouped_by_color(
          self) -> None:
    # Given
    socks = {1: 4, 2: 2, 4: 1, 5: 2}
    expected = (2, 1, 0, 1,)

    # When
    actual = get_pairs(socks)

    # Then
    self.assertIsInstance(actual, tuple)
    self.assertEqual(actual, expected)


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = sock_merchant

  def test_should_return_number_of_sock_pairs_with_matching_colors(
          self) -> None:
    # Given
    socks = [1, 2, 5, 4, 5, 2, 1, 1, 1]
    expected = 4

    # When
    actual = self.under_test(..., socks)

    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
