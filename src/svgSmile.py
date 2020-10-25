import os
import numpy as np 
from svgFile import *
from svgBasic import *
from common import gImageOutputPath

def drawSmileSVG(svg, ridus, offsetX=0, offsetY=0,color=None):      
    x = ridus + offsetX
    y = ridus + offsetY
    color = color or '#FFC10E'
    svg.draw(draw_circle(x,y,ridus,color=color))

    x = ridus*0.67 + offsetX
    y = ridus*0.66 + offsetY
    r = ridus*0.16
    svg.draw(draw_circle(x,y,r,color='#333333')) #left eye
    
    x = 2*ridus - x +  2*offsetX
    svg.draw(draw_circle(x,y,r,color='#333333')) #right eye
    
    startPt = [0.40*ridus + offsetX, 1.05*ridus + offsetY]
    stopPt = [2*ridus - startPt[0] + 2*offsetX, startPt[1]]
    cp1 =  [0.6*ridus + offsetX, 1.78*ridus+offsetY]  #Bézier Curves control points
    cp2 =  [2*ridus - cp1[0] + 2*offsetX, cp1[1]]  #Bézier Curves control points
    path = 'M {} {} C {} {}, {} {}, {} {}'.format(startPt[0],startPt[1],\
        cp1[0],cp1[1],cp2[0],cp2[1],stopPt[0],stopPt[1])
    
    color = 'black'
    lineWidth = 0.11*ridus
    svg.draw(draw_path(path, width=lineWidth, color=color)) #mouth
        
    svg.draw(draw_circle(startPt[0], startPt[1], lineWidth/2, color=color))
    svg.draw(draw_circle(stopPt[0], stopPt[1], lineWidth/2, color=color))
    
def testSmile():
    file = gImageOutputPath + r'\smileC.svg'
    s = SVGFileV2(file,W=300,H=300)
    drawSmileSVG(s,ridus=100,offsetX=20,offsetY=45)
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
           
            #drawSmileSVG(svg,ridus = r,offsetX=offsetX,offsetY=offsetY,color=randomColor())
            drawSmileSVG(svg,ridus = r,offsetX=offsetX,offsetY=offsetY,color='#FFC10E')
              
    svg.close()
       
def main():
    #testSmile()
    #testSmile2()
    testSmile3()
    
if __name__=='__main__':
    main()         