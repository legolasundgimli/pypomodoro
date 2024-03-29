'''
Created on Dec 28, 2009

@author: uolter
'''
import datetime

class MyTask():
    '''
    classdocs
    '''
    
    #__timeformat__='%A, %d. %B %Y %I:%M%p'
    
    __timeformat__='%d/%m/%Y %I:%M%p'
    
    def __init__(self, name=''):
        self.name=name
        self._startAt=datetime.datetime.now()                
        self._stopAt=None
        self.sent=False        
        
    def restart(self):        
        self._startAt=datetime.datetime.now()
        return self._startAt
    
    def stop(self):
        self._stopAt=datetime.datetime.now()
        return self._stopAt
        
    def startAt(self):
        return self._startAt.strftime(self.__timeformat__)
    
    def stopAt(self):
        return self._stopAt.strftime(self.__timeformat__)
    
    def life(self):
        self._life=self._stopAt-self._startAt
        return self._life
    
    def ended(self):
        
        if self._stopAt != None:
            return True
        return False
    
    
class MyTaskList():
    
    def __init__(self):
        self.list=[]
        self.current=None
        
    def append(self, name='', task=None):
        
        if task!=None:
            self.current=task
            self.list.append(self.current)
        else:
            self.current=MyTask(name)
            self.list.append(self.current)
            
        return self.current 
    
    def task_to_send(self):
        to_send=[]
        if len(self.list)>0:            
            for item in self.list:
                if item.ended() and not item.sent:
                    to_send.append(item)
                     
        return to_send
               
        
        
from conf import settings
    
SEPARATOR=settings.CSV_SEPARATOR
    
def csvTaskFormatter( _task):
    ret=''
    if _task!= None and isinstance(_task, MyTask) and _task.ended:
        ret+=_task.name
        ret+=SEPARATOR
        ret+=_task.startAt()
        ret+=SEPARATOR
        if _task.ended():
            ret+=_task.stopAt()
        else:
            ret+='running'
        ret+=SEPARATOR        
    elif _task != None and isinstance(_task, MyTaskList):
        for item in _task.list:
            ret+=csvTaskFormatter(item)
            ret+='\n'                            
    return ret
    

class Counter():
    
    def __init__(self):
        self.file_name=settings.COUNTER_FILE_NAME
        self.value=self.get_number()
        
        
    def __open(self):
        try:
            file = open(self.file_name, 'r')
            self.counter=file.readline()            
            file.close()
        except IOError:
            self.counter=0
        
    def get_number(self):
        self.__open()
        if self.counter and self.counter!='':
            return int(self.counter)
        else:
            return 0
    
    def save_number(self, number=0):
        file = open(self.file_name, 'w')
        file.write(str(number))
        file.close()
        
        
        
        