"""
Tests for problem: Sales by Match
Script: main.py
"""

import unittest

from main import (
  sock_merchant,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You might want to skip these tests if your approach changes.
  """

  ...


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = sock_merchant

  def test_should_return_number_of_sock_pairs_with_matching_colors(self) -> None:
    ...


if __name__ == '__main__':
  unittest.main()
