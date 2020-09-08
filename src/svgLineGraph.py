#python3 Steven
import random 
import numpy as np
from svgFile import SVGFileV2
from svgBasic import *
from svgFunction import *

def drawlinePoints(svg,pts,stroke_width=0.5,color=None):
    for i in pts:
        x1,y1,x2,y2 = i
        x1 = x1.round(1)
        y1 = y1.round(1)
        x2 = x2.round(1)
        y2 = y2.round(1)
        svg.draw(draw_line(x1,y1,x2,y2, stroke_width=stroke_width, color = color or randomColor()))
        
def drawLineGrapic(svg):
    W,H = svg.svgSize()
    times=100
    len=0
    offsetX = W//2 #
    offsetY = 0 
    
    pts=[]
    for _ in range(times):
        len = len + 0.5        
        offsetY = offsetY + 0.5
        
        x1 = offsetX-len
        y1 = offsetY
        x2 = offsetX + len
        y2 = y1 
        pts.append((x1,y1,x2,y2))
        
    for _ in range(times):
        len = len - 0.5       
        offsetY = offsetY + 0.5
        pts.append((offsetX-len,offsetY,offsetX+len,offsetY))

    drawlinePoints(svg,pts)
    
def drawLineGrapic2(svg):
    W,H = svg.svgSize()
    len=0
    offsetX = W/4 #
    offsetY = 0 
    yInter = 0.5
    wStep = 0.5
    
    pts=[]
    while(offsetY < H/2):
        offsetY = offsetY + yInter
        if offsetY < H/4:
            len = len + wStep
        else:
            len = len - wStep
            if(len<0):
                break
        pts.append((offsetX-len,offsetY,offsetX + len,offsetY))
        
    offsetX = W*3/4
    offsetY = 0
    len = 0 
    while(offsetY < H/2):
        offsetY = offsetY + yInter
        if offsetY < H/4:
            len = len + wStep
        else:
            len = len - wStep
            if(len<0):
                break
        pts.append((offsetX-len,offsetY,offsetX + len,offsetY))
        
    offsetX = W/4 #
    offsetY = H/2
    len = 0
    while(offsetY < H):
        offsetY = offsetY + yInter
        if offsetY < H*3/4:
            len = len + wStep
        else:
            len = len - wStep
            if(len<0):
                break
        pts.append((offsetX-len,offsetY,offsetX + len,offsetY))
           
    offsetX = W*3/4 #
    offsetY = H/2
    len = 0
    while(offsetY < H):
        offsetY = offsetY + yInter
        if offsetY < H*3/4:
            len = len + wStep
        else:
            len = len - wStep
            if(len<0):
                break
        pts.append((offsetX-len,offsetY,offsetX + len,offsetY))
            
    drawlinePoints(svg,pts)

def drawTrianglePoints(svg,pt1,pt2,pt3):
    pts=[]
    pts.append((pt1[0],pt1[1],pt2[0],pt2[1])) #pt1,pt2
    pts.append((pt1[0],pt1[1],pt3[0],pt3[1])) #pt1,pt3
    pts.append((pt2[0],pt2[1],pt3[0],pt3[1])) #pt2,pt3
    
    drawlinePoints(svg,pts,stroke_width=0.1,color=randomColor())
    
def drawLsoscelesTrianglePoints(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    
    times = 40
    width = 0
    rotation = True
    for i in range(times):
        #width = width + 4
        width = 160
        
        x = [] #np.zeros((3,),dtype=float)
        y = [] #np.zeros((3,),dtype=float)
        
        # pt1 = (cx - width/2, cy + (width/2)*np.tan(np.pi/6))
        # pt2 = (cx + width/2, cy + (width/2)*np.tan(np.pi/6))
        # pt3 = (cx, cy - (width/2)*(np.tan(np.pi/3) - np.tan(np.pi/6)))
        x.append(cx - width/2)
        x.append(cx + width/2)
        x.append(cx)
        x = np.array(x)
        
        y.append(cy + (width/2)*np.tan(np.pi/6))
        y.append(cy + (width/2)*np.tan(np.pi/6))
        y.append(cy - (width/2)*(np.tan(np.pi/3) - np.tan(np.pi/6)))
        y = np.array(y)
        
        if rotation:
            #theta = i*2*np.pi/(times+1)
            theta = random.random()*2*np.pi
            x,y = rotationMatrixCenter(x,y,(cx,cy),theta)
                
        pt1 = (x[0],y[0])
        pt2 = (x[1],y[1])
        pt3 = (x[2],y[2])
        drawTrianglePoints(svg,pt1,pt2,pt3)
    

if __name__=='__main__':    
    file=r'.\images\lingGraphic.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H)
    #drawLineGrapic(svg)
    #drawLineGrapic2(svg)
    drawLsoscelesTrianglePoints(svg)
    svg.close()