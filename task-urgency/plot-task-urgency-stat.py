#!/usr/bin/env python

import sys
import fileinput
import linecache
from numpy import *
from pylab import *
from matplotlib import rc

step = []
du_m = []
#du_sd = []
du_se = []

SCALE_FACTOR = 10

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
            #s = (s / SCALE_FACTOR + s % SCALE_FACTOR)
            m = float(line.split(';')[1])
            #sd = float(line.split(';')[2])
            se = float(line.split(';')[3])
            #print "line:", s, m, se
            step.append(s)
            du_m.append(m)
            #du_sd.append(sd)
            du_se.append(se)  
        fileinput.close()   
        x = array(step)
        y = array(du_m)
        err = array(du_se)
        #print y
        errorbar(step, du_m, yerr=du_se, ecolor = '#C0C0C0')
        plot(x, y, 'k')

        xlabel('Time step (s)')
        ylabel(r'Sum of changes in task-urgencies ($\Delta \Phi$)')
        #title('Sum of task urgency changes over time ')
        grid(True)
        savefig(outfile)
        show()   
