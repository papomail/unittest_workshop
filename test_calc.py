import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(0,1), 1)
        self.assertEqual(calc.add(5,0), 5)
        self.assertEqual(calc.add(10,-20), -10)

    def test_substract(self):
        self.assertEqual(calc.substract(0,1), -1)
        self.assertEqual(calc.substract(5,0), 5)
        self.assertEqual(calc.substract(10,-20), 30)  

    def test_divide(self):
        self.assertEqual(calc.divide(0,1), 0)
        self.assertEqual(calc.divide(10,-20), -0.5)    
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == "__main__":
    unittest.main()




        