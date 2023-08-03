import unittest

from lib import rand_gen


class TestRandGen(unittest.TestCase):
    def test_generate_random_number(self):
        self.assertEqual(rand_gen.generate_random_number(), 4)
