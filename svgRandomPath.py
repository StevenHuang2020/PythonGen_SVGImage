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
    
def drawOnePathcSVG(svg, ptX, ptY, width=1,onlyPath=True):     
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
        svg.draw(draw_path(path,width=width,color=randomColor())) 
    
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
    
def rotationMatrix(x,y,theta):
    #a = np.concatenate((x.T, y.T),axis=0)
    a = np.stack(([x,y]))
    #print(a)

    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c,-s],[s,c]])
    res = np.dot(R, a)
    #return np.dot(R, a)
    return res[0][:],res[1][:]

def rotationMatrixCenter(x,y,center,theta):
    #a = np.concatenate((x.T, y.T),axis=0)
    a = np.stack(([x,y]))
    #print(a)

    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c,-s],[s,c]])
    res = np.dot(R, a)
    #return np.dot(R, a)
    newX = center[0] + (x-center[0])*c - (y-center[1])*s
    newY = center[1] + (x-center[0])*s + (y-center[1])*c
    return newX,newY

def getRectanglePtsSVG(svg, w,h, N=10, noise=True,onlyPath=True):          
    ptX,ptY, center = getRectanglePoints(w=w,h=h,N=N)
    ptX = ptX
    ptY = ptY
    
    if noise:
        ptX,ptY = addNoise(ptX,ptY,alpha=0.6)
    return ptX,ptY,center

def drawRandomRectanglePath():
    file=r'.\images\randomRectanglePath.svg'
    H,W=200,200
    svg = SVGFile(file,W,H)

    styles=['rectangle','rectangle roation','rotataion Center']
    
    onlyPath = False
    times=80
    w=2
    h=w
    offsetX = 5
    offsetY = 5
    style=styles[2]
    
    if style == styles[0]:
        for _ in range(times):
            w = w + random.random()*4
            h = w
            ptX,ptY,_ = getRectanglePtsSVG(svg, w,h, N=20, noise=True,onlyPath=onlyPath)
            ptX = ptX + offsetX
            ptY = ptY + offsetY
            drawOnePathcSVG(svg,ptX,ptY,onlyPath=onlyPath)
            
    elif style == styles[1]:
        times=150
        offsetX = W//2
        offsetY = H//2
        theta = 0
        for _ in range(times):
            w = w + random.random()*1
            h = w
            ptX,ptY,center = getRectanglePtsSVG(svg, w,h, N=20, noise=False,onlyPath=onlyPath)
        
            ptX,ptY = rotationMatrix(ptX,ptY,theta)
            theta = theta + 2*np.pi/(times-1)
            
            ptX = ptX + offsetX
            ptY = ptY + offsetY
            drawOnePathcSVG(svg,ptX,ptY,width=0.5,onlyPath=onlyPath)
    elif style == styles[2]:
        times=180
        offsetX = 20 #W//2
        offsetY = 20 #H//2
        theta = 0
        for _ in range(times):
            offsetX = offsetX + random.random()*1  #8
            w = w + random.random()*1
            h = w
            ptX,ptY,center = getRectanglePtsSVG(svg, w,h, N=20, noise=False,onlyPath=onlyPath)
        
            ptX,ptY = rotationMatrixCenter(ptX,ptY,center, theta)
            theta = theta + 2*np.pi/(times-1)
            
            ptX = ptX + offsetX
            ptY = ptY + offsetY
            drawOnePathcSVG(svg,ptX,ptY,width=0.5,onlyPath=onlyPath)
               
    print(w,H)         
    svg.close()
    
if __name__=='__main__':    
    #drawRandomPath()
    #drawRandomCirclePath()
    drawRandomRectanglePath()
    