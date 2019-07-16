import random
import time
import win32api
import win32gui


def random_color():
    # return "{:06X}".format(random.randint(0, 0xFFFFFF))
    return random.randint(0, 0xFFFFFF)
    
    
def set_colors():
     # colors = tuple([0x118811 for x in range(10)])
    number = 200
    colors = tuple([random_color() for x in range(number)])
    elements = tuple([x for x in range(number)])
    
    elements = (4, )
    colors = (0xdddddd, )
    if False:
        # every element one by one
        for key, value in enumerate(elements):
            print((value, ), (colors[key], ))
            win32api.SetSysColors((value, ), (colors[key], ))       # first tuple -> elements; second tuple -> (R, G, B)
            # time.sleep(2)
    else:
        # all elements at once
        win32api.SetSysColors(elements, colors)       # first tuple -> elements; second tuple -> (R, G, B)
    return True
    
    
def get_windows_hwnd(window_title):
    toplist = []
    winlist = []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    win32gui.EnumWindows(enum_cb, toplist)
    # windows = [(hwnd, title) for hwnd, title in winlist if window_title in title.lower()]
    windows = [(hwnd, title) for hwnd, title in winlist]
    return windows
    
    
if __name__ == "__main__":
    windows = get_windows_hwnd('python')
    for key, (hwnd, title) in enumerate(windows):
        print((hwnd, title))
        try:
            win32gui.DrawFocusRect(hwnd, (200+key, 200+key, 600+key, 600+key))
        except:
            pass
        ask = input('stop? ')
        if ask == 'yes':
            break
    
'''
todo:
    write script which change colors of elements, depend on time of the day, weather, sun...
    
'''


'''
https://docs.microsoft.com/pl-pl/windows/win32/api/winuser/nf-winuser-getsyscolor

sys colors:
win32api.GetSysColor(4)         # returns the color of element nr 4



Parameters
nIndex

Type: int

The display element whose color is to be retrieved. This parameter can be one of the following values.

Value	Meaning
COLOR_3DDKSHADOW
21
Dark shadow for three-dimensional display elements.
COLOR_3DFACE
15
Face color for three-dimensional display elements and for dialog box backgrounds.
COLOR_3DHIGHLIGHT
20
Highlight color for three-dimensional display elements (for edges facing the light source.)
COLOR_3DHILIGHT
20
Highlight color for three-dimensional display elements (for edges facing the light source.)
COLOR_3DLIGHT
22
Light color for three-dimensional display elements (for edges facing the light source.)
COLOR_3DSHADOW
16
Shadow color for three-dimensional display elements (for edges facing away from the light source).
COLOR_ACTIVEBORDER
10
Active window border.
COLOR_ACTIVECAPTION
2
Active window title bar.
The associated foreground color is COLOR_CAPTIONTEXT.

Specifies the left side color in the color gradient of an active window's title bar if the gradient effect is enabled.

COLOR_APPWORKSPACE
12
Background color of multiple document interface (MDI) applications.
COLOR_BACKGROUND
1
Desktop.
COLOR_BTNFACE
15
Face color for three-dimensional display elements and for dialog box backgrounds. The associated foreground color is COLOR_BTNTEXT.
COLOR_BTNHIGHLIGHT
20
Highlight color for three-dimensional display elements (for edges facing the light source.)
COLOR_BTNHILIGHT
20
Highlight color for three-dimensional display elements (for edges facing the light source.)
COLOR_BTNSHADOW
16
Shadow color for three-dimensional display elements (for edges facing away from the light source).
COLOR_BTNTEXT
18
Text on push buttons. The associated background color is COLOR_BTNFACE.
COLOR_CAPTIONTEXT
9
Text in caption, size box, and scroll bar arrow box. The associated background color is COLOR_ACTIVECAPTION.
COLOR_DESKTOP
1
Desktop.
COLOR_GRADIENTACTIVECAPTION
27
Right side color in the color gradient of an active window's title bar. COLOR_ACTIVECAPTION specifies the left side color. Use SPI_GETGRADIENTCAPTIONS with the SystemParametersInfo function to determine whether the gradient effect is enabled.
COLOR_GRADIENTINACTIVECAPTION
28
Right side color in the color gradient of an inactive window's title bar. COLOR_INACTIVECAPTION specifies the left side color.
COLOR_GRAYTEXT
17
Grayed (disabled) text. This color is set to 0 if the current display driver does not support a solid gray color.
COLOR_HIGHLIGHT
13
Item(s) selected in a control. The associated foreground color is COLOR_HIGHLIGHTTEXT.
COLOR_HIGHLIGHTTEXT
14
Text of item(s) selected in a control. The associated background color is COLOR_HIGHLIGHT.
COLOR_HOTLIGHT
26
Color for a hyperlink or hot-tracked item. The associated background color is COLOR_WINDOW.
COLOR_INACTIVEBORDER
11
Inactive window border.
COLOR_INACTIVECAPTION
3
Inactive window caption.
The associated foreground color is COLOR_INACTIVECAPTIONTEXT.

Specifies the left side color in the color gradient of an inactive window's title bar if the gradient effect is enabled.

COLOR_INACTIVECAPTIONTEXT
19
Color of text in an inactive caption. The associated background color is COLOR_INACTIVECAPTION.
COLOR_INFOBK
24
Background color for tooltip controls. The associated foreground color is COLOR_INFOTEXT.
COLOR_INFOTEXT
23
Text color for tooltip controls. The associated background color is COLOR_INFOBK.
COLOR_MENU
4
Menu background. The associated foreground color is COLOR_MENUTEXT.
COLOR_MENUHILIGHT
29
The color used to highlight menu items when the menu appears as a flat menu (see SystemParametersInfo). The highlighted menu item is outlined with COLOR_HIGHLIGHT.
Windows 2000:  This value is not supported.

COLOR_MENUBAR
30
The background color for the menu bar when menus appear as flat menus (see SystemParametersInfo). However, COLOR_MENU continues to specify the background color of the menu popup.
Windows 2000:  This value is not supported.

COLOR_MENUTEXT
7
Text in menus. The associated background color is COLOR_MENU.
COLOR_SCROLLBAR
0
Scroll bar gray area.
COLOR_WINDOW
5
Window background. The associated foreground colors are COLOR_WINDOWTEXT and COLOR_HOTLITE.
COLOR_WINDOWFRAME
6
Window frame.
COLOR_WINDOWTEXT
8
Text in windows. The associated background color is COLOR_WINDOW.

'''