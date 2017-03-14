


import os
import sys
import time


def timer(t):
   while t:
       for i in range(t, 0, -1):
           sys.stdout.write("\r" + str(t))
           time.sleep(1)
           sys.stdout.flush()
          # os.system('clear')
           t -= 1


timer(6)
