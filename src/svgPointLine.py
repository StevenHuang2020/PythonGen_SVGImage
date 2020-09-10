#python3 Steven
from svgFile import *
from svgBasic import *
from svgFunction import *
from geoTransformation import *
from graph.graphPoints import GraphPoints
from svgLineGraph import drawlinePoints 

def drawPointsCircle(svg,pts,r=2,color='black'):
    for pt in pts:
        svg.draw(draw_circle(pt[0],pt[1],radius=r,color=color))

def drawPointsLineGraphic(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 100
    
    pts = getRandomPoints((N,2),min=2,max=W-2)
    drawPointsCircle(svg, pts)
    
    graph = GraphPoints(pts)
    #graph.show()
    
    conMatrix = graph.getConnectionMatrix(K=3,KNearst=4)
    #print('conMatrix=',conMatrix)
    linePoints = []
    for i in conMatrix:
        s,t =  i[0], i[1] #start stop point index
        if t == -1:
            continue
        linePoints.append((pts[s][0],pts[s][1],pts[t][0],pts[t][1]))

    drawlinePoints(svg,linePoints)
    
    
def drawPointsLineGraphic2(svg):
    W,H = svg.svgSize()
    cx,cy = W//2,H//2
    N = 200
    
    color1='green'
    color2 = 'yellow'
    
    svg.draw(draw_rect(0,0,W,H,color='#808B96')) #background
    
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
    
def drawPointLine():
    file = gImageOutputPath + r'\pointsLine.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawPointsLineGraphic(svg)
    drawPointsLineGraphic2(svg)
    svg.close()
    
def main():
    drawPointLine()
    
if __name__=='__main__':    
    main()

