#!/usr/bin/env python

import time
import sys
import fileinput

import numpy 
import pylab 


HEADER_LINE_END = 2
MAX_SHOPTASK = 8
ts = []
step = []
task1 = []
task2 = []
task3 = []
task4 = []
task5 = []
task6 = []
task7 = []
task8 = []

def plot_urgency(outfile):    
    for line in fileinput.input(outfile):
        if fileinput.lineno() <= HEADER_LINE_END:
            continue
        else:
            tm1 = line.split(";")[0]
            tm2 = line.split(";")[1]
            s = line.split(";")[2]
            tasks = line.split(";")[3:]
            t1 = tasks[0]
            t2 = tasks[1]
            t3 = tasks[2]
            t4 = tasks[3]
            t5 = tasks[4]
            t6 = tasks[5]
            t7 = tasks[6]
            t8 = tasks[7]
            ts.append(float(tm1))
            step.append(float(s))
            task1.append(float(t1))
            task2.append(float(t2))
            task3.append(float(t3))
            task4.append(float(t4))
            task5.append(float(t5))
            task6.append(float(t6))
            task7.append(float(t7))
            task8.append(float(t8))
        
    x = numpy.arange(len(task1))
    y1 = numpy.array(task1)
    y2 = numpy.array(task2)
    y3 = numpy.array(task3)
    y4 = numpy.array(task4)
    y5 = numpy.array(task5)
    y6 = numpy.array(task6)
    y7 = numpy.array(task7)
    y8 = numpy.array(task8)
    
    pylab.plot(x, y1, 'r+', x, y2, 'r,',  x, y3, 'r--',  x, y4, 'r',\
               x, y5, 'b+', x, y6, 'b.', x, y7, 'g--', x, y8, 'g')
    #pylab.ylim(0,1)
    pylab.xlabel('Time Step (s)')
    pylab.ylabel('Task Urgency')
    pylab.xlim()
    #pylab.title('Task urgencies recorded at Task-Server ')
    pylab.grid(True)
    pylab.legend(('Task1', 'Task2', 'Task3', 'Task4',\
                  'Task5', 'Task6', 'Task7', 'Task8'))
    fn = 'Plot' + outfile.split('.')[0] + '.png'
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
