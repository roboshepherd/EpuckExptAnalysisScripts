#!/usr/bin/python

# 5 args: <signal raw log file> <expt-start> <expt-end> <count-interval>\
#       <outfile-prefix>

import sys
import fileinput
import linecache

from numpy import *
from pylab import *
from scipy.stats import *
HEADER_END = 0
signal_ts = []
infile = sys.argv[1] # signal log input
START_TIME = int(sys.argv[2])
END_TIME = int(sys.argv[3])
interval = int(sys.argv[4]) # interval point: inclusive this value
outfile = sys.argv[5] + '-SignalStat-' + str(interval) + 's-' + '.txt'

f = open(outfile, 'w')
start = START_TIME
tm = START_TIME
end = start + interval
step = 0

line_read = 0

#point lineno to START time
discarded = 0
added = 0
print 'start', START_TIME
print 'end:', END_TIME
for line in fileinput.input(infile):
    ts = int(line.split()[1])
    if (ts >= START_TIME)  and (ts < END_TIME):
        signal_ts.append(ts)
        added += 1
    else:
        #print "Discarding unwanted data ..."
        discarded += 1

print "discarded: ", discarded 
print "added:%d len:%d" %(added, len(signal_ts))      
fileinput.close()

v = array(signal_ts)
h  = hist(v, bins=interval)       # matplotlib version (plot)
m = min(h[0])
sd = std(h[0])
se = sem(h[0])
data = "Mean: " + str(m) + ';' + 'SD: ' + str(sd) + '; SE: ' + str(se)
print data
f.write(data)
show()
# data backup
f.close()
