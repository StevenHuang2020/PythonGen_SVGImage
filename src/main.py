#python3 Steven Scalable Vector Graphics(SVG)
#reference: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
#SVG: https://www.w3.org/Graphics/SVG/
import os
import numpy as np 
import random
from svgBasic import *
from svgFile import SVGFile
from svgImageMask import SVGImageMask
from svgSmile import SVGSmile

class drawArt:
    def __init__(self,svg=None):
        self.styles=['Line','DiagLine','Rectangle','Circle','Rings']
        self.svg = svg
        
    def DrawCircleByPt(self,pt1,pt2,pt3,pt4,circle=True):
        ptCenter = np.array([(pt1[0]+pt3[0])/2,(pt1[1]+pt3[1])/2])
        r = abs(ptCenter[0]-pt1[0])
        
        if circle:
            rings=4
            r = random.choice(range(1,rings))*r/rings
            self.svg.draw(draw_circle(ptCenter[0],ptCenter[1],r))
        else:
            for i in draw_circleRings(ptCenter[0],ptCenter[1],r):
                self.svg.draw(i)

    def DrawLineByPt(self,startPt,stopPt):
        if startPt[0]>stopPt[0]: #switch
            startPt = startPt + stopPt
            stopPt = startPt - stopPt
            startPt = startPt -stopPt
        self.svg.draw(draw_line(startPt[0],startPt[1],stopPt[0],stopPt[1]))

    def DrawRectangleByPt(self,startPt,stopPt):
        if startPt[0]>stopPt[0]: #switch
            startPt = startPt + stopPt
            stopPt = startPt - stopPt
            startPt = startPt -stopPt
        self.svg.draw(draw_rect(startPt[0],startPt[1],stopPt[0]-startPt[0],stopPt[1]-startPt[1]))
        
    def drawDiagLine(self,pt1,pt2,pt3,pt4,ptCenter,style,N):
        a=[0,1]
        if N == 1:
            if random.choice(a):
                self.DrawLineByPt(pt1,pt3)
            else:
                self.DrawLineByPt(pt2,pt4)
        
        self.plotArt(pt1, ptCenter, N-1,style=style)
        self.plotArt(pt2, ptCenter, N-1,style=style)
        self.plotArt(pt3, ptCenter, N-1,style=style)
        self.plotArt(pt4, ptCenter, N-1,style=style)
    
    def drawLine(self,pt1,pt2,pt3,pt4,ptCenter,style,N):
        a=[0,1]
        if N == 1:
            if random.choice(a):
                self.DrawLineByPt(pt1,pt2)
            if random.choice(a):
                self.DrawLineByPt(pt2,pt3)
            if random.choice(a):
                self.DrawLineByPt(pt3,pt4)
            if random.choice(a):
                self.DrawLineByPt(pt1,pt4)
        
        self.plotArt(pt1, ptCenter, N-1,style=style)
        self.plotArt(pt2, ptCenter, N-1,style=style)
        self.plotArt(pt3, ptCenter, N-1,style=style)
        self.plotArt(pt4, ptCenter, N-1,style=style)
            
    def drawRectangle(self,pt1,pt2,pt3,pt4,ptCenter,style,N):
        a=[0,1]
        if N == 1:
            #if random.choice(a):
            self.DrawRectangleByPt(pt1,pt3)
        
        self.plotArt(pt1, ptCenter, N-1,style=style)
        self.plotArt(np.array([ptCenter[0],pt2[1]]), np.array([pt2[0],ptCenter[1]]), N-1,style=style)
        self.plotArt(pt3, ptCenter, N-1,style=style)
        self.plotArt(np.array([pt4[0],ptCenter[1]]), np.array([ptCenter[0],pt4[1]]), N-1,style=style)
        
    def drawCircle(self,pt1,pt2,pt3,pt4,ptCenter,style,N,circle=True):
        a=[0,1]
        if N == 1:
            #if random.choice(a):
            self.DrawCircleByPt(pt1,pt2,pt3,pt4,circle=circle)
        
        self.plotArt(pt1, ptCenter, N-1,style=style)
        self.plotArt(np.array([ptCenter[0],pt2[1]]), np.array([pt2[0],ptCenter[1]]), N-1,style=style)
        self.plotArt(pt3, ptCenter, N-1,style=style)
        self.plotArt(np.array([pt4[0],ptCenter[1]]), np.array([ptCenter[0],pt4[1]]), N-1,style=style)

    def plotArt(self,startPt,stopPt,N,style):
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
            
            if style == self.styles[0]:
                self.drawLine(pt1,pt2,pt3,pt4,ptCenter,style,N)
            elif style == self.styles[1]:
                self.drawDiagLine(pt1,pt2,pt3,pt4,ptCenter,style,N)
            elif style == self.styles[2]:
                self.drawRectangle(pt1,pt2,pt3,pt4,ptCenter,style,N)
            elif style == self.styles[3]:
                self.drawCircle(pt1,pt2,pt3,pt4,ptCenter,style,N)
            elif style == self.styles[4]:
                self.drawCircle(pt1,pt2,pt3,pt4,ptCenter,style,N,circle=False)
            else:
                print('Not handled!')
        else:
            return 
    
def drawTest():
    file=r'.\images\test.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    svg.draw(draw_line(0,0,100,100))
    svg.close()
    
def drawArtSvg():
    styles = drawArt().styles
    
    recurse=[4,5]
    for N in recurse:
        for style in styles:
            fileName='art_' + style + '_' + str(N)+'.svg'
            file=r'.\images\\'+fileName
            H,W=200,200
            svg = SVGFile(file,W,H)
            draw = drawArt(svg)
            draw.plotArt(np.array([0,0]), np.array([W,H]), N=N, style=style)
            svg.close()
            
def GeFile():
    file = r'.\images\hi.txt'
    with open(file, 'r') as f:
        return f.readlines()
    
def insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def drawText():
    file=r'.\images\Hi.svg'
    H,W=200,1200
    #str='Hello'
    
    svg = SVGFile(file,W,H)
    if 0:
        y0 = 15
        for i in range(10):
            svg.draw(draw_text(0,y0,'.    Hello     World!        1'))
            y0 += 12
    else:
        strs = GeFile()
        y0 = 15
        h=12
        for i in strs:
            i = '.'.join(i)#insert(i,'.',0)
            print(i)
            svg.draw(draw_text(0,y0,i))
            y0+=h
    svg.close()
    
def maskImage():
    f = r'.\res\trumps.jpg'
    d = r'.\images\trump.svg'
    svg = SVGImageMask(f,d)
    svg.drawStep()
    svg.close()
    
def drawSmile():
    file=r'.\images\smile.svg'
    ridus = 100
    s = SVGSmile(file, ridus=100)
    s.draw()
    s.close()
   
def drawRandomPath():
    file=r'.\images\randomPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    svg.draw(add_style_path(stroke_width=0.5))
    times=1
    N=10
    r = 10
    cx,cy = 50,50
    
    for i in range(times):
        path='M 100 50 L '
        if 1:
            for i in range(N+1):
                rd = np.random.rand()
                x = (cx*np.cos(np.pi*2*i/N) + cx)*rd
                y = (cy*np.sin(np.pi*2*i/N) + cy)*rd
                x = x.round(1)
                y = y.round(1)
                path = path + ' ' + str(x) + ' ' + str(y)
            path = path + ' Z'
        else:    
            path='M 0 0 L '    
            ptX = np.random.randint(cx-r,cx+r, size=(N,)).round(1)
            ptY = np.sqrt(r**2-(ptX-cx)**2).round(1)
            print(ptX)
            print(ptY)

            for x,y in zip(ptX,ptY):
                path = path + ' ' + str(x) + ' ' + str(y)
            path = path + ' Z'    
            
            #path = 'M {} {} L {} {} {} {} {} {} Z'.format(startPt[0],startPt[1],\
                #cp1[0],cp1[1],cp2[0],cp2[1],stopPt[0],stopPt[1])
                
        #print(path)
        svg.draw(draw_Only_path(path)) 
        
    svg.close()
    
def drawHearCurve():
    def heart(x,offsetX=50,lam=4/5,offsetY=50,r=10,up=True): #heart equation: x**2+ (5*y/4 - sqrt(abs(x)))**2 = r**2
        #lam = 4/5 #4/5
        if up:
            a = np.sqrt(r**2 - (x-offsetX)**2)*1 + np.sqrt(abs(x-offsetX))
        else:
            a = np.sqrt(r**2 - (x-offsetX)**2)*(-1) + np.sqrt(abs(x-offsetX))
        return a*lam*(-1) + offsetY

    file=r'.\images\heartPath.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    
    offsetX = W//2
    offsetY = H//2
    
    svg.draw(add_style_path(stroke='red', stroke_width=0.5,fill='red'))
    
    N = 100
    r = 50
    lam = 4/5.5
    path = 'M %.1f %.1f L ' % (0+offsetX, (lam)*r*(-1)+offsetY)
    x = np.linspace(-r+offsetX, r+offsetX, N)
    y = heart(x,r=r,lam=lam,offsetX=offsetX,offsetY=offsetY)    #Up part points of heart curve, set sqrt value positive       
    xr = np.flip(x) #Down part points of heart curve, set sqrt value negative
    yr = heart(xr,r=r,lam=lam, offsetX=offsetX,offsetY=offsetY,up=False)
      
    x = np.concatenate((x, xr), axis=0)
    y = np.concatenate((y, yr), axis=0)
    print('x=',x)
    print('y=',y)
    
    for i,j in zip(x,y):
        path = path + ' ' + str(i.round(1)) + ' ' + str(j.round(1))
        
    print(path)
    svg.draw(draw_Only_path(path))
    svg.close()
    
    
def main():
    #drawTest()
    #drawArtSvg()
    #drawText()
    #maskImage()
    #drawSmile()
    #drawRandomPath()
    #drawHearCurve()
    pass
    
if __name__=='__main__':
    main()
    