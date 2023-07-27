from rich import print
from windows_tools.installed_software import get_installed_software
import pandas as pd

"""
requirements:
    pip install rich pandas windows-tools.installed-software

related:
    https://learn.microsoft.com/en-us/windows/win32/shell/app-registration
    https://stackoverflow.com/questions/429738/detecting-installed-programs-via-registry
    https://stackoverflow.com/questions/53132434/list-of-installed-programs
    https://github.com/netinvent/windows_tools
    
reg commands:
    reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\\Uninstall  # remove last double slash
    reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\\Uninstall  # remove last double slash
"""

data = []
for software in get_installed_software():
    # print(software['name'], software['version'], software['publisher'])
    data.append((software['name'], software['version'], software['publisher']))

df = pd.DataFrame(data)
df.columns = ['name', 'version', 'publisher']
df.index += 1
# df.to_csv('installed-apps.csv')
md = df.to_markdown()
input('resize and press enter ')
print(md)
