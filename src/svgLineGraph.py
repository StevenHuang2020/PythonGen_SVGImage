#python3 Steven
import random 
import numpy as np
from scipy.linalg import solve
from svgFile import SVGFileV2
from svgBasic import *
from svgFunction import *
from geoTransformation import *
from svgPointLine import drawPloygon

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

def drawTrianglePoints(svg,pt1,pt2,pt3,color=None):
    pts=[]
    pts.append((pt1[0],pt1[1],pt2[0],pt2[1])) #pt1,pt2
    pts.append((pt1[0],pt1[1],pt3[0],pt3[1])) #pt1,pt3
    pts.append((pt2[0],pt2[1],pt3[0],pt3[1])) #pt2,pt3
    
    drawlinePoints(svg,pts,stroke_width=0.1,color=color or randomColor())
    
def drawTrianglePointsXY(svg,x,y):
    """x&y are (3,) vector, three points"""
    pt1 = (x[0],y[0])
    pt2 = (x[1],y[1])
    pt3 = (x[2],y[2])
    drawTrianglePoints(svg,pt1,pt2,pt3)
        
def drawLsoscelesTrianglePoints(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2

    times = 40
    width = 0
    rotation = True
    for i in range(times):
        #width = width + 4
        width = 160
        
        x = [] 
        y = [] 
        
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

        drawTrianglePointsXY(svg,x,y)


def getCenterPoint(p1, p2, p3):
    """get center point of three points"""
    #return get_outer_circle(p1,p2,p3)
    return get_inner_circle(p1,p2,p3)

def get_inner_circle(A, B, C):
    xa, ya = A[0], A[1]
    xb, yb = B[0], B[1]
    xc, yc = C[0], C[1]

    ka = (yb - ya) / (xb - xa) if xb != xa else None
    kb = (yc - yb) / (xc - xb) if xc != xb else None

    alpha = np.arctan(ka) if ka != None else np.pi / 2
    beta  = np.arctan(kb) if kb != None else np.pi / 2

    a = np.sqrt((xb - xc)**2 + (yb - yc)**2)
    b = np.sqrt((xa - xc)**2 + (ya - yc)**2)
    c = np.sqrt((xa - xb)**2 + (ya - yb)**2)

    ang_a = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    ang_b = np.arccos((a**2 + c**2 - b**2) / (2 * a * c))

    # slop
    k1 = np.tan(alpha + ang_a / 2)
    k2 = np.tan(beta + ang_b / 2)
    kv = np.tan(alpha + np.pi / 2)

    # circle center calculate
    y, x = solve([[1.0, -k1], [1.0, -k2]], [ya - k1 * xa, yb - k2 * xb])
    ym, xm = solve([[1.0, -ka], [1.0, -kv]], [ya - ka * xa, y - kv * x])
    r1 = np.sqrt((x - xm)**2 + (y - ym)**2)

    return(x, y, r1)

def get_outer_circle(px1, px2, px3):
    x1 = px1[0]
    y1 = px1[1]
    x2 = px2[0]
    y2 = px2[1]
    x3 = px3[0]
    y3 = px3[1]
    e = 2 * (x2 - x1)
    f = 2 * (y2 - y1)
    g = x2*x2 - x1*x1 + y2*y2 - y1*y1
    a = 2 * (x3 - x2)
    b = 2 * (y3 - y2)
    c = x3*x3 - x2*x2 + y3*y3 - y2*y2
    X = (g*b - c*f) / (e*b - a*f)
    Y = (a*g - c*e) / (a*f - b*e)
    R = np.sqrt((X-x1)*(X-x1)+(Y-y1)*(Y-y1))
    return X,Y,R

def drawRandomTrianglePoints(svg):
    """draw a random triangle and zoom this to seris"""
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    
    r = 10
    if 1:
        pts = getRandomProper3Points(min=r, max=W-r)
    else:
        pts = getRandomPoints((3,2), min=cx-r, max=cx+r)
        print(pts)
    
    #drawTrianglePoints(svg,pts[0],pts[1],pts[2])
    
    cx, cy, _ = getCenterPoint(pts[0],pts[1],pts[2])
    x = pts.T[0]
    y = pts.T[1]
    print('cx,cy=',cx,cy)
    
    #zoomPoint = (0,0)
    zoomPoint = (cx,cy)
    times = 30
    for z in np.linspace(0.1, 1.0, times):
        zx, zy = zoomMatrixCenter(x,y,zoomPoint,z)  
        drawTrianglePointsXY(svg, zx, zy)

def getCenterPointOf2Pts(pt1,pt2,ratio=1/2):
    x = (pt1[0] + pt2[0] )*ratio
    y = (pt1[1] + pt2[1] )*ratio
    return np.array([[x, y]])

def getTrianglesCenterPoints(points):
    #print('points,shape=',points,points.shape)
    pt1 = getCenterPointOf2Pts(points[0],points[1])
    pt2 = getCenterPointOf2Pts(points[1],points[2])
    pt3 = getCenterPointOf2Pts(points[2],points[0])
    
    pts = np.concatenate((pt1,pt2),axis=0)
    pts = np.concatenate((pts,pt3),axis=0)
    return pts
    
def drawRandomTriangles(svg):
    """draw a random triangle and inter center triangles"""
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    
    r = 10
    color=None #'black'
    pts = getRandomProper3Points(min=10, max=W-10)
    #print(pts)
    drawTrianglePoints(svg,pts[0],pts[1],pts[2],color=color)
    
    for _ in range(5):
        pts = getTrianglesCenterPoints(pts)
        drawTrianglePoints(svg,pts[0],pts[1],pts[2],color=color)
    
def getLinePointFromSlope(slope=1, p0=(20,0)):
    b = slope*p0[0] - p0[1]
    ptYaxis = [0,0]
    y = -slope*ptYaxis[0] + b
    ptYaxis[1] = y
    return ptYaxis

def drawAbstractLine(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 10
    
    #svg.draw(draw_rect(0,0,W,H,color='#808B96')) #background
    
    slope = 1.7
    #ptYaxis = getLinePointFromSlope(slope,(20,0))
    #print('ptYaxis=',ptYaxis)
    pts1 = getRandomPoints((N,),min=0,max=W).reshape((N,1))
    pts1 = np.append(pts1,np.zeros_like(pts1),axis=1)
    
    pts2 = None
    for i in pts1:
        pt = getLinePointFromSlope(slope,(i[0],i[1]))
        pt = np.array(pt).reshape(1,2)
        #print('pt=',pt)
        #pts2 = np.append(pts2, pt, axis=1)
        pts2 = np.concatenate((pts2, pt),axis=0) if pts2 is not None else pt
    
    #print('pts1=',pts1)
    #print('pts2=',pts2)
    
    linePoints = []
    widths = []
    for pt1,pt2 in zip(pts1,pts2):
        linePoints.append((pt1[0],pt1[1],pt2[0],pt2[1]))
        widths.append(random.choice([2,2,4,6,8,10]))
    #print(widths)
    drawlinePoints(svg,linePoints,color=None,stroke_widths=widths)

def drawArrowCircleLine(svg):
    def getPointCircle(r,theta):
        #return np.array([[r*np.cos(theta), r*np.sin(theta)]])
        return (r*np.cos(theta), r*np.sin(theta))
    
    def getTwinPoints(r,theta, sTheta=2*np.pi/80):
        pt1 =  getPointCircle(r,theta - sTheta/2)
        pt2 =  getPointCircle(r,theta + sTheta/2)
        return pt1,pt2
    
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 40
    R0 = 80
    rMin = 8
    rMax = 30
    theta = 0
    for i in range(1,N):
        theta = theta + 2*np.pi/(N-1)
        R = R0 + random.normalvariate(mu=0,sigma=1)*3
        r = random.choice(np.linspace(rMin,rMax,10))
        
        ptInner = getPointCircle(r,theta)
        sTheta = 2*np.pi/random.choice(range(80,200,2))
        ptOuter1, ptOuter2 = getTwinPoints(R,theta,sTheta=sTheta)
        
        x = [ptInner[0],ptOuter1[0],ptOuter2[0]]
        y = [ptInner[1],ptOuter1[1],ptOuter2[1]]
        
        x,y = translationMatrix(x,y,(cx,cy))
        #drawTrianglePoints(svg,(x[0],y[0]), (x[1],y[1]), (x[2],y[2]))
        drawPloygon(svg, [(x[0],y[0]), (x[1],y[1]), (x[2],y[2])], color='black')
        
def drawLineGraphic():
    file = gImageOutputPath + r'\lingGraphic.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawLineGrapic(svg)
    #drawLineGrapic2(svg)
    #drawLsoscelesTrianglePoints(svg)
    #drawRandomTrianglePoints(svg)
    #drawRandomTriangles(svg)
    #drawAbstractLine(svg)
    drawArrowCircleLine(svg)
    svg.close()
    
if __name__=='__main__':    
    drawLineGraphic()    
    #print(comb(4,3))