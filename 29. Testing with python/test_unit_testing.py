# Always the testing function should begin with ""test"" then only it will check the unit testing... 
# unittest is a module which tests testing
# For more information refer the python module for unittest
# To get more information about the tests, 
# Use the following command -> python filename.py -v
# Testing exceptions is little different than normal testing
import unittest
from unit_testing import nap, eat

class UnitTestingTest(unittest.TestCase):
    def test_healthy_eating(self):
        """Testing healthy eating"""
        self.assertEqual(
            eat("brocolli", is_healthy=True), 
            "I am eating brocolli, which is healthy"
            )

    def test_unhealthy_eating(self):
        """Testing unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False), 
            "I am eating pizza, which is unhealthy"
            )

    def test_short_nap(self):
        """Testing short nap"""
        self.assertEqual(
            nap(1),
            "Yoo this is a short nap"
            )

    def test_long_nap(self):
        """Testing long nap"""
        self.assertEqual(
            nap(3),
            "Yoo this is a long nap"
            )
    
    def test_healthy_eating_boolean(self):
        """Testing for boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", "who cares..!")

if __name__ == "__main__":
    unittest.main()

# some more functions of unittest
# self.assertEqual(x, y) -> if a value is equal to the other value
# self.assertNotEqual(x, y) -> if the value is not equal to the other value (anything would do except that value)
# self.assertTrue(x) -> if the value is True
# self.assertFalse(x) -> if the value is False (actually checks for falsy values)
# self.assertIsNone(x) -> checks for None
# self.assertIsNotNone(x) -> checks for not None
# self.assertIn(x, y) -> checks for value is in x
# self.assertNotIn(x, y) -> checks for value is not in x
# and many more...

# Testing exceptions is little different
    # def test_healthy_eating_boolean(self):
    #     """Testing for boolean"""
    #     with self.assertRaises(ValueError):
    #         eat("pizza", "who cares..!")