'''
Created on Dec 28, 2009

@author: uolter
'''
import unittest

from data import task
import time


class TestTask(unittest.TestCase):


    def test1_Task(self):
        mytask=task.MyTask('my first task')
        time.sleep(3)
        mytask.stop()
        self.assertNotEqual(mytask.startAt(), None)
        self.assertNotEqual(mytask.stopAt(), None)
        
    def test2_Task(self):
        mytask=task.MyTask('my first task')
        time.sleep(3)
        mytask.stop()
        print '%s %s' %(mytask.name, mytask.life())
        self.assertNotEqual(mytask.life(), None)
        
    def test3_TaskList(self):
        tList=task.MyTaskList()
        tList.append('Task 1')
        time.sleep(3)        
        tList.current.stop()        
        print tList.current.life()        
        self.assertNotEqual(tList.current.life(), None)

    def test4_TaskList(self):
        tList=task.MyTaskList()
        tList.append('Task 1')
        time.sleep(3)        
        tList.current.stop()
        tList.append('', task.MyTask('Task 2'))
        self.assertTrue(len(tList.list), 2)
        time.sleep(2)
        tList.current.stop()
        
        for i in tList.list:
            sec=i.life().seconds
            print '%s %d' %(i.name, sec)
            self.assertTrue( sec > 0)
            
    def test5_TaskEnd(self):
        mytask=task.MyTask('my first task')
        time.sleep(2)
        self.assertFalse(mytask.ended())
    
    def test6_TaskName(self):
        mytaskList=task.MyTaskList()
        
        mytaskList.append('Task 1')
        
        self.assertEqual(mytaskList.current.name, 'Task 1')
        
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1_Tasl']
    unittest.main()