#!/usr/bin/env python

import time
import sys
import fileinput
from matplotlib import rc
import numpy 
import pylab 
import fnmatch
import os

HEADER_LINE_END = 4
MAX_SHOPTASK = 4


def plot_sensitization(infile, outfile): 
    ts = []
    step = []
    task1 = []
    task2 = []
    task3 = []
    task4 = []
    x = None
    y1 = None
    y2 = None
    y3 = None
    y4 = None
    
    for line in fileinput.input(infile):
        if fileinput.lineno() <= HEADER_LINE_END:
            continue
        else:
            tm1 = line.split(";")[0]
            tm2 = line.split(";")[1]
            s = line.split(";")[2]
            tasks = line.split(";")[5:]
            #print tasks
            t1 = tasks[0]
            t2 = tasks[1]
            t3 = tasks[2]
            t4 = tasks[3]
            #ts.append(float(tm1))
            step.append(int(s))
            task1.append(float(t1))
            task2.append(float(t2))
            task3.append(float(t3))
            task4.append(float(t4))
        
    x = numpy.array(step)
    print "X axis len:", len(x)
    y1 = numpy.array(task1)
    y2 = numpy.array(task2)
    y3 = numpy.array(task3)
    y4 = numpy.array(task4)
    
    pylab.plot(x, y1, 'r+', x, y2, 'g,',  x, y3, 'b--',  x, y4, 'k')
    #pylab.ylim(0,1)
    pylab.xlabel('Time Step (s)')
    pylab.ylabel('Sensitization (k)')
    #pylab.title('Task urgencies recorded at Task-Server ')
    pylab.grid(True)
    pylab.legend(('Task1', 'Task2', 'Task3', 'Task4'), loc=2)
    fn = 'Plot' + outfile
    pylab.savefig(fn)
    
    # clear lists
    #task1[:] = []
    #task2[:] = []
    #task3[:] = []
    #task4[:] = []
    

    #pylab.show()


if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 :
        print "Usage: %s <rawfile>" %sys.argv[0]
        sys.exit(1)
    else:
        infile =  sys.argv[1]
        outfile = 'Plot' + infile.split('.')[0] + '.png'
        #dir_path = sys.argv[1]
        #for file in os.listdir(dir_path):
            #if fnmatch.fnmatch(file, '*.txt'):
                #print "Parsing: ", file
                #infile =  dir_path + '/' + file
                #outfile = 'Plot' + file.split('.')[0] + '.png'
        plot_sensitization(infile, outfile)
