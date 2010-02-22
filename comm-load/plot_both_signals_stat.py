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
se1 = []
se2 = []

infile1 = sys.argv[1] # Sum of server signals
infile2 = sys.argv[2] # Sum of local signals

outfile = 'Combined-Signals-Stat-Plot.png'

for line in fileinput.input(infile1):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        s = line.split(";")[0]
        sig = float(line.split(";")[1])
        e1 = float(line.split(";")[3])
        step.append(s)
        signals1.append(sig)
        se1.append(e1)
fileinput.close()

for line in fileinput.input(infile2):
    if fileinput.lineno() <= HEADER_END:
        continue
    else:
        sig = float(line.split(";")[1])
        signals2.append(sig)
        e2 = float(line.split(";")[3])
        se2.append(e2)
fileinput.close()

combined = [x+y for x, y in zip(signals1, signals2)]
x = array(step)
y1 = array(signals1)
y2 = array(signals2)
y3 = array(combined)

fig = figure()
errorbar(x, y1, yerr=se1, fmt='k--', ecolor = '#C0C0C0',\
 label='Signals emitted by task-server')
errorbar(x, y2, yerr=se2, fmt='k.', ecolor = '#C0D000',\
 label='Signals emitted by local peers')
errorbar(x, y3, yerr=None, fmt='k', ecolor = '#C0D000',\
 label='Sum of both signals')
ax = fig.add_subplot(111)
ax.plot(x, y1, 'k--', x, y2, 'k.', x, y3, 'k')


#plot(x, y1, x, y2, x, y3)
title("Task Info Signaling Frequency" )
xlabel("Time Step")
ylabel("No. of Signals")
grid("True")
#leg = ax.legend( ('Task server\'s task info signals', 'Local task info signals', 'Sum of both signals'),\
 #   loc=9,  prop = FontProperties(size='smaller'))
#legend( loc=9,  prop = FontProperties(size='smaller'))
legend()
savefig(outfile)
show()


