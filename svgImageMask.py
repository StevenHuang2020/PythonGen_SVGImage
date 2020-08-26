import os
import cv2
import numpy as np 
from svgFile import SVGFile
from svgBasic import *

def getImgHW(img):
    return img.shape[0],img.shape[1]

def loadImg(file,mode=cv2.IMREAD_COLOR):
    #mode = cv2.IMREAD_COLOR cv2.IMREAD_GRAYSCALE cv2.IMREAD_UNCHANGED
    return cv2.imread(file,mode)

class SVGImageMask:
    def __init__(self,imageFile, dstSvgfile,step=3):
        self.image = loadImg(imageFile,cv2.IMREAD_GRAYSCALE)
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.step = step
        self.svgH = int((self.height//step) * step)
        self.svgW = int((self.width//step) * step)
        self.svg = SVGFile(dstSvgfile,W=self.svgW,H=self.svgH)
        print('step=',step,'image H,W=',self.height,self.width,'SVG H,W=',self.svgH,self.svgW)
        
    def draw(self):
        r = self.step/2
        for i in range(0,self.svgH,self.step):
            for j in range(0,self.svgW,self.step):
                x = i+1/2*self.step 
                y = j+1/2*self.step 
                
                roi = self.image[i:i+self.step, j:j+self.step]
                #print(i,j,self.svgH,self.svgW,i+self.step,j+self.step)            
                color = randomColor3(np.mean(roi))
                if 1:
                    self.svg.draw(draw_circle(y,x,r,color=color))
                else:
                    self.svg.draw(draw_rect(y,x,self.step,self.step,color=color))
                
        self.svg.close()
    
def main():
    f = r'.\res\trump.jpg'
    d = r'.\images\trump.svg'
    SVGImageMask(f,d).draw()

if __name__=='__main__':
    main()         
 