#!/usr/bin/python
import sys
from numpy import *
from pylab import *

DATA_MAGNIFY = 10
#FFWD = 0

fn1 = sys.argv[1] # task-urgency stat file
fn2 = sys.argv[2] # signal freq stat file
FFWD = int(sys.argv[3]) # step forward 

taskurg = []
sigfreq = []
steps = []

f1 = open(fn1, 'r')
f2 = open(fn2, 'r') 

for line in f1.readlines():
    u = line.split(';')[1]
    st = line.split(';')[0]
    taskurg.append(20 * float(u))
    steps.append(st)
f1.close()

for line in f2.readlines():
    s = line.split(';')[1]
    sigfreq.append(float(s))
f1.close()

# trim list
taskurg1 = taskurg[FFWD:]
sigfreq1 = sigfreq[FFWD:]
steps1 = steps[FFWD:]

x = array(steps1)
y1 = array(taskurg1, dtype=float)
y2 = array(sigfreq1, dtype=float)
#print a2
c= corrcoef([y1,y2])
print c

outfile = 'CorrelationTaskUrgency-SignallingFrequency-PostConvergence.txt'
f = open(outfile, 'w')
res = 'Corelation after ' + str(FFWD) + 'steps: \n' + str(c) + '\n'
f.write(res)
f.close()

errorbar(x, y1, yerr=None, fmt='k--', ecolor = '#C0C0C0',\
    label='Sum of task urgency changes x10')
errorbar(x, y2, yerr=None, fmt='k', ecolor = '#C0D000',\
    label='Local signaling frequecy of robots')

ym = [v*DATA_MAGNIFY for v in y1]
x2 = x[:]
plot(x, ym, 'k--', x2, y2, 'k')

xlabel('Time Step (s)')
ylabel('')
#yticks(arange(2), ('U', 'S'))
title('Correlation of Task urgency and Signalling frequency')
grid(True)
legend()

outfile = 'CorrelationTaskUrgency-SignallingFrequency-PostConvergence.png'
savefig(outfile)
show()   
