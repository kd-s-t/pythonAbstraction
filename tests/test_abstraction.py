import unittest
from controllers import Abstraction

class TestAbstraction(unittest.TestCase):

    def test_success(self):
        R = Abstraction.Triangle()
        r = R.noofsides()

        K = Abstraction.Quadrilateral()
        k = K.noofsides()

        P = Abstraction.Pentagon()
        p = P.noofsides()

        H = Abstraction.Hexagon()
        h = H.noofsides()

        self.assertEqual(r, "I have 3 sides")
        self.assertEqual(k, "I have 4 sides")
        self.assertEqual(p, "I have 5 sides")
        self.assertEqual(h, "I have 6 sides")

    def test_error(self):
        R = Abstraction.Triangle()
        r = R.noofsides()

        K = Abstraction.Quadrilateral()
        k = K.noofsides()

        P = Abstraction.Pentagon()
        p = P.noofsides()

        H = Abstraction.Hexagon()
        h = H.noofsides()

        self.assertNotEqual(r, "I have 23 sides")
        self.assertNotEqual(k, "I have 43 sides")
        self.assertNotEqual(p, "I have 51 sides")
        self.assertNotEqual(h, "I have 67 sides")
