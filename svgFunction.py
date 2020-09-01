import os
import numpy as np 
from svgFile import SVGFile
from svgBasic import *
#plot function to svg

def funcIdentity(x):
    return x #y=x

def funcQuadratic(x):
    return x**2

def funcSin(x):
    return np.sin(x)

def funcCos(x):
    return np.cos(x)

def normalDistribution(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5*x**2)
    
def softmaxFuc(x):
    softmax = np.exp(x)/np.sum(np.exp(x))
    #print(softmax)
    #print(np.sum(softmax))
    return softmax

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def drawFuncSVG(svg, offsetX=0, offsetY=0,color=None):          
    N=500
    x = np.linspace(-100,100,N)
    ptX = x + offsetX
    ptY = funcIdentity(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptY = funcQuadratic(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptY = funcSin(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptY = funcCos(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptY = normalDistribution(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    ptY = softmaxFuc(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    ptY = sigmoid(x)*-1 + offsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
def drawOneFuncSVG(svg, ptX,ptY, N=10, color=None):     
    x = ptX[0]
    y = ptY[0]
    path = 'M %.1f %.1f L ' % (x, y)     
    for x,y in zip(ptX,ptY):
        x = x.round(1)
        y = y.round(1)
        path = path + ' ' + str(x) + ' ' + str(y)
 
    svg.draw(draw_path(path,width=0.2,color=color or randomColor())) 
    
class SVGFunction:
    def __init__(self, dstSvgfile=None, svgW=None,svgH=None):
        self.svgW = svgW
        self.svgH = svgH
        
        if dstSvgfile:
            self.svg = SVGFile(dstSvgfile,W=self.svgW,H=self.svgH)
            print('dstSvgfile=',dstSvgfile,'SVG H,W=',self.svgH,self.svgW)
        
    def draw(self, offsetX=0, offsetY=0,color=None):
        return drawFuncSVG(self.svg, offsetX=offsetX, offsetY=offsetY,color=color)

    def close(self):
        self.svg.close()
    
def testFunc():
    d = r'.\images\func.svg'
    s = SVGFunction(dstSvgfile=d,svgW=100,svgH=100)
    s.draw(offsetX=10,offsetY=10)
    s.close()
    
def main():
    testFunc()
    
if __name__=='__main__':
    main()         