#!/usr/bin/python

from pylab import *
from matplotlib.numerix import array
import sys

import fileinput
HEADER_END = 0
#step = []
sig_ts = []

infile = sys.argv[1]
INTERVAL = int(sys.argv[2])
outfile = sys.argv[1].split('.')[0] + '.pdf'

for line in fileinput.input(infile):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        ts = line.split()[1]
        sig_ts.append(int(ts))
    
items = len(sig_ts)
#x = arange(len(sig_ts))
y1 = array(sig_ts)
b = (sig_ts[items-1] - sig_ts[0])/INTERVAL
hist(y1, b)


#plot(x, y1)
#title("TaskInfo Signaling Frequency" )
xlabel("TimeStamp (s)")
ylabel("No. of Received Peer Signals")
grid("True")
savefig(outfile)
show()


