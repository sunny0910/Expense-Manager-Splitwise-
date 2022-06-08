import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_get_id(self):
        u = User("woody")
        u.set_id(1)
        self.assertEqual(u.get_id(), 1)

    def test_set_id(self):
        u = User("woody")
        self.assertTrue(u.set_id(1))

    def test_get_name(self):
        u = User("woody")
        self.assertEqual(u.get_name(), "woody")

    def test_set_name(self):
        u = User("woody")
        self.assertTrue(u.set_name("woo"), "woo")


if __name__ == '__main__':
    unittest.main()