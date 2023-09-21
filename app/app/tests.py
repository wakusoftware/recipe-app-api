"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Sample tests
    """

    def test_add_numbers(self):
        """
        Test add numbers
        """
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract_numbers(self):
        """
        Tests subtract numbers
        """
        self.assertEqual(calc.subtract(5, 11), 6)
