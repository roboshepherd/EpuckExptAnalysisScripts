#!/usr/bin/env python
import time
import sys
import os
import fnmatch
import fileinput

HEADER_LINE_END = 2
INTERVAL = 300

def sum_translation(infile, outfile):
    time_start = 0
    time_end = 0
    cum_trans= 0
    iter = 1
    
    f = open(outfile, 'w')
    header = "##;## \n Time; Step; TranslationSum \n"
    f.write(header)
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() <= HEADER_LINE_END:
                continue
            print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            step = line.split(";")[1]
            u = line.split(";")[2]
            print u
            if fileinput.lineno() == 2:
                time_start = float(ts)
                time_end = time_start  + INTERVAL
                cum_trans = float(u)
                continue
            if float(ts) <= time_end:
                cum_trans += float(u)
            else:
                print "Cumulative translation:%f at iter %d" %(cum_trans, iter)
                outline = ts + ";" + step + ";" + str(cum_trans) + "\n"
                f.write(outline)
                iter += 1
                cum_trans = 0
                time_end = float(ts) + INTERVAL
        
    except Exception, e:
        print e
    f.close()

if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, 'Delta*.txt'):
                print "Parsing: ", file
                outfile = "SumOver" + str(INTERVAL) + "sec-" + file
                infile = dir_path + '/' + file    
                sum_translation(infile, outfile)
