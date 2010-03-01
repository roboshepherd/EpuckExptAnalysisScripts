#!/usr/bin/env python

import sys
import linecache
#from numpy import *
from pylab import *
from scipy import *
from scipy.stats import *

HEADER_LINE_END = 2
du_m = []
du_sd = []
du_se = []

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 3:
        print "Usage: %s <max-step> <file1> ..." %sys.argv[0]
        sys.exit(1)
    else:
        max_step = int(sys.argv[1])
        input_files = sys.argv[2:]
        file_count = len(input_files)
        lineno = HEADER_LINE_END + 1
        fn = "RobotDist2TasksStat-Total-" + str(max_step)  +  "steps.txt"
        f = open(fn, 'w')
        step = 1
        try:
            while lineno <= (max_step + HEADER_LINE_END) :
                du = []
                for file in input_files:
                    i = input_files.index(file)
                    line = linecache.getline(file, lineno)
                    if(line == '\n'):
                        continue
                    else:
                        v = line.split(";")[1]
                        du.append(float(v))                        
                        linecache.clearcache()
                # reset
                lineno = lineno + 1
                step = step + 1
                # calculate
                a = array(du)
                m  = mean(a)
                sd = std(a)
                se = sem(a)
                #print "At%d: min:%.2f avg:%.2f  max:%.2f"\
                # %(lineno, min, avg, max)
                du_m.append(m)
                du_sd.append(sd)
                du_se.append(se)
                data = str(step) + ';' + str(m) + ';' + str(sd) + ';'\
                 + str(se) + '\n'
                f.write(data)

        except Exception, e:
            print "Err: ", e
        f.close()
 


