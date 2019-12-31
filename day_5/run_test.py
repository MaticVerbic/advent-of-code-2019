import unittest
from run import *

class TestHandlerOpcode(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(handler_opcode(1), [1, 0, 0, 0])
        self.assertEqual(handler_opcode(11102), [2, 1, 1, 1])
        self.assertEqual(handler_opcode(11102), [2, 1, 1, 1])
        self.assertEqual(handler_opcode(102), [2, 1, 0, 0])
        self.assertEqual(handler_opcode(11199), [99, 1, 1, 1])
    
    def test_incorrect(self):
        self.assertRaises(Exception, handler_opcode, 65402)
        
if __name__ == '__main__':
    unittest.main()