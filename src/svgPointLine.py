#python3 Steven
from svgFile import *
from svgBasic import *
from svgFunction import *
from geoTransformation import *
from graph.graphPoints import GraphPoints


def drawPointsCircle(svg,pts,r=2,color='black'):
    for pt in pts:
        svg.draw(draw_circle(pt[0],pt[1],radius=r,color=color))
        
def drawPointsLine(svg,pts,stroke_width=2,color='black'):
    for pt in pts:
        x1,y1,x2,y2 = pt
        x1 = clipFloat(x1)
        y1 = clipFloat(y1)
        x2 = clipFloat(x2)
        y2 = clipFloat(y2)
        svg.draw(draw_line(x1,y1,x2,y2, stroke_width=stroke_width, color = color or randomColor()))
        
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

    drawPointsLine(svg,linePoints)
    
    
def drawPointLine():
    file = gImageOutputPath + r'\pointsLine.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    drawPointsLineGraphic(svg)
    svg.close()
    
def main():
    drawPointLine()
    
if __name__=='__main__':    
    main()

