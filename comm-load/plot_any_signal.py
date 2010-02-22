#!/usr/bin/python

from pylab import *
from matplotlib.numerix import array
import sys

import fileinput
HEADER_END = 0
step = []
signals = []

infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.png'

for line in fileinput.input(infile):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        s = line.split(";")[0]
        sig = line.split(";")[1]
        step.append(s)
        signals.append(sig)
    
x = array(step)
y1 = array(signals)



plot(x, y1)
title("TaskInfo Signaling Frequency" )
xlabel("TimeStamp")
ylabel("No. of Emitted Signals")
grid("True")
savefig(outfile)
show()


