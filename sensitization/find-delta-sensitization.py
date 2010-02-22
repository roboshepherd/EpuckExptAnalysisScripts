#!/usr/bin/env python

import time
import sys
import fileinput
import math

import fnmatch
import os

#DIR_PATH = './raw-pose'
DATA_LINE_START = 5
MAX_SHOPTASK = 4

def main():
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, 'Robot*.txt'):
                print "Parsing: ", file
                outfile = "Delta" + file
                infile = dir_path + '/' + file    
                find_delta_sensitization(infile, outfile)

def find_delta_sensitization(infile, outfile):
    f = open(outfile, 'w')
    header = "##;## \n Time; Step; Delta Sensitization"
    last_line = [0 for x in range(MAX_SHOPTASK)]
    f.write(header)
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() < DATA_LINE_START:
                continue
            #print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            step = line.split(";")[2]       
            this_line = line.split(";")[5:]
            print "last_line: ", last_line
            print "this_line: ", this_line
            dt_sz = 0
            for v in range(MAX_SHOPTASK):                
                dt_sz += abs((float(this_line[v]))) - abs(float(last_line[v]))
            #print dt_urgency
            out_line = ts + ";" + step +";"+ str(dt_sz) + "\n"
            last_line = this_line
            if fileinput.lineno() == DATA_LINE_START:
                continue # skip first data line
            else:
                f.write(out_line)                
    except Exception, e:
        print e
    fileinput.close()
    f.close()


if __name__ == '__main__':
    main()

