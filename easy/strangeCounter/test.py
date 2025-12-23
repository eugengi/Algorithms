"""
Tests for problem: Strange Counter
Script: main.py
"""

from itertools import islice
import unittest

from main import (
  strange_counter,
  _generate_cycle_fv_sequence,
  _compute_cycle_time,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You might want to skip these tests if your approach changes.
  """

  def test_should_generate_sequence_where_each_number_is_double_previous(self) -> None:
    # Given
    expected = (3, 6, 12, 24,)

    # When
    result = _generate_cycle_fv_sequence()
    actual = tuple(islice(result, len(expected)))

    # Then
    self.assertTrue(hasattr(result, '__iter__'))
    self.assertEqual(actual, expected)

  def test_should_compute_first_and_last_time_for_a_cycle(self) -> None:
    # Given
    first_value = 24
    expected = (22, 45,)

    # When
    actual = _compute_cycle_time(first_value)

    # Then
    self.assertIsInstance(actual, tuple)
    self.assertEqual(len(actual), 2)
    self.assertEqual(actual, expected)



class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = strange_counter

  def test_should_display_counter_value_for_given_time(self) -> None:
    # Given
    time = 57
    expected = 37

    # When
    actual = self.under_test(time)

    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
