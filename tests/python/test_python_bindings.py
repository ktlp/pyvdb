import pyvdb
import unittest


class TestPyvdb(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(pyvdb.add_one(1), 2)

    def test_one_plus_one(self):
        self.assertEqual(pyvdb.one_plus_one(), 2)


if __name__ == '__main__':
    unittest.main()
