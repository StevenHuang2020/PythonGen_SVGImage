#python3 Steven 10/24/20 Auckland,NZ
#https://css-tricks.com/guide-svg-animations-smil/
from svgBasic import *
from svgFile import *
from svgFunction import *

def circleInfalation(svg, x, y, r, color=None, fromR=0, toR=0, durS=5):
    x,y, r = clipFloat(x),clipFloat(y),clipFloat(r)
    circle = svg.draw(draw_circle(x, y, r, color=color or randomColor()))
    id = 'circle_' + ranstr(4)
    svg.setNodeAttri(circle,'id',id)
    if 0:
        animate = svg.draw(draw_tag('animate'))
    else:
        animate = svg.addChildNode(circle,'animate')  
          
    animateDict={}
    #animateDict['xlink:href'] = f'#{id}' 
    animateDict["{{{}}}".format(svg.xlink) + 'href'] = f'#{id}'
    
    animateDict['id'] = 'animate_' + id
    animateDict['fill'] = 'freeze'
    animateDict['attributeName'] = 'r' 
    animateDict['from'] = str(fromR) #'10'
    animateDict['to'] = str(toR) #'50' 
    animateDict['dur'] = str(durS) #'5'
    animateDict['begin'] = str(random.randint(0,5)) + 's' #'0s' #'click' #
    animateDict["repeatCount"] = "indefinite" #"5"
    svg.setNodeAttriDict(animate, animateDict)
    
def animCircleInfaltion(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    circleInfalation(svg,cx,cy,r=10,fromR=10, toR=50,durS=3)
    
def animCircleInfaltion2(svg):
    H,W = svg.getSize()
    
    N=30 #total points
    offset = 10 #margin to border
    pts = getRandomPoints((N,2), min=offset, max=W-offset)
    #print(pts)
    
    for pt in pts:
        r = random.randint(1, 6)
        circleInfalation(svg, pt[0], pt[1], r=r, fromR=r, toR=r*5, durS=3)
        
def main():
    file = gImageOutputPath + r'\animation.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    
    #animCircleInfaltion(svg)
    animCircleInfaltion2(svg)
    
    svg.close()
    
if __name__ == '__main__':
    main()
