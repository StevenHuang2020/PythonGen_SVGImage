#python3 Steven
from svgFile import *
from svgBasic import *
from svgFunction import *
from geoTransformation import *
from graph.graphPoints import GraphPoints
from graph.interPoints import GetLineSegInterPoint

def drawlinePoints(svg,pts,stroke_width=0.5,color=None,stroke_widths=None):
    for i,pt in enumerate(pts):
        x1,y1,x2,y2 = pt
        x1 = clipFloat(x1)
        y1 = clipFloat(y1)
        x2 = clipFloat(x2)
        y2 = clipFloat(y2)
        if stroke_widths:
            stroke_width = stroke_widths[i]
        svg.draw(draw_line(x1,y1,x2,y2, stroke_width=stroke_width, color = color or randomColor()))        
    
def drawPointsCircle(svg,pts,r=2,color='black'):
    for pt in pts:
        x = clipFloat(pt[0])
        y = clipFloat(pt[1])
        svg.draw(draw_circle(x,y,radius=r,color=color))

def drawPointsLineGraphic(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 50
    
    color = 'black'
    pts = getRandomPoints((N,2),min=2,max=W-2)
    drawPointsCircle(svg, pts,r=1)
    
    graph = GraphPoints(pts)
    #graph.show()
    
    #conMatrix = graph.getConnectionMatrix(K=3,KNearst=4) #style1
    conMatrix = graph.getConnectionMatrix2(KNearst=6) #style2
    #print('conMatrix=',conMatrix)
    linePoints = []
    for i in conMatrix:
        s,t =  i[0], i[1] #start stop point index
        if t == -1:
            continue
        
        conect = (pts[s][0],pts[s][1],pts[t][0],pts[t][1])
        linePoints.append(conect)

    drawlinePoints(svg,linePoints,color=color)
    drawInterPointLines(svg, linePoints, r=1, color=color) #draw intersection points
    
def drawPointsLineGraphic2(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 200
    
    color1='green'
    color2 = '#C70039'
    
    #svg.draw(draw_rect(0,0,W,H,color='#808B96')) #background
    pts = getRandomPoints((N,2),min=2,max=W-2)
    
    pts1 = pts[:N//2]
    pts2 = pts[N//2:]
    drawPointsCircle(svg, pts1, color=color1)
    drawPointsCircle(svg, pts2, color=color2)
        
    linePoints = [(0,0,i[0],i[1]) for i in pts1]
    drawlinePoints(svg,linePoints,color=color1,stroke_width=0.2)
        
    linePoints = [(i[0],i[1],W,H) for i in pts2]
    drawlinePoints(svg,linePoints,color=color2,stroke_width=0.2)

def drawPointsLineGraphic3(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 100
    color1='green'
    #color2 = 'yellow'
    
    pts = getRandomPoints((N,2),min=2,max=W-2)
    
    pts1 = pts[:N//2]
    pts2 = pts[N//2:]
    drawPointsCircle(svg, pts1, r=1, color=color1)
    drawPointsCircle(svg, pts2, r=1, color=color1)
    
    linePoints = [(pt1[0],pt1[1],pt2[0],pt2[1]) for pt1,pt2 in zip(pts1,pts2)]
    
    drawlinePoints(svg,linePoints,color=color1,stroke_width=0.2)    
    drawInterPointLines(svg, linePoints, r=1, color=color1)
    
def drawPointsLineGraphic4(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 300
    r0 = 80
    color='#48C9B0' #'green'
    
    offsetX = cx
    offsetY=cy
    linePoints = []
    theta = 0
    strokeWidths = []
    for i in range(N):
        r = r0 + random.normalvariate(mu=0,sigma=1)*4
        theta = theta + 2*np.pi/(N-1) + random.normalvariate(mu=0,sigma=1)*.01
        x = r*np.cos(theta) + offsetX
        y = r*np.sin(theta) + offsetY
        linePoints.append((offsetX,offsetY,x,y))
        strokeWidths.append(random.choice([0.2,0.3,0.8,1.0,1.5]))
        
    drawlinePoints(svg,linePoints,color=color,stroke_widths=strokeWidths)
    
def drawInterPointLines(svg,linePoints,r=1,color=None):
    for line in linePoints:
        for i in linePoints:
            if line == i:
                continue
            
            #print('line=',line)
            #print('i=',i)
            
            line1 = np.array(list(line)).reshape((2,2))
            line2 = np.array(list(i)).reshape((2,2))
            #print('line1=',line1)
            #print('line2=',line2)
            ptInter = GetLineSegInterPoint(line1,line2).interPoint
            if ptInter:
                #print('ptInter=',ptInter)
                drawPointsCircle(svg, [ptInter], r=1, color=color)#r=3, color='red'

def drawPointsLineGraphic5(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 10
    
    color = 'black'
    pts = getRandomPoints((N,2),min=2,max=W-2)
    drawPointsCircle(svg, pts,r=1)
    
    graph = GraphPoints(pts)
    #graph.show()
    
    conMatrix = graph.getConnectionMatrix2(KNearst=3)
    print('conMatrix=',conMatrix)
    # for i,pt in enumerate(pts):
    #     #print(i,pt, conMatrix[i])
    #     ptsTriangle=[]
    #     ptsTriangle.append(pts[i])
    #     ptsTriangle.append(pts[conMatrix[i][0]])
    #     ptsTriangle.append(pts[conMatrix[i][1]])
        
    #     color = None #randomColor3(random.choice(range(N)), N=10)
    #     drawPloygon(svg,ptsTriangle,color=color)

    linePoints = []
    for i in conMatrix:
        s,t =  i[0], i[1] #start stop point index
        if t == -1:
            continue
        linePoints.append((pts[s][0],pts[s][1],pts[t][0],pts[t][1]))
        
    drawlinePoints(svg,linePoints,color=color)

def drawPloygon(svg, pts,color=None):
    #print('pts',pts)
    points=[]
    for i in pts:
        points.append(str(clipFloat(i[0])) + ',' + str(clipFloat(i[1])) + ' ')
    points = ''.join(points)
    svg.draw(draw_polygon(points,stroke_width=0.5,color=color or randomColor()))
    
def drawPointsLineGraphic6(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 50
    
    color = 'black'
    pts = getRandomPoints((N,2),min=2,max=W-2)
    drawPointsCircle(svg, pts,r=1)
    
    graph = GraphPoints(pts)
    #graph.show()
    
    #conMatrix = graph.getAllConnectionMatrix()
    conMatrix = graph.getConnectionMatrix2(KNearst=4)
    print('conMatrix=',conMatrix)
    linePoints = []
    for i in conMatrix:
        s,t =  i[0], i[1] #start stop point index
        if t == -1:
            continue
        
        conect = (pts[s][0],pts[s][1],pts[t][0],pts[t][1])
        if not IsIntersectionWithAlreayLines(conect,linePoints):
            linePoints.append(conect)
    
    drawlinePoints(svg,linePoints,color=color)

def IsIntersectionWithAlreayLines(conect,linePoints):
    def getLineFrom2Pts(connect):
        return np.array(list(connect)).reshape((2,2))

    line1 = getLineFrom2Pts(conect)
    for i in linePoints:
        line2 = getLineFrom2Pts(i)
        if GetLineSegInterPoint(line1,line2).interPoint:
            return True
    return False
    
def drawPointsLineGraphic7(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2

    r = 50
    x0 = [cx, cx+2*r, cx+r]
    y0 = [cy, cy, cy-r*np.tan(np.pi/6)]
    
    times = 8
    theta = 0
    for i in range(times):
        theta = i*(2*np.pi/times)
        x,y = rotationMatrixCenter(x0,y0,(cx,cy),theta)
        drawPloygon(svg, [(x[0],y[0]), (x[1],y[1]), (x[2],y[2])], color='black')
    
def drawPointsLineGraphic8(svg): #Neuron network
    def getNumberYs(H,N=3):
        offsetY = 190/N
        #hInter = (H-2*offsetY)/(N-1)
        if N == 1:
            return [H/2]
        else:
            return np.linspace(offsetY, H-offsetY,N)
    
    W,H = svg.svgSize()
    cx,cy = W//2,H//2

    layerNumbers=[8,6,6,4]
    ptsLayers = []
    
    inter = 52
    x0 = 15
    for i in range(len(layerNumbers)):
        #x = x0 + i*inter
        N = layerNumbers[i]
        xs = np.zeros((N,)) + x0 + i*inter
        ys = getNumberYs(H,N)
        #print('xs=', len(xs), xs)
        #print('ys=', len(ys), ys)
        
        ptLayer = np.stack(([xs,ys])).T 
        #print('ptLayer=',ptLayer)
        ptsLayers.append(ptLayer)
        
    #print('ptsLayers=',ptsLayers)  
    for i,layPts in enumerate(ptsLayers):
        x = layPts[0][0] - 15
        y = layPts[0][1] - 8
        #print(x,y)
        svg.draw(draw_text(x,y,'layer'+str(i)))
        drawPointsCircle(svg, layPts,r=3,color = randomColor())
    
    for i in range(len(ptsLayers)-1):
        layerPtsPre = ptsLayers[i]
        layerPts = ptsLayers[i+1]
        #print('layerPtsPre=',layerPtsPre)
        #print('layerPts=',layerPts)
        
        linePoints = []
        for pre in layerPtsPre:
            for cur in layerPts:
                #print('pre,cur=',pre,cur)
                conect = (pre[0],pre[1],cur[0],cur[1])
                linePoints.append(conect)

        drawlinePoints(svg,linePoints,color='black')
    
     
def drawPointLine():
    file = gImageOutputPath + r'\pointsLine.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawPointsLineGraphic(svg)
    #drawPointsLineGraphic2(svg)
    #drawPointsLineGraphic3(svg)
    #drawPointsLineGraphic4(svg)
    #drawPointsLineGraphic5(svg)
    #drawPointsLineGraphic6(svg)
    #drawPointsLineGraphic7(svg)
    drawPointsLineGraphic8(svg)
    svg.close()
    
def main():
    drawPointLine()
    
if __name__=='__main__':    
    main()
