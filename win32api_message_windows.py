import sys
import os
import time
import threading

import win32api
import ctypes
import pyautogui

import win32gui_test
import win32gui

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
if __name__ == "__main__":
    script_path()
    # result = win32api.MessageBox(None,"Do you want to open a file?", "title",1)
    # print(result)
    # win32api.MessageBox(0,"msgbox", "title")
    # win32api.MessageBox(0,"ok cancel?", "title",1)
    # win32api.MessageBox(0,"abort retry ignore?", "title",2)
    # win32api.MessageBox(0,"yes no cancel?", "title", 3)
    
    for x in range(30):
        print(x)
        win32api.MessageBox(0, "do?", "title_{}".format(str(x).zfill(2)), x)
        
        
        
'''
get to know, how to change python icon, after create exe file:
    pyinstaller.exe -F --icon=app.ico app.py
    
    
windows ico should be there:
    dllPath = r'C:\Windows\System32\MorIcons.Dll'
    dll = ctypes.WinDLL(dllPath)
    
    
'''