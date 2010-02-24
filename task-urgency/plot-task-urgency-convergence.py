#!/usr/bin/env python

import sys
import fileinput
from numpy import *
from pylab import *
step = []
du_m = []
#du_sd = []
du_se = []

THRESHOLD = 0.2 

def get_summed_list(val_list): 
    sums = [0 for x in range(INTERVAL - 1)]
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
    return sums

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 3:
        print "Usage: %s  <infile> <outfile> <window-interval>" %sys.argv[0]
        sys.exit(1)
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        INTERVAL = int(sys.argv[3])
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
        conv_list = get_summed_list(absolute(du_m))
        conv = array(conv_list)
        # find conv val
        print conv
        conv_x = 0
        conv_y = 0
        conv_not_found = True
        for v in conv_list:
            if (v < THRESHOLD) and conv_not_found:
                #print "Convergence Threshold:%f, Y:%f  X:%f"\
                #%(THRESHOLD, v, conv_list.index(v))
                conv_x = conv_list.index(v) + 1
                conv_y = v
                conv_not_found = False
            elif v >= THRESHOLD:
                conv_x = 0
                conv_not_found = True
        
        #if conv_x != 0:
        print "Convergence Threshold:%f, X:%f  Y:%f"\
                %(THRESHOLD, conv_x, conv_y)
        
        x2 = array(step[INTERVAL:])
        y2 = array(conv[INTERVAL:])
        
        #errorbar(step, du_m, yerr=du_se, ecolor = '#C0C0C0')
        #plot(x, y, x, conv)
       
        
        errorbar(x, y, yerr=du_se, fmt='k--', ecolor = '#C0C0C0',\
        label='Sum of task urgency change')
        errorbar(x2, y2, yerr=None, fmt='k', ecolor = '#C0D000',\
        label='Absolute sum  over a fixed window')
        
        plot(x, y, 'k--', x2, y2, 'k')
        
        annotate('convergence', xy=(conv_x + 0.3, conv_y),  xycoords='data',
                xytext=(0.9, 0.60), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.09),
                horizontalalignment='right', verticalalignment='top',
                fontsize=13)


        
        xlabel('Time Step (s)')
        ylabel('Sum of Task Urgency Change')
        title('Sum of task urgency changes over time ')
        grid(True)
        legend()
        savefig(outfile)
        show()   
