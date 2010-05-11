#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jan  5 18:59:17 2010

import wx.grid
from conf import messages, settings

# begin wxGlade: extracode
# end wxGlade



class TaskDialog(wx.Dialog):
    def __init__(self, parent, id, title, tasklist):
        # begin wxGlade: TaskDialog.__init__
        
        self.tasklist=tasklist
        #kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, parent, id, title)
        self.grid = wx.grid.Grid(self, -1, size=(1, 1))
        self.button = wx.Button(self, wx.ID_CANCEL, messages.DLG_TASK_BTN_CLOSE)
        
        self.__set_properties()
        self.__do_layout()
        if self.tasklist != None:
            self._loadTask()
                        
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: TaskDialog.__set_properties
        self.SetTitle("Task")
        self.SetSize((500, 200))
        self.grid.CreateGrid(len(self.tasklist)+1, 3)        
        self.grid.SetColLabelValue(0, messages.DLG_TASK_GRID_COL0)
        self.grid.SetColSize(0, 50)
        self.grid.SetColLabelValue(1, messages.DLG_TASK_GRID_COL1)
        self.grid.SetColSize(1, 80)
        self.grid.SetColLabelValue(2, messages.DLG_TASK_GRID_COL2)
        self.grid.SetColSize(2, 80)
        self.grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.onCellSelected)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_CHANGE,self.onCellChange)



        
        # end wxGlade
        
    def onCellSelected(self, event):
        if event.GetCol() > 0:
            pass
    
                
    def SetCellValue(self, event):
        row,col = event.GetRow(),event.GetCol()                
        value = self.grid.GetCellValue(row, col)
        if self.tasklist!=None:
            item=self.tasklist[col]
            item.name=value
    
    def onCellChange(self, event):
        '''
        
        '''
        col=event.GetCol()
        
        if event.GetCol() == 1:
            value = self.grid.GetCellValue(event.GetRow(), event.GetCol())
            item = self.tasklist[event.GetRow()]
            item.name=value
            print value
        
        event.Skip()
            


    def __do_layout(self):
        # begin wxGlade: TaskDialog.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        sizer.Add(self.button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade
        
        
    def _loadTask(self):
                        
        row=0                
        for item in self.tasklist:
            self.grid.SetCellValue(row, 0, item.name)
            self.grid.SetColSize(0, len(item.name.ljust(20))*8)            
            self.grid.SetCellValue(row, 1, item.startAt())
            self.grid.SetColSize(1, len(item.startAt())*8)            
            if item.ended():
                self.grid.SetCellValue(row, 2, item.stopAt())
                self.grid.SetColSize(2, len(item.stopAt())*10)
            else:
                self.grid.SetCellValue(row, 2, messages.DLG_TASK_GRID_TASK_RUNNING)
            row+=1

# end of class TaskDialog


class LoginDialog(wx.Dialog):
    
    def __init__(self, parent, id=-1, title="Login",
                 pos=wx.DefaultPosition,
                 size=wx.Size(400, 150)):
        
        wx.Dialog.__init__(self, parent, id, title, pos, size)
        wx.StaticText(self, -1, 'Please type your user name and password.',
                     wx.Point(10, 5))
        wx.StaticText(self, -1, 'User name: ', wx.Point(20, 30))
        wx.StaticText(self, -1, 'Password: ', wx.Point(20, 55))
        self.nameBox = wx.TextCtrl(self, -1, settings.google_calendar_account , wx.Point(100,30), wx.Size(200, -1))
        self.passwordBox = wx.TextCtrl(self, -1, '', wx.Point(100,55), wx.Size(200, -1), style=wx.TE_PASSWORD)
        wx.Button(self, wx.ID_OK,     ' OK ', wx.Point(35, 90), wx.DefaultSize).SetDefault()
        wx.Button(self, wx.ID_CANCEL, ' Cancel ', wx.Point(135, 90), wx.DefaultSize)

    def GetUser(self):
        val = self.ShowModal()        
        if val == wx.ID_OK:
            username = self.nameBox.GetValue()
            # h = sha.new(self.passwordBox.GetValue())
            # password = h.hexdigest()
            password=self.passwordBox.GetValue()
            return [username, password]
        else:
            return None


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    taskDialog = TaskDialog(None, -1, "")
    app.SetTopWindow(taskDialog)
    taskDialog.Show()
    app.MainLoop()

