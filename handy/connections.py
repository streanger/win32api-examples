import psutil
from rich import print

connections = psutil.net_connections()
print(connections)
