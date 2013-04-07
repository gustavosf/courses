import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_if_zero(self):
    	self.assertEqual(a1.num_buses(0), 0)

    def test_if_one(self):
    	self.assertEqual(a1.num_buses(1), 1)

    def test_if_num_equals_capacity(self):
    	self.assertEqual(a1.num_buses(50), 1)

    def test_if_one_more_than_a_single_bus_capacity(self):
    	self.assertEqual(a1.num_buses(51), 2)

    def test_with_a_larger_number(self):
    	self.assertEqual(a1.num_buses(75), 2)

if __name__ == '__main__':
    unittest.main(exit=False)
