#!/usr/bin/env python

import time
import sys
import fileinput

import numpy 
import pylab 

MAX_SHOPTASK = 4
HEADER_LINE_END = 2

def plot_urgency(outfile):
    ts = []
    step = []
    delta_urgency = []
    for line in fileinput.input(outfile):
        if fileinput.lineno() <= HEADER_LINE_END:
            continue
        else:
            t = line.split(";")[0]
            s = line.split(";")[1]
            du = line.split(";")[2]
            ts.append(float(t))
            step.append(float(s))
            delta_urgency.append(float(du))
    fileinput.close()    
    x = numpy.array(ts)
    y = numpy.array(delta_urgency)
    
    pylab.plot(x, y)

    pylab.xlabel('Time Stamp (s)')
    pylab.ylabel('Task Urgency')
    pylab.title('Sum of task urgency changes over time ')
    pylab.grid(True)
    fn = 'Plot' + outfile.split('.')[0]
    pylab.savefig(fn)

    pylab.show()
        


def main():
    f = open(outfile, 'w')
    header = "##;## \n Time; Step; DeltaUrgency \n"
    f.write(header)
    last_line = [0 for x in range(MAX_SHOPTASK)]
    dt_urgency = 0
    try:
        for line in fileinput.input():
            if fileinput.lineno() <= HEADER_LINE_END:
                continue
            else:
                #print "line # : ", fileinput.lineno()
                ts = line.split(";")[0]
                step = line.split(";")[2]        
                this_line = line.split(";")[3:]
                #print "last_line: ", last_line[2]
                #print "this_line: ", this_line[2]
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
    f.close()
    fileinput.close()
    plot_urgency(outfile)
    


if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <filename>" %sys.argv[0]
        sys.exit(1)
    else:
        outfile = "Delta" + sys.argv[1]
        main()
