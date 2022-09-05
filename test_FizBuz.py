import unittest
import FizBuz
class TestFizBuz(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(FizBuz.fizzBuzz(2),[1, 2])
        self.assertEqual(FizBuz.fizzBuzz(1),[1])

      
       
        
        
if __name__ == '__main__':
    unittest.main()