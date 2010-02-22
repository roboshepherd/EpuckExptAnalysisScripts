#!/usr/bin/python

from pylab import *
from numpy import *
import sys
from matplotlib.font_manager import FontProperties

import fileinput
HEADER_END = 0
step = []
signals1 = []
se1 = []


infile1 = sys.argv[1] # Sum of server signals
#infile2 = sys.argv[2] # Sum of local signals

outfile = 'Global-Signals-Stat-Plot.png'

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

x = array(step)
y1 = array(signals1)

fig = figure()
errorbar(x, y1, yerr=se1, fmt='k', ecolor = '#C0C0C0',\
 label='Signals emitted by task-server')

ax = fig.add_subplot(111)
ax.plot(x, y1, 'k')

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


