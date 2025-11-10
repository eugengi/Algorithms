"""
Tests for problem: Strange Counter
Script: main.py
"""

import unittest

from main import (
  strange_counter,
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
    self.under_test = strange_counter

  def test_should_display_counter_value_for_given_time(self) -> None:
    ...


if __name__ == '__main__':
  unittest.main()
