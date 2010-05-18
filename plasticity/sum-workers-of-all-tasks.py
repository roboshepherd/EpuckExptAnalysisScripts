#!/usr/bin/env python
import time
import sys
import fileinput
import math

import fnmatch
import os

#DIR_PATH = './raw'
START_DATA_LINE = 3 
MAX_TASKS = 4

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
                outfile = "SumAll" + file
                infile = dir_path + '/' + file    
                sum_over_all_tasks(infile, outfile)
                #break # uncomment to test a single file first

def sum_over_all_tasks(infile, outfile):
    f = open(outfile, 'w')
    header = "##;## \n Step; Total workers \n"
    f.write(header)
    last_line = [0 for x in range(2)]
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() < START_DATA_LINE:
                continue
            print "line # : ", fileinput.lineno()
            this_line = line.split(";")
            #print this_line
            #ts = line.split(";")[0]
            step = this_line[-(MAX_TASKS +1)] # from right      
            this_workers = this_line[-MAX_TASKS:]   
            total_workers = 0
            for worker in this_workers:
                total_workers += int(worker)
            out_line = step +";"+ str(total_workers) + "\n"
            #if fileinput.lineno() == START_DATA_LINE:
            #    continue # skip first data line
            #else:
            f.write(out_line)
                #break   
    except Exception, e:
        print e
    fileinput.close()
    f.close()


if __name__ == '__main__':
    main()
