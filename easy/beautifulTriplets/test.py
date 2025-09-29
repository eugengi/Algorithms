"""
Tests for problem: Beautiful Triplets
Script: main.py
"""

import unittest

from main import (
  beautiful_triplets,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You want to skip these tests if your approach changes.
  """

  ...


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = beautiful_triplets

  ...


if __name__ == '__main__':
  unittest.main()