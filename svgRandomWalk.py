#python3 Steven
import random 
import numpy as np
from svgFile import *
from svgBasic import *

def randomContinueNumbers(x0=0,N=100):
    res = [x0]
    for i in range(N):
        res.append(res[-1] + np.random.rand())
    return res

def random_walk(x,y, n=1,step=1):
    """Return coordinantes after n block random walk"""
    for _ in range(n):
        (dx, dy) = random.choice([(0,1*step),(0,-1*step),(1*step,0),(-1*step,0)])
        x += dx
        y += dy
    return x,y

def drawRandomNumbersPath():
    file=r'.\images\randomNumberPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    times=100
    N=50
    xW = 5
    
    for i in range(times):
        path='M 0 0 L '
    
        ptX = np.arange(N) + xW
        ptY = randomContinueNumbers(N=N)
        
        print(ptX)
        print(ptY)

        for x,y in zip(ptX,ptY):
            path = path + ' ' + str(x) + ' ' + str(y)
        #path = path    
        svg.draw(draw_path(path,width=0.2,color=randomColor())) 
        
    svg.close()
    
def drawRandomWalkPath():
    file=r'.\images\randomWalkPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    times=1000
    N=50
    xW = 5
    cx,cy = W//2,H//2
    
    x = cx
    y = cy
    path = 'M %.1f %.1f L ' % (x, y)
    for i in range(times):       
        x,y = random_walk(x,y,1,step=2)
        path = path + ' ' + str(x) + ' ' + str(y)           
         
    svg.draw(draw_path(path,width=0.2))     
    svg.close()
    
if __name__=='__main__':    
    #drawRandomNumbersPath()
    drawRandomWalkPath()