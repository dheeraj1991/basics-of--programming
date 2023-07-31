import unittest
from merge_sort import merge_sort


class TestClass(unittest.TestCase):
    def test_unorder_positive_integers(self):
        # Here the list of positive integers [6,1,4,2,6,8,1223,12,752]
        assert merge_sort([6,1,4,2,6,8,1223,12,752]) == [1, 2, 4, 6, 6, 8, 12, 752, 1223]

    def test_unorder_decimals(self):
        # Here the list of positive integers [1.4,-2.6,20.1,2,6.1,-9.12,12.23,-112,7.252]
        assert merge_sort([1.4,-2.6,20.1,2,6.1,-9.12,12.23,-112,7.252]) == [-112, -9.12, -2.6, 1.4, 2, 6.1, 7.252, 12.23, 20.1]

    def test_alphabets(self):
        # Here the list of alphabhets ['s','g','q','t','s','h','a','n','j'] is sorted alphabetically
        assert merge_sort(['s','g','q','t','s','h','a','n','j']) == ['a', 'g', 'h', 'j', 'n', 'q', 's', 's', 't']

if __name__=='__main__':
	unittest.main()
