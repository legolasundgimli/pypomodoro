'''
 Created on Dec Jan, 2010

@author: uolter
'''

import wx

class TaskDialog(wx.Dialog):
    
    def __init__(self, parent, id, title, tasklist):
        wx.Dialog.__init__(self, parent, id, title, size=(500,200), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)    
        # sizer =  self.CreateTextSizer('Tasks')
        sizer=wx.BoxSizer(wx.VERTICAL)
        sheet=TaskSheet(self, tasklist)        
        sizer.Add(sheet, 0, wx.EXPAND | wx.ALL, 20)
                
        self.SetSizer(sizer)
    

from wx.lib import sheet

class TaskSheet(sheet.CSheet):
    
    def __init__(self, parent, tasklist):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.tasklis=tasklist        
        self.SetNumberRows(len(tasklist)+1)
        self.SetNumberCols(3)
                        
        #Columns name:
        self.SetColLabelValue(0, 'Task')
        self.SetColLabelValue(1, 'Start')
        self.SetColLabelValue(2, 'Stop')        
        
        self.loadTask()
        
    def loadTask(self):
        
                
        row=0                
        for item in self.tasklis:
            self.SetCellValue(row, 0, item.name)
            self.SetColSize(0, len(item.name.ljust(20))*8)            
            self.SetCellValue(row, 1, item.startAt())
            self.SetColSize(1, len(item.startAt())*8)            
            if item.ended():
                self.SetCellValue(row, 2, item.stopAt())
                self.SetColSize(2, len(item.stopAt())*10)
            else:
                self.SetCellValue(row, 2, 'Running')
            row+=1            
        
