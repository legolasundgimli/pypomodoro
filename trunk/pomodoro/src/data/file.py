'''
Created on Jan 3, 2010

@author: uolter
'''

from conf import settings 

class CSVTask():
    
    __APPEND__='a'
    __WRITE__='w'
    
        
    def __init__(self, filename=None):
        if filename == None:        
            self.filename=settings.CVS_FILE
        else: 
            self.filename=filename
        
    def write(self, str, mode=__APPEND__):
        try:
            fout = open(self.filename, mode)
            fout.write(str)
            fout.close()
            return True
        except IOError, ex:
            print '%s' %(ex)            
            return False
        
    def reset(self):
        return self.write('', mode=self.__WRITE__)