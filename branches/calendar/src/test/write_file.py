'''
Created on Jan 3, 2010

@author: uolter
'''
import unittest
from data import file

FILE_TEST='test.csv'

class TestCSV(unittest.TestCase):
    

    def test_1_CSV(self):
        csvfile=file.CSVTask(FILE_TEST)
        out=csvfile.reset()
        self.assertTrue(out)
        out=csvfile.write('my csv')
        self.assertTrue(out)
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()