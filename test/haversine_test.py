
import unittest

from haversine import haversine


class HaversineTest(unittest.TestCase):

    def test_distance(self):
        paris = [48.8566, 2.3522]
        lyon = [45.7640, 4.8357]
        self.assertEqual(391499.4724356128, haversine(paris[0], paris[1], lyon[0], lyon[1]))


if __name__ == '__main__':
    unittest.main()
