#!/usr/bin/env python
import time
import sys
import os
import fnmatch
import fileinput

EXPT_START_TIME = 1265905351.19
EXPT_END_TIME = 1265907877.92
EXPT_TIME_BASE = 1265900000.0

INTERVAL = 300
HEADER_LINE = 2
iter = 1
cum_trans = 0
t1 = EXPT_START_TIME
t2 = EXPT_START_TIME + INTERVAL

if __name__ == '__main__':
    numargs = len(sys.argv)

    outfile = "GrandsumTranslationOver"+ str(INTERVAL)+ "s"+ ".txt"
    f = open(outfile, 'w')
    header = "##;## \n AbsTimeStamp;RelativeTimeStamp; Translation \n"
    f.write(header)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        while (t2 <= EXPT_END_TIME): # for each time interval we check
            #print "Iter %d: End time: %f" %(iter, t2)
            for file in os.listdir(dir_path): # for every file we have
                if fnmatch.fnmatch(file, 'Sum*.txt'): # qualified files only
                    #print "Parsing: ", file
                    infile = dir_path + '/' + file                
                    for line in fileinput.input(infile):
                        if line == '\n' or fileinput.lineno() <= HEADER_LINE:
                            continue
                        #print "line # : ", fileinput.lineno()
                        ts = line.split(";")[0]
                        step = line.split(";")[1]
                        dt = line.split(";")[2]                    
                        t = float(ts)
                        d = float(dt)
                        # check ts and include in sum                        
                        if ((t > t1) and (t < t2)):
                            cum_trans += d
                            print "Added: %f at time %f" %(d, t)
                        #fileinput.close()
            print "Cumulative translation:%f upon iter# %d" %(cum_trans, iter)
            rel_ts = t1 - EXPT_TIME_BASE
            outline = str(t1) + ";" + str(rel_ts) + ";" + str(cum_trans) + "\n"
            f.write(outline)
            # reset
            t1 = t2
            t2 = t2 + INTERVAL
            iter += 1
            cum_trans = 0            
    f.close()
