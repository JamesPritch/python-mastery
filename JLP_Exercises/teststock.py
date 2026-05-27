import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    def test_kwarg_create(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(10)
        self.assertEqual(s.shares, 90)
    def test_from_row(self):
        s = Stock('GOOG', 100, 490.1)
        a = s.from_row(['POO', 69, 419.99])
        self.assertEqual(a.name, 'POO')
        self.assertEqual(a.shares, 69)
        self.assertEqual(a.price, 419.99)
    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        a = repr(s)
        self.assertTrue(s == eval(a))
    def test_eq(self):
        s = Stock('GOOG', 100, 490.1)
        a = Stock('GOOG', 100, 490.1)
        self.assertTrue(a == s)

    def test_str_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'
    def test_neg_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50
    def test_str_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '50.23'
    def test_neg_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -50.3
    def test_bad_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = '500 cigarettes'

if __name__ == '__main__':
    unittest.main()
