'''
Created on Jan 24, 2010

@author: uolter
'''
import gdata.calendar
from gdata.calendar.service import CalendarService
from gdata.calendar import CalendarEventEntry
import time

import atom


class EntryManager(gdata.calendar.CalendarEventEntry):

    '''
    classdocs
    '''
    
    def __init__(self, email, password): 
        CalendarEventEntry.__init__(self)                                   
        self.calendar_service = CalendarService()
        self.calendar_service.email = email
        self.calendar_service.password = password
        self.calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
        try:
            self.calendar_service.ProgrammaticLogin()
        except:
            self.calendar_service=None
        
    
    def insert_single_event(self, title, start_time=None, end_time=None):        
        self.title = atom.Title(text=title)
        
        start_strtime=time.strftime('%Y-%m-%dT%H:%M:%S.000Z', start_time.gmtime())
        end_strtime=time.strftime('%Y-%m-%dT%H:%M:%S.000Z', end_time.gmtime())
        
        
        self.when.append(gdata.calendar.When(start_time=start_strtime, end_time=end_strtime))
        
        if self.calendar_service != None:
            try:        
                new_event = self.calendar_service.InsertEvent(self, '/calendar/feeds/default/private/full')            
                return new_event
            except:
                return None
        
        else:
            return None
        
class PostTask():
    
    def __init__(self, user, tasklist):        
        self.user=user
        self.tasklist=tasklist
        
                                    
    def send(self):
        i=0
        self.entry_manager=EntryManager(self.user[0], self.user[1])        
        for item in self.tasklist:
            event=self.entry_manager.insert_single_event(item.name, item._startAt.timetuple(), item._stopAt.timetuple())
            if event != None:
                item.sent=True
                i+=1
            else:                 
                return 0
            
        return i
