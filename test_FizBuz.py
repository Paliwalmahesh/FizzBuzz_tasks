import unittest
import FizBuz
class TestFizBuz(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(FizBuz.fizzBuzz(2),[1, 2])
        self.assertEqual(FizBuz.fizzBuzz(1),[1])
    def test_Print_Multiple_of_3_5(self):
        self.assertEqual(FizBuz.fizzBuzz(3),[1,2,"Fizz"])
        self.assertEqual(FizBuz.fizzBuzz(5),[1, 2, 'Fizz', 4, 'Buzz'])
    

        

      
       
        
        
if __name__ == '__main__':
    unittest.main()