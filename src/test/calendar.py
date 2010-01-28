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


    def testTaskEvent(self):
        
        username=settings.google_calendar_account
        password=raw_input('Password for %s?' %username)
        
        entry = EntryManager(username, password)
        
        mytask=task.MyTask('Google calendar')
        time.sleep(120)
        mytask.stop()
        
        event =entry.insert_single_event(mytask.name, mytask._startAt.timetuple(), mytask._stopAt.timetuple())
        
        self.assertFalse(event == None)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInstartEvent']
    unittest.main()