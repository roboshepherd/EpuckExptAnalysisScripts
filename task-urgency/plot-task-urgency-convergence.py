#!/usr/bin/env python

import sys
import fileinput
from numpy import *
from pylab import *
step = []
du_m = []
#du_sd = []
du_se = []

INTERVAL = 6

def get_summed_array(val_list): 
    sums = [0 for x in range(INTERVAL -1)]
    items_count = len(val_list)
    iter = INTERVAL
   
    while iter <= items_count:
        start_point = iter - INTERVAL       
        end_point = iter
        sum  = 0
        while start_point < end_point:
            start_point += 1            
            if (start_point % INTERVAL) != 0:
                sum += val_list[start_point - 1]
                continue
            else:
                sum += val_list[start_point - 1]
                sums.append(sum)
                #sums.insert(iter + INTERVAL, sum)
                iter += 1
                break
    print "Len: ", len(sums)       
    return array(sums)

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
        x = array(step)
        y = array(du_m)
        err = array(du_se)
        # get convergence line
        conv = get_summed_array(absolute(du_m))
        print conv
        errorbar(step, du_m, yerr=du_se, ecolor = '#C0C0C0')
        plot(x, y, x, conv)

        xlabel('Time Step (s)')
        ylabel('Sum of Task Urgency Change')
        title('Sum of task urgency changes over time ')
        grid(True)
        savefig(outfile)
        show()   
