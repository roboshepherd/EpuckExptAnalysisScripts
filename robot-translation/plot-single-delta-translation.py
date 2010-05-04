#!/usr/bin/env python

import sys
import fileinput
from numpy import *
from pylab import *

HEADER_LINE_END = 2

#step = []
du_m = []

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 2:
        print "Usage: %s  <infile> <outfile>" %sys.argv[0]
        sys.exit(1)
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        for line in fileinput.input(infile):
            if fileinput.lineno() <= HEADER_LINE_END:
                continue
            m = float(line.split(';')[1])
            #m1 = float(line.split(';')[2])
            #step.append(s)
            du_m.append(m/10)
  
        fileinput.close()   
        x = arange(len(du_m))
        y = array(du_m)

        #print y
        #errorbar(x, y, yerr=du_se, ecolor = '#C0C0C0')
        plot(x, y, 'k')

        xlabel('Time Step (s)')
        ylabel('Change of Robot Translation (cm)')
        #title('Sum of robot translation changes over time ')
        grid(True)
        savefig(outfile)
        show()   
