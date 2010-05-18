#!/usr/bin/env python
import time
import sys
import fileinput
import math
import linecache
import fnmatch
import os
from numpy import *
from scipy import *
from scipy.stats import *

#DIR_PATH = './raw'
HEADER_LINES = 2
MINUTE_STEPS = 12

def main():
    numargs = len(sys.argv)

    if numargs < 3 or numargs > 3:
        print "Usage: %s <sum-dir> <max_steps>" %sys.argv[0]
        sys.exit(1)
    try:
        dir_path = sys.argv[1]
        max_steps = int(sys.argv[2])
        outfile = "StatAllExpt.txt" 
        f = open(outfile, 'w')
        header = "##;## \n Step; Max workers; Avg; SE; Min; SD \n"
        f.write(header)
        step = 1;
        while step <= max_steps:
            print "Step:", step
            workers = []
            for file in os.listdir(dir_path):
                if fnmatch.fnmatch(file, '*.txt'):
                    #print "Parsing: ", file                    
                    infile = dir_path + '/' + file
                    ln = step + HEADER_LINES                    
                    if(linecache.getline(infile, ln)):
                        line = linecache.getline(infile, ln )
                        linecache.clearcache()
                    else:
                        line = '0;0'   
                    w = int(line.split(";")[1])
                    workers.append(w)                    
            a = array(workers)
            mx = max(a)
            mn = min(a)
            m  = int((ceil(mean(a))))
            sd = int(ceil(std(a)))
            se = int(ceil(sem(a)))
            data = str(step) + ';' + str(mx) + ';' + str(m) +';' + str(se)\
             + ';' + str(mn) + ';' + str(sd) + '\n'
            f.write(data)
            step += 1   
    except Exception, e:
        print e
    fileinput.close()
    f.close()


if __name__ == '__main__':
    main()
