import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_with_empty_list(self):
        self.assertEquals(a1.stock_price_summary([]), (0, 0))

    def test_with_only_positives(self):
        self.assertEquals(a1.stock_price_summary([1, 2]), (3, 0))

    def test_with_only_negatives(self):
        self.assertEquals(a1.stock_price_summary([-1, -2]), (0, -3))

    def test_with_floats(self):
        self.assertEquals(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]), (0.14, -0.17))

if __name__ == '__main__':
    unittest.main(exit=False)
