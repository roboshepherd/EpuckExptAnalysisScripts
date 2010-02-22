#!/usr/bin/env python

import sys
import linecache
from numpy import *
from pylab import *

HEADER_LINE_END = 1
du_min = []
du_avg = []
du_max = []

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 2:
        print "Usage: %s <max-line> <file1> ..." %sys.argv[0]
        sys.exit(1)
    else:
        max_line = int(sys.argv[1])
        input_files = sys.argv[2:]
        file_count = len(input_files)
        lineno = HEADER_LINE_END + 1
        du = []
        try:
            while lineno <= max_line:
                du = []
                for file in input_files:
                    i = input_files.index(file)
                    line = linecache.getline(file, lineno)
                    if(line == '\n'):
                        break
                    else:
                        v = line.split(";")[2]
                        du.append(float(v))                        
                        linecache.clearcache()
                # reset
                lineno = lineno + 1
                # calculate
                a = array(du)
                #min  = abs(a.min())
                #max = abs(a.max())
                min  = a.min()
                max = a.max()
                avg = average(du)
                #print "At%d: min:%.2f avg:%.2f  max:%.2f"\
                # %(lineno, min, avg, max)
                du_min.append(min)
                du_avg.append(avg)
                du_max.append(max)
        except Exception, e:
            print "Err: ", e
        items = len(du_avg)
        print "Items: ", items
        print "Max:", du_max
        print "Avg:", du_avg
        print "Min:", du_min
        x = arange(items)
        y = array(du_avg)
        errorbar(x, y, yerr=[du_min, du_max], fmt='ro')
        plot(x, y)

        xlabel('Time Step (s)')
        ylabel('Sum of Task Urgency Change')
        title('Sum of task urgency changes over time ')
        grid(True)
        fn = 'AllTaskUrgencyPlot' 
        savefig(fn)
        show()    


