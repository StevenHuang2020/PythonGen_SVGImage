import os
import cv2
import numpy as np 
from svgFile import SVGFile
from svgBasic import *
from svgSmile import *

def getImgHW(img):
    return img.shape[0],img.shape[1]

def changeBgr2Rbg(img): #input color img
    if getImagChannel(img) == 3:
        b,g,r = cv2.split(img)       # get b,g,r
        img = cv2.merge([r,g,b])
    return img

def loadImg(file,mode=cv2.IMREAD_COLOR):
    #mode = cv2.IMREAD_COLOR cv2.IMREAD_GRAYSCALE cv2.IMREAD_UNCHANGED
    try:
        img = cv2.imread(file,mode)
    except:
        print("Load image error,file=",file)
        
    if getImagChannel(img) == 3:
        img = changeBgr2Rbg(img)
    return img

def getImagChannel(img):
    if img.ndim == 3: #color r g b channel
        return 3
    return 1  #only one channel

class SVGImageMask:
    def __init__(self,imageFile, dstSvgfile,step=1):
        self.image = loadImg(imageFile,cv2.IMREAD_COLOR)#cv2.IMREAD_GRAYSCALE
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.step = step
        self.svgH = int((self.height//step) * step)
        self.svgW = int((self.width//step) * step)
        self.svg = SVGFile(dstSvgfile,W=self.svgW,H=self.svgH)
        print('step=',step,'image H,W=',self.height,self.width,'SVG H,W=',self.svgH,self.svgW)
        
    def drawStep(self):
        r = self.step/2
        for i in range(0,self.svgH,self.step):
            for j in range(0,self.svgW,self.step):
                x = i+1/2*self.step 
                y = j+1/2*self.step 
                
                roi = self.image[i:i+self.step, j:j+self.step]
                #print(i,j,self.svgH,self.svgW,i+self.step,j+self.step)            
                color = randomColor3(np.mean(roi))
                if 0:
                    self.svg.draw(draw_circle(y,x,r,color=color))
                else:
                    self.svg.draw(draw_rect(y,x,self.step,self.step,color=color))
        
    def drawColor(self):
        r = 1
        for i in range(0,self.svgH,self.step):
            for j in range(0,self.svgW,self.step):         
                color = convertRGB(self.image[i,j,:])
                self.svg.draw(draw_rect(j,i,r,r,stroke_width=0,color=color))
         
    def close(self):       
        self.svg.close()
        
def main():
    f = r'.\res\trumps.jpg'
    d = gImageOutputPath + r'\trumpX.svg'
    #SVGImageMask(f,d).drawStep()
    svg=SVGImageMask(f,d)
    svg.drawColor()
    
    drawSVG(svg.svg,ridus=10, offsetX=10, offsetY=20)
    svg.close()
    
if __name__=='__main__':
    main()         
 