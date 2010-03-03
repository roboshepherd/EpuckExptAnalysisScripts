#!/usr/bin/env python

import time
import sys
import fileinput

import numpy 
import pylab 


HEADER_LINE_END = 2
MAX_SHOPTASK = 4
ts = []
step = []
task1 = []
task2 = []
task3 = []
task4 = []

def plot_urgency(outfile):    
    for line in fileinput.input(outfile):
        if fileinput.lineno() <= HEADER_LINE_END:
            continue
        else:
            #tm1 = line.split(";")[0]
            #tm2 = line.split(";")[1]
            s = line.split(";")[1]
            tasks = line.split(";")[2:]
            t1 = tasks[0]
            t2 = tasks[1]
            t3 = tasks[2]
            t4 = tasks[3]
            #ts.append(float(tm1))
            step.append(float(s))
            task1.append(float(t1))
            task2.append(float(t2))
            task3.append(float(t3))
            task4.append(float(t4))
        
    x = numpy.array(step)
    y1 = numpy.array(task1)
    y2 = numpy.array(task2)
    y3 = numpy.array(task3)
    y4 = numpy.array(task4)
    
    pylab.plot(x, y1, 'r+', x, y2, 'g,',  x, y3, 'b--',  x, y4, 'k')
    pylab.ylim(0,1)
    pylab.xlabel('Time Stamp (s)')
    pylab.ylabel('Task Urgency')
    pylab.title('Task urgencies recorded at Task-Server ')
    pylab.grid(True)
    pylab.legend(('Task1', 'Task2', 'Task3', 'Task4'))
    fn = 'Plot' + outfile.split('.')[0] 
    pylab.savefig(fn)

    pylab.show()


if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <filename>" %sys.argv[0]
        sys.exit(1)
    else:
        outfile =  sys.argv[1]
        plot_urgency(outfile)
