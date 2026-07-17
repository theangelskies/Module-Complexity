import unittest

from skip_list import SkipList

class SkipListTest(unittest.TestCase):
    def test_single_item(self):
        sl = SkipList()
        sl.insert("a")
        self.assertEqual(sl.to_list(), ["a"])
        self.assertIn("a", sl)
        self.assertNotIn("b", sl)

    def test_general_usage(self):
        sl = SkipList()
        sl.insert(1)
        sl.insert(2)
        sl.insert(3)
        sl.insert(4)
        sl.insert(10)
        sl.insert(5)

        self.assertIn(5, sl)
        self.assertIn(4, sl)
        self.assertNotIn(6, sl)
        self.assertNotIn(7, sl)

        self.assertEqual(sl.to_list(), [1, 2, 3, 4, 5, 10])

    def test_empty_skip_list(self):
        sl = SkipList()
        self.assertEqual(sl.to_list(), [])
        self.assertNotIn("a", sl)

    def test_insert_out_of_order_with_duplicates(self):
        sl = SkipList()
        for value in [5, 3, 5, 1, 4, 2]:
            sl.insert(value)

        self.assertEqual(sl.to_list(), [1, 2, 3, 4, 5, 5])
        self.assertIn(5, sl)
        self.assertNotIn(6, sl)


if __name__ == "__main__":
    unittest.main()
