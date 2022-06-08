import unittest
from models.split.split import Split


class TestSplit(unittest.TestCase):

    def test_get_amount(self):
        s = Split(None)
        s.set_amount(5)
        self.assertEqual(s.get_amount(), 5)

    def test_set_amount(self):
        s = Split(None)
        self.assertTrue(s.set_amount(5))

    def test_get_user(self):
        u = "s"
        s = Split(u)
        self.assertTrue(s.get_user(), u)

    def test_set_user(self):
        s = Split("")
        self.assertTrue(s.set_user("as"), "as")


if __name__ == '__main__':
    unittest.main()
