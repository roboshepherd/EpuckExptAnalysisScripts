#!/usr/bin/env python
import time
import sys
import fileinput
from opencv.cv import *
from opencv.highgui import *
HEADER_LINE_END = 4
MAX_SHOPTASK = 4
#BASE_IMG = "~/EpuckExptAnalysisScripts/trajectory-plotting/Screenshot-robots.png"
ORIG_X = 2400
ORIG_Y = 2144
ROBOT_RADIUS = 3
trajectory = []
iter = 0
specialized_task = 0
other_tasks = 0
random_walk = 0
if __name__ == '__main__':
    numargs = len(sys.argv)
    if numargs < 4:
        print "Usage: %s  <bg-img> <pose-data-file> <task-specilaized>"\
         %sys.argv[0]
        sys.exit(1)
    else:
        imgfile = sys.argv[1]
        datafile = sys.argv[2]
        mark_task = int(sys.argv[3])
        img1 = cvLoadImage(imgfile, 1)
        #print img1
        print "Width:%d Height:%d" %(img1.width, img1.height)
        print "Depth:%d" %(img1.depth)
        img2 = img1
        
        for line in fileinput.input(datafile):
            if line == '\n' or fileinput.lineno() <= HEADER_LINE_END:
                continue
            #print "line # : ", fileinput.lineno()
            iter = iter + 1
            ts = line.split(";")[0]
            step = line.split(";")[2]
            selected_task = int(line.split(";")[3])       
            x = float(line.split(";")[4])
            y = float(line.split(";")[5])
            #break
            #print "data X: %d data Y: %d" %(x,y)
            x1 = int(x * img1.width / ORIG_X)
            y1 = int(y * img1.height / ORIG_Y)
            #print "sclaed X: %d scaled Y: %d" %(x1,y1)
            pt = cvPoint(x1, y1)
            trajectory.append(pt)
            print "Selected task: %d" %selected_task 
            if selected_task == mark_task:
                cvCircle(img2, pt, ROBOT_RADIUS,\
                 CV_RGB(255,128,0))
                specialized_task += 1
            elif selected_task > 0:
                cvCircle(img2, pt, ROBOT_RADIUS,\
                 CV_RGB(255,0,255))
                other_tasks += 1
            elif selected_task == 0:
                random_walk +=1
                cvCircle(img2, pt, ROBOT_RADIUS,\
                 CV_RGB(0,0,0))
                    
            #if selected_task == 0:   
            #    cvCircle(img2, cvPoint(x1, y1), ROBOT_RADIUS,\
            #    CV_RGB(128,128,128))
            font = cvInitFont(CV_FONT_HERSHEY_PLAIN, 0.5, 0.8)
            if selected_task == mark_task:
                cvPutText(img2, step, pt, font, CV_RGB(0,0,255))
            elif selected_task == 0:
                cvPutText(img2, step, pt, font, CV_RGB(0,0,0))  
            elif selected_task > 0:
                #pass  
                cvPutText(img2, step, pt, font, CV_RGB(0,255,0))
            print "iter: ", iter 
            if iter >= 2:
                cvLine(img2, trajectory[iter-2], trajectory[iter-1],\
                 CV_RGB(255,0,0))
        t1 = "Specialized on task[%d], done: %d"\
         %(mark_task, specialized_task)
        t2 = "Other tasks done: %d" %other_tasks
        t3 = "Random_walk done: %d" %random_walk
        cvPutText(img2, t1, cvPoint(10, 20), font, CV_RGB(0,0,255)) 
        cvPutText(img2, t2, cvPoint(20, 30), font, CV_RGB(0,255,0)) 
        cvPutText(img2, t3, cvPoint(30, 40), font, CV_RGB(0,0,0))     
        cvStartWindowThread()
        cvNamedWindow('Image', CV_WINDOW_AUTOSIZE)
        cvMoveWindow('Image', 10, 40)
        #image = highgui.cvLoadImage(img1, 1)
        cvShowImage('Image', img2)
        fn =  datafile.split('.')[0] + '.png'
        cvSaveImage(fn, img2)
        time.sleep(30)


