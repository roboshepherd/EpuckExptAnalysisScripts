#!/usr/bin/env python
import time
import sys
import fileinput
from opencv.cv import *
from opencv.highgui import *
HEADER_LINE_END = 3
MAX_SHOPTASK = 4
ORIG_X = 2400
ORIG_Y = 2144
ROBOT_RADIUS = 3

if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 2:
        print "Usage: %s  <in imgfile> <in pose datafile>" %sys.argv[0]
        sys.exit(1)
    else:
        imgfile = sys.argv[1]
        datafile = sys.argv[2]
        img1 = cvLoadImage(imgfile, 1)
        print "Width:%d Height:%d" %(img1.width, img1.height)
        print "Depth:%d" %(img1.depth)
        img2 = img1
        
        for line in fileinput.input(datafile):
            if line == '\n' or fileinput.lineno() <= HEADER_LINE_END:
                continue
            #print "line # : ", fileinput.lineno()
            ts = line.split(";")[0]
            step = line.split(";")[2]
            #selected_task = int(line.split(";")[3])       
            x = float(line.split(";")[3])
            y = float(line.split(";")[4])
            #break
            #print "data X: %d data Y: %d" %(x,y)
            x1 = int(x * img1.width / ORIG_X)
            y1 = int(y * img1.height / ORIG_Y)
            #print "sclaed X: %d scaled Y: %d" %(x1,y1)
            cvCircle(img2, cvPoint(x1, y1), ROBOT_RADIUS, CV_RGB(255,0,0))
  
        
            
        cvStartWindowThread()
        cvNamedWindow('Image', CV_WINDOW_AUTOSIZE)
        cvMoveWindow('Image', 10, 40)
        #image = highgui.cvLoadImage(img1, 1)
        cvShowImage('Image', img2)
        fn =  'ImposedPosesRaw.png'
        cvSaveImage(fn, img2)
        time.sleep(30)


