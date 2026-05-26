def parse_line(string):
    if string.find('=') == -1:
        return None
    name, value = string.split('=')
    return (name, value)
    
import time
from concurrent.futures import Future

def worker(x,y):
    print('about to work')
    time.sleep(20)
    print('done')
    return x+y

def do_work(x,y,fut):
    fut.set_result(worker(x,y))
