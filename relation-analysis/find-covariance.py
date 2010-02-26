#!/usr/bin/python
import sys
from numpy import *
from pylab import *

DATA_MAGNIFY = 100
FFWD = 15
fn1 = sys.argv[1] # task-urgency stat file
fn2 = sys.argv[2] # signal freq stat file

taskurg = []
sigfreq = []
steps = []

f1 = open(fn1, 'r')
f2 = open(fn2, 'r') 

for line in f1.readlines():
    u = line.split(';')[1]
    st = line.split(';')[0]
    taskurg.append(float(u))
    steps.append(st)

for line in f2.readlines():
    s = line.split(';')[1]
    sigfreq.append(float(s))

# trim list
taskurg1 = taskurg[FFWD:]
sigfreq1 = sigfreq[FFWD:]
steps1 = steps[FFWD:]

a1 = array(taskurg1, dtype=float)
a2 = array(sigfreq1, dtype=float)
#print a2
print cov([a1,a2]) 


x = array(steps1)
plot(x, a1*DATA_MAGNIFY, x, a2)

xlabel('Time Step (s)')
#ylabel('Sum of Task Urgency Change')
title('Task urgency and Signalling frequency Variance ')
grid(True)
#savefig(outfile)
show()   
