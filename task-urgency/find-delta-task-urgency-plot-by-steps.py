#!/usr/bin/env python

import time
import sys
import fileinput
import fnmatch
import os

import numpy 
import pylab 

MAX_SHOPTASK = 2
HEADER_LINE_END = 2

def plot_urgency(outfile):
    #ts = []
    step = []
    delta_urgency = []
    for line in fileinput.input(outfile):
        if fileinput.lineno() <= HEADER_LINE_END:
            continue
        else:
            #t = line.split(";")[0]
            s = line.split(";")[1]
            du = line.split(";")[2]
            #ts.append(float(t))
            step.append(int(s))
            delta_urgency.append(float(du))
        
    x = numpy.array(step)
    y = numpy.array(delta_urgency)
    
    pylab.plot(x, y)

    pylab.xlabel('Time Stamp (s)')
    pylab.ylabel('Task Urgency')
    pylab.title('Sum of task urgency changes over time ')
    pylab.grid(True)
    pylab.savefig('delta_urgency_sum_plot')

    pylab.show()
        


def find_delta_urgency(infile, outfile):
    f = open(outfile, 'w')
    header = "##;## \n Time; Step; DeltaUrgency \n"
    f.write(header)
    last_line = [0 for x in range(MAX_SHOPTASK)]
    dt_urgency = 0
    try:
        for line in fileinput.input(infile):
            print line
            if fileinput.lineno() <= HEADER_LINE_END:
                continue
            else:
                print "line # : ", fileinput.lineno()
                ts = line.split(";")[0]
                step = line.split(";")[1]        
                this_line = line.split(";")[2:]
                #print "last_line: ", last_line[2]
                #print "this_line: ", this_line[2:]
                dt_urgency = 0
                for v in range(MAX_SHOPTASK):                
                    dt_urgency += (float(this_line[v]) - float(last_line[v]))
                #print dt_urgency
                out_line = ts + ";" + step +";"+ str(dt_urgency) + "\n"
                last_line = this_line
                if fileinput.lineno() == (HEADER_LINE_END + 1):
                    continue # skip first data line
                else:
                    f.write(out_line)                
    except Exception, e:
        print e
    fileinput.close()
    f.close()
    #plot_urgency(outfile)
    


if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <raw-urgency-dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, '*.txt'):
                print "Parsing: ", file
                outfile = "Delta" + file
                infile = dir_path + '/' + file                    
                find_delta_urgency(infile, outfile)
