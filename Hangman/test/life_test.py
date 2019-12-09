import unittest
from life import Life


class LifeTest(unittest.TestCase):

    def setUp(self):
        self.life = Life()

    def test_is_alive(self):
        self.assertEqual(self.life.is_alive(), True)
        for i in range(6):
            self.life.decrease()
        self.assertEqual(self.life.is_alive(), False)

    def test_decrease(self):
        self.life.decrease()
        self.assertEqual(self.life.remaining_life, 5)


if __name__ == '__main__':
    unittest.main()