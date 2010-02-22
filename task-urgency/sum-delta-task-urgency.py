#!/usr/bin/env python
import time
import sys
import fileinput

INTERVAL = 50

def main():
    time_start = 0
    time_end = 0
    cum_urgency = 0
    iter = 1
    
    f = open(outfile, 'w')
    header = "##;## \n"
    f.write(header)
    try:
        for line in fileinput.input():
            if line == '\n' or fileinput.lineno() <= 2:
                continue
            print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            step = line.split(";")[1]
            u = line.split(";")[2]
            print u
            if fileinput.lineno() == 2:
                time_start = float(ts)
                time_end = time_start  + INTERVAL
                cum_urgency = float(u)
                continue
            if float(ts) <= time_end:
                cum_urgency += float(u)
            else:
                print "Cumulative urgency:%f at iter %d" %(cum_urgency, iter)
                outline = ts + ";" + step + ";" + str(cum_urgency) + "\n"
                f.write(outline)
                iter += 1
                cum_urgency = 0
                time_end = float(ts) + INTERVAL
        
    except Exception, e:
        print e
    f.close()

if __name__ == '__main__':
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <file>" %sys.argv[0]
        sys.exit(1)
    else:
        infile = sys.argv[1]
        outfile = "SumOver" + str(INTERVAL) + "sec" + sys.argv[1]
        main()
