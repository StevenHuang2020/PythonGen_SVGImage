#python3 Steven
import random 
import numpy as np
from svgFile import *
from svgBasic import *
from common import gImageOutputPath

def randomContinueNumbers(x0=0,N=100):
    res = [x0]
    for _ in range(N):
        res.append(res[-1] + np.random.rand())
    return res

def random_walk(x,y, n=1,step=1):
    """Return coordinantes after n block random walk"""
    for _ in range(n):
        (dx, dy) = random.choice([(0,1*step),(0,-1*step),(1*step,0),(-1*step,0)]) #N,S,E,W
        x += dx
        y += dy
    return x,y

def drawRandomNumbersPath():
    file = gImageOutputPath + r'\randomNumberPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    times=100
    N=500
    xW = 5
    
    for _ in range(times):
        path='M 0 0 L '
    
        ptX = np.arange(N) + xW
        ptY = randomContinueNumbers(N=N)
        
        #print(ptX)
        #print(ptY)

        for x,y in zip(ptX,ptY):
            path = path + ' ' + str(clipFloat(x)) + ' ' + str(clipFloat(y))
        #path = path    
        svg.draw(draw_path(path,width=0.2,color=randomColor())) 
        
    svg.close()
    
def drawRandomWalkPath():
    file = gImageOutputPath + r'\randomWalkPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    times=1000
    cx,cy = W//2,H//2
    
    x = cx
    y = cy
    path = 'M %.1f %.1f L ' % (x, y)
    for _ in range(times):       
        x,y = random_walk(x,y,1,step=2)
        path = path + ' ' + str(clipFloat(x)) + ' ' + str(clipFloat(y))           
         
    svg.draw(draw_path(path,width=0.2))     
    svg.close()
    
if __name__=='__main__':    
    #drawRandomNumbersPath()
    drawRandomWalkPath()