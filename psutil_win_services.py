import pprint
import psutil

def some():
    return True
    
    
if __name__ == "__main__":
    services = psutil.win_service_iter()    # this stuff is very interesting
    # for service in services:
        # print(service)    
        
    names = [service.name() for service in services]
    # print description for all services available on system
    for name in names:
        details = psutil.win_service_get(name)
        out = details.as_dict()
        print(name)
        pprint.pprint(out)
        input()
        
        
'''
info:
    -anitivirus is blocking full list of services
    -
    
'''
