#!/usr/bin/env python

import sys
import fileinput
from numpy import *
from pylab import *
step = []
du_m = []
#du_sd = []
du_se = []

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 2:
        print "Usage: %s  <infile> <outfile>" %sys.argv[0]
        sys.exit(1)
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        for line in fileinput.input(infile):
            s = int(line.split(';')[0])
            m = float(line.split(';')[1])
            #sd = float(line.split(';')[2])
            se = float(line.split(';')[3])
            #print "line:", s, m, se
            step.append(s)
            du_m.append(m)
            #du_sd.append(sd)
            du_se.append(se)  
        fileinput.close()   
        x = arange(len(du_m))
        y = array(du_m)
        err = array(du_se)
        #print y
        errorbar(x, y, yerr=du_se, ecolor = '#C0C0C0')
        plot(x, y)

        xlabel('Time Step (s)')
        ylabel('Sum of Robot Translation (pixel)')
        #title('Sum of robot translation changes over time ')
        grid(True)
        savefig(outfile)
        show()   
