import unittest
import utils

class TestGetOccurencesByFirstDigit(unittest.TestCase):
    def test_get_occurences_by_first_digit(self):
        actual = utils.get_occurences_by_first_digit(values=["1","1","2","3","4","0"])
        expected = [2,1,1,1,0,0,0,0,0]
        self.assertEqual(actual, expected)