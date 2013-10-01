#!/usr/bin/env python
"""
Produces load on all available CPU cores
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import time

def f(x):
    sleeptime = 10
    loopcounter = 1000
    while True:
            for z in range(0, loopcounter):
                x*x
            time.sleep(sleeptime)
            sleeptime = sleeptime -1;
            loopcounter = loopcounter*5
            if sleeptime == 0:
                while True:
                        x *x




if __name__ == '__main__':
    processes = cpu_count()
    print 'utilizing %d cores\n' % processes
    pool = Pool(processes)
    pool.map(f, range(processes))

