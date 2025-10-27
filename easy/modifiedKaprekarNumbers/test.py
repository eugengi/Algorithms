"""
Tests for problem: Modified Kaprekar Numbers
Script: main.py
"""

from contextlib import redirect_stdout
import io
import unittest

from main import (
    kaprekar_numbers,
    _is_mkn,
    _split,
)


class FunctionalTestCase(unittest.TestCase):
  """
  Test case to test logical units that are implementation dependent (coupled).
  Note: You want to skip these tests if your approach changes.
  """

  def test_should_split_value_into_two_where_right_half_length_equals_digits(
          self) -> None:
    # Given
    value = 25
    digits = 1
    expected = 2, 5

    # When
    actual = _split(value, digits)

    # Then
    self.assertIsInstance(actual, tuple)
    self.assertIsInstance(actual[0], int)
    self.assertIsInstance(actual[1], int)
    self.assertEqual(actual, expected)

  def test_should_check_if_value_is_modified_kaprekar_number(self) -> None:
    # Given
    value = 9
    expected = True

    # When
    actual = _is_mkn(value)

    # Then
    self.assertIsInstance(actual, bool)
    self.assertEqual(actual, expected)


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = kaprekar_numbers

  def test_should_output_mkn_list_in_expected_format(self) -> None:
    # Given
    lower, upper = 1, 10
    expected = "1 9 \n"

    # In-memory text stream
    captured_output = io.StringIO()

    # When
    with redirect_stdout(captured_output):
      self.under_test(lower, upper)
    actual = captured_output.getvalue()

    # Then
    self.assertIsInstance(actual, str)
    self.assertEqual(actual, expected)

  def test_should_output_invalid_for_no_mkn_found_in_range(self) -> None:
    # Given
    lower, upper = 10, 30
    expected = "INVALID RANGE\n"

    # In-memory text stream
    captured_output = io.StringIO()

    # When
    with redirect_stdout(captured_output):
      self.under_test(lower, upper)
    actual = captured_output.getvalue()

    # Then
    self.assertIsInstance(actual, str)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
