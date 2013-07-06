#!/opt/local/bin/python
"""
Module for opencv tracking of objects

"""
__author__ = 'wrdeman'
__version__ = '0/0'

import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from ui import Ui_MainWindow
import Plot
 
class Video():
    def __init__(self,capture):
        self.capture = capture
        self.features = []
        self.origin = []
        self.simon = "i am here"
        self.currentFrame=np.array([])
        self.previousFrame=np.array([])
        self.lkp_def=([50,100,50,0.1,0.0])
        self.fp_def=([500,0.001,7,7])
        self.lk_params = dict( winSize  = (self.lkp_def[0], self.lkp_def[0]), 
                               maxLevel = self.lkp_def[1], 
                               criteria = (cv2.TERM_CRITERIA_COUNT | 
                                           cv2.TERM_CRITERIA_EPS, 
                                           self.lkp_def[2], self.lkp_def[3]))

        self.feature_params = dict( maxCorners = self.fp_def[0], 
                                    qualityLevel = self.fp_def[1],
                                    minDistance = self.fp_def[2],
                                    blockSize = self.fp_def[3] )
        self.plot = Plot.Plot(self)


    def captureNextFrame(self,plotOn):
        """
        capture frame and reverse RBG BGR and return opencv image
        """
        ret, readFrame=self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)
            if self.features!=[]:
                self.trackPoints()
                self.drawPoints()
                if plotOn:
                    self.plot.plotPoints()
                    self.plot.plotData()
        else:
            self.currentFrame=np.array([])



    def addPoint(self, lastPos,video_params):
        """
        add a point
        switch between opencv coordinates and PyQt

        """
        image_x=video_params.right()
        image_y=video_params.bottom()
        init_image_x=video_params.left()
        init_image_y=video_params.top()

        if self.currentFrame.size!=0:
            img_event=self.currentFrame
            # x and y position of mouseclick relative to PyQt
            xpos=lastPos.x()  
            ypos=lastPos.y()
            if ((xpos-init_image_x)<image_x and 
                (ypos-init_image_y)<image_y):
                img_event=cv2.cvtColor(img_event,cv2.COLOR_BGR2RGB) 
                height,width=img_event.shape[:2]
                # scale PyQt coordinates to OpenCV
                xscaled=int(width*(xpos-init_image_x)/image_x)  
                yscaled=int(height*(ypos-init_image_y)/image_y)
                term = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
                gray = cv2.cvtColor(img_event, cv2.COLOR_RGB2GRAY)
                mask = np.zeros_like(gray)
                mask[:] = 255
                cv2.circle(mask, (xscaled, yscaled), 100, 1, -1)
                p = cv2.goodFeaturesToTrack(gray, 
                                            mask = mask, 
                                            **self.feature_params)
                add_point=False

                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        if add_point==False:
                            circ=((x-xscaled)**2+(y-yscaled)**2)**0.5
                            if circ<50:
                                self.features.append([(int(x),int(y))])
                                add_point=True
                                cv2.circle(img_event, 
                                           (x, y), 
                                           10, 
                                           (255, 0, 0), 
                                           -1)
                                if (len(self.features)!=0):
                                    for x, y in np.float32(self.features).reshape(-1, 2):
                                        cv2.circle(img_event, 
                                                   (x, y), 
                                                   10, 
                                                   (255, 255, 0), 
                                                   -1)



    def trackPoints(self):
        #track points in self.features and draw circle
        p0 = np.float32([tr[-1] for tr in self.features]).reshape(-1, 1, 2)
        self.features, st,err=cv2.calcOpticalFlowPyrLK(self.previousFrame,
                                                       self.currentFrame,
                                                       p0,
                                                       None, 
                                                       **self.lk_params)
      
    def drawPoints(self):
        new_tracks=[]
        p0 = np.float32([tr[-1] for tr in self.features]).reshape(-1, 1, 2)
        for tr, (x, y) in zip(self.features, p0.reshape(-1, 2)):
            if len(tr) > len(self.features):
                del tr[0]
            new_tracks.append(tr)
            cv2.circle(self.currentFrame, (x, y), 10, (255, 0, 0), -1)
        self.features = new_tracks
      
#draww origin
#        p0 = np.float32([tr[-1] for tr in self.origin]).reshape(-1, 1, 2)
#        for tr, (x, y) in zip(self.origin, p0.reshape(-1, 2)):
#            cv2.circle(cvImage, (x, y), 10, (255, 255, 0), -1)      
#        return cvImage

    def convertFrame(self):
        """
        converts frame to format suitable for QtGui
        """
        try: 
            height,width=self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)              
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

