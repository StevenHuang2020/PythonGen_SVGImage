#python3 Steven 10/24/20 Auckland,NZ
#https://developer.mozilla.org/en-US/docs/Web/SVG
#https://css-tricks.com/guide-svg-animations-smil/
import numpy as np
from svgBasic import *
from svgFile import *
from svgFunction import *
from common import gImageOutputPath
from geoTransformation import *

def addNodeAnitmation(svg, objectNode, animateDict, elementName='animate'):
    #animate = svg.draw(draw_tag('animate'))
    animate = svg.addChildNode(objectNode, elementName)  
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
       
    color= "black"#None #
    for i in range(N):
        begin = str(i)+'s'
        circleInflation(svg, cx, cy, r=r0, color=color, fromR=r0, toR=r1, durS=4, begin=begin)
        
def animCircleInflation5(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    N = 20 #total points
    r0 = 5
    r1 = 60
    
    offset = 10 #margin to border
    pts = getRandomPoints((N,2), min=offset, max=W-offset)
    
    color= None #"black"#
    rList = np.linspace(1, r1/2, 20)
    for i in range(N):
        begin = str(random.randint(1,4)) + 's' #str(i)+'s' #'0s'
        dur = random.randint(3,6)
        r = random.choice(rList)
        id, circle = circleInflation(svg, pts[i][0], pts[i][1], r=r, color=color, fromR=r0, toR=r1, durS=dur, begin=begin)
        
        animateDict={}
        animateDict["{{{}}}".format(svg.xlink) + 'href'] = f'#{id}'
        animateDict['id'] = 'ani_' + id + '_' + ranstr(2)
        animateDict['attributeName'] = 'stroke-width' 
        animateDict['values'] = '0;2;4;2;1;0'
        animateDict['dur'] = '5s' #str(random.randint(0,durS)) #'5'
        animateDict['begin'] = begin #'0s'
        animateDict["repeatCount"] = "indefinite" #"5"
        addNodeAnitmation(svg, circle, animateDict)
       
def drawNodeShape(svg, node):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    r = 50
    x0 = [cx, cx+2*r, cx+r]
    y0 = [cy, cy, cy-r*np.tan(np.pi/6)]
    
    times = 8
    theta = 0
    for i in range(times):
        theta = i*(2*np.pi/times)
        x,y = rotationMatrixCenter(x0,y0,(cx,cy),theta)
        drawPloygonNode(svg, node, [(x[0],y[0]), (x[1],y[1]), (x[2],y[2])], color=None) #color='black'

def drawPloygonNode(svg, node, pts, color=None):
    #print('pts',pts)
    points=[]
    for i in pts:
        points.append(str(clipFloat(i[0])) + ',' + str(clipFloat(i[1])) + ' ')
    points = ''.join(points)
    svg.drawNode(node, draw_polygon(points,stroke_width=0.5,color=color or randomColor()))
          
def anim_Windmill(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    
    g = svg.draw(draw_tag('g'))
    svg.setNodeAttri(g,'opacity', '1.0')
    drawNodeShape(svg, g)
    
    animateTransDict={}
    animateTransDict['attributeName'] = 'transform'
    animateTransDict['attributeType'] = 'xml'
    animateTransDict['type'] = 'rotate' 
    animateTransDict['from'] = f'0 {cx} {cy}'
    animateTransDict['to'] = f'360 {cx} {cy}'
    animateTransDict['dur'] = '5s'
    animateTransDict["repeatCount"] = "indefinite" #"5"
    
    addNodeAnitmation(svg, g, animateTransDict,elementName='animateTransform')
    
def drawAny(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    svg.setTitle('draw anything only use draw_any()')

    g = svg.draw(draw_any('g', opacity=1.0))
    #anyNode = svg.drawNode(g, draw_any('test','222', a=10, b="4",c='red',xml='www.ss'))
    svg.drawNode(g, draw_any('test','hello'))
    
    anyDict={}
    anyDict['test'] = 1
    anyDict['xml'] = 'www.ggg'
    anyDict['a'] = 'aaaaa anything else'
    anyDict['b'] = 'red black xxxxxxxxxxxxxxxxx anything you want'
    svg.drawNode(g, draw_any('test2', **anyDict))
    svg.drawNode(g, draw_any('hello', **anyDict))
    svg.drawNode(g, draw_any('anything', **anyDict))
    
    for i in range(20):
        anyDict={}
        anyDict['cx'] = cx
        anyDict['cy'] = cy
        anyDict['r'] = '5'
        anyDict['stroke'] = '#80ff00'
        anyDict['stroke-width'] = '2'
        anyDict['fill'] = 'none'
        
        circle = svg.drawNode(g, draw_any('circle', **anyDict))
        #'from' is a key word of python for import libs, but here last resort change parameter 
        # from(attribute of animate element for svg) to 'From' to avoid conflict.
        svg.drawNode(circle, draw_any('animate', fill='freeze', attributeName='r', From="5", to="80", dur="4s", begin=str(i), repeatCount="indefinite"))
        
        anyDict={}
        anyDict['fill'] = 'freeze'
        anyDict['attributeName'] = 'fill'
        anyDict['from'] = '#ff0000'
        anyDict['to'] = '#00ff40'
        anyDict['dur'] = '6s'
        anyDict['begin'] = '0s'
        anyDict['repeatCount'] = 'indefinite'
        #svg.drawNode(circle, draw_any('animate', **anyDict))
        
        anyDict['attributeName'] = 'stroke-width'
        anyDict['values'] = '1;2;3;2;1'
        anyDict.pop("from", None)
        anyDict.pop("to", None)
        svg.drawNode(circle, draw_any('animate', **anyDict))
        
        anyDict['attributeName'] = 'stroke'
        anyDict['from'] = '#80ff00'
        anyDict['to'] = '#0000ff'
        anyDict['begin'] = '1s'
        anyDict.pop("values", None)
        svg.drawNode(circle, draw_any('animate', **anyDict))
    
    
def main():
    file = gImageOutputPath + r'\animation.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    
    #animCircleInflation(svg)
    #animCircleInflation2(svg)
    #animCircleInflation3(svg)
    #animCircleInflation4(svg)
    #animCircleInflation5(svg)
    #anim_Windmill(svg)
    drawAny(svg)
    svg.close()
    
if __name__ == '__main__':
    main()
