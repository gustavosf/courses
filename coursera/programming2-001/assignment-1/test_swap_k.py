import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_with_empty_list(self):
        L = []
        a1.swap_k(L, 0)
        self.assertEquals(L, [])

    def test_with_list_of_two(self):
        L = [1,2]
        a1.swap_k(L, 1)
        self.assertEquals(L, [2,1])

    def test_with_list_of_five(self):
        L = [1,2,3,4,5]
        a1.swap_k(L, 2)
        self.assertEquals(L, [4,5,3,1,2])

    def test_with_num_zero(self):
        L = [1,2,3,4,5]
        a1.swap_k(L, 0)
        self.assertEquals(L, [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main(exit=False)
