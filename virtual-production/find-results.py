#!/usr/bin/env python
import time
import sys
import fileinput
import math

import fnmatch
import os
from numpy import *

#DIR_PATH = './raw'
START_DATA_LINE = 3 
MAX_TASKS = 4
SAMPLE_SIZE = 10
MAX_STEPS = 480
OPT_PCT = 50
D_PHI_INC = 0.005

prod_compl_step = []
task_pmw = {0:[], 1:[], 2:[],3:[]}

outfile = "VMS-Results.txt"
f = open(outfile, 'w')
header = "taskid; prod_comp_step\n"
f.write(header) 

f2 = open("VMS-Stat.txt", 'w')

def main():
    numargs = len(sys.argv)

    if numargs < 2 or numargs > 2:
        print "Usage: %s <dir>" %sys.argv[0]
        sys.exit(1)
    else:
        dir_path = sys.argv[1]
        for file in os.listdir(dir_path):
            if fnmatch.fnmatch(file, '*.txt'):
                print "Parsing: ", file
                infile = dir_path + '/' + file
                
                find_pct(infile, outfile)
                #break # uncomment to test a single file first
        #f.close()
        a = array(prod_compl_step)    
        avg = int(mean(a))
        sd = int(std(a))    
        stat1 =  "items: %d , apc steps:%d (SD=%d)" %(len(prod_compl_step), avg, sd)
        stat2 = "\napcd: %f \n" %((float(avg) - OPT_PCT)/OPT_PCT)
        f2.write(stat1)
        f2.write(stat2)
        print stat1, stat2
        # pmw
        total_pmw = 0
        #total_pmw_steps = 0
        t = []
        for tid in xrange(0, MAX_TASKS):
            t += task_pmw[tid]      
        #print t
        print "maint. steps: %d" %len(t)
        b = array(t)
        total_pmw = sum(b)        
        avg_pmw = mean(b)
        sd_pmw = std(b)
        stat3 = "avg pmw: %f steps: %d (SD=%d)\n" \
         %(avg_pmw, int(ceil(avg_pmw/D_PHI_INC)), 
         int(ceil(sd_pmw/D_PHI_INC)) )
        print stat3
        f2.write(stat3)      
        
        
def find_pct(infile, outfile):    
    search_pct = [True for x in xrange(MAX_TASKS+1)]
    try:
        for line in fileinput.input(infile):
            if line == '\n' or fileinput.lineno() < START_DATA_LINE:
                continue
            #print "line # : ", fileinput.lineno()
            this_line = line.split(";")
            #print this_line
            #ts = line.split(";")[0]
            step = this_line[-(MAX_TASKS +1)] # from right      
            if(int(step) > MAX_STEPS):
                break  
            urgencies = this_line[-MAX_TASKS:]
            for tid in range(0, MAX_TASKS):
                   if(search_pct[tid]):
                        u = eval(urgencies[tid])
                        if(u == 0):
                            prod_compl_step.append(int(step))
                            search_pct[tid] = False
                            out_line = str(tid+1) +";"+ step + "\n"
                            #print out_line
                            f.write(out_line)
                            #print this_line
                   else:
                       if(u >= 0):
                        task_pmw[tid].append(u)     
                          
        #tid = 0
        #print "task %d maint steps: %d" %(tid+1, len(task_pmw[tid]))    
    except Exception, e:
        print e
    fileinput.close()
    



if __name__ == '__main__':
    main()

