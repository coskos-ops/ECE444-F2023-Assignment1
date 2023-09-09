import unittest
from utils import utils


class MyTestCase(unittest.TestCase):
    def test_reversed(self):
        # test integers
        x = utils.reversed(12345678)
        self.assertEqual(x, 87654321)

        x = utils.reversed(18)
        self.assertEqual(x, 81)

        # test negative integer
        x = utils.reversed(-7214)
        self.assertEqual(x, -4127)

        # Test float
        try:
            x = utils.reversed(1.78)
            self.fail("Only integer values should be accepted by this function")
        except:
            pass

        # Test a valid string representing an integer
        try:
            x = utils.reversed("13")
            self.fail("Only integer values should be accepted by this function")
        except:
            pass

        # Test an invalid string
        try:
            x = utils.reversed("nonsense")
            self.fail("Only integer values should be accepted by this function")
        except:
            pass

    def test_formatter(self):
        # Test integers
        x = utils.formatter(5)
        self.assertEqual(x[0], "0b101")
        self.assertEqual(x[1], "0o5")

        x = utils.formatter(47)
        self.assertEqual(x[0], "0b101111")
        self.assertEqual(x[1], "0o57")

        # Test negative integer
        x = utils.formatter(-43)
        self.assertEqual(x[0], "-0b101011")
        self.assertEqual(x[1], "-0o53")

        # Test float
        try:
            x = utils.formatter(165.18)
            self.fail("Only integer values should be accepted by this function")
        except TypeError:
            pass

        # Test a valid string representing an integer
        try:
            x = utils.formatter("13")
            self.fail("Only integer values should be accepted by this function")
        except TypeError:
            pass

        # Test an invalid string
        try:
            x = utils.formatter("nonsense")
            self.fail("Only integer values should be accepted by this function")
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()
