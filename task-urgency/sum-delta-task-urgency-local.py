#!/usr/bin/env python
import time
import sys
import os
import fnmatch
import fileinput

#INTERVAL = 50
HEADER_LINE = 2


def sum_urgency(infile, outfile):
    time_start = 0
    time_end = 0
    cum_urgency = 0
    iter = 1
    
    f = open(outfile, 'w')
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() <= HEADER_LINE:
                continue
            elif fileinput.lineno() == HEADER_LINE + 1:
                ts = line.split(";")[0]
                step = line.split(";")[1]
                u = line.split(";")[2]
                expt_begin = float(ts)
                time_start = float(ts)
                time_end = time_start  + INTERVAL
                cum_urgency = float(u)
                continue
            else:
                print "line # : ", fileinput.lineno()
                ts = line.split(";")[0]
                step = line.split(";")[1]
                u = line.split(";")[2]
                print u
            
            if float(ts) <= time_end:
                cum_urgency += float(u)
            else:
                print "Cumulative urgency:%f at iter %d" %(cum_urgency, iter)
                outline = str(expt_begin + INTERVAL * iter) + ";" + str(iter)\
                 + ";" + str(cum_urgency) + "\n"

                iter += 1
                cum_urgency = 0
                time_end = float(ts) + INTERVAL
                if  fileinput.lineno() == HEADER_LINE + 1: # skip fisrt line
                    continue
                else:
                    f.write(outline)
    except Exception, e:
        print e
    fileinput.close()
    f.close()
    

if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 3 or numargs > 3:
        print "Usage: %s <delta-dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        INTERVAL = int(sys.argv[2])
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, 'Delta*.txt'):
                print "Parsing: ", file
                outfile = "SumOver" + str(INTERVAL) + "sec-" + file
                infile = dir_path + '/' + file    
                sum_urgency(infile, outfile)
