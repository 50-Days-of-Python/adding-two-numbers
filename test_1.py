import unittest
import main

# DO NOT TOUCH THE BELOW CODE

class Test_1(unittest.TestCase):
  def test_01(self):
    self.assertEqual(main.sum_0f_num(5,4), 9)

  def test_02(self):
    self.assertEqual(main.sum_0f_num(6,94), 100)
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
    
