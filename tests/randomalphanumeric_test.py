import unittest

from src.randomalphanumeric import generate_alphanumeric_string


class test_reandomalphanumeric(unittest.TestCase):
    def test_random_alpha(self):
        alpha_srting = generate_alphanumeric_string(6) 
        self.assertEqual(len(alpha_srting), 6)
        self.assertTrue(alpha_srting.isalnum())
        print (f"alphanumeric string: {alpha_srting}")


