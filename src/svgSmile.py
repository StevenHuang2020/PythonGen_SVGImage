import os
import numpy as np 
from svgFile import *
from svgBasic import *
from common import gImageOutputPath

def drawSmileSVG(svg, radius, offsetX=0, offsetY=0,color=None):      
    return drawSmileSVGNode(svg, node=None, radius=radius, offsetX=offsetX, offsetY=offsetY,color=color)
    
def drawSmileSVGNode(svg, node, radius, offsetX=0, offsetY=0,color=None):      
    x = radius + offsetX
    y = radius + offsetY
    color = color or '#FFC10E'
    svg.drawNode(node, draw_circle(x,y,radius,color=color))

    x = radius*0.67 + offsetX
    y = radius*0.66 + offsetY
    r = radius*0.16
    svg.drawNode(node, draw_circle(x,y,r,color='#333333')) #left eye
    
    x = 2*radius - x +  2*offsetX
    svg.drawNode(node, draw_circle(x,y,r,color='#333333')) #right eye
    
    startPt = [0.40*radius + offsetX, 1.05*radius + offsetY]
    stopPt = [2*radius - startPt[0] + 2*offsetX, startPt[1]]
    cp1 =  [0.6*radius + offsetX, 1.78*radius+offsetY]  #Bézier Curves control points
    cp2 =  [2*radius - cp1[0] + 2*offsetX, cp1[1]]  #Bézier Curves control points
    path = 'M {} {} C {} {}, {} {}, {} {}'.format(startPt[0],startPt[1],\
        cp1[0],cp1[1],cp2[0],cp2[1],stopPt[0],stopPt[1])
    
    color = 'black'
    lineWidth = 0.11*radius
    svg.drawNode(node, draw_path(path, width=lineWidth, color=color)) #mouth
        
    svg.drawNode(node, draw_circle(startPt[0], startPt[1], lineWidth/2, color=color))
    svg.drawNode(node, draw_circle(stopPt[0], stopPt[1], lineWidth/2, color=color))

def testSmile():
    file = gImageOutputPath + r'\smileC.svg'
    s = SVGFileV2(file,W=300,H=300)
    drawSmileSVG(s,radius=100,offsetX=20,offsetY=45)
    s.close()
    
def testSmile2():
    d = gImageOutputPath + r'\smileC2.svg'
    N = 6
    inter = 5
    offsetX=0
    offsetY=0
    r0 = 10
    
    totalW = N*(N-1)*r0 + N*inter + offsetX
    totalH = (N-1)*2*r0 + offsetY
    
    svg = SVGFileV2(d,W=totalW,H=totalH)
    #svg = SVGSmile(dstSvgfile=d,svgW=totalW,svgH=totalH)
    for i in range(1,N):
        r = i*r0
        drawSmileSVG(svg,ridus = r,offsetX=offsetX,offsetY=offsetY)
        offsetX += (2*r + inter)
        
    svg.close()
    
def testSmile3():
    d = gImageOutputPath + r'\smileC3.svg'
    H,W = 6,6
    inter = 5
    offsetX=0
    offsetY=0
    r0 = 20
    
    totalW = W*2*r0 + W*inter + offsetX
    totalH = H*2*r0 + H*inter + offsetY
    
    svg = SVGFileV2(d,W=totalW,H=totalH)
    for i in range(H):
        for j in range(W):
            r = r0
            offsetX = j*(2*r + inter)
            offsetY = i*(2*r + inter)
           
            #drawSmileSVG(svg,radius = r,offsetX=offsetX,offsetY=offsetY,color=randomColor())
            drawSmileSVG(svg,radius = r,offsetX=offsetX,offsetY=offsetY,color='#FFC10E')
              
    svg.close()
       
def main():
    #testSmile()
    #testSmile2()
    testSmile3()
    
if __name__=='__main__':
    main()         