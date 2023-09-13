import os
import time
import psutil
from rich import print


def now():
    """datetime now template"""
    return time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    # set title
    title = '💀 psycho killer 💀'
    title_print = 'psycho killer'
    os.system(f'title {title}')
    print(f'[*] {title_print} start to work')
    
    blacklist = {
        "msedge.exe",  # "Microsoft Edge"
        # '',
    }
    while True:
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                process_id = proc.pid
                if process_name in blacklist:
                    proc.terminate()
                    status = proc.is_running()
                    print(f'{now()} | {process_name} {process_id:>5} | [red]\[*] sent signal to terminate[/red]')
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        time.sleep(60)
