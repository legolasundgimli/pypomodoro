'''
Created on Dec 10, 2009

@author: uolter
'''

import time 

def countdown(minutes=1,secs=0, interval=1):

    secs=(minutes*60)+secs
    
    while secs>0:
        yield secs
        secs=secs-interval     
        time.sleep(interval)        
    print 'Time is up'


#for count in countdown(25,0,120):
#    print count
