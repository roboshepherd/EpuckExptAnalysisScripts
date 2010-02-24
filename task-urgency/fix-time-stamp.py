#!/usr/bin/env python
import time
import sys
import os
import fnmatch
import fileinput

HEADER_LINE = 2


def fix_timestamp(infile, outfile):
    f = open(outfile, 'w')
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() <= HEADER_LINE:
                continue
            print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            s = line.split(";")[1]
            u = line.split(";")[2]
            H = int(ts.split(':')[0])
            M = int(ts.split(':')[1])
            S = int(ts.split(':')[2])
            t = (YYYY, MM, DD, H, M, S, WDAY, JDAY, -1)
            tm = time.mktime(t)
            outline = str(tm) + ";" + s + ';' +  u 
            f.write(outline)
            r = None
    except Exception, e:
        print e
    fileinput.close()
    f.close()
    

if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 7 or numargs > 7:
        print "Usage: %s <delta-dir> <YYYY> <MM> <DD> <WEEK_DAY> <JUL_DAY>"\
         %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        YYYY = int(sys.argv[2])
        MM = int(sys.argv[3])
        DD = int(sys.argv[4])
        WDAY = int(sys.argv[5])
        JDAY = int(sys.argv[6])
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, 'Delta*.txt'):
                print "Fixing: ", file
                outfile = dir_path + '/' +  file.split('.')[0] + 'AbsTime.txt'
                infile = dir_path + '/' + file    
                fix_timestamp(infile, outfile)
