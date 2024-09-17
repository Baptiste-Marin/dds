import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from baptiste.main import donne_des_sous

class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = donne_des_sous(8, 10)
        self.assertEqual(18, compte_en_banque)

if __name__ == '__main__':
    unittest.main()