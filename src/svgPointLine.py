#python3 Steven
from svgFile import *
from svgBasic import *
from svgFunction import *
from geoTransformation import *
from graph.graphPoints import GraphPoints
from svgLineGraph import drawlinePoints 
from graph.interPoints import GetLineSegInterPoint

def drawPointsCircle(svg,pts,r=2,color='black'):
    for pt in pts:
        svg.draw(draw_circle(pt[0],pt[1],radius=r,color=color))

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
        linePoints.append((pts[s][0],pts[s][1],pts[t][0],pts[t][1]))

    drawlinePoints(svg,linePoints,color=color)
    
    drawInterPointLines(svg, linePoints, r=1, color=color) #draw intersection points
    
def drawPointsLineGraphic2(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 200
    
    color1='green'
    color2 = 'yellow'
    
    #svg.draw(draw_rect(0,0,W,H,color='#808B96')) #background
    
    pts = getRandomPoints((N,2),min=2,max=W-2)
    
    pts1 = pts[:N//2]
    pts2 = pts[N//2:]
    drawPointsCircle(svg, pts1, color=color1)
    drawPointsCircle(svg, pts2, color=color2)
    
    linePoints = []
    for i in pts1:
        linePoints.append((0,0,i[0],i[1]))
    drawlinePoints(svg,linePoints,color=color1,stroke_width=0.2)
    
    linePoints = []
    for i in pts2:
        linePoints.append((i[0],i[1],W,H))
    drawlinePoints(svg,linePoints,color=color2,stroke_width=0.2)
    
def drawPointsLineGraphic3(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 100
    
    color1='green'
    color2 = 'yellow'
    
    pts = getRandomPoints((N,2),min=2,max=W-2)
    
    pts1 = pts[:N//2]
    pts2 = pts[N//2:]
    drawPointsCircle(svg, pts1, r=1, color=color1)
    drawPointsCircle(svg, pts2, r=1, color=color1)
    
    linePoints = []
    for pt1,pt2 in zip(pts1,pts2):
        linePoints.append((pt1[0],pt1[1],pt2[0],pt2[1]))
        
    drawlinePoints(svg,linePoints,color=color1,stroke_width=0.2)    
    drawInterPointLines(svg, linePoints, r=1, color=color1)
    
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

    
def drawPointLine():
    file = gImageOutputPath + r'\pointsLine.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawPointsLineGraphic(svg)
    drawPointsLineGraphic2(svg)
    #drawPointsLineGraphic3(svg)
    svg.close()
    
def main():
    drawPointLine()
    
if __name__=='__main__':    
    main()

