#!/usr/bin/python

from pylab import *
from numpy import *
import sys
from matplotlib.font_manager import FontProperties

import fileinput
HEADER_END = 0
step = []
signals1 = []
signals2 = []


infile1 = sys.argv[1] # Sum of server signals
infile2 = sys.argv[2] # Sum of local signals

outfile = 'Combined-Signals-Plot.png'

for line in fileinput.input(infile1):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        s = line.split(";")[0]
        sig = line.split(";")[1]
        step.append(s)
        signals1.append(sig)
fileinput.close()

for line in fileinput.input(infile2):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        sig = line.split(";")[1]
        signals2.append(sig)
fileinput.close()

combined = [eval(x) + eval(y) for x, y in zip(signals1, signals2)]
x = array(step)
y1 = array(signals1, dtype=int)
y2 = array(signals2, dtype=int)
y3 = array(combined, dtype=int)
#print y3
#print y1.shape
#print y2.shape
#print y3.shape

y3 = array(combined)
plot(x, y1, x, y2, x, y3)
title("TaskInfo Signaling Frequency" )
xlabel("TimeStamp")
ylabel("No. of Emitted Signals")
grid("True")
leg = legend(('task server signals', 'local signals', 'Sum of both signals'),\
    loc=9,  prop = FontProperties(size='smaller'))
savefig(outfile)
show()


