'''
Created on Dec 10, 2009

@author: uolter
'''

import wx

import time
from timer import countdown

ID_ABOUT=101
ID_EXIT=110


class Label(wx.StaticText):
    
    def __init__(self, parent, *args, **kwargs):
        wx.StaticText.__init__(self, parent, *args, **kwargs)
        self.count=1        
          
    def run(self):                
        out='Time is running %s' %self.count
        self.SetLabel(out)        
        self.count+=1
        time.sleep(10)
        self.run()



class MainWindow(wx.Frame):
    
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,wx.ID_ANY, title, size = (200,100))
        #self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.quote = Label(self, 1, "Time is running :", wx.Point(20, 30), wx.Size(200, -1))
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        # Setting up the menu.
        filemenu= wx.Menu()
        filemenu.Append(ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")
        
        # Creating the menubar.
        menuBar = wx.MenuBar()        
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)       # attach the menu-event ID_ABOUT to the
                                                        # method self.OnAbout
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)         # attach the menu-event ID_EXIT to the                                                            # method self.OnExit        
        self.Show(True)
        
    
    def OnAbout(self,e):
        d= wx.MessageDialog( self, " A sample editor in wxPython","About Sample Editor", wx.OK)
        # Create a message dialog box
        d.ShowModal() # Shows it
        d.Destroy() # finally destroy it when finished.
        
    def OnExit(self,e):
        #self.Close(True)  # Close the frame.
        self.quote.run()
                        

app = wx.PySimpleApp()
frame = MainWindow(None, -1, "pomodoro")
# frame.run()
app.MainLoop()
