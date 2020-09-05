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

def heartFuc(x,r=1,up=True):#heart equation: x**2+ (5*y/4 - sqrt(abs(x)))**2 = r**2
    if up:
        a = np.sqrt(r**2 - x**2)*1 + np.sqrt(abs(x))
    else:
        a = np.sqrt(r**2 - x**2)*(-1) + np.sqrt(abs(x))
    return a*4/5
    
def circleFuc(x,r=1,up=True):#circle equation: x**2+ y**2 = r**2
    if up:
        a = np.sqrt(r**2 - x**2)*1 
    else:
        a = np.sqrt(r**2 - x**2)*(-1)
    return a

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def getCirclePoints(r=1,N=10,func=heartFuc):
    x = np.linspace(-r, r, N)
    y = func(x,r=r)    #Up part points of curve, set sqrt value positive       
    xDown = np.flip(x) #Down part points of curve, set sqrt value negative
    yDown = func(xDown,r=r,up=False)
      
    #connect from start  
    x = np.concatenate((x, xDown), axis=0)
    y = np.concatenate((y, yDown), axis=0)
        
    if 0:#connect from random
        rand = np.random.randint(1, len(x),size=1)[0]
        x = np.concatenate((x[rand:], x[:rand]), axis=0)
        y = np.concatenate((y[rand:], y[:rand]), axis=0)
        
        #print('rand=',rand,N,len(x))
        # xL = x[:rand]
        # xR = x[rand:]
        # print(len(xL),len(xR))
        
        # x = np.concatenate((xR, xDown), axis=0)
        # x = np.concatenate((x, xL), axis=0)
        
        # yL = y[:rand]
        # yR = y[rand:]
        # y = np.concatenate((yR, yDown), axis=0)
        # y = np.concatenate((y, yL), axis=0)
    
    #print('x=',x)
    #print('y=',y)
    return x,y
    
def drawFuncSVG(svg, offsetX=0, offsetY=0,color=None):          
    N=500
    x = np.linspace(-100,100,N)
    
    fOffsetX = 50
    fOffsetY = 100
    ptX = x + offsetX + offsetX
    ptY = funcIdentity(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    fOffsetX = 50
    fOffsetY = 50
    ptX = x + offsetX + fOffsetX
    ptY = funcQuadratic(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    fOffsetX = 50
    fOffsetY = 50
    ptX = x + offsetX + fOffsetX
    ptY = funcSin(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptX = x + offsetX + fOffsetX
    ptY = funcCos(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptX = x + offsetX + fOffsetX
    ptY = normalDistribution(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    ptX = x + offsetX + fOffsetX
    ptY = softmaxFuc(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    ptX = x + offsetX + fOffsetX
    ptY = sigmoid(x)*-1 + offsetY + fOffsetY
    drawOneFuncSVG(svg,ptX,ptY,N=N,color=color) 
    
    ptX,ptY = getCirclePoints(r=10,N=10,func=circleFuc)
    ptX = ptX + offsetX + fOffsetX
    ptY = ptY + offsetY + fOffsetY
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