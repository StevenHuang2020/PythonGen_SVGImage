#python3 Steven
import random 
import numpy as np
from svgFile import *
from svgBasic import *
from svgFunction import *

def addNoise(x,y,alpha=10):
    x = x + np.random.randn(len(x))*alpha
    y = y + np.random.randn(len(y))*alpha
    return x,y
    
def drawOnePathcSVG(svg, ptX,ptY, N=10, onlyPath=True):     
    x = ptX[0]
    y = ptY[0]
    path = 'M %.1f %.1f L ' % (x, y)     
    for x,y in zip(ptX,ptY):
        x = x.round(1)
        y = y.round(1)
        path = path + ' ' + str(x) + ' ' + str(y)
    path = path + 'z'
    
    if onlyPath:
        svg.draw(draw_Only_path(path)) 
    else:
        svg.draw(draw_path(path,width=1,color=randomColor())) 
    
def drawFuncSVG(svg, r=1, N=10, offsetX=50, offsetY=50, noise=True,onlyPath=True):          
    #x = np.linspace(-100,100,N)
    ptX,ptY = getCurvePoints(r=r,N=N,func=circleFuc)
    ptX = ptX + offsetX
    ptY = ptY + offsetY
    
    if noise:
        ptX,ptY = addNoise(ptX,ptY)
        
    drawOnePathcSVG(svg,ptX,ptY,N=N,onlyPath=onlyPath) 
    
def drawRandomPath():
    file=r'.\images\randomShapePath.svg'
    H,W=500,1000
    svg = SVGFile(file,W,H)
    
    singleColor=False
    if singleColor:
        onlyPath = True
        color='#33FFC9'
        svg.draw(add_style_path(stroke=color, stroke_width=1, fill='transparent'))
    else:
        onlyPath = False

    times=200
    r=2

    offsetX = 50 #W//2 #
    offsetY = H//2
    for _ in range(times):
        r = r + random.random()*2
        #r = r + random.normalvariate(mu=0,sigma=1)*4
        
        offsetX = offsetX + random.random()*6  #8
        #offsetX = offsetX + random.normalvariate(mu=0,sigma=1)*1
        
        #offsetY = offsetY + random.random()*1
        #offsetX = 50 + random.random()*10
        #offsetY = 50 + random.random()*2
        
        #drawFuncSVG(svg, r=r, offsetX=offsetX, offsetY=offsetY, N=10, noise=True) #N=random.randint(1,10)
        drawFuncSVG(svg, r=r, offsetX=offsetX, offsetY=offsetY, N=random.randint(5,10), noise=True,onlyPath=onlyPath)
        
    svg.close()

    
if __name__=='__main__':    
    drawRandomPath()
