#!/usr/bin/env python

import sys
import fileinput
from numpy import *
from pylab import *
step = []
max_workers = []
avg_workers = []
se_workers = []

GROUP_SIZE = 16
START_DATA_LINE = 3
HEADER_LINE_END = 2
LAST_DATA_LINE = 480 + HEADER_LINE_END

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 3:
        print "Usage: %s  <infile> <outfile>" %sys.argv[0]
        sys.exit(1)
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() < START_DATA_LINE:
               continue
            if fileinput.lineno() >= LAST_DATA_LINE:
                break   
            s = int(line.split(';')[0])
            mx = float(line.split(';')[1])
            avg = float(line.split(';')[2])
            se = float(line.split(';')[3])
            step.append(s)
            max_workers.append(mx/GROUP_SIZE)
            avg_workers.append(avg/GROUP_SIZE)
            se_workers.append(se/GROUP_SIZE)  
        fileinput.close()       
        x = array(step)
        y1 = array(max_workers)
        y2 = array(avg_workers)
        err = array(se_workers)
        # sqeeze into 1 min scale
        #xx = arange(1, TOTAL_STEPS)
        #a = 1
        #print y1
        #print y
        #errorbar(x, y1, yerr=None, fmt='k--', ecolor = '#C0C0C0',\
        #    label='Max. working robots')
        errorbar(x, y2, yerr=err, fmt='k', ecolor = '#C0D000',\
            label='Average working robots')
        #plot(x, y1, 'k--', x, y2, 'k')
        plot(x, y2, 'k')
        
        xlabel('Time Step (s)')
        ylabel('Active workers ratio')
        #title('Sum of task urgency changes over time ')
        grid(True)
        #legend()
        savefig(outfile)
        show()   
