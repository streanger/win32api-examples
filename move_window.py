import time
import win32api
import win32gui



def get_windows_hwnds():
    toplist = []
    winlist = []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    win32gui.EnumWindows(enum_cb, toplist)
    # windows = [(hwnd, title) for hwnd, title in winlist if window_title in title.lower()]
    windows = [(hwnd, title) for hwnd, title in winlist]
    return windows
    
    
if __name__ == "__main__":
    hwnds = get_windows_hwnds()
    hwnds = sorted(hwnds, key=lambda x: x[1])
    
    data = []
    for (hwnd, title) in hwnds:
        if title:
            print((hwnd, title))
            # data.append((hwnd, title))   # this will crash everything :)
            
            # if title.startswith('python'):
            if 'python' in title:
                data.append((hwnd, title))
    # input('press enter, to continue... ')
    for key, (hwnd, title) in enumerate(data):
        print((hwnd, title))
        try:
            for x in range(100):
                win32gui.MoveWindow(hwnd, 20 + key*75, 20 + key**2*2, 100, 500, True)
                # win32gui.MoveWindow(hwnd, 0 + x*4, 0 + x*4, 500 - x*4, 500 - x*4, True)     # resize down to center
                # time.sleep(0.001)
        except:
            pass
        time.sleep(0.01)
    
    
'''
info:
    -move window --> https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-movewindow
    -inb4 --> script is just for test
    -
    
'''
