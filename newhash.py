# encoding : utf-8 
import time

def gethash():
    time.sleep(1)
    now = time.time()
    key = 10000000000-int(now)
    return key
if __name__ == '__main__':
    print gethash()
    