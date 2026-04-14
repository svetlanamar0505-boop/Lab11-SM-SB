import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
            self.assertEqual(add(5, 7), 12)
            self.assertEqual(add(-3, 8), 5)
            self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(4, 10), -6)
        self.assertEqual(sub(-5, -2), -3)


        ######## Partner 1
    def test_multiply(self):
         self.assertEqual(mul(2, 3), 6)
         self.assertEqual(mul(0, 5), 0)
         self.assertEqual(mul(-2, 4), -8)


     def test_divide(self):
         self.assertEqual(div(10, 2), 5)
         self.assertEqual(div(1, 3), 0.33333333333333)
         self.assertEqual(div(9, 3), 3)




    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
       with self.assertRaises(ZeroDivisionError):
          div(0, 5)

    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(3, 81), 4.0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    #     # use same technique from test_divide_by_zero

    
    ######## Partner 1
     def test_log_invalid_argument(self):
         with self.assertRaises(ValueError):
             log(10, -1)


    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 5), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)


    def test_sqrt(self):
        self.assertAlmostEqual(square_root(4), 2.0 )
        self.assertAlmostEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(9), 3.0)



# Do not touch this
if __name__ == "__main__":
    unittest.main()