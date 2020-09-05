#python3 Steven
import random 
import numpy as np
from svgFile import *
from svgBasic import *
from svgFunction import *

def addNoise(x,y,alpha=2):
    x = x + np.random.randn(len(x))*alpha
    y = y + np.random.randn(len(y))*alpha
    return x,y
    
def drawOnePathcSVG(svg, ptX, ptY, onlyPath=True):     
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
    
def getCirclePtsSVG(svg, r=1, N=10, offsetX=50, offsetY=50, noise=True,onlyPath=True):          
    ptX,ptY = getCirclePoints(r=r,N=N,func=circleFuc)
    ptX = ptX + offsetX
    ptY = ptY + offsetY
    
    if noise:
        ptX,ptY = addNoise(ptX,ptY)
    return ptX,ptY


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
    r=1

    offsetX = 50 #W//2 #
    offsetY = H//2
    for _ in range(times):
        r = r + random.random()*2
        #r = r + random.normalvariate(mu=0,sigma=1)*8
        
        offsetX = offsetX + random.random()*5  #8
        #offsetX = offsetX + random.normalvariate(mu=0,sigma=1)*1
        
        #offsetY = offsetY + random.random()*1
        #offsetX = 50 + random.random()*10
        #offsetY = 50 + random.random()*2
        
        ptX,ptY = getCirclePtsSVG(svg, r=r, N=80, offsetX=offsetX, offsetY=offsetY, noise=True,onlyPath=onlyPath)
        drawOnePathcSVG(svg,ptX,ptY,onlyPath=onlyPath) 
     
    svg.close()

    
def drawRandomCirclePath():
    file=r'.\images\randomCirclePath.svg'
    H,W=200,200
    svg = SVGFile(file,W,H)

    styles=['circles','circle points','circle points random']
    
    onlyPath = False
    times=100
    r=2
    offsetX = W//2
    offsetY = H//2
    style=styles[1]
    
    if style == styles[0]:
        for _ in range(times):
            r = r + random.random()*8
            ptX,ptY = getCirclePtsSVG(svg, r=r, N=200, offsetX=offsetX, offsetY=offsetY, noise=False,onlyPath=onlyPath)
            drawOnePathcSVG(svg,ptX,ptY,onlyPath=onlyPath)
            
    elif style == styles[1]:
        times = 50
        for _ in range(times):
            r = r + random.random()*8
            ptX,ptY = getCirclePtsSVG(svg, r=r, N=200, offsetX=offsetX, offsetY=offsetY, noise=False,onlyPath=onlyPath)
            ptNumber = int(5*r)
            #ptX = np.random.choice(ptX, ptNumber)
            
            ptX = ptX.reshape((len(ptX),1))
            ptY = ptY.reshape((len(ptY),1))
            pts = np.concatenate((ptX, ptY), axis=1)
            #print(ptX.shape,pts.shape)

            ptsIndex = np.random.randint(len(pts), size=ptNumber)
            #print('ptsIndex=',ptsIndex,len(pts))
            pts = pts[ptsIndex,:]
            
            for i in pts:
                #print('i=',i)
                #ra = 0.5
                ra =  np.random.random()*(3-0.2) + 0.2
                svg.draw(draw_circle(i[0],i[1],radius=ra,color=randomColor()))
                
    svg.close()
    
if __name__=='__main__':    
    drawRandomPath()
    #drawRandomCirclePath()
    