#!/usr/bin/python
'''
Created on Dec 14, 2009

@author: uolter
'''

from gui import tomato
from conf import messages
import wx

if __name__ == '__main__':
    app = wx.App()
    tomato.Tomato(None, -1, messages.TITLE)
    app.MainLoop()