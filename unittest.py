import unittest
from Calculator import Calculator
class CalculatorTest(unittest.TestCase):
  def setUp(self):
    self.calc = Calculator()
  def test_add(self):
    self.assertEqual(10, self.calc.add(3, 7), "The addition is       wrong")
  def test_subtract(self):
    self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is  wrong")
  def test_multiply(self):
    self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication     is wrong")
  def test_multiple_addition(self):
    for a in range(10):
      for b in range(10):
        with self.subTest("add " + str(a) + " and " + str(b)):
          self.assertEqual(a+b, self.calc.add(a, b))
  
  def test_negative_root(self):
    self.assertRaises(ValueError, self.calc.squareRoot, -1)
if __name__ == '__main__':
  unittest.main()