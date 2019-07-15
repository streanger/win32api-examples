''' grab window screen '''
import sys
import os

from PIL import ImageGrab
import win32gui


def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
def get_image(window_title):
    toplist = []
    winlist = []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    win32gui.EnumWindows(enum_cb, toplist)
    windows = [(hwnd, title) for hwnd, title in winlist if window_title in title.lower()]
    # just grab the hwnd for first window matching 'window_title'
    windows = windows[0]
    hwnd = windows[0]
    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    return img
    
    
if __name__ == "__main__":
    script_path()
    img = get_image('python')
    img.save('python.png')
    # img.show()
