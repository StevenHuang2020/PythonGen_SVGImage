import os
import numpy as np 
from svgFile import SVGFile
from svgBasic import *


class SVGSmile:
    def __init__(self, dstSvgfile, ridus=None, svgW=None,svgH=None):
        self.ridus = ridus
        if svgW == None:
            self.svgW = int(ridus*2 + 0.5)
            self.svgH = self.svgW
        else:
            self.svgW = svgW
            self.svgH = svgH
        self.svg = SVGFile(dstSvgfile,W=self.svgW,H=self.svgH)
        print('ridus=',ridus,'SVG H,W=',self.svgH,self.svgW)
        
    def draw(self, ridus=None, offsetX=0, offsetY=0):
        ridus = ridus or self.ridus
        
        x = ridus + offsetX
        y = ridus + offsetY
        self.svg.draw(draw_circle(x,y,ridus,color='#FFC10E'))
    
        x = ridus*0.68 + offsetX
        y = ridus*0.66 + offsetY
        r = ridus*0.16
        self.svg.draw(draw_circle(x,y,r,color='#333333')) #left eye
        
        x = 2*ridus - x +  2*offsetX
        self.svg.draw(draw_circle(x,y,r,color='#333333')) #right eye
        
        startPt = [0.42*ridus + offsetX, 1.30*ridus + offsetY]
        stopPt = [2*ridus - startPt[0] + 2*offsetX, startPt[1]]
        cp1 =  [0.71*ridus + offsetX, 1.88*ridus+offsetY]  #Bézier Curves control points
        cp2 =  [2*ridus - cp1[0] + 2*offsetX, cp1[1]]  #Bézier Curves control points
        path = 'M {} {} C {} {}, {} {}, {} {}'.format(startPt[0],startPt[1],\
            cp1[0],cp1[1],cp2[0],cp2[1],stopPt[0],stopPt[1])
        
        self.svg.draw(draw_path(path, width=0.127*ridus, color='black')) #mouth
    
    def close(self):
        self.svg.close()
    
def testSmile():
    d = r'.\images\smileC.svg'
    s = SVGSmile(dstSvgfile=d,ridus=100,svgW=300,svgH=300)
    s.draw(offsetX=20,offsetY=45)
    s.close()
    
def testSmile2():
    d = r'.\images\smileC2.svg'
    N = 6
    inter = 5
    offsetX=0
    offsetY=0
    r0 = 10
    
    totalW = N*(N-1)*r0 + N*inter + offsetX
    totalH = (N-1)*2*r0 + offsetY
    
    s = SVGSmile(dstSvgfile=d,svgW=totalW,svgH=totalH)
    for i in range(1,N):
        r = i*r0
        s.draw(ridus = r,offsetX=offsetX,offsetY=offsetY)
        offsetX += (2*r + inter)
        
    s.close()
       
def main():
    #testSmile()
    testSmile2()
    
if __name__=='__main__':
    main()         