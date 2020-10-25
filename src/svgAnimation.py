#python3 Steven 10/24/20 Auckland,NZ
#https://css-tricks.com/guide-svg-animations-smil/
import numpy as np
from svgBasic import *
from svgFile import *
from svgFunction import *
from common import gImageOutputPath

def addNodeAnitmation(svg, objectNode, animateDict):
    #animate = svg.draw(draw_tag('animate'))
    animate = svg.addChildNode(objectNode,'animate')  
    svg.setNodeAttriDict(animate, animateDict)
    
def createCircle(svg, x,y,r,color=None):
    id = 'circle_' + ranstr(4)
    color = color or randomColor()
    circle = svg.draw(draw_circle(x, y, r, color=color))
    svg.setNodeAttri(circle,'id',id)
    
    if 1: #rings
        svg.setNodeAttri(circle,'fill','none')
        svg.setNodeAttri(circle,'stroke-width', "2")
        svg.setNodeAttri(circle,'stroke', color)
    return id, circle

def circleInflation(svg, x, y, r, color=None, fromR=0, toR=0, durS=5, begin=None):
    x, y, r = clipFloat(x),clipFloat(y),clipFloat(r)
    fromR,toR = clipFloat(fromR),clipFloat(toR)
     
    id, circle = createCircle(svg, x,y,r,color)
         
    animateDict={}
    #animateDict['xlink:href'] = f'#{id}' 
    animateDict["{{{}}}".format(svg.xlink) + 'href'] = f'#{id}'
    animateDict['id'] = 'ani_' + id + '_' + ranstr(2)
    animateDict['fill'] = 'freeze'
    animateDict['attributeName'] = 'r' 
    animateDict['from'] = str(fromR) #'10'
    animateDict['to'] = str(toR) #'50' 
    animateDict['dur'] = str(durS) #str(random.randint(0,durS)) #'5'
    animateDict['begin'] = begin or str(random.randint(0,5)) + 's' #'0s' #'click' #
    animateDict["repeatCount"] = "indefinite" #"5"
    
    addNodeAnitmation(svg, circle, animateDict)
    return id, circle

def animCircleInflation(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    circleInflation(svg,cx,cy,r=10,fromR=10, toR=50,durS=3)
    
def animCircleInflation2(svg):
    H,W = svg.getSize()
    
    N=30 #total points
    offset = 10 #margin to border
    pts = getRandomPoints((N,2), min=offset, max=W-offset)
    #print(pts)
    
    color=None #"black" #None
    for pt in pts:
        r = random.randint(1, 6)
        circleInflation(svg, pt[0], pt[1], r=r, color=color, fromR=r, toR=r*5, durS=3)
        
def animCircleInflation3(svg):
    H,W = svg.getSize()
    
    blockSize = 20 #blocksize
    color = "black" #None #
    r0 = blockSize/2
    rList = np.linspace(1, r0*3/4, 20)
    for i in range(0, W, blockSize):
        for j in range(0, H, blockSize):
            x = i + r0
            y = j + r0
            r = random.choice(rList)
            circleInflation(svg, x, y, r=r, color=color, fromR=r, toR=r0*3/4, durS=random.randint(0,10))
        
def animCircleInflation4(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    N = 20 #total points
    r0 = 5
    r1 = 60
    
    offset = 10 #margin to border
    pts = getRandomPoints((N,2), min=offset, max=W-offset)
    
    color= None #"black"#
    for i in range(N):
        begin = str(i)+'s'
        #id, circle = circleInflation(svg, cx, cy, r=r0, color=color, fromR=r0, toR=r1, durS=4, begin=begin)
        id, circle = circleInflation(svg, pts[i][0], pts[i][1], r=r0, color=color, fromR=r0, toR=r1, durS=4, begin=begin)
        
        animateDict={}
        animateDict["{{{}}}".format(svg.xlink) + 'href'] = f'#{id}'
        animateDict['id'] = 'ani_' + id + '_' + ranstr(2)
        animateDict['attributeName'] = 'stroke-width' 
        animateDict['values'] = '0;2;4;2;1;0'
        animateDict['dur'] = '5s' #str(random.randint(0,durS)) #'5'
        animateDict['begin'] = begin #'0s'
        animateDict["repeatCount"] = "indefinite" #"5"
        addNodeAnitmation(svg, circle, animateDict)
        
def main():
    file = gImageOutputPath + r'\animation.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    
    #animCircleInflation(svg)
    #animCircleInflation2(svg)
    #animCircleInflation3(svg)
    animCircleInflation4(svg)
    svg.close()
    
if __name__ == '__main__':
    main()
