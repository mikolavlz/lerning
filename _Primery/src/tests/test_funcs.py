from unittest import TestCase

from tests.funcs import comp,sum


class Test(TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,3),5)

    def test_comp(self):
        self.assertEqual(comp(2, 9), 6)
