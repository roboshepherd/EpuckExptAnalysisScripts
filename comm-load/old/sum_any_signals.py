#!/usr/bin/env python

import sys
import linecache

INTERVAL = 10 # sec
SUM_LINES = 5
PERIOD = INTERVAL * SUM_LINES


def main(max_lines, infile, outfile):
    f = open(outfile, 'w')
    step = 1
    lineno = 1
    sum = 0
    last_line = SUM_LINES
    while last_line <= max_lines:
        step = step + 1
        lineno = lineno + 1
        sum = 0
        last_line = last_line + SUM_LINES
        while (lineno <= last_line):     
            lineno += 1        
            line = linecache.getline(infile, lineno)
            if(line == '\n'):
                continue
            signals = int(line.split(';')[1])
            sum += signals
            linecache.clearcache()      
        data = str(step) + ';' + str(sum) + '\n'
        print data
        f.write(data)
    f.close()

if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 4 or numargs > 4:
        print "Usage: %s <max-line> <file> <outfile-prefix>" %sys.argv[0]
        sys.exit(1)
    else:
        max_lines = int(sys.argv[1])
        infile = sys.argv[2]
        pfx = sys.argv[3]
        outfile = pfx + "SumOver" + str(PERIOD) + "sec-" + infile
        main(max_lines, infile, outfile)
