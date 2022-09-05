import unittest
import FizBuz
class TestFizBuz(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(FizBuz.fizzBuzz(2),[1, 2])
        self.assertEqual(FizBuz.fizzBuzz(1),[1])
    def test_Print_Multiple_of_3_5(self):
        self.assertEqual(FizBuz.fizzBuzz(3),[1,2,"Fizz"])
        self.assertEqual(FizBuz.fizzBuzz(5),[1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(FizBuz.fizzBuzz(15),[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz'])
        self.assertEqual(FizBuz.fizzBuzz(20),[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz', 16, 17, 'Fizz', 19, 'Buzz'])



        

      
       
        
        
if __name__ == '__main__':
    unittest.main()