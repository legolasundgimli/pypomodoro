'''
Created on Dec 10, 2009

@author: uolter
'''
from google.calendar import PostTask

import wx
import img
import os
from conf import settings
from conf import messages
from data import task, file

from gui import dialog

ID_RESET=101
ID_EXIT=102
#ID_START=
ID_NEW_TASK=201
ID_VIEW_TASK=202
ID_SAVE_TASK=203
ID_SEND_TASK=204

class Tomato(wx.Frame):
    
    def __init__(self, parent, id, title):
        
        self.maxtime=settings.MAX_TIME*60
        self.count = 0
        self.taskname=''
        wx.Frame.__init__(self, parent, id, title, size=(250, 170))
                
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

        self.gauge = wx.Gauge(panel, -1, settings.MAX_TIME*60, size=(250, 20))
        self.btn1 = wx.Button(panel, wx.ID_OK, messages.BUTTON_START)
        self.btn2 = wx.Button(panel, wx.ID_STOP)
        self.text = wx.StaticText(panel, -1, messages.TASK_TOBE_DONE)
        
        
        self.Bind(wx.EVT_CLOSE, self.OnExit, self)
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
        
        self.CreateStatusBar()
        
        self.Centre()
        
        self.__menu__()  
        
        # Task list:
        self.tasklist=task.MyTaskList()
        self.tosave=False
        self.username=settings.google_calendar_account                                   
        self.Show(True)

    def OnOk(self, event):
        if self.count >= self.maxtime:
            return        
        # Create a new task
        if self.count == 0:
            # Assign the task name 
            self.tasklist.append(self.taskname)           
            self.OnTextEntry(event)            
        
        self.tosave=True
        self.timer.Start(1000)        

    def OnStop(self, event):
        if self.count == 0 or self.count >= self.maxtime or not self.timer.IsRunning():
            return
        self.timer.Stop()
        self.text.SetLabel(messages.TASK_INTERRUPTED)
        wx.Bell()

    def OnTimer(self, event):        
        self.count += 1
        self.tosave=True
        self.gauge.SetValue(self.count)
        self.text.SetLabel(messages.TASK_INPROGRESS %(self.count/60, self.count%60))
        self.SetTitle('%s (%d)' %(messages.TITLE, (settings.MAX_TIME - self.count/60)))        
        if self.count == self.maxtime:            
            self.timer.Stop()
            self.text.SetLabel(messages.TASK_COMPLETED)
            self.SetTitle(messages.TASK_COMPLETED)
            self.count=0
            self.tasklist.current.stop()
            self.taskname=''            
            wx.Bell()
            wx.Bell()
            wx.Bell()
            
    def OnReset(self, event):
        self.count=0
        self.gauge.SetValue(self.count)
        self.text.SetLabel(messages.TASK_TOBE_DONE)
        self.SetTitle(messages.TITLE)
    
    def OnExit(self, event):
        if not self.tosave:
            self.Destroy()
        else:
            dlg=wx.MessageDialog(self, messages.DLG_TASK_WIN_CLOSE, messages.TITLE, wx.YES | wx.NO | wx.ICON_EXCLAMATION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Destroy()
                        
    def OnTextEntry(self, event):
        dlg = wx.TextEntryDialog(self, messages.DLG_TEXT_MESSAGE,messages.DLG_TEXT_TITLE)
        dlg.SetValue(self.taskname)
        
        if dlg.ShowModal() == wx.ID_OK:
            #self.SetStatusText('You entered: %s\n' % dlg.GetValue())
            if len(dlg.GetValue())>0:
                self.taskname=dlg.GetValue()             
                if self.tasklist.current != None:
                    self.tasklist.current.name=self.taskname
                    self.tosave=True                    
            else:
                self.OnTextEntry(event)
                            
        dlg.Destroy()
    
    def OnShowTaskDialog(self, event):
        dlg=dialog.TaskDialog(self, -1, messages.DLG_TASK_TITLE, self.tasklist.list)        
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnSave(self, event):
        csvtask=file.CSVTask()
        if self.tasklist != None:                                 
            dialog = wx.FileDialog( None, style = wx.SAVE | wx.OVERWRITE_PROMPT)
            if dialog.ShowModal() == wx.ID_OK:                
                csvtask.filename = dialog.GetPath()
                csvtask.write(task.csvTaskFormatter(self.tasklist))
                self.tosave=False            
            # Destroy the dialog
            dialog.Destroy()
    
    def OnSent(self, event):
        tasks=self.tasklist.task_to_send()
        
        if len(tasks)>0: 
            self.SetStatusText(messages.TASK_SENDING %len(tasks))
            dlg=dialog.LoginDialog(self)
            user = dlg.GetUser()        
            if user != None:
                post=PostTask(user, tasks)
                i=post.send()
                settings.google_calendar_account=user[0]
                if i!=len(tasks):
                    self.SetStatusText(messages.ERROR_SENFING_TASK)
                self.SetStatusText(messages.TASK_SENT %i)
        else:
            self.SetStatusText(messages.TASK_NONE)
    
        
    def __menu__(self):                    
        # Menu
        resetmenu= wx.Menu()
        resetmenu.Append(ID_RESET, messages.MENU_MENU_RESET, messages.MENU_MENU_RESET_MSG)                    
        resetmenu.Append(ID_EXIT, messages.MENU_MENU_EXIT, messages.MENU_MENU_EXIT_MSG)
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(resetmenu,messages.MENU_MENU) # Adding the "resetmenu" to the MenuBar
        
        # Task
        taskmenu=wx.Menu()
        taskmenu.Append(ID_NEW_TASK, messages.MENU_TASK_RENAME, messages.MENU_TASK_RENAME_MSG)
        taskmenu.Append(ID_VIEW_TASK, messages.MENU_TASK_VIEW, messages.MENU_TASK_VIEW_MSG )
        taskmenu.Append(ID_SAVE_TASK, messages.MENU_TASK_SAVE, messages.MENU_TASK_SAVE_MSG)
        taskmenu.Append(ID_SEND_TASK, messages.MENU_TASK_SEND, messages.MENU_TASK_SEND_MSG )        
        menuBar.Append(taskmenu,messages.MENU_TASK)
        
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.        
        wx.EVT_MENU(self, ID_RESET, self.OnReset)       # attach the menu-event ID_RESET to the
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)       # attach the menu-event ID_EXIT to the
        
        wx.EVT_MENU(self, ID_NEW_TASK, self.OnTextEntry)
        wx.EVT_MENU(self, ID_VIEW_TASK, self.OnShowTaskDialog)
        wx.EVT_MENU(self, ID_SAVE_TASK, self.OnSave)
        wx.EVT_MENU(self, ID_SEND_TASK, self.OnSent)
