'''
Created on Dec 10, 2009

@author: uolter
'''

# gauge.py

import wx
import img
import os
from conf import settings
from conf import messages


ID_RESET=101
ID_EXIT=102
#ID_START=

class Tomato(wx.Frame):
    
    def __init__(self, parent, id, title):
        
        self.maxtime=settings.MAX_TIME*60
        self.count = 0
        wx.Frame.__init__(self, parent, id, title, size=(250, 150))
                
        self.timer = wx.Timer(self, 1)
        
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        
        iconFile = '%s/%s' %(os.path.dirname(img.__file__), settings.ICON)
        icon1 = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon1)
        

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(panel, -1, 25*60, size=(250, 25))
        self.btn1 = wx.Button(panel, wx.ID_OK, 'Start')
        self.btn2 = wx.Button(panel, wx.ID_STOP)
        self.text = wx.StaticText(panel, -1, messages.TASK_TOBE_DONE)

        self.Bind(wx.EVT_BUTTON, self.OnOk, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)

        hbox1.Add(self.gauge, 1, wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, 1, wx.RIGHT, 10)
        hbox2.Add(self.btn2, 1)
        hbox3.Add(self.text, 1)
        vbox.Add((0, 10), 0)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTRE)
        vbox.Add(hbox1, 0, wx.ALIGN_CENTRE)
        vbox.Add((0, 20), 0)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTRE)
                        
        panel.SetSizer(vbox)
        self.Centre()
        
        self.__menu__()                
        self.Show(True)

    def OnOk(self, event):
        if self.count >= self.maxtime:
            return
        self.timer.Start(1000)        

    def OnStop(self, event):
        if self.count == 0 or self.count >= self.maxtime or not self.timer.IsRunning():
            return
        self.timer.Stop()
        self.text.SetLabel(messages.TASK_INTERRUPTED)
        wx.Bell()

    def OnTimer(self, event):
        self.count = self.count +1
        self.gauge.SetValue(self.count)
        self.text.SetLabel(messages.TASK_INPROGRESS %(self.count/60, self.count%60))
        self.SetTitle('%s (%d)' %(settings.TITLE, (settings.MAX_TIME - self.count/60)))        
        if self.count == self.maxtime:
            self.timer.Stop()
            self.text.SetLabel(messages.TASK_COMPLETED)
            self.SetTitle(messages.TASK_COMPLETED)
            
    def OnReset(self, event):
        self.count=0
        self.gauge.SetValue(self.count)
        self.text.SetLabel(messages.TASK_TOBE_DONE)
        self.SetTitle(settings.TITLE)
    
    def OnExit(self, event):
        self.Close(True)  # Close the frame.
    
        
    def __menu__(self):                    
        # Menu
        resetmenu= wx.Menu()
        resetmenu.Append(ID_RESET, "&Reset"," Reset Conut")                    
        resetmenu.Append(ID_EXIT, "E&xit"," Exit Tomato")
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(resetmenu,"&Menu") # Adding the "resetmenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.        
        wx.EVT_MENU(self, ID_RESET, self.OnReset)       # attach the menu-event ID_RESET to the
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)       # attach the menu-event ID_EXIT to the

