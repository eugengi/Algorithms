"""
Tests for problem: Modified Kaprekar Numbers
Script: main.py
"""

import unittest

from main import (
  kaprekar_numbers,
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
    self.under_test = kaprekar_numbers

  def test_should_output_mkn_list_in_expected_format(self) -> None:
    ...

  def test_should_output_invalid_for_no_mkn_found_in_range(self) -> None:
    ...


if __name__ == '__main__':
  unittest.main()