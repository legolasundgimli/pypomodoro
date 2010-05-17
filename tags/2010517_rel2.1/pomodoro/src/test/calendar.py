'''
Created on Jan 24, 2010

@author: uolter
'''
from google.calendar import EntryManager
from data import task
import time
import unittest
from conf import settings


class Test(unittest.TestCase):


    def test1_TaskEvent(self):
        
        username=settings.google_calendar_account
        password=raw_input('Password for %s?' %username)
        
        entry = EntryManager(username, password)
        
        mytask=task.MyTask('Google calendar')
        time.sleep(120)
        mytask.stop()
        
        event =entry.insert_single_event(mytask.name, mytask._startAt.timetuple(), mytask._stopAt.timetuple())
        
        self.assertFalse(event == None)
        
    def test2_TaskEvent(self):
        
        username=settings.google_calendar_account
        password=raw_input('Password for %s?' %username)
        
        entry = EntryManager(username, password)
        
        my_task_list=task.MyTaskList()        
        my_task_list.append('Google calendar')
        time.sleep(120)
        my_task_list.current.stop()
        
        tasks=my_task_list.task_to_send()
        
        for item in tasks:
            event =entry.insert_single_event(item.name, item._startAt.timetuple(), item._stopAt.timetuple())
            self.assertFalse(event == None)
                
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInstartEvent']
    unittest.main()