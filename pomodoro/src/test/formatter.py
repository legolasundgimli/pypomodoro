'''
Created on Jan 1, 2010

@author: uolter
'''
import unittest
from data import task
import time


class TestFormatter(unittest.TestCase):


    def test_1_TaskCSV(self):
        mytask=task.MyTask('my task')
        mytask.restart()
        time.sleep(2)
        mytask.stop()
        out=task.csvTaskFormatter(mytask)
        print out
        self.assertTrue(out.find('my task')>-1)
        
    def test_2_TaskCSV(self):
        mytaskList=task.MyTaskList()
        mytaskList.append('task 1')
        mytaskList.current.stop()
        mytaskList.append('task 2')
        mytaskList.current.stop()        
        out=task.csvTaskFormatter(mytaskList)
        print out
        self.assertTrue(((out.find('task 1')>-1) and (out.find('task 2')>-1)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFormatter']
    unittest.main()