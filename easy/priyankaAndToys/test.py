import unittest

from main import toys


# ---------------------------- Tests ---------------------------- #


"""
Tests for problem: Priyanka and Toys
Script: main.py
"""


class IntegrationTestCase(unittest.TestCase):
  """
  Test case to test the behavior of HackerRank entry-point.
  """

  def setUp(self) -> None:
    self.under_test = toys

  def test_should_return_number_of_containers_to_ship_all_toys(self) -> None:
    # Given
    items: list[int] = [1, 2, 3, 21, 7, 12, 14, 21]
    expected = 4

    # When
    actual = self.under_test(items)

    # Then
    self.assertIsInstance(actual, int)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
