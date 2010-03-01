#!/usr/bin/env python

import time
import sys
import fileinput
import math

import fnmatch
import os

#DIR_PATH = './raw-pose'
START_DATA_LINE = 5 # for pose-at ts : 5,  else 4

def main():
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, '*.txt'):
                print "Parsing: ", file
                outfile = "Delta" + file
                infile = dir_path + '/' + file    
                find_delta_translation(infile, outfile)
                #break

def find_delta_translation(infile, outfile):
    f = open(outfile, 'w')
    header = "##;## \n Time; Step; Delta Translation \n"
    f.write(header)
    last_line = [0 for x in range(2)]
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() < START_DATA_LINE:
                continue
            #print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            step = line.split(";")[2]       
            this_line = line.split(";")[4:]
            #print "last_line: ", last_line
            #print "this_line: ", this_line
            dx = (float(this_line[0]) - float(last_line[0]))
            dy = (float(this_line[1]) - float(last_line[1]))
            #print "dx:%f, dy:%f" %(dx,dy)
            delta_dist = math.sqrt(dx*dx + dy*dy)
            #print delta_dist
            out_line = ts + ";" + step +";"+ str(delta_dist) + "\n"
            last_line = this_line[:]
            if fileinput.lineno() == START_DATA_LINE:
                continue # skip first data line
            else:
                f.write(out_line)
                #break   
    except Exception, e:
        print e
    fileinput.close()
    f.close()


if __name__ == '__main__':
    main()
