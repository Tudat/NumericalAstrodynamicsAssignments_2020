import unittest
import os
from ..src.Main import Main

class Test_main(unittest.TestCase):
    
    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        
        self.main = Main()
        print(f'self.main.addTwo(3)={self.main.addTwo(3)}')
        
    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # tests unit test on main class
    def test_addTwo(self):
        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result,result)
    
    # Example: Verifies an exception is thrown in nqueens for n <5
    #def test_ThreeQueens(self):
    #   with self.assertRaises(Exception) as context:
    #       n_queens = N_queens(4)
    #    self.assertTrue('There are no non-trivial solutions for n<5, please increase n and try again.' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()