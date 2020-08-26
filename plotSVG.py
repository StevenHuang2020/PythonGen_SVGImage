#python3 Steven 08/25/2020
import matplotlib.pyplot as plt
import numpy as np 
import random
import matplotlib.patches as patches

gStyles=['Line','Diag Line','Rectangle','Circle']

def plotXY(x,y,color='k'):
    plt.plot(x,y,color=color)

def plotXYColor(x,y):
    plt.plot(x,y)  

def DrawPolygonByPt(pt1,pt2,pt3,pt4):
    ax = plt.gca()
    rect = patches.Polygon([pt1,pt2,pt3,pt4],color=(random.random(), random.random(), random.random())) 
    ax.add_patch(rect)

def DrawCircleByPt(pt1,pt2,pt3,pt4):
    ax = plt.gca()
    ptCenter = np.array([(pt1[0]+pt3[0])/2,(pt1[1]+pt3[1])/2])
    r = abs(ptCenter[0]-pt1[0])
    rect = patches.Circle(ptCenter,radius=r,color=(random.random(), random.random(), random.random())) 
    ax.add_patch(rect)

def DrawLineByPt(startPt,stopPt):
    if startPt[0]>stopPt[0]: #switch
        startPt = startPt + stopPt
        stopPt = startPt - stopPt
        startPt = startPt -stopPt
        
    plotXY([startPt[0],stopPt[0]],[startPt[1],stopPt[1]])

def DrawRectangleByPt(startPt,stopPt):
    if startPt[0]>stopPt[0]: #switch
        startPt = startPt + stopPt
        stopPt = startPt - stopPt
        startPt = startPt -stopPt
    
    ax = plt.gca()
    
    W = abs(stopPt[0]-startPt[0])
    H = abs(stopPt[1]-startPt[1])
    # Create a Rectangle patch
    rect = patches.Rectangle((startPt[0],startPt[1]), W, H, linewidth=1,color=(random.random(), random.random(), random.random())) # edgecolor=None, facecolor=None
    # Add the patch to the Axes
    ax.add_patch(rect)
    #plotXY([startPt[0],stopPt[0]],[startPt[1],stopPt[1]])
   
def drawDiagLine(pt1,pt2,pt3,pt4,ptCenter,style,N):
    a=[0,1]
    if N == 1:
        if random.choice(a):
            DrawLineByPt(pt1,pt3)
        else:
            DrawLineByPt(pt2,pt4)
    
    plotArt(pt1, ptCenter, N-1,style=style)
    plotArt(pt2, ptCenter, N-1,style=style)
    plotArt(pt3, ptCenter, N-1,style=style)
    plotArt(pt4, ptCenter, N-1,style=style)
  
def drawLine(pt1,pt2,pt3,pt4,ptCenter,style,N):
    a=[0,1]
    if N == 1:
        if random.choice(a):
            DrawLineByPt(pt1,pt2)
        if random.choice(a):
            DrawLineByPt(pt2,pt3)
        if random.choice(a):
            DrawLineByPt(pt3,pt4)
        if random.choice(a):
            DrawLineByPt(pt1,pt4)
    
    plotArt(pt1, ptCenter, N-1,style=style)
    plotArt(pt2, ptCenter, N-1,style=style)
    plotArt(pt3, ptCenter, N-1,style=style)
    plotArt(pt4, ptCenter, N-1,style=style)
          
def drawRectangle(pt1,pt2,pt3,pt4,ptCenter,style,N):
    a=[0,1]
    if N == 1:
        #if random.choice(a):
        DrawRectangleByPt(pt1,pt3)
    
    plotArt(pt1, ptCenter, N-1,style=style)
    plotArt(np.array([ptCenter[0],pt2[1]]), np.array([pt2[0],ptCenter[1]]), N-1,style=style)
    plotArt(pt3, ptCenter, N-1,style=style)
    plotArt(np.array([pt4[0],ptCenter[1]]), np.array([ptCenter[0],pt4[1]]), N-1,style=style)
    
def drawCircle(pt1,pt2,pt3,pt4,ptCenter,style,N):
    a=[0,1]
    if N == 1:
        #if random.choice(a):
        DrawCircleByPt(pt1,pt2,pt3,pt4)
    
    plotArt(pt1, ptCenter, N-1,style=style)
    plotArt(np.array([ptCenter[0],pt2[1]]), np.array([pt2[0],ptCenter[1]]), N-1,style=style)
    plotArt(pt3, ptCenter, N-1,style=style)
    plotArt(np.array([pt4[0],ptCenter[1]]), np.array([ptCenter[0],pt4[1]]), N-1,style=style)

def plotArt(startPt,stopPt,N,style):
    if N>0:                        
        if startPt[0]>stopPt[0]: #switch
            startPt = startPt + stopPt
            stopPt = startPt - stopPt
            startPt = startPt -stopPt
            
        pt1 = startPt
        pt2 = np.array([stopPt[0],startPt[1]])
        pt3 = stopPt
        pt4 = np.array([startPt[0],stopPt[1]])
        ptCenter = np.array([(startPt[0]+stopPt[0])/2,(startPt[1]+stopPt[1])/2])
        
        if style == gStyles[0]:
            drawLine(pt1,pt2,pt3,pt4,ptCenter,style,N)
        elif style == gStyles[1]:
            drawDiagLine(pt1,pt2,pt3,pt4,ptCenter,style,N)
        elif style == gStyles[2]:
            drawRectangle(pt1,pt2,pt3,pt4,ptCenter,style,N)
        elif style == gStyles[3]:
            drawCircle(pt1,pt2,pt3,pt4,ptCenter,style,N)
        else:
            print('Not handled!')
    else:
        return 
    
def plotRecursiveArt():
    H,W = 200,200
    for i in range(len(gStyles)):
        plt.clf()
        plotArt(np.array([0,0]), np.array([W,H]), N=5, style=gStyles[i])
        plt.axis('square')
        plt.savefig(r'.\images\\' + 'gStyles'+str(i)+"_test.svg", format="svg")
        plt.show()
    
def plotQuadrangle():
    H,W = 200,200
    N=20
    x = range(0,W,W//N)
    y = np.zeros_like(x) + H
    
    xi = range(0,W,N)
    
    #plt.plot(x,y)
    yPre = y
    for i in range(1, 20):
        y1 = H - np.random.randn(W//N) - H*i/20
        print('y=',len(y),y)
        print('y1=',len(y1),y1)
        print('xi=',len(xi),xi)
        #plt.plot(xi,y1)
                
        for j in range(1,W//N):
            pt1=[N*(j-1),yPre[j-1]]
            pt2=[N*j,yPre[j]]
            pt3=[N*j,y1[j]]
            pt4=[N*(j-1),y1[j-1]]
            DrawPolygonByPt(pt1,pt2,pt3,pt4)
        yPre = y1
            
    plt.axis('square')
    plt.ylim(0,H+10)
    plt.show()
    
def main():
    plotRecursiveArt()
    #plotQuadrangle()
    
if __name__ == "__main__":
    main()